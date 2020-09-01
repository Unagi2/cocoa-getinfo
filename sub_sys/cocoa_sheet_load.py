# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import os.path


def sheet_load():

    print("[4/5 Google Sheet download in progress... ]\n")

    # 時刻取得
    genzai = datetime.now()
    str_date = genzai.strftime('%m%d')

    # グラフ画像の取得先URL
    url_today = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT5VMVHVap55nc8cC27_Y94rda9iA9_daY1Wvc6R40x8M5Y6XrIwVc9pqVzGgieMDSL7WqFvKg6J4Vy/pubchart?oid=1220842384&format=image"
    url_date = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT5VMVHVap55nc8cC27_Y94rda9iA9_daY1Wvc6R40x8M5Y6XrIwVc9pqVzGgieMDSL7WqFvKg6J4Vy/pubchart?oid=429287342&format=image"
    url_dy = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT5VMVHVap55nc8cC27_Y94rda9iA9_daY1Wvc6R40x8M5Y6XrIwVc9pqVzGgieMDSL7WqFvKg6J4Vy/pubchart?oid=626433765&format=image"
    url_today_eng = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT5VMVHVap55nc8cC27_Y94rda9iA9_daY1Wvc6R40x8M5Y6XrIwVc9pqVzGgieMDSL7WqFvKg6J4Vy/pubchart?oid=179478230&format=image"
    url_date_eng = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT5VMVHVap55nc8cC27_Y94rda9iA9_daY1Wvc6R40x8M5Y6XrIwVc9pqVzGgieMDSL7WqFvKg6J4Vy/pubchart?oid=48708961&format=image"
    url_dy_eng = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT5VMVHVap55nc8cC27_Y94rda9iA9_daY1Wvc6R40x8M5Y6XrIwVc9pqVzGgieMDSL7WqFvKg6J4Vy/pubchart?oid=731084205&format=image"

    # 画像の保存先パス
    my_path = os.path.abspath(os.path.dirname(__file__))

    #file_name_today = os.path.join(my_path, r"..\chart_pool\sheet_today" + str_date + r".png")
    file_name_today = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_today' + str_date + '.png'))
    #file_name_date = os.path.join(my_path, r"..\chart_pool\sheet_date" + str_date + r".png")
    file_name_date = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_date' + str_date + '.png'))
    #file_name_dy = os.path.join(my_path, r"..\chart_pool\sheet_dy" + str_date + r".png")
    file_name_dy = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_dy' + str_date + '.png'))
    #file_name_today_eng = os.path.join(my_path, r"..\chart_pool\sheet_today_eng" + str_date + r".png")
    file_name_today_eng = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_today_eng' + str_date + '.png'))
    #file_name_date_eng = os.path.join(my_path, r"..\chart_pool\sheet_date_eng" + str_date + r".png")
    file_name_date_eng = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_date_eng' + str_date + '.png'))
    #file_name_dy_eng = os.path.join(my_path, r"..\chart_pool\sheet_dy_eng" + str_date + r".png")
    file_name_dy_eng = os.path.normpath(os.path.join(os.path.dirname(
        __file__), '../chart_pool/sheet_dy_eng' + str_date + '.png'))

    # sheet_today
    response = requests.get(url_today)
    image = response.content

    with open(file_name_today, "wb") as aaa:
        aaa.write(image)

    # sheet_date
    response = requests.get(url_date)
    image = response.content

    with open(file_name_date, "wb") as aaa:
        aaa.write(image)

    # sheet_date_ENG
    response = requests.get(url_dy)
    image = response.content

    with open(file_name_dy, "wb") as aaa:
        aaa.write(image)

    # sheet_today_ENG
    response = requests.get(url_today_eng)
    image = response.content

    with open(file_name_today_eng, "wb") as aaa:
        aaa.write(image)

    # sheet_date_ENG
    response = requests.get(url_date_eng)
    image = response.content

    with open(file_name_date_eng, "wb") as aaa:
        aaa.write(image)

    # sheet_date
    response = requests.get(url_dy_eng)
    image = response.content

    with open(file_name_dy_eng, "wb") as aaa:
        aaa.write(image)

    print("[Completed!]\n")


if __name__ == "__main__":
    sheet_load()
