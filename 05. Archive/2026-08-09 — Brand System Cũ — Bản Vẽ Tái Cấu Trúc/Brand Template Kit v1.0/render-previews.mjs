import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import puppeteer from "puppeteer";

const kitDir = path.dirname(fileURLToPath(import.meta.url));
const targets = [
  ["templates/short-video-9x16.html", "previews/short-video-9x16.png", 1080, 1920],
  ["templates/youtube-thumbnail-16x9.html", "previews/youtube-thumbnail-16x9.png", 1280, 720],
  ["templates/social-carousel-4x5.html", "previews/social-carousel-4x5.png", 1080, 1350],
  ["templates/framework-slide-16x9.html", "previews/framework-slide-16x9.png", 1920, 1080],
  ["templates/quote-cover-1x1.html", "previews/quote-cover-1x1.png", 1080, 1080],
];

const browser = await puppeteer.launch({ headless: true });

for (const [source, output, width, height] of targets) {
  const page = await browser.newPage();
  await page.setViewport({ width, height, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(kitDir, source)).href, { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(kitDir, output), fullPage: false });
  await page.close();
}

const board = await browser.newPage();
await board.setViewport({ width: 1740, height: 1200, deviceScaleFactor: 1 });
await board.goto(pathToFileURL(path.join(kitDir, "index.html")).href, { waitUntil: "networkidle0" });
await board.evaluate(() => document.fonts.ready);
await board.screenshot({ path: path.join(kitDir, "previews/contact-sheet.png"), fullPage: true });
await board.close();

await browser.close();
