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
import csv
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
###
    #Nanに対する補間（新たにデータフレームを作成df_interpolate）
    df_interpolate = df.copy()
    #print(df_interpolate)
    #print(len(df_interpolate))
    #df_interpolate.to_csv(filename_csv2)

    #df.at['行名','列名']
    #col_pick = 5 #sample "Download"

    for set in range(2,6):
        #列番号セット
        col_pick = set

        #ダウンロード，陽性登録ごとにデータの発表開始時期が違う　count_dfを列ごとに変化
        if col_pick == 3 or col_pick == 5:
            count_df = 27
        else:
            count_df = 0 #行番号

        count_two_df = 0

        #列番号を指定する方法：df_interpolate.iloc[:, col_pick]

        for a in df_interpolate.iloc[:, col_pick][count_df:]: #"Download"列に対してcount_dfからfor開始
            #print("count_df:")
            #print(count_df) #カウント変数
            #print("変数a:")
            #print(a) #現在の要素値
            #print("NaN判定:")
            #print(np.isnan(a)) #NaN検出（True:検出）

            #df_interpolateの処理終了条件
            if count_df == len(df_interpolate):
                print('!!BREAK!!')
                break
            ###Nanを検索とセル位置取得
            #NaNを補間する処理条件
            elif np.isnan(a) == True:
                index_num = 0
                df_memory = pd.DataFrame([0],index=[0], columns=['val'])
                
                #print("メモリーデータフレーム作成時")
                #print(df_memory)
                df_memory.iat[index_num,0] = 0 #NaNのセルを仮想的に0とおく


                ###次の値がNan以外になるまで繰り返す。カウント
                for b in df_interpolate.iloc[:, col_pick][count_df:]:    #次の要素が欠損以外になるまで要素取得
                    #print(df.at[df.index[2], 'age'])

                    ###Nanのセルとその後ろにある値に対して，データ値/カウント数で算出した平均値で全て置換
                    if np.isnan(b) == False: #終了処理
                        count_two_df += 1
                        index_num += 1
                        df_memory.loc[index_num] = b #bデータをdfに書き込む重要
                        #print("メモリーデータフレーム")
                        #print(df_memory)

                        #平均値算出
                        #print("平均値算出")
                        ave = df_memory['val'].sum() / (count_two_df)
                        #print(ave)
                        
                        #要素平均値置換
                        #print("置換処理")
                        count_three_df = count_df
                        for b in df_interpolate.iloc[:, col_pick][count_df:(count_df + count_two_df)]:
                            
                            #print("count_two_df:")
                            #print(count_two_df)
                            #print("count_three_df:")
                            #print(count_three_df)
                            df_interpolate.iat[count_three_df,col_pick] = ave
                            count_three_df += 1


                        #print("置換処理後のdf_interpolate")
                        #print(df_interpolate.iloc[:, col_pick])
                        count_two_df = 0 #初期化
                        df_memory = df_memory.set_index('val') #df初期化
                        df_memory.reset_index(drop=True)
                        #print('!!BREAK 欠損ブロック!!')
                        break

                    else: #継続処理
                        index_num += 1
                        #print("継続処理")
                        #print(b)
                        df_memory.loc[index_num] = 0 #NaNのセルを仮想的に0とおく
                        count_two_df += 1
                print("NaN Alert")
            
            count_df = count_df + 1 + count_two_df #スキップした分を加算途中からfor再開
        else:
            print("単列補間処理終了")

    #補間処理結果   
    #print(df_interpolate.iloc[:, [col_pick]])
    df_new = df_interpolate.copy()
    
    #dataframe output
    file_df_csv = os.path.normpath(os.path.join(os.path.dirname(__file__), '../log_pool/df.csv'))
    df.to_csv(file_df_csv)
    
    file_df_interpolate_csv = os.path.normpath(os.path.join(os.path.dirname(__file__), '../log_pool/df_interpolate.csv'))
    df_new.to_csv(file_df_interpolate_csv)
    
    ###Spread Sheet Output
    sheetName = 'Datasheet_interpolate'
    csvFile = file_df_interpolate_csv
    
    wb.values_update(
        sheetName,
        params={'valueInputOption': 'USER_ENTERED'},
        body={'values': list(csv.reader(open(csvFile)))})
    
    # ターミナルの表示設定
    pd.set_option('display.max_columns', 8)
    pd.set_option('display.max_rows', 500)

    #####dfの処理
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
    
    
    #####df_newの処理
    # print(df)
    # print(df.dtypes)
    df_new['Download(×10,000)'] = df_new['Download(×10,000)'].astype(float)
    df_new['Downlowd incremental(×10,000)'] = df_new['Downlowd incremental(×10,000)'].astype(
        float)
    df_new['Increment of positive registration'] = df_new['Increment of positive registration'].astype(
        float)

    ###年月日変換プログラム###
    flg_new = df_new["Update"].astype("str").str.isdigit()
    from_serial_new = pd.to_timedelta(df_new.loc[flg_new, "Update"].astype(
        "float") - 2, unit="D") + pd.to_datetime("1900/1/1")
    # 書式の統一
    from_string_new = pd.to_datetime(df_new.loc[~flg_new, "Update"])
    # 結合
    df_new["Update"] = pd.concat([from_serial_new, from_string_new])

    return df,df_new


if __name__ == '__main__':

    #DataFlame Get
    df = sheet_pull()
    #print(df)
    #print(gspread_pull())

    # Plot of Accumulation
    cocoa_create_plot.graph_date(df[0])

    # Plot of the increase
    cocoa_create_plot.graph_dy(df[0])

    # Moving average
    # download
    cocoa_rolling_plot.graph_dl_rol(df[0],df[1])

    # positive
    cocoa_rolling_plot.graph_posi_rol(df[0],df[1])
