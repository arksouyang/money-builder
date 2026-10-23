// Builds every script in scripts/<channel>/*.md into one PDF (scripts/all-scripts.pdf) with headless Chrome.
// Run: node scripts/make-pdf.mjs
import { readdirSync, readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { tmpdir } from "node:os";
import { fileURLToPath } from "node:url";
import assert from "node:assert";

const DIR = dirname(fileURLToPath(import.meta.url));
const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const CHANNELS = ["psychology", "history", "anime-webtoons", "movies-tv"];

// shortcut: handles only the markdown our scripts use (headings, bullets, ---, bold/italic/code/links).
const inline = (s) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(/`([^`]+)`/g, "<code>$1</code>");

const block = (b) => {
  const lines = b.split("\n");
  if (b.startsWith("# ")) return `<h1>${inline(b.slice(2))}</h1>`;
  if (b === "---") return "<hr>";
  if (lines.every((l) => l.startsWith("- "))) return `<ul>${lines.map((l) => `<li>${inline(l.slice(2))}</li>`).join("")}</ul>`;
  // A beat label followed by its spoken line: show the line big, it's what gets read on camera.
  if (/^\*\*[A-Z]/.test(lines[0]) && lines.length > 1 && !lines[0].includes(":**"))
    return `<p class="label">${inline(lines[0])}</p><p class="say">${lines.slice(1).map(inline).join("<br>")}</p>`;
  return `<p>${lines.map(inline).join("<br>")}</p>`;
};

const toHtml = (md) => md.trim().split(/\n\s*\n/).map((b) => block(b.trim())).join("\n");

assert.equal(inline("**a** *b* [c](d) <x>"), '<strong>a</strong> <em>b</em> <a href="d">c</a> &lt;x&gt;');
assert.equal(block("**HOOK (0–3 s)**\nHi."), '<p class="label"><strong>HOOK (0–3 s)</strong></p><p class="say">Hi.</p>');

const files = CHANNELS.flatMap((c) => {
  // ._ files are macOS junk on exFAT
  try { return readdirSync(join(DIR, c)).filter((f) => f.endsWith(".md") && !f.startsWith("._")).sort().map((f) => join(DIR, c, f)); }
  catch { return []; } // channel folder not made yet
});

const css = `
  @page { size: letter; margin: 0.7in; }
  body { font: 11pt/1.45 -apple-system, "Helvetica Neue", sans-serif; color: #1a1a1a; }
  h1 { font-size: 20pt; margin: 0 0 10px; page-break-before: always; }
  .cover h1 { page-break-before: avoid; font-size: 28pt; }
  ul { padding-left: 18px; color: #444; }
  hr { border: 0; border-top: 1px solid #ccc; margin: 14px 0; }
  .label { margin: 16px 0 2px; font-size: 10pt; color: #6b3fa0; letter-spacing: .04em; }
  .say { margin: 0; font-size: 15pt; line-height: 1.5; }
  a { color: #1a1a1a; }
  code { font-size: 10pt; }`;

const titleOf = (f) => readFileSync(f, "utf8").match(/^# (.*)/m)[1];
const cover = `<div class="cover"><h1>Shorts scripts</h1><p>Built ${new Date().toISOString().slice(0, 10)} · ${files.length} scripts</p>
  <ul>${files.map((f) => `<li>${inline(titleOf(f))}</li>`).join("")}</ul></div>`;
const body = files.map((f) => toHtml(readFileSync(f, "utf8"))).join("\n");

const tmp = join(mkdtempSync(join(tmpdir(), "scripts-pdf-")), "scripts.html");
writeFileSync(tmp, `<!doctype html><meta charset="utf-8"><style>${css}</style>${cover}${body}`);
const out = join(DIR, "all-scripts.pdf");
execFileSync(CHROME, ["--headless", "--disable-gpu", "--no-pdf-header-footer", `--print-to-pdf=${out}`, `file://${tmp}`], { stdio: "ignore" });
console.log(`Wrote ${out} (${files.length} scripts)`);
