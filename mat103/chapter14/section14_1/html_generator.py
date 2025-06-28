import re
import shutil
import subprocess
from pathlib import Path

# === Settings ===
input_md = "source123.md"
output_root = Path("output_pages")
output_root.mkdir(exist_ok=True)

# === Get the directory where this script resides ===
script_dir = Path(__file__).parent.resolve()

# === Read the Markdown source file ===
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

# === Extract <page>...</page> blocks ===
pages = re.findall(r"<page>(.*?)</page>", content, re.DOTALL)

for i, page in enumerate(pages, start=1):
    # Extract the title from the first heading
    heading_match = re.search(r"^\s*#\s+(.*)", page, re.MULTILINE)
    title = heading_match.group(1).strip() if heading_match else f"Chapter {i}"

    # Remove first heading from the body
    body_md = re.sub(r"^\s*#\s+.*\n", '', page, count=1, flags=re.MULTILINE).strip()

    # === Replace <ans>...</ans> blocks with toggle button BELOW the content ===
    def replace_ans_blocks(text):
        def _repl(match):
            inner = match.group(1).strip()
            return f"""
<button onclick="
  const ans = this.nextElementSibling;
  const isVisible = ans.style.display !== 'none';
  ans.style.display = isVisible ? 'none' : 'block';
  this.innerText = isVisible ? 'Show Answer' : 'Hide Answer';
">Show Answer</button>
<div class="answer-block" style="display: none;">
{inner}
</div>
""".strip()
        return re.sub(r"<ans>(.*?)</ans>", _repl, text, flags=re.DOTALL)

    body_md_processed = replace_ans_blocks(body_md)

    # === Create chapter output folder ===
    chapter_dir = output_root / f"chapter_{i}"
    chapter_dir.mkdir(parents=True, exist_ok=True)

    # === Copy image files used in this page ===
    img_paths = re.findall(r'!\[.*?\]\((.*?)\)', body_md_processed)
    for img in img_paths:
        img_file = Path(img).name
        src_path = script_dir / img_file
        dest_dir = chapter_dir
    # === Write temp markdown file for Pandoc ===
    md_path = chapter_dir / "temp.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(body_md_processed)

    # === Convert Markdown to HTML using Pandoc ===
    html_body_path = chapter_dir / "body.html"
    subprocess.run([
        "pandoc", str(md_path),
        "-t", "html",
        "--mathjax",
        "-o", str(html_body_path)
    ])

    # === Read Pandoc output HTML ===
    with open(html_body_path, "r", encoding="utf-8") as f:
        html_body = f.read()

    # === Wrap in full HTML structure ===
    final_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <script type="text/javascript" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
{html_body.strip()}
</body>
</html>
"""

    # === Save final index.html ===
    with open(chapter_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    # === Cleanup temp files ===
    md_path.unlink()
    html_body_path.unlink()

    print(f"✅ Chapter {i} written to {chapter_dir}/index.html")

print("\n🎉 All chapters generated with toggles, images, and MathJax support.")
