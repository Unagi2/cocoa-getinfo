# -*- coding: utf-8 -*-
from pylab import rcParams
from sub_sys import cocoa_create_plot
from sub_sys import cocoa_rolling_plot
import japanize_matplotlib
from datetime import datetime
import pandas as pd
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import seaborn as sns
import os.path


#### セルの読み込み方法####
# 1.ラベルを指定してセルの値を取得する
#import_value = ws.acell('B1').value
# 2.行番号と列番号を指定してセルの値を取得する（左：行番号、右：列番号）
#import_value = ws.cell(1, 2).value
# 3.ラベルを指定して複数セルの値を一次元配列に格納する
#range = ws.range('A19:F96')
# 4.シート全取得
#import_all_value = ws.get_all_values()


def sheet_pull():


    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # 認証情報設定
    # ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
    path_api = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../key_pool/google_api.json'))
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        path_api, scope)

    # OAuth2の資格情報を使用してGoogle APIにログインします。
    gc = gspread.authorize(credentials)

    # 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
    SPREADSHEET_KEY = '1mq_yfYhArPPoL_n3zNZSoL_dMaxGLMmBkVnM3gcJGgM'

    # 共有設定したスプレッドシートのシート1を開く
    wb = gc.open_by_key(SPREADSHEET_KEY)
    ws = wb.worksheet('Datasheet')

    # Elapsed days
    days_list = ws.col_values(1)
    # 範囲指定で要素削除
    del days_list[:18]

    # Update
    update_list = ws.col_values(2)
    del update_list[:18]

    # Download(×10,000)
    download_list = ws.col_values(3)
    del download_list[:18]

    # Positive registration
    positive_list = ws.col_values(4)
    del positive_list[:18]

    # Downlowd incremental(×10,000)
    download_incr_list = ws.col_values(5)
    del download_incr_list[:18]

    # Increment of positive registration
    positive_incr_list = ws.col_values(6)
    del positive_incr_list[:18]

    # 確認用
    # print(days_list)
    # print(update_list)
    # print(download_list)
    # print(positive_list)
    # print(download_incr_list)
    # print(positive_incr_list)

    # セルの関数読み取り
    all = ws.get_all_values(value_render_option='FORMULA')
    del all[:17]
    df = pd.DataFrame(all)
    #print(df.drop(index=df.index[[1, 3, 5]]))
    df.columns = list(df.loc[0, :])
    df.drop(0, inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    df.drop('App Version', axis=1, inplace=True)
    df.drop('Announce', axis=1, inplace=True)
    #df.fillna('None', inplace=True)

    # 欠損値をNaNで置換
    df.replace('', np.nan, inplace=True)
    df['Download(×10,000)'].replace('N/A', np.nan, True)
    df['Positive registration'].replace('N/A', np.nan, True)
    df['Downlowd incremental(×10,000)'].replace('N/A', np.nan, True)
    df['Increment of positive registration'].replace('N/A', np.nan, True)

    # ターミナルの表示設定
    pd.set_option('display.max_columns', 8)
    pd.set_option('display.max_rows', 500)

    # print(df)
    # print(df.dtypes)
    df['Download(×10,000)'] = df['Download(×10,000)'].astype(float)
    df['Downlowd incremental(×10,000)'] = df['Downlowd incremental(×10,000)'].astype(
        float)
    df['Increment of positive registration'] = df['Increment of positive registration'].astype(
        float)

    #print(pd.to_datetime(df['Update'], format='%m/%d'))

    # NaN判定関数
    # print(pd.isnull(df))

    # セル値取得
    #val = ws.cell(19, 2).value
    # セル内式取得
    #val = ws.acell('B19', value_render_option='FORMULA').value

    ###年月日変換プログラム###
    flg = df["Update"].astype("str").str.isdigit()
    # print(flg)
    from_serial = pd.to_timedelta(df.loc[flg, "Update"].astype(
        "float") - 2, unit="D") + pd.to_datetime("1900/1/1")
    #datetime(1900, 1, 1) + timedelta(days=42785 - 2)
    # 書式の統一
    from_string = pd.to_datetime(df.loc[~flg, "Update"])
    # 結合
    df["Update"] = pd.concat([from_serial, from_string])
    #print(df['Update'])

    return df

if __name__ == '__main__':

    #DataFlame Get
    df = sheet_pull()
    #print(df)
    #print(gspread_pull())

    # Plot of Accumulation
    cocoa_create_plot.graph_date(df)

    # Plot of the increase
    cocoa_create_plot.graph_dy(df)

    # Moving average
    # download
    cocoa_rolling_plot.graph_dl_rol(df)

    # positive
    cocoa_rolling_plot.graph_posi_rol(df)
