# HeyGen MCP OAuth — Non-Host Environments (Hermes desktop, plain curl, custom clients)

The companion reference `heygen-mcp-setup.md` documents the **Codex CLI** flow
(`codex mcp login heygen` opens a browser, user approves, host stores JWT).
That flow does not apply when the agent is **not** a recognized MCP host (Hermes
desktop, custom MCP client, ad-hoc curl scripts). Those environments must drive
the OAuth handshake manually via the MCP tools themselves.

This doc captures the procedure observed working (and where it can stall) on
**Hermes Agent desktop / Rocket Agent**, July 2026.

---

## When to use this reference vs. the Codex CLI doc

| Environment | Doc to follow |
|---|---|
| Codex CLI (verified) | `references/heygen-mcp-setup.md` §4 — `codex mcp login heygen` |
| Claude desktop / Cursor (host-managed) | Same as Codex — the host handles the browser dance |
| **Hermes Agent / Rocket Agent desktop** | **This doc** — use `mcp__heygen__authenticate` |
| Custom MCP client / curl-only | This doc — adapt the Python listener snippet |

The deciding factor: does the host (Codex, Claude desktop, Cursor) **own** the
browser window for OAuth? If yes, use `codex mcp login`. If the agent has to
ask the user to open the browser themselves and paste back a URL, use the flow
below.

---

## The MCP tools themselves

When a HeyGen MCP server is registered but **not yet authenticated**, only two
tools are exposed:

| Tool | Purpose |
|---|---|
| `mcp__heygen__authenticate` | Returns an OAuth authorize URL the user must visit |
| `mcp__heygen__complete_authentication` | Accepts the callback URL pasted back from the browser |

After `complete_authentication` succeeds, the deferred tool list expands with
the real HeyGen tools: `create_video_from_avatar`, `create_avatar_video`,
`get_video`, `list_avatar_looks`, etc.

`HEYGEN_API_KEY` is **not** used for MCP tool calls — it is a separate
credential for the REST asset-upload endpoint
(`POST https://upload.heygen.com/v1/asset`, header `X-Api-Key`). See
`heygen-mcp-setup.md` for that detail.

---

## Procedure (Hermes desktop)

### Step 1 — Detect unauthenticated state

Either the agent has loaded the MCP tools and any call returns
`401 invalid_token`, or the deferred tool list only shows
`mcp__heygen__authenticate` + `mcp__heygen__complete_authentication`. Both
indicate "need to drive OAuth."

### Step 2 — Start a localhost callback listener

The OAuth `redirect_uri` returned by `mcp__heygen__authenticate` is typically
`http://localhost:<port>/callback` or similar. The MCP server will hit that URL
after the user approves in the browser, and the agent must capture the redirect
to extract the `code` it needs.

A minimal Python listener (runs in `execute_code` or a background terminal):

```python
import http.server, socketserver, urllib.parse, threading, sys

PORT = 8765  # use the port the authorize URL specifies — DO NOT guess

captured = {"code": None, "state": None, "full": None}

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a, **kw): pass  # silence access log
    def do_GET(self):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        captured["code"]  = (params.get("code")  or [None])[0]
        captured["state"] = (params.get("state") or [None])[0]
        captured["full"]  = self.path
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h2>OK - ban co the dong tab nay va quay lai chat.</h2>")

def run():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.handle_request()  # exit after first request

t = threading.Thread(target=run, daemon=True); t.start()
print(f"listening on http://127.0.0.1:{PORT}/callback")
print("waiting for redirect ...")
# the agent then sleeps/polls `captured` until filled
```

Pitfalls:

- **Port must match the `redirect_uri` port exactly.** If `mcp__heygen__authenticate` returns
  `redirect_uri=http://localhost:9123/callback`, bind to `9123`, not 8765.
- **Bind to `127.0.0.1` not `0.0.0.0`** — IPv6 `::` is also fine, but
  `localhost` resolution occasionally picks the wrong family on macOS.
- **Use `handle_request()` not `serve_forever()`** — one redirect is enough,
  and a daemon thread that exits cleanly is easier to reason about.

### Step 3 — Call `mcp__heygen__authenticate`

The tool returns a payload like:

```json
{
  "authorization_url": "https://app.heygen.com/oauth/authorize?response_type=code&client_id=...&redirect_uri=http%3A%2F%2Flocalhost%3A8765%2Fcallback&state=...&scope=...",
  "redirect_uri": "http://localhost:8765/callback",
  "state": "..."
}
```

Surface the **authorization_url** to the user verbatim and tell them to:

1. Open it in a browser (the agent's browser, or theirs)
2. Complete login (email + password, Google, Apple, **or SSO**)
3. After approving, the browser redirects to `http://localhost:8765/callback?code=...&state=...`
4. The agent's listener captures the `code`

### Step 4 — Wait for the callback

Poll the `captured` dict (or `print` from the listener thread) until `code` is
non-None. **Cap the wait at ~5 minutes** — if nothing arrives, do not keep
waiting silently; surface a status message so the user knows to act.

### Step 5 — Call `mcp__heygen__complete_authentication`

Pass:

```yaml
callback_url: "http://localhost:8765/callback?code=<captured_code>&state=<captured_state>"
```

(Or whatever shape the tool expects — some implementations take `code` +
`state` separately. Use the full URL if unsure.)

On success, the deferred tool list should now include the real HeyGen tools.
Continue with the avatar-video creation flow described in the parent
`heygen-mp3-to-mp4` or `heygen-short-video` SKILL.md.

---

## SSO work-email gotchas (this is where the flow commonly hangs)

Several real failures observed in production:

### Symptom: SSO panel resets to login every time

The user has a work-email HeyGen account (e.g. `name@company.com`) gated behind
Okta / Azure AD / Google Workspace SSO. The HeyGen authorize URL triggers the
IdP login page, but if:

- The IdP session cookie is expired → user types the work email, IdP sends
  them through password / MFA, then **redirects them back to the HeyGen
  authorize endpoint with a fresh state** — and the agent's listener is
  waiting on the old state, which never arrives.
- The IdP rejects the email as "unknown tenant" — user sees a blank page or a
  generic 500 and the OAuth silently aborts.

Fix:

- Ask the user to **first log into their work IdP in a separate tab** (so the
  SSO cookie is warm), then return to the HeyGen URL. This often skips the
  IdP form entirely on the second pass.
- If SSO is consistently failing, **abandon the OAuth path entirely** and
  suggest the user create a personal HeyGen account at `app.heygen.com` with
  their personal email. The MCP server accepts OAuth from any HeyGen tenant;
  work-email SSO is not required.

### Symptom: blank / white page after submitting the form

The IdP redirected but the next hop failed (corporate proxy, browser
extension, etc.). The browser shows white, but the OAuth flow may still have
completed server-side — the user just needs to look at the address bar for
`localhost:<port>/callback?code=...` and paste that URL back to the agent.

### Symptom: callback never lands on the listener

Common cause: the `redirect_uri` registered with the OAuth client does **not**
include the port the agent chose. The authorize URL advertises one port, but
the IdP strips it during the redirect chain, sending the user to a different
host or path. **Always use the port advertised by `mcp__heygen__authenticate`,
not one you picked arbitrarily.**

If the listener never fires:

1. Confirm the listener bound to the right port (`lsof -iTCP:8765 -sTCP:LISTEN` or
   equivalent).
2. Ask the user to copy the **full address-bar URL** from their browser, even
   if it looks like a regular HeyGen page — sometimes the redirect lands on a
   different host and the user just doesn't realize it's the callback.

### Symptom: agent keeps looping on "is the callback there yet?"

The agent must not infinite-loop polling for the callback. After ~5 minutes
without a callback, surface the situation and ask the user to confirm what they
see in the browser. Do not block silently — the user has no other way to know
the agent is waiting.

---

## Quick escalation ladder

When `mcp__heygen__*` calls keep failing after OAuth appears complete:

1. Re-check `codex mcp list | grep heygen` (or the host equivalent) — confirm
   the server is still listed as logged in.
2. If the host says "logged in" but tools still 401, the JWT may be expired;
   re-run the OAuth flow.
3. If the user has only a work-email SSO account, fall back to **creating a
   personal HeyGen account** at `app.heygen.com` — most "HeyGen MCP setup"
   blockers are SSO-related, not protocol-related.
4. As a last resort, the asset-upload + REST video-create endpoints are
   documented publicly and accept v3 API keys with `X-Api-Key` headers. The
   MCP OAuth dance is convenience, not a hard requirement.

---

## Verification

After `complete_authentication` succeeds, the easiest smoke test is to list
avatar looks:

```bash
mcp__heygen__list_avatar_looks
```

If this returns the user's avatar pool, OAuth is live. If it 401s, the JWT
didn't take — re-run from Step 3.

---

## Hermes desktop `hermes mcp` CLI gotchas (verified July 2026)

Hermes ships its own MCP client (`hermes mcp ...` subcommands). Several
behaviors are non-obvious and cost iterations to discover — pre-bake them
so the next session doesn't redo the detective work.

### File locations

| File | Purpose |
|---|---|
| `~/.rocketagent/profiles/<profile>/mcp.json` | MCP server registrations per profile (current convention) |
| `~/.rocketagent/mcp/auth/<server>.json` | Cached OAuth tokens (per-server) |
| `~/.rocketagent/profiles/<profile>/permission.yaml` | Profile access control — cross-profile MCP access requires grants here |

`hermes mcp list` reports what's currently registered for the active
profile. Read the JSON file directly when the CLI disagrees with reality,
or when the schema is being silently rewritten.

### Schema gotcha — `auth: oauth` is silently stripped on non-interactive add

```bash
# THIS WILL NOT PERSIST the auth field — even though the CLI says it added the server:
hermes mcp add heygen https://mcp.heygen.com/mcp/v1/ --auth oauth
```

The CLI registers the server (URL is fine), but the `auth: oauth` field
is dropped from the persisted `mcp.json`. On next host reload the server
appears with no auth requirement and the deferred-tool list collapses to
just `authenticate` / `complete_authentication` — which is functionally
OK for the OAuth-from-non-host flow above, but means **do NOT assume the
CLI wrote a complete schema**. Always inspect the `mcp.json` file after
`hermes mcp add` to verify what actually landed.

What you actually need in `mcp.json` (verified working):

```json
{
  "heygen": {
    "url": "https://mcp.heygen.com/mcp/v1/",
    "auth": "oauth",
    "enabled": true
  }
}
```

If `auth` is missing, the host still loads the server but treats auth as
"not configured" — which still allows `authenticate` to fire, so the
non-host flow above proceeds normally. The real danger is when the agent
**assumes** the CLI set up OAuth-ready config and skips the
`mcp__heygen__authenticate` step.

### Validator scope — `hermes mcp add --auth oauth` is silently accepted

The Hermes MCP config validator (e.g. `utils/fast_safe_load.py`) only
checks shell interpreter entries for safety; it does not validate that
the OAuth field is present or correct. A server registered with no auth
field passes the validator, so the CLI returns success even though the
agent's mental model of "auth: oauth persisted" is wrong. Verify by
reading the JSON, not by trusting the CLI exit code.

### Cross-profile access is a hard boundary

`cross_profile=True` on a tool call opts out of an unrelated sandbox /
container-mirror warning — it does NOT grant access to another profile's
`mcp.json`, `auth/`, or `permission.yaml`. To use HeyGen MCP from a
non-`video-editor` profile, the user must grant access via
`permission.yaml` in the owning profile. Tell the user when this is the
blocker; don't try to bypass it.

### `read_file` vs terminal cat for MCP config files

Hermes desktop's `read_file` tool is not always available in the active
session's toolset. When investigating `mcp.json` or `auth/*.json`, use a
terminal `cat` directly — same bytes, no permission dance, and it
survives toolset changes across sessions.