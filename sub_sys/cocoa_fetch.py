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
    #soup = BeautifulSoup(html.content, "html.parser")
    soup = BeautifulSoup(html.content, "lxml")


    #img_select = soup.select_one('#content > div.l-contentBody > div > div.l-contentMain > div:nth-child(4) > div > p:nth-child(7) > img')
    #img_select = soup.select('#content')
    img_select = soup.select('#content > div.l-contentBody > div > div.l-contentMain > div:nth-of-type(3) > div > p:nth-of-type(5) > img')
    # > div.l-contentBody > div > div.l-contentMain > div:nth-of-type(4) > div > p:nth-of-type(9) > img
    #img_select = soup.find_all('img')
    img_select = img_select[0].attrs['src']
    #imgcode_fit = img_select.replace('data:image/png;base64,', '')
    
    print(img_select)
    

    file_name_dy = os.path.normpath(os.path.join(os.path.dirname(
            __file__), '../getIMG_pool/cocoa_info_' + str_date + '.png'))
            
            
    if 'base64' in img_select:
        #base64
        img_decode = base64.b64decode(imgcode_fit.encode())
        
        with open(file_name_dy, "wb") as aaa:
            aaa.write(img_decode)
    
    elif '.png' in img_select:
        #png 
        img =  "https://www.mhlw.go.jp"  + img_select
    
        url =  img
        dst_path = file_name_dy
        download_file(url, dst_path)
    
    elif '.jpg' in img_select:
        #png 
        img =  "https://www.mhlw.go.jp"  + img_select
    
        url =  img
        dst_path = file_name_dy
        download_file(url, dst_path)
        
    else:
        print('error')
    

    
    """
    # IDで検索し、その中のすべてのliタグを検索して表示する
    # 要素 = soup.find(class_="class名")
    # 「class」はPythonの予約語でそのままでは使えないので「class_」と書く。
    chap2 = soup.find(class_="m-grid__col1")    # idが「chap2」を検索
    for element in chap2.find_all('data:image/png;base64'):    # その中のimgタグの文字列を表示

        
        imgcode = element['src']
        #imgcode = element[1].attrs['src']
        imgcode_clear = imgcode.replace('data:image/png;base64,', '')
        # print(element['src'])
        print(imgcode_clear)

        #base64
        img = base64.b64decode(imgcode_clear.encode())
        #png 
        #img =  "https://www.mhlw.go.jp"  + imgcode
        

        # 取得画像保存
        #file_name_dy = os.path.join(my_path, r"..\getIMG_pool\cocoa_info_" + str_date + r".png")
        file_name_dy = os.path.normpath(os.path.join(os.path.dirname(
            __file__), '../getIMG_pool/cocoa_info_' + str_date + '.png'))
        
        with open(file_name_dy, "wb") as aaa:
            aaa.write(img)
            
        #url =  img
        #dst_path = file_name_dy
        #download_file(url, dst_path)
    """
    print("[Completed!]\n")


if __name__ == "__main__":
    fetch_image()
