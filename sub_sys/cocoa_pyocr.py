from datetime import datetime
from PIL import Image
import pyocr
import os
import os.path
# インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
# OS自体に設定してあれば以下の2行は不要
path = 'C:\\Program Files\\Tesseract-OCR'
os.environ['PATH'] = os.environ['PATH'] + path

my_path = os.path.abspath(os.path.dirname(__file__))


def py_ocr():

    print("[2/5 Processing OCR...]\n")

    genzai = datetime.now()
    str_date = genzai.strftime('%m%d')

    file_name_dy = os.path.join(
        my_path, r"..\getIMG_pool\cocoa_info_" + str_date + r".png")

    # pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    tool = tools[0]

    # OCR対象の画像ファイルを読み込む
    img = Image.open(file_name_dy)

    # 画像を読みやすいように加工。
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

    # 画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    text = tool.image_to_string(img2, lang="jpn", builder=builder)

    print("\n" + text + "\n")

    log_path = os.path.join(my_path, r"..\log_pool\log.txt")
    with open(log_path, 'w', encoding="utf_8") as f:
        print(text, file=f)
        f.write('\n')

    print("[Completed!]\n")


if __name__ == "__main__":
    py_ocr()