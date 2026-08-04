import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render():
    with open("data/contributions.json", "r", encoding="utf-8") as f:
        days = json.load(f)

    width = 860
    height = 140
    box_size = 10
    gap = 3

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
    svg += '<rect width="100%" height="100%" fill="#0d1117" rx="6" />\n'
    svg += '<g transform="translate(15, 20)">\n'

    for idx, day in enumerate(days):
        week = idx // 7
        day_of_week = idx % 7
        x = week * (box_size + gap)
        y = day_of_week * (box_size + gap)
        color = PALETTE[min(day['level'], 5)]
        
        svg += f'  <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" rx="2" />\n'

    svg += '</g>\n</svg>'

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("contrib-heatmap.svg oluşturuldu!")

if __name__ == "__main__":
    render()