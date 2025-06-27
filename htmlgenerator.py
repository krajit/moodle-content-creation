import re
import subprocess
from pathlib import Path

# === Settings ===
input_md = "source.md"
output_dir = Path("output_pages")
output_dir.mkdir(exist_ok=True)

# === Read file ===
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

# === Extract <page>...</page> blocks ===
pages = re.findall(r"<page>(.*?)</page>", content, re.DOTALL)

for i, page in enumerate(pages, start=1):
    # Extract title from first # heading
    heading_match = re.search(r"^\s*#\s+(.*)", page, re.MULTILINE)
    title = heading_match.group(1).strip() if heading_match else f"Page {i}"

    # Remove first heading from body
    body_md = re.sub(r"^\s*#\s+.*\n", '', page, count=1, flags=re.MULTILINE).strip()

    # Process answer blocks and escape LaTeX delimiters
    lines = body_md.splitlines()
    processed_lines = []
    for line in lines:
        # Escape LaTeX inline math delimiters \( and \)
        #        line = line.replace(r'\(', r'\\(').replace(r'\)', r'\\)')
        #line = re.sub(r'\\\((.*?)\\\)', r'\\\\(\1\\\\)', line)
        #line = re.sub(r'(?<!\\)\\\((.+?)\\\)(?!\\)', r'\\\\(\1\\\\)', line)


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

    # Write markdown to temp file
    md_path = output_dir / f"page_{i}.md"
    html_body_path = output_dir / f"body_{i}.html"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(body_md_processed)

    # Convert to HTML fragment
    subprocess.run([
        "pandoc", str(md_path),
        "-t", "html",
        "--mathjax",  # <-- THIS FIXES THE ISSUE
        "-o", str(html_body_path)
    ])

    # Read HTML body
    with open(html_body_path, "r", encoding="utf-8") as f:
        html_body = f.read()

    # Final HTML structure
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

    # Save output
    final_path = output_dir / f"page_{i}.html"
    with open(final_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    # Clean up
    html_body_path.unlink()
    md_path.unlink()

    print(f"✅ {final_path.name} generated with escaped math delimiters.")

print("\n🎉 All pages are ready for Moodle upload and MathJax rendering.")
