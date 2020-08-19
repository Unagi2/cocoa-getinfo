import tweepy
from datetime import datetime
import time

import json
import os.path


def tweet():

    print("[5/5 Processing Tweet... ]\n")

    # twitter API認証情報読み込み
    my_path = os.path.abspath(os.path.dirname(__file__))

    path = os.path.join(my_path, r"..\key_pool\twitter_api.json")

    with open(path) as json_open:
        json_load = json.load(json_open)
        CK = json_load["ConsumerKey"]
        CS = json_load["ConsumerSecret"]
        AT = json_load["AccessToken"]
        AS = json_load["AccessTokenSecret"]

    # ここでTwitter APIキーに関するJSONファイルの作成を推奨
    """key_poolディレクトリに保存(twitter_api.json)
    {
      "ConsumerKey": "1234",
      "ConsumerSecret": "5678",
      "AccessToken": "9abc",
      "AccessTokenSecret": "defg"
    }
    """

    # 現在時刻
    genzai = datetime.now()
    str_date = genzai.strftime('%m%d')

    # 画像元のパス
    file_name_today = os.path.join(
        my_path, r"..\chart_pool\sheet_today" + str_date + r".png")
    file_name_date = os.path.join(
        my_path, r"..\chart_pool\sheet_date" + str_date + r".png")
    file_name_dy = os.path.join(
        my_path, r"..\chart_pool\sheet_dy" + str_date + r".png")

    # テキスト内容に入れるデータ参照パス
    output_path = r'..\log_pool\download.txt'
    path_1 = os.path.join(my_path, output_path)
    output_path2 = r'..\log_pool\positive.txt'
    path_2 = os.path.join(my_path, output_path2)

    # ダウンロード前回データ
    y1 = open(path_1, 'r', encoding='utf-8')
    found1 = y1.read()
    found1 = found1.replace('.', ',')

    # 陽性登録数前回データ
    y2 = open(path_2, 'r', encoding='utf-8')
    found2 = y2.read()
    found2 = found2.replace('.', ',')

    # テキスト個別生成
    text1 = genzai.strftime('%m').lstrip("0") + "月" + \
        genzai.strftime('%d').lstrip("0") + "日17:00現在\n"
    text2 = "・ダウンロードは、合計" + str(found1) + "万件\n"
    text3 = "・陽性登録件数は、合計" + str(found2) + "件\n\n"
    text4 = "Google Sheetにてグラフを公開中\n"
    text5 = "より詳細にデータを読み取ることができます。\n"
    text6 = "https://t.co/an3puQWSOJ?amp=1\n\n"
    text7 = "#COCOA #接触確認アプリ"

    text9 = "更新日毎の増分変化についてのグラフ\n\n"
    text10 = "Google Data Portalにてレポートを公開しています。\n"
    text11 = "https://datastudio.google.com/u/0/reporting/f9081247-b6d3-48b8-a6e2-82d3b0b018ce/page/EczbB\n\n"

    text12 = "Sheetデータを閲覧用で公開"
    text13 = "https://docs.google.com/spreadsheets/d/1mq_yfYhArPPoL_n3zNZSoL_dMaxGLMmBkVnM3gcJGgM/edit?usp=sharing"

    # ツイート本文生成
    twitter_first = text1 + text2 + text3 + text10 + text5 + text11 + text7
    twitter_second = text1 + text9 + text10 + text5 + text11 + text7

    # 確認用
    print("\n\n[First tweet]\n\n" + twitter_first + "\n\n")
    print("\n\n[Second tweet]\n\n" + twitter_second + "\n\n")

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)

    # 画像付きツイート
    api.update_with_media(status='[Auto Tweet Mode]\n\n' +
                          twitter_first, filename=file_name_date)

    time.sleep(5)

    api.update_with_media(status='[Auto Tweet Mode]\n\n' +
                          twitter_second, filename=file_name_dy)

    print("[Completed!]\n")


if __name__ == "__main__":
    tweet()
