# update_skills.py

import os

# 1. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

old_avatar = '<div class="avatar-inner">🧑‍💻</div>'
new_avatar = '<div class="avatar-inner" style="overflow: hidden;"><img src="programmer.jpeg" alt="Programmer" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;"></div>'

about_content = about_content.replace(old_avatar, new_avatar)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)


# 2. Update skills.html
with open('skills.html', 'r', encoding='utf-8') as f:
    skills_content = f.read()

# Replace language bars
lang_bars = """                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">Java</span><span
                                class="skill-bar-pct">85%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill" data-width="85"></div>
                        </div>
                    </div>
                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">Python</span><span
                                class="skill-bar-pct">80%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill" data-width="80"></div>
                        </div>
                    </div>
                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">JavaScript (ES6+)</span><span
                                class="skill-bar-pct">80%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill" data-width="80"></div>
                        </div>
                    </div>"""
lang_pills = """                    <div class="skill-pills">
                        <span class="pill">Java</span>
                        <span class="pill">Python</span>
                        <span class="pill">JavaScript (ES6+)</span>
                    </div>"""
skills_content = skills_content.replace(lang_bars, lang_pills)

# Replace web bars
web_bars = """                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">HTML5</span><span
                                class="skill-bar-pct">95%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill" data-width="95"></div>
                        </div>
                    </div>
                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">CSS3</span><span
                                class="skill-bar-pct">90%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill" data-width="90"></div>
                        </div>
                    </div>
                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">Streamlit</span><span
                                class="skill-bar-pct">75%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill purple" data-width="75"></div>
                        </div>
                    </div>"""
web_pills = """                    <div class="skill-pills">
                        <span class="pill">HTML5</span>
                        <span class="pill">CSS3</span>
                        <span class="pill">Streamlit</span>
                    </div>"""
skills_content = skills_content.replace(web_bars, web_pills)

# Replace AI bars
ai_bars = """                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">LangChain</span><span
                                class="skill-bar-pct">75%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill purple" data-width="75"></div>
                        </div>
                    </div>
                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">WebRTC / P2P</span><span
                                class="skill-bar-pct">70%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill purple" data-width="70"></div>
                        </div>
                    </div>
                    <div class="skill-bar-item">
                        <div class="skill-bar-header"><span class="skill-bar-name">Web Crypto API</span><span
                                class="skill-bar-pct">72%</span></div>
                        <div class="bar-track">
                            <div class="bar-fill purple" data-width="72"></div>
                        </div>
                    </div>"""
ai_pills = """                    <div class="skill-pills">
                        <span class="pill">LangChain</span>
                        <span class="pill">WebRTC / P2P</span>
                        <span class="pill">Web Crypto API</span>
                    </div>"""
skills_content = skills_content.replace(ai_bars, ai_pills)

# Replace emojis
emojis_map = {
    "🧩": '<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19.439 7.85c-.049.322.059.648.289.878l1.568 1.568c.47.47.706 1.087.706 1.704s-.235 1.233-.706 1.704l-1.611 1.611a.98.98 0 0 1-.837.276c-.47-.07-.802-.48-.968-.925a2.501 2.501 0 1 0-3.214 3.214c.446.166.855.497.925.968a.979.979 0 0 1-.276.837l-1.61 1.611c-.47.47-1.088.706-1.705.706s-1.234-.236-1.704-.706l-1.568-1.568a1.026 1.026 0 0 0-.877-.29c-.493.074-.84.504-1.02.953a2.499 2.499 0 0 1-3.214-3.214c.449-.18.879-.527.953-1.02.049-.322-.059-.648-.289-.878l-1.568-1.568c-.47-.47-.706-1.087-.706-1.704s.235-1.233.706-1.704l1.611-1.611a.98.98 0 0 1 .837-.276c.47.07.802.48.968.925a2.501 2.501 0 1 0 3.214-3.214c-.446-.166-.855-.497-.925-.968a.979.979 0 0 1 .276-.837l1.61-1.611c.47-.47 1.088-.706 1.705-.706s1.234.236 1.704.706l1.568 1.568c.23.23.556.338.877.29.493-.074.84-.504 1.02-.953A2.499 2.499 0 0 1 18.42 4.2c-.449.18-.879.527-.953 1.02Z"></path></svg>',
    "🤝": '<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    "⏱️": '<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>',
    "🔄": '<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>'
}

for emoji, svg in emojis_map.items():
    skills_content = skills_content.replace(emoji, svg)
    # in case of missing variation selector
    skills_content = skills_content.replace(emoji.strip('\uFE0F'), svg)

with open('skills.html', 'w', encoding='utf-8') as f:
    f.write(skills_content)

print("Updates successful")
