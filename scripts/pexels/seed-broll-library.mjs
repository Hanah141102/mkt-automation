import { createHash } from "node:crypto";
import { createReadStream, createWriteStream } from "node:fs";
import { mkdir, readFile, rename, stat } from "node:fs/promises";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";
import { spawnSync } from "node:child_process";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const projectRoot = resolve(scriptDir, "../..");
const libraryRoot = join(projectRoot, ".media-library");
const videosDir = join(libraryRoot, "assets/videos");
const thumbnailsDir = join(libraryRoot, "thumbnails");
const framesDir = join(libraryRoot, "previews/frames");
const contactSheetPath = join(libraryRoot, "previews/contact-sheet.jpg");
const databasePath = join(libraryRoot, "library.sqlite");

const seedAssets = [
  {
    pexelsId: 6266251,
    slug: "cash-counting",
    category: "cash_flow",
    query: "cash flow business finance",
    description: "Một người đếm tiền mặt trên bàn làm việc.",
    purpose: "Minh họa dòng tiền, doanh thu, chi phí, lợi nhuận hoặc áp lực tài chính của doanh nghiệp.",
    suitableFor: "hook, pain point, cash flow, revenue, cost, profit",
    avoidWhen: "Không dùng cho cảnh thanh toán số hoặc biểu đồ tăng trưởng nếu cần hình ảnh chính xác.",
    keywordsVi: "dòng tiền, doanh thu, tiền mặt, chi phí, lợi nhuận, tài chính doanh nghiệp",
    keywordsEn: "cash flow, revenue, cash, cost, profit, business finance"
  },
  {
    pexelsId: 31775440,
    slug: "busy-modern-office",
    category: "office",
    query: "modern office business team",
    description: "Nhân viên làm việc và trao đổi trong một văn phòng hiện đại.",
    purpose: "Minh họa môi trường doanh nghiệp, đội nhóm phối hợp và hoạt động vận hành hằng ngày.",
    suitableFor: "business context, teamwork, collaboration, office operations",
    avoidWhen: "Không dùng cho nội dung làm việc một mình hoặc làm việc từ xa.",
    keywordsVi: "văn phòng, đội nhóm, doanh nghiệp, cộng tác, nhân viên, vận hành",
    keywordsEn: "office, team, business, collaboration, employees, operations"
  },
  {
    pexelsId: 35280159,
    slug: "humanoid-ai-robot",
    category: "ai_agent",
    query: "artificial intelligence business assistant",
    description: "Robot hình người được trưng bày trong không gian công nghệ.",
    purpose: "Minh họa AI agent, trợ lý AI, tự động hóa thông minh hoặc làn sóng công nghệ mới.",
    suitableFor: "AI agent, AI assistant, automation, future of work, technology",
    avoidWhen: "Hạn chế dùng khi cần thể hiện phần mềm AI thực tế hoặc quy trình văn phòng cụ thể.",
    keywordsVi: "AI agent, trợ lý AI, robot, tự động hóa, công nghệ, tương lai công việc",
    keywordsEn: "AI agent, AI assistant, robot, automation, technology, future of work"
  },
  {
    pexelsId: 38901929,
    slug: "finance-dashboard",
    category: "analytics",
    query: "business analytics dashboard",
    description: "Người dùng tương tác với dashboard tài chính và các biểu đồ dữ liệu số.",
    purpose: "Minh họa đo lường KPI, phân tích dữ liệu, ra quyết định và theo dõi hiệu quả kinh doanh.",
    suitableFor: "analytics, KPI, dashboard, measurement, data-driven decision",
    avoidWhen: "Không dùng nếu nội dung yêu cầu số liệu Việt Nam hoặc dashboard của một phần mềm cụ thể.",
    keywordsVi: "dashboard, KPI, dữ liệu, phân tích, đo lường, quyết định, hiệu quả",
    keywordsEn: "dashboard, KPI, data, analytics, measurement, decision, performance"
  },
  {
    pexelsId: 7591943,
    slug: "customer-support-agent",
    category: "customer_support",
    query: "customer support office",
    description: "Nữ nhân viên đeo headset đang trò chuyện với khách hàng tại bàn làm việc.",
    purpose: "Minh họa chăm sóc khách hàng, tổng đài, sales call hoặc AI hỗ trợ nhân viên CSKH.",
    suitableFor: "customer support, call center, sales call, omnichannel service",
    avoidWhen: "Không dùng để mô tả chatbot hoàn toàn tự động nếu không có lời giải thích bổ sung.",
    keywordsVi: "chăm sóc khách hàng, tổng đài, headset, sales call, hỗ trợ khách hàng",
    keywordsEn: "customer support, call center, headset, sales call, customer service"
  },
  {
    pexelsId: 7287929,
    slug: "packing-online-orders",
    category: "ecommerce",
    query: "small business packing online orders",
    description: "Hai người chuẩn bị và đóng gói các kiện hàng để giao cho khách.",
    purpose: "Minh họa SME, thương mại điện tử, xử lý đơn hàng và tự động hóa vận hành bán hàng.",
    suitableFor: "SME, ecommerce, order fulfillment, operations, online sales",
    avoidWhen: "Không dùng cho doanh nghiệp dịch vụ thuần túy hoặc sản phẩm số.",
    keywordsVi: "SME, thương mại điện tử, đơn hàng, đóng gói, vận hành, bán hàng online",
    keywordsEn: "SME, ecommerce, orders, packing, operations, online sales"
  },
  {
    pexelsId: 8519534,
    slug: "entrepreneur-laptop",
    category: "entrepreneur",
    query: "entrepreneur working laptop",
    description: "Doanh nhân làm việc tập trung trên laptop tại bàn.",
    purpose: "Cảnh trám phổ thông cho chủ doanh nghiệp, người điều hành, làm việc số hoặc triển khai công cụ AI.",
    suitableFor: "entrepreneur, business owner, productivity, digital work, AI tools",
    avoidWhen: "Không dùng cho cảnh họp đội nhóm hoặc chăm sóc khách hàng qua điện thoại.",
    keywordsVi: "doanh nhân, chủ doanh nghiệp, laptop, năng suất, công việc số, công cụ AI",
    keywordsEn: "entrepreneur, business owner, laptop, productivity, digital work, AI tools"
  }
];

function readEnvValue(source, name) {
  const line = source.split(/\r?\n/).find((entry) => entry.startsWith(`${name}=`));
  return line ? line.slice(name.length + 1).trim() : "";
}

function sql(value) {
  if (value === null || value === undefined) return "NULL";
  return `'${String(value).replaceAll("'", "''")}'`;
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: projectRoot,
    encoding: "utf8",
    stdio: options.capture ? "pipe" : "inherit"
  });
  if (result.status !== 0) {
    throw new Error(`${command} failed: ${result.stderr || result.stdout || result.status}`);
  }
  return result.stdout || "";
}

async function fetchWithRetry(url, options = {}, attempts = 3) {
  let lastError;
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      const response = await fetch(url, options);
      if (response.ok || response.status < 500 || attempt === attempts) return response;
      await response.body?.cancel();
      lastError = new Error(`HTTP ${response.status}: ${url}`);
    } catch (error) {
      lastError = error;
      if (attempt === attempts) break;
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, attempt * 750));
  }
  throw lastError;
}

async function download(url, destination) {
  try {
    const existing = await stat(destination);
    if (existing.size > 0) return false;
  } catch {
    // Download below.
  }

  const response = await fetchWithRetry(url);
  if (!response.ok || !response.body) {
    throw new Error(`Download failed (${response.status}): ${url}`);
  }

  const temporary = `${destination}.part`;
  await pipeline(Readable.fromWeb(response.body), createWriteStream(temporary));
  await rename(temporary, destination);
  return true;
}

async function sha256(filePath) {
  const hash = createHash("sha256");
  await pipeline(createReadStream(filePath), hash);
  return hash.digest("hex");
}

function parseRate(rate) {
  const [numerator, denominator] = String(rate || "0/1").split("/").map(Number);
  return denominator ? numerator / denominator : 0;
}

function probeVideo(filePath) {
  const raw = run("ffprobe", [
    "-v", "error",
    "-select_streams", "v:0",
    "-show_entries", "stream=width,height,avg_frame_rate:format=duration",
    "-of", "json",
    filePath
  ], { capture: true });
  const data = JSON.parse(raw);
  const stream = data.streams?.[0];
  if (!stream?.width || !stream?.height) throw new Error(`Invalid video: ${filePath}`);
  return {
    width: stream.width,
    height: stream.height,
    fps: parseRate(stream.avg_frame_rate),
    durationMs: Math.round(Number(data.format?.duration || 0) * 1000)
  };
}

function choosePortraitFile(videoFiles) {
  const candidates = videoFiles.filter((file) =>
    file.file_type === "video/mp4" && file.height > file.width && file.link
  );
  candidates.sort((left, right) => {
    const leftScore = Math.abs(left.height - 1280) + Math.abs(left.width - 720) * 2;
    const rightScore = Math.abs(right.height - 1280) + Math.abs(right.width - 720) * 2;
    return leftScore - rightScore;
  });
  return candidates[0];
}

function initializeDatabase() {
  const schema = `
    PRAGMA journal_mode=WAL;
    CREATE TABLE IF NOT EXISTS assets (
      id TEXT PRIMARY KEY,
      media_type TEXT NOT NULL,
      file_path TEXT NOT NULL,
      thumbnail_path TEXT,
      provider TEXT NOT NULL,
      provider_asset_id TEXT NOT NULL,
      source_url TEXT NOT NULL,
      creator_name TEXT,
      creator_url TEXT,
      query TEXT,
      category TEXT,
      literal_description TEXT NOT NULL,
      communication_purpose TEXT NOT NULL,
      suitable_for TEXT,
      avoid_when TEXT,
      keywords_vi TEXT,
      keywords_en TEXT,
      orientation TEXT,
      width INTEGER,
      height INTEGER,
      duration_ms INTEGER,
      fps REAL,
      sha256 TEXT UNIQUE,
      license TEXT NOT NULL,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS asset_usages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      asset_id TEXT NOT NULL,
      project_name TEXT,
      scene_id TEXT,
      script_excerpt TEXT,
      intended_purpose TEXT,
      suggestion_score REAL,
      accepted INTEGER,
      used_at TEXT NOT NULL,
      FOREIGN KEY(asset_id) REFERENCES assets(id)
    );
    CREATE VIRTUAL TABLE IF NOT EXISTS asset_search USING fts5(
      asset_id UNINDEXED,
      literal_description,
      communication_purpose,
      keywords_vi,
      keywords_en,
      suitable_for,
      avoid_when
    );
  `;
  run("sqlite3", [databasePath, schema], { capture: true });
}

function upsertAsset(seed, video, filePath, thumbnailPath, probe, digest) {
  const assetId = `pexels-${video.id}`;
  const now = new Date().toISOString();
  const values = {
    id: assetId,
    mediaType: "video",
    filePath: relative(projectRoot, filePath),
    thumbnailPath: relative(projectRoot, thumbnailPath),
    provider: "pexels",
    providerAssetId: video.id,
    sourceUrl: video.url,
    creatorName: video.user?.name || "",
    creatorUrl: video.user?.url || "",
    query: seed.query,
    category: seed.category,
    description: seed.description,
    purpose: seed.purpose,
    suitableFor: seed.suitableFor,
    avoidWhen: seed.avoidWhen,
    keywordsVi: seed.keywordsVi,
    keywordsEn: seed.keywordsEn,
    orientation: probe.height > probe.width ? "portrait" : "landscape",
    width: probe.width,
    height: probe.height,
    durationMs: probe.durationMs,
    fps: probe.fps,
    digest,
    license: "Pexels License",
    now
  };

  const statement = `
    INSERT INTO assets (
      id, media_type, file_path, thumbnail_path, provider, provider_asset_id,
      source_url, creator_name, creator_url, query, category, literal_description,
      communication_purpose, suitable_for, avoid_when, keywords_vi, keywords_en,
      orientation, width, height, duration_ms, fps, sha256, license, created_at, updated_at
    ) VALUES (
      ${sql(values.id)}, ${sql(values.mediaType)}, ${sql(values.filePath)}, ${sql(values.thumbnailPath)},
      ${sql(values.provider)}, ${sql(values.providerAssetId)}, ${sql(values.sourceUrl)},
      ${sql(values.creatorName)}, ${sql(values.creatorUrl)}, ${sql(values.query)}, ${sql(values.category)},
      ${sql(values.description)}, ${sql(values.purpose)}, ${sql(values.suitableFor)}, ${sql(values.avoidWhen)},
      ${sql(values.keywordsVi)}, ${sql(values.keywordsEn)}, ${sql(values.orientation)}, ${values.width},
      ${values.height}, ${values.durationMs}, ${values.fps}, ${sql(values.digest)}, ${sql(values.license)},
      ${sql(values.now)}, ${sql(values.now)}
    )
    ON CONFLICT(id) DO UPDATE SET
      file_path=excluded.file_path,
      thumbnail_path=excluded.thumbnail_path,
      source_url=excluded.source_url,
      creator_name=excluded.creator_name,
      creator_url=excluded.creator_url,
      query=excluded.query,
      category=excluded.category,
      literal_description=excluded.literal_description,
      communication_purpose=excluded.communication_purpose,
      suitable_for=excluded.suitable_for,
      avoid_when=excluded.avoid_when,
      keywords_vi=excluded.keywords_vi,
      keywords_en=excluded.keywords_en,
      orientation=excluded.orientation,
      width=excluded.width,
      height=excluded.height,
      duration_ms=excluded.duration_ms,
      fps=excluded.fps,
      sha256=excluded.sha256,
      updated_at=excluded.updated_at;
    DELETE FROM asset_search WHERE asset_id=${sql(values.id)};
    INSERT INTO asset_search VALUES (
      ${sql(values.id)}, ${sql(values.description)}, ${sql(values.purpose)},
      ${sql(values.keywordsVi)}, ${sql(values.keywordsEn)},
      ${sql(values.suitableFor)}, ${sql(values.avoidWhen)}
    );
  `;
  run("sqlite3", [databasePath, statement], { capture: true });
  return assetId;
}

function createPreviewFrames(results) {
  const framePaths = [];
  for (const result of results) {
    const duration = result.probe.durationMs / 1000;
    for (const [label, ratio] of [["early", 0.15], ["middle", 0.5], ["late", 0.85]]) {
      const framePath = join(framesDir, `${result.category}-${label}.jpg`);
      run("ffmpeg", [
        "-hide_banner", "-loglevel", "error", "-y",
        "-ss", String(Math.max(0, duration * ratio)),
        "-i", result.filePath,
        "-frames:v", "1",
        "-vf", "scale=270:-2",
        framePath
      ], { capture: true });
      framePaths.push(framePath);
    }
  }
  run("montage", [
    ...framePaths,
    "-font", "/System/Library/Fonts/Supplemental/Arial.ttf",
    "-label", "%t",
    "-tile", "3x",
    "-geometry", "270x480+8+24",
    "-background", "#101418",
    "-fill", "white",
    contactSheetPath
  ], { capture: true });
}

async function main() {
  await Promise.all([
    mkdir(videosDir, { recursive: true }),
    mkdir(thumbnailsDir, { recursive: true }),
    mkdir(framesDir, { recursive: true })
  ]);

  const env = await readFile(join(projectRoot, ".env"), "utf8");
  const apiKey = readEnvValue(env, "PEXELS_API_KEY");
  if (!apiKey) throw new Error("PEXELS_API_KEY is missing from .env");

  const healthResponse = await fetchWithRetry("https://api.pexels.com/v1/videos/popular?per_page=1", {
    headers: { Authorization: apiKey }
  });
  if (!healthResponse.ok) throw new Error(`Pexels API key failed: HTTP ${healthResponse.status}`);
  await healthResponse.body?.cancel();

  initializeDatabase();
  const results = [];

  for (const seed of seedAssets) {
    const response = await fetchWithRetry(`https://api.pexels.com/v1/videos/videos/${seed.pexelsId}`, {
      headers: { Authorization: apiKey }
    });
    if (!response.ok) throw new Error(`Pexels video ${seed.pexelsId}: HTTP ${response.status}`);
    const video = await response.json();
    const selectedFile = choosePortraitFile(video.video_files || []);
    if (!selectedFile) throw new Error(`No portrait MP4 found for Pexels ${video.id}`);

    const filePath = join(videosDir, `${seed.category}-${seed.slug}-pexels-${video.id}.mp4`);
    const thumbnailPath = join(thumbnailsDir, `${seed.category}-${seed.slug}-pexels-${video.id}.jpg`);
    const downloaded = await download(selectedFile.link, filePath);
    await download(video.image, thumbnailPath);

    const probe = probeVideo(filePath);
    if (probe.height <= probe.width) throw new Error(`Pexels ${video.id} is not portrait`);
    const digest = await sha256(filePath);
    const assetId = upsertAsset(seed, video, filePath, thumbnailPath, probe, digest);
    results.push({ assetId, category: seed.category, filePath, probe, downloaded });
    console.log(`${downloaded ? "downloaded" : "reused"} ${assetId} -> ${relative(projectRoot, filePath)} (${probe.width}x${probe.height}, ${(probe.durationMs / 1000).toFixed(1)}s)`);
  }

  createPreviewFrames(results);
  const totalBytes = (await Promise.all(results.map((result) => stat(result.filePath)))).reduce((sum, item) => sum + item.size, 0);
  console.log(`library ${results.length} assets -> ${relative(projectRoot, databasePath)}`);
  console.log(`contact sheet -> ${relative(projectRoot, contactSheetPath)}`);
  console.log(`batch size ${(totalBytes / 1024 / 1024).toFixed(1)} MB`);
}

await main();
