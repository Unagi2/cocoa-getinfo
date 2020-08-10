import sys
import re
from datetime import datetime

# csv処理
import csv
# google sheetの前処理
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#パス
import os.path


def search_and_push():

    print("[Processing data extraction and output... ]\n")

    my_path = os.path.abspath(os.path.dirname(__file__))
    # google Sheet前処理
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # 秘密鍵（JSONファイル）のファイル名を入力
    path_api = os.path.join(my_path, r"..\key_pool\google_api.json")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        path_api, scope)
    gc = gspread.authorize(credentials)

    # 入出力のパス
    input_path = os.path.join(my_path, r"..\log_pool\log.txt")
    output_path = os.path.join(my_path, r"..\log_pool\download.txt")
    output_path2 = os.path.join(my_path, r"..\log_pool\positive.txt")

    # ファイル読み込みと改行コード削除
    f = open(input_path, 'r', encoding='utf-8')
    Allf = f.read()

    text = Allf.replace('\n', '')
    text = text.replace('\r', '')
    print(text)

    f.close()

    # with open(input_path, mode='r',encoding='utf-8') as file:
    #clear = file.replace('\n','')
    # print(clear)
    genzai = datetime.now()

    # ワード検索及びデータの抽出処理
    # 重要処理のため、原文の書式変更に合わせる必要あり（数字の前後）

    # ダウンロードデータの抽出
    try:
        found = re.search('ダウンロード数は、8月' + genzai.strftime('%d').lstrip("0") +
                          '日17:00現在、合計で約(.+?)万件です。', text).group(1)
    except AttributeError:
        # AAA, ZZZ not found in the original string
        found = 'N/A'  # apply your error handling

    # 陽性登録件数データの抽出
    try:
        found2 = re.search('陽性登録件数は、8月' + genzai.strftime('%d').lstrip("0") +
                           '日17:00現在、合計で(.+?)件です。', text).group(1)
    except AttributeError:
        # AAA, ZZZ not found in the original string
        found2 = 'N/A'  # apply your error handling
        # sample-code:print(int('10,000'.replace(',', '')))

    # 時間取得
    str_date = genzai.strftime('%m/%d')

    # リリース日からの経過日数
    today = datetime.now() - datetime(2020, 6, 19)
    # print(today.days)

    # googleスプレッドシートに追加処理と各種値更新
    if found is 'N/A' and found2 is 'N/A':
        print("\nデータ取得日 : " + str_date + "\n")
        print("Mode : 土日祝日処理\n")
        print("ダウンロード数 : " + found + "\n")
        print("陽性者登録数 : " + found2 + "\n")
        print("経過日数 : " + str(today.days))

        # csv出力
        path_log = os.path.join(my_path, r"..\log_pool\cocoa_data.csv")
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
        ws.append_row(datas)
    else:
        print("\nデータ取得日 : " + str_date + "\n")
        print("Mode : データ更新処理\n")
        print("ダウンロード数 : " + found + "\n")
        print("陽性者登録数 : " + found2 + "\n")
        print("経過日数 : " + str(today.days))

        # 文字列のint化
        ffound = int(found.replace('.', ''))  # カンマやピリオド消去
        ffound2 = int(found2.replace('.', ''))

        # 前回データとの差
        y1 = open(output_path, 'r', encoding='utf-8')
        yy1 = y1.read()
        y2 = open(output_path2, 'r', encoding='utf-8')
        yy2 = y2.read()

        dx1 = ffound - int(yy1.replace('.', ''))
        dx2 = ffound2 - int(yy2.replace('.', ''))
        # print(dx1)

        # csv出力
        path_log = os.path.join(my_path, r"..\log_pool\cocoa_data.csv")
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
        ws.append_row(datas)

        str_genzai = genzai.strftime('%Y/%m/%d %H:%M')

        # 前回データの更新処理
        with open(output_path, mode='w', encoding='utf-8') as f:
            #f.write(str_genzai + ':')
            f.writelines(found)

        with open(output_path2, mode='w', encoding='utf-8') as f:
            #f.write(str_genzai + ':')
            f.writelines(found2)
            # f.write('\n')

    print("[Completed data extraction and output processing]\n")

if __name__ == "__main__":
    search_and_push()
