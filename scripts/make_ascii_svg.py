from PIL import Image

# Siyah arkaplan ve koyu renkler boşluk (şeffaf), beyaz kısımlar yoğun karakter olacak (12 karakter)
RAMP = "   ..-=+*#%@"

def image_to_ascii(img_path, width_chars=100):
    img = Image.open(img_path).convert('L')
    aspect_ratio = img.height / img.width
    
    # Karakter boyutlarına göre en-boy oranını (0.6) hesaba katıyoruz ki kare ezilmesin
    height_chars = int(width_chars * aspect_ratio * 0.6)
    img = img.resize((width_chars, height_chars))
    
    pixels = img.getdata()
    ascii_str = ""
    for i, pixel in enumerate(pixels):
        index = pixel // 22
        if index >= len(RAMP): index = len(RAMP) - 1
        ascii_str += RAMP[index]
        if (i + 1) % width_chars == 0:
            ascii_str += "\n"
    return ascii_str.splitlines()

def generate_svg():
    lines = image_to_ascii("source-prepped.png", width_chars=100)
    
    font_size = 12
    line_height = 12
    char_width = 7.2
    
    # İç çözünürlüğü yüksek tutarak (viewBox) GitHub'ın dış çerçevesine (width=370) sığdırıyoruz
    internal_width = int(100 * char_width) + 40
    internal_height = len(lines) * line_height + 40
    
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="370" viewBox="0 0 {internal_width} {internal_height}">\n'
    svg += '<style>\n'
    svg += f'  .ascii {{ font-family: monospace; font-size: {font_size}px; fill: #c9d1d9; white-space: pre; }}\n'
    svg += '  @keyframes type { from { width: 0; } to { width: 100%; } }\n'
    svg += '  .line { overflow: hidden; display: inline-block; animation: type 0.05s steps(40, end) forwards; }\n'
    svg += '</style>\n'
    svg += '<rect width="100%" height="100%" fill="#0d1117" rx="10" />\n'
    svg += f'<text x="20" y="30" class="ascii">\n'
    
    for i, line in enumerate(lines):
        delay = i * 0.02
        svg += f'<tspan x="20" dy="{line_height if i > 0 else 0}" style="animation: type 0.15s ease-out {delay}s both;">{line}</tspan>\n'
        
    svg += '</text>\n</svg>'
    
    with open("avi-ascii.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("avi-ascii.svg oluşturuldu!")

if __name__ == "__main__":
    generate_svg()