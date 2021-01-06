# -*- coding: utf-8 -*-
import tweepy
from datetime import datetime
import time

import json
import os.path


def tweet():

    print("[5/5 Processing Tweet... ]\n")

    # twitter API認証情報読み込み
    my_path = os.path.abspath(os.path.dirname(__file__))
    target_path_1 = os.path.join(os.path.dirname(
        __file__), '../key_pool/twitter_api.json')
    print('normalize    : ', os.path.normpath(target_path_1))
    path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../key_pool/twitter_api.json'))

    with open(path) as json_open:
        json_load = json.load(json_open)
        CK = json_load["ConsumerKey"]
        CS = json_load["ConsumerSecret"]
        AT = json_load["AccessToken"]
        AS = json_load["AccessTokenSecret"]

    # ここでTwitter APIキーに関するJSONファイルの作成を推奨
    """下記形式をkey_poolディレクトリに作成保存(twitter_api.json)
    {
      "ConsumerKey": "1234",
      "ConsumerSecret": "5678",
      "AccessToken": "9abc",
      "AccessTokenSecret": "defg"
    }
    """

    # 現在時刻
    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    # 画像元のパス
    file_name_today = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_today' + str_date + '.png'))
    ## 累計と日毎
    file_name_date = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_date' + str_date + '.png'))
    file_name_dy = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_dy' + str_date + '.png'))
    ## 移動平均グラフ２種
    file_name_dl_moveave = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_dl_moveave' + str_date + '.png'))
    file_name_posi_moveave = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_posi_moveave' + str_date + '.png'))

    # テキスト内容に入れるデータ参照パス
    path_1 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/download.txt'))
    path_2 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/positive.txt'))
    path_3 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/download_increment.txt'))
    path_4 = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../log_pool/positive_increment.txt'))

    # ダウンロード前回データ
    y1 = open(path_1, 'r', encoding='utf-8')
    found1 = y1.read()
    found1 = "{:,.0f}".format(float(found1))

    # 陽性登録数前回データ
    y2 = open(path_2, 'r', encoding='utf-8')
    found2 = y2.read()
    found2 = "{:,.0f}".format(float(found2))
    
    y3 = open(path_3, 'r', encoding='utf-8')
    download_increment = y3.read()
    
    y4 = open(path_4, 'r', encoding='utf-8')
    positive_increment = y4.read()

    # テキスト個別生成
    text1 = genzai.strftime('%m').lstrip("0") + "月" + \
        genzai.strftime('%d').lstrip("0") + "日17:00時点\n"
    text2 = "・ダウンロードは、合計" + str(found1) + "万件\n"
    text3 = "・陽性登録件数は、合計" + str(found2) + "件\n\n"
    #text4 = "Google Sheetにてグラフを公開中\n"
    text5 = "より詳細に変化を読み取ることができます。\n"
    #text6 = "https://t.co/an3puQWSOJ?amp=1\n\n"
    text7 = "#COCOA #接触確認アプリ"
    text9 = "更新日毎の増分変化について\n\n"
    text10 = "\nGoogle Data Studioにてレポート公開\n"
    text11 = "https://datastudio.google.com/u/0/reporting/f9081247-b6d3-48b8-a6e2-82d3b0b018ce/page/EczbB\n\n"
    text12= "前回更新より、\n"
    text13 = "・ダウンロード数は、" + str(download_increment) + "万件増\n"
    text14 = "・陽性登録件数は、" + str(positive_increment) + "件増\n\n"
    text15 = "ダウンロード数に関する移動平均グラフ\n\n"
    text16 = "陽性登録数に関する移動平均グラフ\n\n"
    
    #text12 = "Sheetデータを閲覧用で公開"
    #text13 = "https://docs.google.com/spreadsheets/d/1mq_yfYhArPPoL_n3zNZSoL_dMaxGLMmBkVnM3gcJGgM/edit?usp=sharing"

    # ツイート本文生成
    twitter_first = text1 + text2 + text3 + text10 + text11 + text7
    twitter_second = text1 + text9 + text12 + text13 + text14 + text10 + text11 + text7
    twitter_third = text1 + text15 + text10 + text11 + text7
    twitter_forth = text1 + text16 + text10 + text11 + text7

    # 確認用
    print("\n\n[First tweet]\n" + twitter_first + "\n\n")
    print("\n\n[Second tweet]\n" + twitter_second + "\n\n")
    print("\n\n[Third tweet]\n" + twitter_third + "\n\n")
    print("\n\n[Forth tweet]\n" + twitter_forth + "\n\n")

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)

    api = tweepy.API(auth)
    
    '''
    # 画像付きツイート
    api.update_with_media(status='[Auto Tweet]\n\n' + twitter_first, filename=file_name_date)
    time.sleep(5)
    api.update_with_media(status='[Auto Tweet]\n\n' + twitter_second, filename=file_name_dy)
    '''

    # upload images and get media_ids https://stackoverrun.com/ja/q/11956428
    ## 累計グラフ
    media_ids = []
    res = api.media_upload(file_name_date)
    media_ids.append(res.media_id)

    ## 日毎グラフ
    media_ids2 = []
    res2 = api.media_upload(file_name_dy)
    media_ids2.append(res2.media_id)

    ## ダウンロードと移動平均グラフ
    media_ids3 = []
    res3 = api.media_upload(file_name_dl_moveave)
    media_ids3.append(res3.media_id)

    ## 陽性登録と移動平均グラフ
    media_ids4 = []
    res4 = api.media_upload(file_name_posi_moveave)
    media_ids4.append(res4.media_id)

    # tweet with images https://stackoverflow.com/questions/62291918/how-to-create-a-twitter-thread-with-tweepy-on-python
    original_tweet = api.update_status(status='[Auto Tweet]\n\n' + twitter_first, media_ids=media_ids)

    reply1_tweet = api.update_status(status='[Auto Tweet]\n\n' + twitter_second, media_ids=media_ids2,in_reply_to_status_id=original_tweet.id,auto_populate_reply_metadata='true')

    reply2_tweet = api.update_status(status='[Auto Tweet]\n\n' + twitter_third, media_ids=media_ids3,in_reply_to_status_id=reply1_tweet.id,auto_populate_reply_metadata='true')

    reply3_tweet = api.update_status(status='[Auto Tweet]\n\n' + twitter_forth, media_ids=media_ids4,in_reply_to_status_id=reply2_tweet.id,auto_populate_reply_metadata='true')
    
    print("[Completed!]\n")

if __name__ == "__main__":
    tweet()
