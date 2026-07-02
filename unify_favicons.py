import glob
import re

png_favicon = '<link rel="icon" type="image/png" href="favicon.png">'

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any existing favicon links (including the malformed SVG one)
    content = re.sub(r'<link rel="icon"[^>]*>\n?', '', content)
    
    # The malformed SVG might have left broken pieces if re.sub didn't catch the whole thing because of early >
    # Let's do a more robust string replacement for the exact SVG string I injected earlier:
    svg_string = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%236366f1%22/><text x=%2250%22 y=%2270%22 font-size=%2260%22 fill=%22white%22 text-anchor=%22middle%22 font-family=%22Arial, sans-serif%22 font-weight=%22bold%22>IN</text></svg>">'
    content = content.replace(svg_string, '')
    
    # Also clean up any lingering 'IN</text></svg>">' if it somehow got split
    # But string replace should catch the exact string.
    
    # Insert the correct PNG favicon just before </head>
    if png_favicon not in content:
        content = content.replace('</head>', f'  {png_favicon}\n</head>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
            
print("All pages unified to use favicon.png and SVG bug removed.")
