import re

java_svg = '<svg viewBox="0 0 128 128" width="1em" height="1em"><path fill="currentColor" d="M83.2 47.7c-5.8-9.4-2.8-19.9-2-22.9.2-.8-.6-1.5-1.3-1.1-7.8 4.2-18.7 17.6-13.6 30.2 4.2 10.3 16 11.8 16.9 20.3-6.1-7.6-15.5-5.5-15.5-5.5-1.4 3.7 1.2 9.1 5.9 12.8 5.7 4.5 13.9 6.4 17.4 12.1 4.5 7.2.9 17.6.9 17.6s12.5-11.8 7.3-25.2c-5.4-14-22.4-16.7-16-35.3z"/><path fill="currentColor" d="M60.4 20.8c-7.9-9.5-3.3-20-2.4-22.9.2-.7-.7-1.3-1.3-.9-7.3 4.8-16.5 18.5-10.7 30.6 5.1 10.6 17.5 11.2 19 19.9-6.3-7.2-15.6-4.5-15.6-4.5-1.1 3.5 1.9 8.7 6.8 11.8 5.9 3.8 14.1 4.9 18.3 10.3 5.4 6.8 2.5 17 2.5 17s11.5-12 5.5-24.9c-6.2-13.4-23.7-14.7-17.3-33.1z"/><path fill="currentColor" d="M96.7 87.5c-4.4 2.1-13.8 5.5-26 5.5-14.8 0-26.6-4.1-30.8-6-1.3-.6-2.5 1.1-1.4 1.9 6 4.4 22.4 11.4 46.2 3.1 1.7-.6 1.4-3.1-.7-3.1-2.1 0-4.8.1-7.3-1.4z"/><path fill="currentColor" d="M103 98c-5.2 3-18.6 7.4-33.8 7.4-17.7 0-29.6-4.5-33.3-6.2-1.3-.6-2.5 1.1-1.3 1.9 6.7 4.2 26 10 47.9 3 2.1-.7 1.2-3.3-.6-3.3-2.9 0-5.8.1-8.9-2.8z"/></svg>'

coffee_cup_svg = '<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>'

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace java logo
idx_content = idx_content.replace(coffee_cup_svg, java_svg)

# Replace the featured projects block
# Currently it has: Iyyappan AI Assistant, Stealth Chat, CPU Scheduling Visualizer
# Replace with Stealthchat, naturize, Multiplayer elemental game
new_featured = '''        <div class="feat-card reveal">
          <span class="feat-icon-big"><svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></span>
          <div class="feat-num">01 — Secure Messaging</div>
          <h3>Stealth Chat — P2P Encrypted</h3>
          <p>Serverless browser P2P app with AES-GCM + ECDH encryption via WebRTC — messages never touch the server. Auto-destructing timers included.</p>
          <div class="feat-tags">
            <span class="feat-tag">WebRTC</span>
            <span class="feat-tag">Node.js</span>
            <span class="feat-tag">Web Crypto API</span>
          </div>
        </div>

        <div class="feat-card reveal" style="transition-delay:0.1s">
          <span class="feat-icon-big"><svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"></path><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"></path></svg></span>
          <div class="feat-num">02 — Web App</div>
          <h3>naturize</h3>
          <p>A web app that converts AI-generated text into natural, human-like writing to make content sound conversational and less robotic.</p>
          <div class="feat-tags">
            <span class="feat-tag">HTML5</span>
            <span class="feat-tag">CSS3</span>
            <span class="feat-tag">JavaScript</span>
            <span class="feat-tag">Groq API</span>
          </div>
        </div>

        <div class="feat-card reveal" style="transition-delay:0.2s">
          <span class="feat-icon-big"><svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"></line><line x1="8" y1="10" x2="8" y2="14"></line><line x1="15" y1="13" x2="15.01" y2="13"></line><line x1="18" y1="11" x2="18.01" y2="11"></line><path d="M17.32 5H6.68a4 4 0 0 0-3.978 3.59c-.006.052-.01.101-.017.152C2.604 9.416 2 14.456 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.414-1.414A2 2 0 0 1 9.828 16h4.344a2 2 0 0 1 1.414.586L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.545-.604-6.584-.685-7.258-.007-.05-.011-.1-.017-.151A4 4 0 0 0 17.32 5z"></path></svg></span>
          <div class="feat-num">03 — Web Game</div>
          <h3>Multiplayer Elemental Game</h3>
          <p>Real-time multiplayer browser game with elemental powers. Build with HTML5 Canvas, WebSocket, and Express.</p>
          <div class="feat-tags">
            <span class="feat-tag">HTML5 Canvas</span>
            <span class="feat-tag">Node.js</span>
            <span class="feat-tag">Socket.io</span>
          </div>
        </div>'''

idx_content = re.sub(r'<div class="feat-card reveal">.*?</div>\s*</div>\s*<div class="view-all-wrap reveal">', new_featured + '\n\n      </div>\n\n      <div class="view-all-wrap reveal">', idx_content, flags=re.DOTALL)

# Update "View all X projects" in index.html to 7
idx_content = re.sub(r'View all \d+ projects', 'View all 7 projects', idx_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)


# Update projects.html
with open('projects.html', 'r', encoding='utf-8') as f:
    prj_content = f.read()

# Replace naturize description and tech tags
naturize_desc_old = '<p>\n                            A nature-themed web project developed using HTML.\n                        </p>\n                    </div>\n                    <div class="project-footer">\n                        <span class="tech-tag">HTML</span>'
naturize_desc_new = '''<p>
                            Naturize is a web app that converts AI-generated text into natural, human-like writing. It helps users make emails, blogs, reports, and other content sound more conversational and less robotic.
                        </p>
                    </div>
                    <div class="project-footer">
                        <span class="tech-tag">HTML</span>
                        <span class="tech-tag">CSS</span>
                        <span class="tech-tag">JavaScript</span>
                        <span class="tech-tag purple-tag">Groq API</span>'''
prj_content = prj_content.replace(naturize_desc_old, naturize_desc_new)

# Replace BYC Academy description and tech tags
byc_desc_old = '<p>\n                            A web project built with HTML for an academy interface.\n                        </p>\n                    </div>\n                    <div class="project-footer">\n                        <span class="tech-tag">HTML</span>'
byc_desc_new = '''<p>
                            BYC Academy is a promotional website developed for a tuition academy to showcase their courses, faculty, facilities, and student-focused learning programs. The website helps the academy build an online presence, attract new students, and provide important information in a clean and responsive interface.
                        </p>
                    </div>
                    <div class="project-footer">
                        <span class="tech-tag">HTML</span>
                        <span class="tech-tag">CSS</span>
                        <span class="tech-tag">JavaScript</span>'''
prj_content = prj_content.replace(byc_desc_old, byc_desc_new)

# Remove E-commerce and Memory Game Java
# Project names are: 
# 1. Stealth Chat
# 2. Multiplayer
# 3. Naturize
# 4. OS CPU
# 5. BYC
# 6. Iyyappan AI
# 7. E-Commerce
# 8. CRUD
# 9. Memory Game Java

# Actually, the grid contains <!-- Project X: Y -->
articles = re.split(r'(<!-- Project \d+.*?(?=<!-- Project|<!-- GitHub CTA))', prj_content, flags=re.DOTALL)

# Let's cleanly rebuild the project grid, excluding E-commerce and Memory Game
projects_to_keep = []
github_cta = ''
for part in articles:
    if '<!-- GitHub CTA' in part:
        github_cta = part
        continue
    if '<!-- Project' in part:
        if 'E-Commerce' in part or 'Memory Game' in part:
            continue
        else:
            projects_to_keep.append(part)

# Rebuild
# The text before projects grid
start_idx = prj_content.find('<div class="projects-grid">') + len('<div class="projects-grid">')
pre_text = prj_content[:start_idx]

# the text after
cta_idx = prj_content.find('<!-- GitHub CTA -->')
post_text = prj_content[cta_idx:]

new_grid = ""
for i, part in enumerate(projects_to_keep):
    num = i + 1
    # replace 'Project \d+'
    part = re.sub(r'Project \d+', f'Project {num}', part)
    # replace '0X / 09' with '0X / 07'
    part = re.sub(r'\d{2} / 09', f'{num:02d} / 07', part)
    
    # Fix transition delays
    delay = (i % 3) * 0.1
    part = re.sub(r' style="transition-delay:0\.\ds"', '', part)
    if delay > 0:
        part = part.replace('class="project-card reveal"', f'class="project-card reveal" style="transition-delay:{delay}s"')
        
    new_grid += part

# Reassemble
final_prj = pre_text + '\n' + new_grid + '\n                ' + post_text
# Update / 09 to / 07 in case it was missed, and fix total counter if any.
final_prj = final_prj.replace('/ 09', '/ 07')

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(final_prj)

print("Updates successful")
