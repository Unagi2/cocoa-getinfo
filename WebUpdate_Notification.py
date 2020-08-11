import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os.path
import COCOA_Analysis

my_path = os.path.abspath(os.path.dirname(__file__))
# 当「WebUpdate_Notification.py」のスクリプト自体を毎分おきに実行する

def web_update():
    # データlog
    #web_log = r"log_pool\web_data_log.txt"
    file_path = os.path.join(my_path,r".\log_pool\web_data_log.txt")
    # 監視対象URL
    load_url = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html"

    # Webページを取得して解析する
    html = requests.get(load_url)
    html.raise_for_status()
    soup = BeautifulSoup(html.content, "html.parser")

    chap2 = soup.find(class_="m-grid__col1")    # idが「chap2」を検索
    for element in chap2.find_all('img'):    # その中のimgタグの文字列を表示
        imgcode = element['src']
        imgcode_clear = imgcode.replace('data:image/png;base64,', '')
        str_imgcode = str(imgcode_clear)

    try:
        file_log = open(file_path, 'r', encoding='utf-8')
        old_data = file_log.read()
    except:
        old_data = ' '

    if(str_imgcode == old_data):
        print("[不検知]")
        return False
    else:
        file_log = open(file_path, 'w', encoding='utf-8')
        file_log.writelines(str_imgcode)
        file_log.close()
        return True

if __name__ == "__main__":
    print("\nWeb更新の監視スクリプト開始\n")

    if(web_update()):
        #更新通知
        print("\n[！！更新検知！！]\n")

        # 現在時刻取得
        genzai = datetime.now()
        str_now = genzai.strftime('%Y/%m/%d %H:%M')
        print("検知時刻:" + str_now + "\n")

        #更新作業実行
        COCOA_Analysis.main_process()


    print("\n監視スクリプト終了\n")
