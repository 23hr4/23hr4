import sys
import cv2
import numpy as np
from rembg import remove
from PIL import Image

def prep(input_path):
    # 1. Arka planı sil
    with open(input_path, 'rb') as f:
        img_bytes = f.read()
    output_bytes = remove(img_bytes)
    
    # 2. Gri tonlamaya çevir ve CLAHE kontrast uygula
    nparr = np.frombuffer(output_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    
    alpha = img[:, :, 3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # 3. Beyaz arka plana oturt
    white_bg = np.ones_like(enhanced) * 255
    final_img = np.where(alpha > 10, enhanced, white_bg)
    
    cv2.imwrite("source-prepped.png", final_img)
    print("source-prepped.png başarıyla oluşturuldu!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prep(sys.argv[1])
    else:
        print("Kullanım: python scripts\\prep_photo.py foto.jpg")