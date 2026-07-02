import glob
import re

new_favicon = '<link rel="icon" type="image/png" href="favicon.png">'

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the old inline SVG favicon
    content = re.sub(r'<link rel="icon" href="data:image/svg\+xml.*?>\n?', '', content)
    
    # Insert the new favicon just before </head>
    if new_favicon not in content:
        content = content.replace('</head>', f'  {new_favicon}\n</head>')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Favicon links updated to favicon.png.")
