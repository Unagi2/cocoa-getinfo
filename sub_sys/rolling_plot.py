# -*- coding: utf-8 -*-
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pylab import rcParams
import japanize_matplotlib #matplotlib日本語モジュール

from scipy import interpolate # scipyのモジュールを使う
import matplotlib as mpl

def spline_interp(x,y):
    print("spline function [start]\n")

    dt = timedelta(days=1)  # 時間間隔

    # 補間用の時刻列作成。
    # ここでは元の時間間隔の半分の時刻列を作る
    smooth = 20
    dt_new = dt/smooth

    #len(x)を元データのリスト数にする
    num_new = smooth*len(x)-(smooth-1) #-1は，重要　/2=1 /3=2 /4=3
    t_new = [(x[x.index.values[0]]) + a * dt_new for a in range(num_new)]

    # interp関数はdatetime型を受け付けない
    # 時刻をdatetime型からunix時間（float）に変換する
    t_unix = [a.timestamp() for a in x]
    t_new_unix = [a.timestamp() for a in t_new]

    '''
    # 方法2: scipy で補間
    # 補間方法選択
    # kind = "linear", "nearest", "zero", "slinear", "quadratic", "cubic", "previous", "next"
    kind = "cubic"
    f = interpolate.interp1d(t_unix, y, kind=kind)
    x_scipy = f(t_new_unix)
    '''

    ####秋間####
    t_uni = [a.timestamp() for a in x]
    t_new_uni = [a.timestamp() for a in t_new]
    f = interpolate.Akima1DInterpolator(t_uni,y)
    x_scipy = f(t_new_uni)


    #print("t_new output\n")
    #print(t_new)

    '''
    #グラフ出力

    rcParams['figure.figsize'] = 10, 5
    fig, ax1 = plt.subplots()
    ax1.plot(t_new, x_scipy, "-")
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))
    ax1.legend(['interp data (cubic) : scipy'])

    ax1.xaxis.set_major_locator(mdates.DayLocator(
        bymonthday=None, interval=7, tz=None))
    daysFmt = mdates.DateFormatter('%m/%d')
    ax1.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    labels = ax1.get_xticklabels()

    #レイアウト整理
    plt.tight_layout()

    plt.show()
    '''
    print("spline function [finish]\n")
    return t_new, x_scipy

def rol_meen(x,y):
    print("rolling function [start]\n")

    dt = timedelta(days=1)  # 時間間隔

    # 補間用の時刻列作成。
    # ここでは元の時間間隔の半分の時刻列を作る
    smooth = 20
    dt_new = dt/smooth
    print(x.index.values[0])

    # len(x)を元データのリスト数にする
    num_new = smooth*len(x)-(smooth-1) #-1は，重要　/2=1 /3=2 /4=3
    t_new = [(x[x.index.values[0]]) + a * dt_new for a in range(num_new)]

    #print(x)
    #print("補間用時刻\n")
    #print("\nlen(x)の出力\n")
    #print(len(x))
    #print("\nrange(num_new)の出力\n")
    #print(range(num_new))

    # interp関数はdatetime型を受け付けない
    # 時刻をdatetime型からunix時間（float）に変換する
    t_unix = [a.timestamp() for a in x]
    t_new_unix = [a.timestamp() for a in t_new]


    ####秋間####
    t_uni = [a.timestamp() for a in x]
    t_new_uni = [a.timestamp() for a in t_new]
    f = interpolate.Akima1DInterpolator(t_uni,y)
    x_scipy = f(t_new_uni)


    #print("t_new output\n")
    #print(t_new)

    '''
    #グラフ出力

    rcParams['figure.figsize'] = 10, 5
    fig, ax1 = plt.subplots()
    ax1.plot(t_new, x_scipy, "-")
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))
    ax1.legend(['interp data (cubic) : scipy'])

    ax1.xaxis.set_major_locator(mdates.DayLocator(
        bymonthday=None, interval=7, tz=None))
    daysFmt = mdates.DateFormatter('%m/%d')
    ax1.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    labels = ax1.get_xticklabels()

    #レイアウト整理
    plt.tight_layout()

    plt.show()
    '''
    print("rolling function [finish]\n")

    return t_new, x_scipy

def graph_dl_rol(df):

    print("Plot of Download Moving Average[start]\n")

    #　時刻
    #　フォーマット指定
    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    # Graph Create

    sns.set(style="whitegrid", font="IPAexGothic")

    rcParams['figure.figsize'] = 10, 5

    # Figure and Axes
    plt.close(1)  # 既にFigure1が開かれていれば閉じる

    # twinx設定
    fig, ax1 = plt.subplots()

    # styleを適用している場合はgrid線を片方消す
    ax1.grid(False)

    # グラフのグリッドをグラフの本体の下にずらす
    ax1.set_axisbelow(True)

    # 色の設定(tab20採用)
    color_1 = cm.tab20.colors[1]
    color_2 = cm.tab20.colors[2]
    color_3 = cm.tab20.colors[7]

    # Nanを無視して点間を結ぶ
    s1mask = np.isfinite(df['Downlowd incremental(×10,000)'])
    s2mask = np.isfinite(df['Increment of positive registration'])

    #補間用のデータフレーム設定と補間処理
    df_copy = df.copy()
    df_copy.interpolate('akima',inplace=True)


    # 補間データフレーム内のNanを無視して点間を結ぶ
    s11mask = np.isfinite(df_copy['Downlowd incremental(×10,000)'])
    s22mask = np.isfinite(df_copy['Increment of positive registration'])


    #スプライン関数生成
    #spline = spline_interp(df['Update'][s1mask],df['Download(×10,000)'][s1mask])
    spline = spline_interp(df_copy['Update'][s11mask],df_copy['Downlowd incremental(×10,000)'][s11mask])


    # 移動平均データ生成
    df_copy['Downlowd incremental(×10,000)']= df_copy['Downlowd incremental(×10,000)'].rolling(window=7).mean()

    # 移動平均データフレーム内のNanを無視して点間を結ぶ
    s111mask = np.isfinite(df_copy['Downlowd incremental(×10,000)'])
    s222mask = np.isfinite(df_copy['Increment of positive registration'])

    #移動平均データのスプライン化
    rol = rol_meen(df_copy['Update'][s111mask],df_copy['Downlowd incremental(×10,000)'][s111mask])


    # 1つのaxesオブジェクトのlines属性に2つのLine2Dオブジェクトを追加
    ## 棒グラフ
    ax1.bar(df['Update'][s1mask], df['Downlowd incremental(×10,000)'][s1mask],
             color=color_1, label="ダウンロード数",zorder=1)

    ## 移動平均線
    ax1.plot(rol[0],rol[1],color=color_2, label="移動平均",zorder=2)


    # 軸の目盛りの最大値をしている
    # axesオブジェクトに属するYaxisオブジェクトの値を変更
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))

    # 軸の縦線の色を変更している
    ax1.tick_params(axis='y', direction='in')
    ax1.tick_params(axis='x', direction='in')

    #重ね順として折れ線グラフを前面
    #棒グラフに折れ線が隠れてしまうのを防ぐ
    ax1.set_zorder(2)
    #ax2.set_zorder(1)

    #折れ線グラフの背景を透明
    #重ね順が後ろに設定した棒グラフが消えるのを防ぐ
    ax1.patch.set_alpha(0)

    # 凡例
    # グラフの本体設定時に、ラベルを手動で設定する必要があるのは、barplotのみ。plotは自動で設定される
    handler1, label1 = ax1.get_legend_handles_labels()

    # Title
    ax1.text(x=0.5, y=1.1, s='COCOA 更新日毎のダウンロード数の変化', fontsize=16,
             weight='bold', ha='center', va='bottom', transform=ax1.transAxes)
    ax1.text(x=0.5, y=1.05, s='土日祝日データ欠損', fontsize=8, alpha=0.75,
             ha='center', va='bottom', transform=ax1.transAxes)
    ax1.set_ylabel('ダウンロード数[万件]')
    ax1.set_xlabel('更新日')

    # 凡例をまとめて出力する
    ax1.legend(handler1, label1,
               loc="upper left", borderaxespad=1)

    # 最大値設定
    download_max = 1.2 * max(df['Downlowd incremental(×10,000)'])
    ax1.set_ylim([0, download_max])
    #ax2.set_ylim([0, positive_max])

    # x軸の設定(表示形式)
    ax1.xaxis.set_major_locator(mdates.DayLocator(
        bymonthday=None, interval=7, tz=None))
    daysFmt = mdates.DateFormatter('%m/%d')
    ax1.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    labels = ax1.get_xticklabels()

    # ローテーション設定
    plt.setp(labels, rotation=45, fontsize=10)

    #レイアウト自動整理
    plt.tight_layout()

    print("Saving\n")
    file_name_date = os.path.normpath(os.path.join(os.path.dirname(__file__), '../chart_pool/sheet_dl_movave' + str_date + '.png'))
    plt.savefig(file_name_date, dpi=600)
    #plt.show()

    print("Plot of Download Moving Average[finish]\n")

def graph_posi_rol(df):

    print("Plot of Positive Moving Average[start]\n")

    # 時刻フォーマット指定
    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    # Graph
    sns.set(style="whitegrid", font="IPAexGothic")
    rcParams['figure.figsize'] = 10, 5

    # Figure and Axes
    plt.close(1)  # 既にFigure1が開かれていれば閉じる

    fig, ax1 = plt.subplots()

    # styleを適用している場合はgrid線を片方消す
    ax1.grid(False)

    # グラフのグリッドをグラフの本体の下にずらす
    ax1.set_axisbelow(True)

    # 色の設定
    color_1 = cm.tab20.colors[1]
    color_2 = cm.tab20.colors[7]
    color_3 = cm.tab20.colors[8]

    #新たなデータフレーム
    df_copy = df.copy()
    df_copy.interpolate('akima',inplace=True)

    # Nanを無視して点間を結ぶ
    s1mask = np.isfinite(df['Downlowd incremental(×10,000)'])
    s2mask = np.isfinite(df['Increment of positive registration'])
    s11mask = np.isfinite(df_copy['Downlowd incremental(×10,000)'])
    s22mask = np.isfinite(df_copy['Increment of positive registration'])

    #スプライン関数生成
    spline = spline_interp(df_copy['Update'][s22mask],df_copy['Increment of positive registration'][s22mask])

    #移動平均生成
    df_copy['Increment of positive registration']= df_copy['Increment of positive registration'].rolling(window=7).mean()
    s111mask = np.isfinite(df_copy['Downlowd incremental(×10,000)'])
    s222mask = np.isfinite(df_copy['Increment of positive registration'])

    rol = rol_meen(df_copy['Update'][s222mask],df_copy['Increment of positive registration'][s222mask])

    # 1つのaxesオブジェクトのlines属性に2つのLine2Dオブジェクトを追加
    ## 棒グラフ
    ax1.bar(df['Update'][s2mask], df['Increment of positive registration'][s2mask], color=color_2, label="陽性登録数",zorder=1)

    ## 移動平均線
    ax1.plot(rol[0],rol[1],color=color_3, label="移動平均",zorder=2,linewidth=3)

    # 軸の目盛りの最大値をしている
    # axesオブジェクトに属するYaxisオブジェクトの値を変更
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))

    # 軸の縦線の色を変更している
    ax1.tick_params(axis='y',direction='in')
    ax1.tick_params(axis='x', direction='in')
    ax1.tick_params(labelbottom=True)

    #重ね順として折れ線グラフを前面
    #棒グラフに折れ線が隠れてしまうのを防ぐ
    ax1.set_zorder(2)
    #ax2.set_zorder(1)

    #折れ線グラフの背景を透明
    #重ね順が後ろに設定した棒グラフが消えるのを防ぐ
    ax1.patch.set_alpha(0)

    # 凡例
    # グラフの本体設定時に、ラベルを手動で設定する必要があるのは、barplotのみ。plotは自動で設定される
    handler1, label1 = ax1.get_legend_handles_labels()

    ax1.text(x=0.5, y=1.1, s='COCOA 更新日毎の陽性登録数の変化', fontsize=16,
             weight='bold', ha='center', va='bottom', transform=ax1.transAxes)
    ax1.text(x=0.5, y=1.05, s='土日祝日データ欠損', fontsize=8, alpha=0.75,
             ha='center', va='bottom', transform=ax1.transAxes)
    ax1.set_ylabel('陽性登録数[件]')
    ax1.set_xlabel('更新日')

    # 凡例をまとめて出力
    ax1.legend(handler1, label1,
               loc="upper left", borderaxespad=4)

    # x軸の設定(表示形式)
    ax1.xaxis.set_major_locator(mdates.DayLocator(
        bymonthday=None, interval=7, tz=None))
    daysFmt = mdates.DateFormatter('%m/%d')
    ax1.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    plt.rcParams["xtick.major.size"] = 10
    plt.rcParams["ytick.major.size"] = 10
    labels = ax1.get_xticklabels()

    #ローテーション設定
    plt.setp(labels, rotation=45, fontsize=10)

    #レイアウト整理
    plt.tight_layout()

    print("Saving\n")
    file_name_date = os.path.normpath(os.path.join(os.path.dirname(__file__), '../chart_pool/sheet_posi_movave' + str_date + '.png'))
    plt.savefig(file_name_date, dpi=600)
    #plt.show()

    print("Plot of Positive Moving Average[finish]\n")
