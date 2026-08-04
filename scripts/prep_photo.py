import sys
import cv2
import numpy as np
from rembg import remove
from PIL import Image

def prep(input_path):
    with open(input_path, 'rb') as f:
        img_bytes = f.read()
    output_bytes = remove(img_bytes)
    
    nparr = np.frombuffer(output_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    
    alpha = img[:, :, 3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # Maske beyaz olduğu için arkaplanı SİYAH (0) yapıyoruz ki ikisi birbirine karışmasın
    black_bg = np.zeros_like(enhanced)
    final_img = np.where(alpha > 10, enhanced, black_bg)
    
    cv2.imwrite("source-prepped.png", final_img)
    print("source-prepped.png başarıyla oluşturuldu!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prep(sys.argv[1])
    else:
        print("Kullanım: python scripts\\prep_photo.py foto.jpg")