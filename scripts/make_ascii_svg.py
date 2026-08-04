from PIL import Image

RAMP = " .`:-=+*cs#%@"  # Açık renkten koyuya ASCII karakter skalası

def image_to_ascii(img_path, width=100):
    img = Image.open(img_path).convert('L')
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, height))
    
    pixels = img.getdata()
    ascii_str = ""
    for i, pixel in enumerate(pixels):
        ascii_str += RAMP[pixel // 22]
        if (i + 1) % width == 0:
            ascii_str += "\n"
    return ascii_str.splitlines()

def generate_svg():
    lines = image_to_ascii("source-prepped.png")
    line_height = 14
    width = 370
    height = len(lines) * line_height + 20
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
    svg += '<style>\n'
    svg += '  .ascii { font-family: monospace; font-size: 10px; fill: #c9d1d9; white-space: pre; }\n'
    svg += '  @keyframes type { from { width: 0; } to { width: 100%; } }\n'
    svg += '  .line { overflow: hidden; display: inline-block; animation: type 0.05s steps(40, end) forwards; }\n'
    svg += '</style>\n'
    svg += '<rect width="100%" height="100%" fill="#0d1117" rx="6" />\n'
    svg += f'<text x="15" y="20" class="ascii">\n'
    
    for i, line in enumerate(lines):
        delay = i * 0.03
        svg += f'<tspan x="15" dy="{line_height if i > 0 else 0}" style="animation: type 0.2s ease-out {delay}s both;">{line}</tspan>\n'
        
    svg += '</text>\n</svg>'
    
    with open("avi-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("avi-ascii.svg oluşturuldu!")

if __name__ == "__main__":
    generate_svg()