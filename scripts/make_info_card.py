def generate_info_card():
    width = 490
    height = 300
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
  .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1; rx: 6px; }}
  .title {{ font-family: monospace; font-size: 14px; fill: #58a6ff; font-weight: bold; }}
  .label {{ font-family: monospace; font-size: 12px; fill: #79c0ff; font-weight: bold; }}
  .text {{ font-family: monospace; font-size: 12px; fill: #c9d1d9; }}
  .line {{ animation: fadeIn 0.5s ease-in forwards; opacity: 0; }}
  @keyframes fadeIn {{ to {{ opacity: 1; }} }}
</style>
<rect width="100%" height="100%" class="bg" />
<text x="20" y="35" class="title">23hr4@github-pc</text>
<line x1="20" y1="45" x2="470" y2="45" stroke="#30363d" stroke-width="1" />

<g class="line" style="animation-delay: 0.2s"><text x="20" y="75" class="label">Name:</text><text x="100" y="75" class="text">Fatuma Zehra Erdem</text></g>
<g class="line" style="animation-delay: 0.4s"><text x="20" y="105" class="label">Edu:</text><text x="100" y="105" class="text">Istanbul Technical University</text></g>
<g class="line" style="animation-delay: 0.6s"><text x="20" y="135" class="label">Stack:</text><text x="100" y="135" class="text">C/C++, Python, React, Node.js</text></g>
<g class="line" style="animation-delay: 0.8s"><text x="20" y="165" class="label">Interests:</text><text x="100" y="165" class="text">UI/UX Design, Board Games</text></g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("info-card.svg oluşturuldu!")

if __name__ == "__main__":
    generate_info_card()