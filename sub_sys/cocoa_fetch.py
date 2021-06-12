# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import base64
from datetime import datetime 
import urllib.error
import urllib.request

import os.path
my_path = os.path.abspath(os.path.dirname(__file__))

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)
        
def fetch_image():

    print("\n[1/5 Processing image acquisition...]\n")

    # 時刻取得
    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    headers = {
        'User-Agent': '[COCOA-App Usage Status] I am scraping for the purpose of obtaining App information.',
        'From': '30.unagi@gmail.com'  # This is another valid field
    }

    # Webページを取得して解析する
    load_url = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html"
    html = requests.get(load_url, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")

    # IDで検索し、その中のすべてのliタグを検索して表示する
    # 要素 = soup.find(class_="class名")
    # 「class」はPythonの予約語でそのままでは使えないので「class_」と書く。
    chap2 = soup.find(class_="m-grid__col1")    # idが「chap2」を検索
    for element in chap2.find_all('img'):    # その中のimgタグの文字列を表示
        imgcode = element['src']
        imgcode_clear = imgcode.replace('data:image/png;base64,', '')
        # print(element['src'])
        # print(imgcode_clear)

        #img = base64.b64decode(imgcode_clear.encode())
        img =  "https://www.mhlw.go.jp"  + imgcode
        

        # 取得画像保存
        #file_name_dy = os.path.join(my_path, r"..\getIMG_pool\cocoa_info_" + str_date + r".png")
        file_name_dy = os.path.normpath(os.path.join(os.path.dirname(
            __file__), '../getIMG_pool/cocoa_info_' + str_date + '.png'))
        
        #with open(file_name_dy, "wb") as aaa:
        #    aaa.write(img)
            
        url =  img
        dst_path = file_name_dy
        download_file(url, dst_path)

    print("[Completed!]\n")


if __name__ == "__main__":
    fetch_image()
