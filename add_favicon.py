import glob

svg_favicon = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%236366f1%22/><text x=%2250%22 y=%2270%22 font-size=%2260%22 fill=%22white%22 text-anchor=%22middle%22 font-family=%22Arial, sans-serif%22 font-weight=%22bold%22>IN</text></svg>">'

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Remove manifest link to prevent it from pulling broken PWA icons
    if '<link rel="manifest" href="manifest.json">' in content:
        content = content.replace('<link rel="manifest" href="manifest.json">', '')
        modified = True

    # Add the new professional favicon
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', f'  {svg_favicon}\n</head>')
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Favicons fixed successfully.")
