import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os.path
import COCOA_Analysis
import COCOA_Analysis_holiday
import holiday
import time

my_path = os.path.abspath(os.path.dirname(__file__))
# 当「WebUpdate_Notification.py」のスクリプト自体を毎分おきに実行する

genzai = datetime.now()
DATE = genzai.strftime('%Y%m%d')

def web_update():
    # データlog
    #web_log = r"log_pool\web_data_log.txt"
    file_path = os.path.join(my_path,r".\log_pool\web_data_log.txt")

    #接続する側の連絡先を明記（連絡先の使い回しは認めない。必ず変更すること）
    headers = {
    'User-Agent': '[COCOA-App Usage Status] I am scraping for the purpose of obtaining App information.',
    'From': '30.unagi@gmail.com'  # This is another valid field
    }

    # 監視対象URL
    load_url = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html"

    # Webページを取得して解析する
    html = requests.get(load_url,headers=headers)
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
        print("[不検知]\n")
        return False
    else:
        file_log = open(file_path, 'w', encoding='utf-8')
        file_log.writelines(str_imgcode)
        file_log.close()
        return True

if __name__ == "__main__":
    count = 0
    total = 1   #Loop End triger
    triger = 0 #Max Time Count
    print("\nholiday.py Start process\n")

    if(holiday.isBizDay(DATE) == 1):    #Weekday=1
        print("Weekday Mode\n")
        print("\nWeb更新チェック開始\n")

        while count < 1 and triger < 12:
            print(triger*5, "分経過\n")
            print(triger+1,"/6回目の検知\n")

            if(web_update()):
                #更新通知
                print("\n[！！更新検知！！]\n")

                # 現在時刻取得
                # genzai = datetime.now()
                str_now = genzai.strftime('%Y/%m/%d %H:%M')
                print("検知時刻:" + str_now + "\n")

                #更新作業実行
                COCOA_Analysis.main_process()

                #検知成功条件ではループ中断
                #break
                count += 1
                continue

            #Interval
            time.sleep(300)    #1sec/60sec=1min/300sec=5min/600sec=10min
            triger += 1
        else:
            print("\n更新チェック終了\n")

    elif(holiday.isBizDay(DATE) == 0):  #Holiday=0
        print("[Holiday Mode]\n")

        #更新作業実行
        print("\n休日用データの出力開始\n")

        COCOA_Analysis_holiday.main_process()

        print("\n休日用データの出力終了\n")

    else:   #Error
        print("Error-holiday.py ~All Processing Stopped!!~")

    print("\nholiday.py END process\n")
"""
    while count < 1 and triger < 45:
        print(triger*5, "分経過\n")
        print(triger+1,"/6回目の検知\n")

        if(web_update()):
            #更新通知
            print("\n[！！更新検知！！]\n")

            # 現在時刻取得
            # genzai = datetime.now()
            str_now = genzai.strftime('%Y/%m/%d %H:%M')
            print("検知時刻:" + str_now + "\n")

            #更新作業実行
            COCOA_Analysis.main_process()

            #検知成功条件ではループ中断
            #break
            count += 1
            continue

        #Interval
        time.sleep(60)    #1sec/60sec=1min/300sec=5min/600sec=10min
        triger += 1
    else:
        print("\n更新チェック終了\n")
"""
