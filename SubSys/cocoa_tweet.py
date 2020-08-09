import tweepy
from datetime import datetime
import time


def tweet():

    print("[Processing Tweet... ]\n")

    # Twitter API各種キーを代入する
    CK = "Consumer Key"
    CS = "Consumer Secret"
    AT = "Access Token"
    AS = "Access Token Secret"

    # 現在時刻
    genzai = datetime.now()
    str_date = genzai.strftime('%m%d')

    # 画像元のパス
    file_name_today = r'..\chart_pool\sheet_today' + str_date + r'.png'
    file_name_date = r'..\chart_pool\sheet_date' + str_date + r'.png'
    file_name_dy = r'..\chart_pool\sheet_dy' + str_date + r'.png'

    # テキスト内容に入れるデータ参照パス
    output_path = r'..\log_pool\download.txt'
    output_path2 = r'..\log_pool\positive.txt'

    y1 = open(output_path, 'r', encoding='utf-8')
    found1 = y1.read()
    found1 = found1.replace('.', ',')
    y2 = open(output_path2, 'r', encoding='utf-8')
    found2 = y2.read()
    found2 = found2.replace('.', ',')

    # テキスト個別生成
    text1 = genzai.strftime('%m').lstrip("0") + "月" + \
        genzai.strftime('%d').lstrip("0") + "日17:00現在\n"
    text2 = "・ダウンロードは、合計" + str(found1) + "万件\n"
    text3 = "・陽性登録件数は、合計" + str(found2) + "件\n\n"
    text4 = "Google Sheetにてグラフ公開\n"
    text5 = "パソコンなどでご覧いただくと，より詳細にデータを読み取ることが可能です\n"
    text6 = "https://t.co/an3puQWSOJ?amp=1\n\n"
    text7 = "#COCOA #接触確認アプリ"

    text9 = "更新日毎の増分変化についてのグラフ\n\n"
    text10 = "Google Sheetにてグラフ公開\n"
    text11 = "https://t.co/doJh6Y0Uzm?amp=1\n\n"

    # ツイート本文生成
    twitter_first = text1 + text2 + text3 + text4 + text5 + text6  # + text7
    twitter_second = text1 + text9 + text10 + text11  # + text7

    # 確認用
    print("\n\n[First tweet]\n" + twitter_first + "\n\n")
    print("\n\n[Second tweet]\n" + twitter_second + "\n\n")

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    # 画像付きツイート
    api.update_with_media(status='画像付きツイートテスト' +
                          twitter_first, filename=file_name_date)

    time.sleep(5)

    api.update_with_media(status='画像付きツイートテスト2' +
                          twitter_second, filename=file_name_dy)

    print("[Tweet processing completed]\n")
