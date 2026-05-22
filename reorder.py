import re

file_path = "projects.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the projects grid
start_str = '<div class="projects-grid">'
end_str = '<!-- GitHub CTA -->'
start_idx = content.find(start_str) + len(start_str)
end_idx = content.find(end_str)

grid_content = content[start_idx:end_idx]

# Split articles
articles = re.split(r'(<!-- Project \d+:.*?-->)', grid_content)

# articles array structure: [pre_text, comment1, content1, comment2, content2, ...]
projects = []
for i in range(1, len(articles), 2):
    comment = articles[i]
    body = articles[i+1]
    
    # identify name
    name = ""
    if "Iyyappan AI Assistant" in comment: name = "iyyappan ai assistant"
    elif "Stealth Chat" in comment: name = "stealthchat"
    elif "Multiplayer Game" in comment: name = "multiplayer elemental game"
    elif "OS CPU Scheduling" in comment: name = "os cpu scheduling"
    elif "E-Commerce" in comment: name = "e-commerce platform"
    elif "CRUD APP" in comment: name = "crud app"
    elif "Memory Game" in comment: name = "memory game java"
    elif "BYC Academy" in comment: name = "byc academy"
    elif "naturize" in comment: name = "naturize"
    
    projects.append({"name": name, "comment": comment, "body": body})

# Requested order
order_names = [
    "stealthchat",
    "multiplayer elemental game",
    "naturize",
    "os cpu scheduling",
    "byc academy",
    "iyyappan ai assistant",
    "e-commerce platform",
    "crud app",
    "memory game java"
]

ordered_projects = []
for name in order_names:
    for p in projects:
        if p["name"] == name:
            ordered_projects.append(p)
            break

# Now renumber the comments and project-number spans, and transition delays
new_grid = "\n"
for i, p in enumerate(ordered_projects):
    num = i + 1
    # Update comment
    comment = re.sub(r'Project \d+', f'Project {num}', p["comment"])
    body = p["body"]
    # Update 0X / 09
    body = re.sub(r'\d{2} / 09', f'{num:02d} / 09', body)
    
    # Update transition delays (staggered every 3 items in a grid maybe?)
    # Original delays: None, 0.1s, 0.2s
    # I'll just assign them logically: 0, 0.1, 0.2 repeating
    delay = (i % 3) * 0.1
    if delay == 0:
        body = re.sub(r' style="transition-delay:0\.\ds"', '', body)
    else:
        if 'transition-delay' in body:
            body = re.sub(r'transition-delay:0\.\ds', f'transition-delay:{delay}s', body)
        else:
            body = body.replace('class="project-card reveal"', f'class="project-card reveal" style="transition-delay:{delay}s"')
            
    new_grid += "                " + comment + body

final_content = content[:start_idx] + new_grid + "                " + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print("Done reordering")
