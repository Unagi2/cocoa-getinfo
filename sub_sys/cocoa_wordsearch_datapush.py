# -*- coding: utf-8 -*-
import sys
import re
from datetime import datetime

# csv処理
import csv
# google sheetの前処理
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# パス
import os.path


def search_and_push(set):

    print("[3/5 Processing data extraction and output... ]\n")

    my_path = os.path.abspath(os.path.dirname(__file__))
    # google Sheet前処理
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # 秘密鍵（JSONファイル）のファイル名を入力
    #target_path_1 = os.path.join(os.path.dirname(__file__), '..\key_pool\google_api.json')
    path_api = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../key_pool/google_api.json'))
    #path_api = os.path.normpath(target_path_1)
    #path_api = os.path.join(my_path, r"..\key_pool\google_api.json")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        path_api, scope)
    gc = gspread.authorize(credentials)

    # 入出力のパス
    #input_path = os.path.join(my_path, r"..\log_pool\log.txt")
    input_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/log.txt'))
    #output_path = os.path.join(my_path, r"..\log_pool\download.txt")
    output_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/download.txt'))
    #output_path2 = os.path.join(my_path, r"..\log_pool\positive.txt")
    output_path2 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/positive.txt'))
    output_path3 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/download_increment.txt'))
    output_path4 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/positive_increment.txt'))

    # ファイル読み込みと改行コード削除
    f = open(input_path, 'r', encoding='utf-8')
    
    lines = f.readlines()
    f.close()
    
    f= [line.strip() for line in lines]
    f = [a for a in f if a != '']

    #Allf = f.read()

    #text = Allf.replace('\n', '')
    #text = text.replace('\r', '')
    #text = text.replace(' ', '')
    print(f)
    
    #read_data_line = f.readlines
    #print(read_data_line)
    
    #f1 = f.readline()
    f1 = str(f[0])
    #f1 = f.read().splitlines()
    
    #f2 = f.readline()
    f2 = str(f[1])
    #f2 = f.read().splitlines()
    print(f1)
    print(f2)

    #f.close()

    # 現在時刻取得
    genzai = datetime.now()

    # 時間取得
    str_date = genzai.strftime('%Y/%m/%d')

    # リリース日からの経過日数
    today = datetime.now() - datetime(2020, 6, 19)
    # print(today.days)

    # Spreadsheet用日付取得（テスト用）
    #today_gs = "=today()"

    # ワード検索及びデータの抽出処理
    # 重要処理のため、原文の書式変更に合わせる必要あり（数字の前後）
    regex = re.compile('\d{3,}')

    if set == 1:
        # ダウンロードデータの抽出
        try:
            '''
            found = re.search('ダウンロード数は、' + genzai.strftime('%m').lstrip("0") + '月' + genzai.strftime('%d').lstrip("0") +
                            '日17:00時点、合計で約(.+?)万件です。', text).group(1)
            '''
            for line in open(input_path, 'r', encoding='utf-8'):
                if "ダウンロード数" in line.replace(' ', ''):
                    line = line.replace(' ', '').translate(
                        str.maketrans({',': '', '.': ''}))
                    match = regex.findall(line.replace(' ', ''))
                    found = match[0]
                    # print(line)
                    print(match[0])
                
                if f1 is not None:
                    f1 = f1.replace(' ', '').translate(
                        str.maketrans({',': '', '.': ''}))
                    match = regex.findall(f1.replace(' ', ''))
                    found = match[0]
                    # print(line)
                    #print(match)
                    print(match[0])
                    break
                    

        except:
            # AAA, ZZZ not found in the original string
            found = 'N/A'  # apply your error handling

        # 陽性登録件数データの抽出
        try:
            '''
            found2 = re.search('陽性登録件数は、' + genzai.strftime('%m').lstrip("0") + '月' + genzai.strftime('%d').lstrip("0") +
                            '日17:00時点、合計で(.+?)件です。', text).group(1)
            '''
            for line in open(input_path, 'r', encoding='utf-8'):
                if "陽性登録件数" in line.replace(' ', ''): # 陽性登録件数
                    line2 = line.replace(' ', '').translate(
                        str.maketrans({',': '', '.': ''}))
                    match2 = regex.findall(line2.replace(' ', ''))
                    found2 = match2[0]
                    # print(line2)
                    print(match2[0])
                    
                if f2 is not None:
                    f2 = f2.replace(' ', '').translate(
                        str.maketrans({',': '', '.': ''}))
                    match2 = regex.findall(f2.replace(' ', ''))
                    found2 = match2[0]
                    # print(line2)
                    print(match2[0])
                    break

        except:
            # AAA, ZZZ not found in the original string
            found2 = 'N/A'  # apply your error handling
            # sample-code:print(int('10,000'.replace(',', '')))
    else:
        found = 'N/A'
        found2 = 'N/A'
    
    # googleスプレッドシートに追加処理と各種値更新
    if found == 'N/A' and found2 == 'N/A':  # 追加処理のみ更新無
        print("\nデータ取得日 : " + str_date + "\n")
        print("Mode : 土日祝日処理\n")
        print("ダウンロード数 : " + found + "\n")
        print("陽性者登録数 : " + found2 + "\n")
        print("経過日数 : " + str(today.days))

        # csv出力
        #path_log = os.path.join(my_path, r"..\log_pool\cocoa_data.csv")
        path_log = os.path.normpath(os.path.join(
            os.path.dirname(__file__), '../log_pool/cocoa_data.csv'))

        with open(path_log, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(
                [today.days, str_date, found, found2, "N/A", "N/A"])

        # N/Aのsheet追加
        # 「キー」でワークブックを取得
        SPREADSHEET_KEY = '1mq_yfYhArPPoL_n3zNZSoL_dMaxGLMmBkVnM3gcJGgM'
        wb = gc.open_by_key(SPREADSHEET_KEY)
        ws = wb.sheet1

        # 複数のセルに値を入力（1行のみ）
        datas = [today.days, str_date, found, found2, "N/A", "N/A"]
        ws.append_row(datas, value_input_option='USER_ENTERED')
        # value_input_option (str) – (optional) Determines how input data should be interpreted. Possible values are RAW or USER_ENTERED.

    else:   # データ更新処理
        print("\nデータ取得日 : " + str_date + "\n")
        print("Mode : データ更新処理\n")
        print("ダウンロード数 : " + found + "\n")
        print("陽性者登録数 : " + found2 + "\n")
        print("経過日数 : " + str(today.days))

        # 文字列のint化と数値整形
        ffound = int(re.sub("\\D", "", found))
        # print(ffound)

        ffound2 = int(re.sub("\\D", "", found2))
        # print(ffound2)

        # 前回データとの差
        y1 = open(output_path, 'r', encoding='utf-8')
        yy1 = y1.read()
        first_line = yy1.split('\n', 1)[0]
        y2 = open(output_path2, 'r', encoding='utf-8')
        yy2 = y2.read()
        first_line2 = yy2.split('\n', 1)[0]

        dx1 = ffound - int(first_line)
        dx2 = ffound2 - int(first_line2)
        #dx1 = ffound - int(yy1.replace(',', ''))
        #dx1 = ffound - int(yy1.translate(str.maketrans({',': None, '.': None})))
        #dx2 = ffound2 - int(yy2.replace('.', ''))
        #dx2 = ffound2 - int(yy2.translate(str.maketrans({',': None, '.': None})))

        # print(dx1)
        # print(dx2)

        # csv出力
        #path_log = os.path.join(my_path, r"..\log_pool\cocoa_data.csv")
        path_log = os.path.normpath(os.path.join(
            os.path.dirname(__file__), '../log_pool/cocoa_data.csv'))

        with open(path_log, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([today.days, str_date, ffound, ffound2, dx1, dx2])

        # 新たな値のsheet追加
        # 「キー」でワークブックを取得
        SPREADSHEET_KEY = '1mq_yfYhArPPoL_n3zNZSoL_dMaxGLMmBkVnM3gcJGgM'
        wb = gc.open_by_key(SPREADSHEET_KEY)
        ws = wb.sheet1

        # 複数のセルに値を入力（1行のみ）
        datas = [today.days, str_date, ffound, ffound2, dx1, dx2]
        ws.append_row(datas, value_input_option='USER_ENTERED')

        # データ記録用日付
        str_genzai = genzai.strftime('%Y/%m/%d %H:%M')

        # 前回データの更新処理
        with open(output_path, mode='w', encoding='utf-8') as f:
            #f.write(str_genzai + ':')
            f.writelines(found)

        with open(output_path2, mode='w', encoding='utf-8') as f:
            #f.write(str_genzai + ':')
            f.writelines(found2)
            # f.write('\n')
        
        with open(output_path3, mode='w', encoding='utf-8') as f:
            #f.write(str_genzai + ':')
            f.writelines(str(dx1))
        
        with open(output_path4, mode='w', encoding='utf-8') as f:
            #f.write(str_genzai + ':')
            f.writelines(str(dx2))
    
    print("\n[Completed!]\n")


if __name__ == "__main__":
    search_and_push(1)
