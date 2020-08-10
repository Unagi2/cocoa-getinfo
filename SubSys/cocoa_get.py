import requests
from bs4 import BeautifulSoup
import base64
from datetime import datetime
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))

def get_image():

    print("\n[Processing image acquisition...]\n")

    # 時刻取得
    genzai = datetime.now()
    str_date = genzai.strftime('%m%d')

    # Webページを取得して解析する
    load_url = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    # IDで検索し、その中のすべてのliタグを検索して表示する
    chap2 = soup.find(class_="m-grid__col1")    # idが「chap2」を検索
    for element in chap2.find_all('img'):    # その中のliタグの文字列を表示
        imgcode = element['src']
        imgcode_clear = imgcode.replace('data:image/png;base64,', '')
        # print(element['src'])
        # print(imgcode_clear)

        img = base64.b64decode(imgcode_clear.encode())
        # f = open(r"C:\Users\KITAKAMI\Desktop\web_python\infoimg.png", 'bw')
        # f.write(img)

        # 取得画像保存
        # file_name_dy = r'..\getIMG_pool\cocoa_info_' + str_date + r'.png'
        file_name_d = os.path.join(my_path, r"..\getIMG_pool\cocoa_info_" + str_date + r".png")
        with open(file_name_dy, "wb") as aaa:
            aaa.write(img)
            #要素 = soup.find(class_="class名")
            # 「class」はPythonの予約語でそのままでは使えないので「class_」と書きます。

    print("[Image acquisition processing completed]\n")
