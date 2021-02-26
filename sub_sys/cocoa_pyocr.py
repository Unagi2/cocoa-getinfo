# -*- coding: utf-8 -*-
from datetime import datetime
from PIL import Image
import pyocr
import os
import os.path
import re
# インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
# OS自体に設定してあれば以下の2行は不要
path = 'C:\\Program Files\\Tesseract-OCR'
os.environ['PATH'] = os.environ['PATH'] + path

my_path = os.path.abspath(os.path.dirname(__file__))


def py_ocr():

    print("[2/5 Processing OCR...]\n")

    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    #file_name_dy = os.path.join(my_path, r"..\getIMG_pool\cocoa_info_" + str_date + r".png")
    file_name_dy = os.path.normpath(os.path.join(os.path.dirname(__file__), '../getIMG_pool/cocoa_info_' + str_date + '.png'))
    #file_name_dy = os.path.normpath(os.path.join(os.path.dirname(__file__), '../getIMG_pool/cocoa_info_0901.png'))

    # pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    tool = tools[0]

    # OCR対象の画像ファイルを読み込む
    img_in = Image.open(file_name_dy)
    img_out = img_in.crop((50, 50, 320, 160))
    img = img_out.resize((880,330), resample=Image.LANCZOS) #270*110
    
    # 画像を読みやすいように加工。
    """
    img = img.convert('RGB')
    size = img.size
    img2 = Image.new('RGB', size)

    border = 110

    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = img.getpixel((x, y))
            if r > border or g > border or b > border:
                r = 255
                g = 255
                b = 255
                img2.putpixel((x, y), (r, g, b))
    """
    
    img_rgb = img.convert("RGB")
    pixels = img_rgb.load()            
    c_max = 159 #169
    for j in range(img_rgb.size[1]):
        for i in range(img_rgb.size[0]):
            if (pixels[i, j][0] > c_max or pixels[i, j][1] > c_max or
                    pixels[i, j][0] > c_max):
                pixels[i, j] = (255, 255, 255)
    img_rgb.save('/home/pi/Desktop/img_rgb.png')
    

    # 画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    text = tool.image_to_string(img_rgb, lang="jpn", builder=builder)

    print("\n" + text + "\n")
    #result = re.sub('[^0-9]','', text)
    new_text = re.sub(r"[a-z]", "", text.lower())
    print("\n" + new_text + "\n")

    #log_path = os.path.join(my_path, r"..\log_pool\log.txt")
    log_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/log.txt'))

    with open(log_path, 'w', encoding="utf_8") as f:
        print(new_text, file=f)
        f.write('\n')

    print("[Completed!]\n")


if __name__ == "__main__":
    py_ocr()
