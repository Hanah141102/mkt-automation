# HeyGen MCP Server — Setup & Authentication Reference

How to connect HeyGen's remote MCP server to a host (Codex CLI verified; Claude
desktop / Cursor follow the same pattern) and authenticate via OAuth. All
HeyGen skills (`heygen-mp3-to-mp4`, `heygen-script-to-mp4`, `heygen-short-video`)
assume an authenticated MCP server is live — this doc explains how to get there.

---

## 1. Server endpoint (stable)

```
URL: https://mcp.heygen.com/mcp/v1/
Transport: HTTP (Streamable HTTP), JSON-RPC 2.0
Auth: OAuth 2.0 (Authorization Code + PKCE) — Bearer JWT issued by HeyGen
```

The endpoint is **HTTP/HTTPS only** — no stdio, no subprocess. That means the
host config asks for a `url`, not a `command` + `args` pair. The MCP server
does not accept long-lived API keys as bearer tokens; using `HEYGEN_API_KEY`
as `Authorization: Bearer …` returns `401 invalid_token` with a
`www-authenticate` resource-metadata hint pointing to the OAuth issuer.

**Plugins ≠ MCP servers.** Codex ships `[plugins."heygen@openai-curated"]` as a
**skills bundle** (`.app.json`, agents, brand guidance) — it does **not** auto-
connect the MCP server. You still have to add the `[mcp_servers.heygen]` entry
described below.

---

## 2. Codex CLI config (verified)

Config file: `~/.codex/config.toml`

```toml
[mcp_servers.heygen]
url = "https://mcp.heygen.com/mcp/v1/"
```

Schema is `[mcp_servers.<name>]` with `url` (HTTP MCP). **Not** Claude's
`{ command, args }` shape — Codex cannot launch a stdio MCP server that way for
remote HTTP endpoints.

**Always back up before editing:**

```bash
cp ~/.codex/config.toml ~/.codex/config.toml.bak.$(date +%Y%m%d_%H%M%S)
```

Append `heygen` to the existing `[mcp_servers]` section — don't replace the
file. Other MCP servers (chrome-devtools, etc.) stay intact.

---

## 3. Verify the server is registered

```bash
codex mcp list
```

Healthy output:

```
Name      URL                                  Status    Auth
heygen    https://mcp.heygen.com/mcp/v1/       enabled   Not logged in
```

If the server shows up as `enabled` + `Not logged in`, the network side is
fine — you only need to run the OAuth flow.

---

## 4. OAuth flow (human required)

```bash
codex mcp login heygen
```

The agent **cannot complete this step** — the host opens a browser window to
the HeyGen authorization page, the user clicks Approve, and the host stores
the resulting JWT in its local credential store. Until this step finishes,
`codex mcp list` will keep showing `Not logged in` and any `mcp__heygen__*`
tool call will return `401 invalid_token`.

**Tell the user explicitly:**

> HeyGen MCP đã được cấu hình. Chạy `codex mcp login heygen` — sẽ mở browser
> để authorize. Sau khi login xong, `codex mcp list` sẽ báo `Logged in` rồi
> các MCP tools (`create_avatar_video`, `get_video`, …) sẽ dùng được.

Re-check auth after the user confirms:

```bash
codex mcp list | grep heygen   # expect "Logged in"
```

---

## 5. Failure modes the agent WILL hit

| Symptom | Root cause | Fix |
|---|---|---|
| `401 invalid_token` from MCP tool | OAuth not completed yet | `codex mcp login heygen` (host-managed); `mcp__heygen__authenticate` + `complete_authentication` (Hermes desktop — see `heygen-mcp-oauth-non-host.md`) |
| `403` / `404` on `/mcp/v1/` | Host sent `command`/`args` instead of `url` | Edit config to use `[mcp_servers.<name>].url` |
| `codex mcp list` doesn't show the server | Wrong TOML section name or syntax | Check `[mcp_servers.heygen]` (not `[mcp.heygen]`, not `[servers]`); restart host after edit |
| Asset upload ok but `create_avatar_video` fails | Upload used v3 API key as Bearer | Upload step needs `X-Api-Key: $HEYGEN_API_KEY` header (separate from MCP); only MCP talks OAuth |
| Tool returns `audio upload not allowed` | Used `script` + `voiceId` (TTS path) instead of `audioAssetId` (lip-sync path) | Upload asset first, then pass `audioAssetId` to the tool |
| User pastes authorize URL, browser opens but SSO shows "blank page" or keeps resetting to login dialog | SSO work-email account (Okta/Azure AD/Google Workspace); IdP session expired or email not in the OAuth tenant | Warm the IdP cookie in a separate tab first; if SSO keeps failing, fall back to a personal HeyGen account |
| Browser authorizes, no callback on the agent's localhost listener | OAuth `redirect_uri` advertises one port but the agent bound to a different port (or never bound at all) | Use the exact port from `mcp__heygen__authenticate`'s returned `redirect_uri`; confirm `lsof -iTCP:<port> -sTCP:LISTEN` |
| `mcp__heygen__complete_authentication` returns "code not found" / "session expired" | User took too long authorizing (>5 min), or pasted a URL whose `state` was already rotated | Re-call `mcp__heygen__authenticate` for a fresh URL; have the user retry within a few minutes |

For environments that are NOT Codex/Claude desktop/Cursor (Hermes Agent, custom
MCP clients, plain curl), the OAuth dance is different — see
`references/heygen-mcp-oauth-non-host.md` for the `mcp__heygen__authenticate`
+ localhost callback listener procedure and the SSO work-email escape hatch.

The upload step uses **REST with `HEYGEN_API_KEY`** (`X-Api-Key` header), not
MCP — the post-2026 MCP server does not expose an asset-upload tool. v3 key
auth is fine for upload; v3 key auth is **not** fine for the MCP tools.

---

## 6. Check the host has the MCP tools available

After `Logged in`, list the tools the host actually exposes. From the host:

```bash
# Codex: tools show up automatically once a server is logged in; no separate enable step.
# Claude desktop: Settings → Developer → MCP server shows tool list.
```

Expected HeyGen tools (names may vary slightly by host):

- `create_avatar_video` (lip-sync via `audioAssetId`)
- `get_video` (poll status, fetch `video_url`)
- `list_avatars`, `list_voices` (look up IDs)

If `create_avatar_video` is missing but the server is listed, the host may not
have refreshed — restart the host and re-check.

---

## 7. Config snippet to remember

For a fresh Codex install, the minimum delta to add HeyGen is exactly this —
verified working on macOS with codex-cli 0.134.0:

```toml
# ~/.codex/config.toml (append, do not replace)
[mcp_servers.heygen]
url = "https://mcp.heygen.com/mcp/v1/"
```

Then: `codex mcp login heygen` → browser → Approve → done.
