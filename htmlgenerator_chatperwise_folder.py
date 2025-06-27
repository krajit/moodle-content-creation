import re
import shutil
import subprocess
from pathlib import Path

# === Settings ===
input_md = "source_folderWiseChapter.md"
output_root = Path("output_pages_folder")
output_root.mkdir(exist_ok=True)

# === Read the full Markdown file ===
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

# === Extract <page>...</page> blocks ===
pages = re.findall(r"<page>(.*?)</page>", content, re.DOTALL)

for i, page in enumerate(pages, start=1):
    # Extract title from first heading
    heading_match = re.search(r"^\s*#\s+(.*)", page, re.MULTILINE)
    title = heading_match.group(1).strip() if heading_match else f"Chapter {i}"

    # Remove first heading from body
    body_md = re.sub(r"^\s*#\s+.*\n", '', page, count=1, flags=re.MULTILINE).strip()

    # === Process for answer toggle buttons ===
    lines = body_md.splitlines()
    processed_lines = []
    for line in lines:
        if line.strip().startswith("**Ans**"):
            answer_html = f'''
<div id="ans" style="display: none;">{line}</div>
<button onclick="
  const ans = this.previousElementSibling;
  const showing = ans.style.display !== 'none';
  ans.style.display = showing ? 'none' : 'block';
  this.innerText = showing ? 'Show Answer' : 'Hide Answer';
">Show Answer</button>
'''.strip()
            processed_lines.append(answer_html)
        else:
            processed_lines.append(line)
    body_md_processed = "\n".join(processed_lines)

    # === Create chapter folder ===
    chapter_dir = output_root / f"chapter_{i}"
    chapter_dir.mkdir(parents=True, exist_ok=True)

    # === Create chapter images folder ===
    images_dir = chapter_dir / "images"
    images_dir.mkdir(exist_ok=True)

    # === Copy images used in this chapter ===
    img_paths = re.findall(r'!\[.*?\]\((images/.*?)\)', body_md_processed)
    for img_rel_path in img_paths:
        src_path = Path(img_rel_path)
        dest_path = images_dir / Path(img_rel_path).name
        if src_path.exists():
            shutil.copy(src_path, dest_path)
        else:
            print(f"⚠️  Image not found: {src_path}")

    # === Write to a temp markdown file in the chapter folder ===
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

    # === Read the HTML fragment ===
    with open(html_body_path, "r", encoding="utf-8") as f:
        html_body = f.read()

    # === Wrap with full HTML document structure ===
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

    # === Save final HTML as index.html ===
    with open(chapter_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    # === Clean up temp files ===
    md_path.unlink()
    html_body_path.unlink()

    print(f"✅ Chapter {i} with images → {chapter_dir}/index.html")

print("\n🎉 All chapters generated with folder structure and images.")
