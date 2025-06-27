import re
import subprocess
from pathlib import Path

# === Settings ===
input_md = "source.md"  # Your input file
output_dir = Path("output_pages")
output_dir.mkdir(exist_ok=True)

# === Read file ===
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

# === Extract <page>...</page> blocks ===
pages = re.findall(r"<page>(.*?)</page>", content, re.DOTALL)

for i, page in enumerate(pages, start=1):
    # Extract heading as title
    heading_match = re.search(r"^\s*#\s+(.*)", page, re.MULTILINE)
    title = heading_match.group(1).strip() if heading_match else f"Page {i}"

    # Remove heading from body
    body_md = re.sub(r"^\s*#\s+.*\n", '', page, count=1, flags=re.MULTILINE).strip()

    # Write temp markdown file
    md_path = output_dir / f"page_{i}.md"
    html_body_path = output_dir / f"body_{i}.html"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(body_md)

    # Use Pandoc to generate fragment (body only)
    subprocess.run([
        "pandoc", str(md_path),
        "-t", "html",
        "-o", str(html_body_path)
    ])

    # Read fragment content
    with open(html_body_path, "r", encoding="utf-8") as f:
        html_body = f.read()

    # Wrap with <html><head><title>... etc.
    final_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
</head>
<body>
{html_body.strip()}
</body>
</html>
"""

    # Save final HTML
    html_final_path = output_dir / f"page_{i}.html"
    with open(html_final_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    # Optionally delete temp body
    html_body_path.unlink()
    md_path.unlink()

    print(f"✅ {html_final_path.name} generated with <title>{title}</title>")

print("\n🎉 All pages successfully created with plain HTML and proper <title> tags.")
