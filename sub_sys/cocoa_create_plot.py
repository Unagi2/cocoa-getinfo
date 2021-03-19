# -*- coding: utf-8 -*-
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import cm
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker #as ticker

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pylab import rcParams
import japanize_matplotlib #matplotlib日本語モジュール

from scipy import interpolate # scipyのモジュールを使う
import matplotlib as mpl

import os.path

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def spline_interp(x,y):
    print("spline function [start]\n")

    dt = timedelta(days=1)  # 時間間隔

    # 補間用の時刻列作成。
    # ここでは元の時間間隔の半分の時刻列を作る
    smooth = 20
    dt_new = dt/smooth

    #len(x)を元データのリスト数にする
    num_new = smooth*len(x)-(smooth-1) #-1は，重要　/2=1 /3=2 /4=3
    t_new = [x[0] + a * dt_new for a in range(num_new)]

    # interp関数はdatetime型を受け付けない
    # 時刻をdatetime型からunix時間（float）に変換する
    t_unix = [a.timestamp() for a in x]
    t_new_unix = [a.timestamp() for a in t_new]

    ####秋間####
    t_uni = [a.timestamp() for a in x]
    t_new_uni = [a.timestamp() for a in t_new]
    f = interpolate.Akima1DInterpolator(t_uni,y)
    x_scipy = f(t_new_uni)

    # 確認用
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

    # len(x)を元データのリスト数にする
    num_new = smooth*len(x)-(smooth-1) #-1は，重要　/2=1 /3=2 /4=3
    t_new = [x[33] + a * dt_new for a in range(num_new)]

    # interp関数はdatetime型を受け付けない
    # 時刻をdatetime型からunix時間（float）に変換する
    t_unix = [a.timestamp() for a in x]
    t_new_unix = [a.timestamp() for a in t_new]


    ####秋間####
    t_uni = [a.timestamp() for a in x]
    t_new_uni = [a.timestamp() for a in t_new]
    f = interpolate.Akima1DInterpolator(t_uni,y)
    x_scipy = f(t_new_uni)

    # 確認用
    #print("t_new output\n")
    #print(t_new)

    print("rolling function [finish]\n")
    return t_new, x_scipy

def graph_date(df):

    print("Plot of Accumulation[start]\n")

    #　時刻フォーマット指定
    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    # Graph main settings
    sns.set(style="whitegrid", font="IPAexGothic")
    rcParams['figure.figsize'] =  9, 5

    #plt.rcParams['font.family'] ='sans-serif'#使用するフォント
    plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
    plt.rcParams['font.size'] = 8 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ

    # Figure and Axes
    plt.close(1)  # 既にFigure1が開かれていれば閉じる

    # twinx設定
    fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx()

    # styleを適用している場合はgrid線を片方消す
    ax1.grid(False)
    #ax2.grid(False)

    # グラフのグリッドをグラフの本体の下にずらす
    ax1.set_axisbelow(True)

    # 色の設定(tab20採用)
    color_1 = cm.tab20.colors[0]
    color_2 = cm.tab20.colors[7]
    color_3 = cm.tab20.colors[6]

    # Nanを無視して点間を結ぶ
    s1mask = np.isfinite(df['Download(×10,000)'])
    s2mask = np.isfinite(df['Positive registration'])

    #補間用のデータフレーム設定と補間処理
    df_copy = df.copy()
    df_copy.interpolate('akima',inplace=True)

    # 確認用
    #print(df)
    #print(df['Update'][s1mask])
    #print(df.interpolate('akima'))
    #print(np.asarray(df['Update'][s1mask]).shape)
    #print(np.asarray(df['Download(×10,000)'][s1mask]).shape)

    # 補間データフレーム内のNanを無視して点間を結ぶ
    s11mask = np.isfinite(df_copy['Download(×10,000)'])
    s22mask = np.isfinite(df_copy['Positive registration'])

    # 確認用
    #print(len(df_copy['Update']))
    #print(len(df_copy['Update'][s11mask]))


    #スプライン関数生成
    #spline = spline_interp(df['Update'][s1mask],df['Download(×10,000)'][s1mask])
    spline = spline_interp(df_copy['Update'][s11mask],df_copy['Download(×10,000)'][s11mask])

    # 確認用
    #print("spline[0] output\n")
    #print(spline[0])

    # 移動平均データ生成
    #df_copy['Download(×10,000)']= df_copy['Download(×10,000)'].rolling(window=7).mean()
    df_copy['Positive registration']= df_copy['Positive registration'].rolling(window=7).mean()

    # 移動平均データフレーム内のNanを無視して点間を結ぶ
    s111mask = np.isfinite(df_copy['Download(×10,000)'])
    s222mask = np.isfinite(df_copy['Positive registration'])

    #移動平均データのスプライン化
    rol = rol_meen(df_copy['Update'][s222mask],df_copy['Positive registration'][s222mask])


    # 1つのaxesオブジェクトのlines属性に2つのLine2Dオブジェクトを追加 
    # 曲線グラフのプロットデータ設定
    ax1.plot(df['Update'][s1mask], df['Download(×10,000)'][s1mask],
             color=color_1, label="累積ダウンロード数", marker="o",zorder=2,linestyle="None",markersize=1)
    
    # スプライン曲線設定
    ax1.plot(spline[0],spline[1],color=color_1, label="",zorder=3)
    
    ax1.grid(axis='y', color='black', lw=0.4)
    ax2 = ax1.twinx()
    
    ## 移動平均線設定
    #ax2.plot(rol[0],rol[1],color=color_3, label="移動平均",zorder=4)
    
    # 棒グラフデータ設定
    ax2.bar(df['Update'][s2mask], df['Positive registration']
            [s2mask], color=color_2, label="累積陽性登録数",zorder=1)
    ax2.grid(None)

    # 軸の目盛り設定
    ## axesオブジェクトに属するYaxisオブジェクトの値を変更
    #ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))
    #ax2.yaxis.set_major_locator(MaxNLocator(nbins=5))


    # Y-axis setting(edited 2021/1)
    nticks = 6
    mticks = 11

    ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
    ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))

    ax1.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(mticks))
    ax2.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(mticks))

    # round()で四捨五入して丸める
    ax1.set_ylim(0,round(max(df['Download(×10,000)'][s1mask])+100, -2))
    #ax1.set_xlim(0,10)
    ax2.set_ylim(0,round(max(df['Positive registration'][s2mask])+100, -2))

    # 軸の縦線の色を変更している
    ## axesオブジェクトに属するSpineオブジェクトの値を変更
    ## 図を重ねてる関係で、ax2のみ
    ax2.spines['left'].set_color(color_1)
    ax2.spines['right'].set_color(color_2)

    ax1.spines['left'].set_color(color_1)
    ax1.spines['right'].set_color(color_2)

    # 軸の縦線の色を変更している
    ax1.tick_params(axis='y', colors=color_1, direction='in',length = 5,width = 1)
    ax2.tick_params(axis='y', colors=color_3, direction='in',length = 5,width = 1)
    ax1.tick_params(axis='x', which='major',direction='in',length = 5,width = 1)
    ax2.tick_params(axis='x', which='major',direction='in',length = 5,width = 1)

    # 軸の目盛りの単位を設定
    # ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d件"))
    # ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d件"))

    # 重ね順として折れ線グラフを前面
    # 棒グラフに折れ線が隠れてしまうのを防ぐ
    ax1.set_zorder(2)
    ax2.set_zorder(1)

    # 折れ線グラフの背景を透明
    # 重ね順が後ろに設定した棒グラフが消えるのを防ぐ
    ax1.patch.set_alpha(0)

    # 凡例
    # グラフの本体設定時に、ラベルを手動で設定する必要があるのは、barplotのみ。plotは自動で設定される
    handler1, label1 = ax1.get_legend_handles_labels()
    handler2, label2 = ax2.get_legend_handles_labels()

    # ax1.set_title('COCOA 累計ダウンロード数と累計陽性者登録数の変化', pad=8, fontsize=20, color='black')
    ax1.text(x=0.5, y=1.1, s='COCOA 累計ダウンロード数と累計陽性者登録数の変化', fontsize=16,
             weight='bold', ha='center', va='bottom', transform=ax1.transAxes)
    ax1.text(x=0.5, y=1.05, s='土日祝日データ欠損', fontsize=8, alpha=0.75,
             ha='center', va='bottom', transform=ax1.transAxes)
    ax1.set_ylabel('累積ダウンロード数[万件]')
    ax2.set_ylabel('累積陽性登録数[件]')
    ax1.set_xlabel('更新日')

    # 凡例をまとめて出力する
    ax1.legend(handler1 + handler2, label1 + label2,
               loc="upper left", borderaxespad=1)

    download_max = 3 * max(df['Download(×10,000)'])
    positive_max = 1.2 * max(df['Positive registration'])

    # 最大値設定
    #ax1.set_ylim([0, download_max])
    #ax2.set_ylim([0, positive_max])

    # X-axis setting(表示形式)
    ax1.xaxis.set_major_locator(mdates.DayLocator(
        bymonthday=None, interval=14, tz=None))
    daysFmt = mdates.DateFormatter('%m/%d')
    ax1.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    labels = ax1.get_xticklabels()

    #ローテーション設定
    plt.setp(labels, rotation=45, fontsize=10)

    #レイアウト自動整理
    plt.tight_layout()

    print("Saving sheet_date\n")

    file_name_date = os.path.normpath(os.path.join(os.path.dirname(__file__), '../chart_pool/sheet_date' + str_date + '.png'))
    plt.savefig(file_name_date, dpi=400)
    #plt.show()

    print("Plot of Accumulation[finish]\n")

def graph_dy(df):

    print("Plot of the increase[start]\n")

    # 時刻フォーマット指定
    genzai = datetime.now()
    str_date = genzai.strftime('%Y%m%d')

    # Graph main settings
    sns.set(style="whitegrid", font="IPAexGothic")
    rcParams['figure.figsize'] =  9, 5

    #plt.rcParams['font.family'] ='sans-serif'#使用するフォント
    plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
    plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
    plt.rcParams['font.size'] = 8 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ

    # Figure and Axes
    plt.close(1)  # 既にFigure1が開かれていれば閉じる

    fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx()

    # styleを適用している場合はgrid線を片方消す(2021/1)
    ax1.grid(False)
    #ax2.grid(False)

    # グラフのグリッドをグラフの本体の下にずらす
    ax1.set_axisbelow(True)

    # 色の設定
    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']  # ココがポイント
    color_1 = cm.tab20.colors[0]
    color_2 = cm.tab20.colors[7]
    color_3 = cm.tab20.colors[6]

    #新たなデータフレーム
    #print(df)
    df_copy = df.copy()
    df_copy.interpolate('akima',inplace=True)

    #確認用
    #print(df.interpolate('akima'))

    # Nanを無視して点間を結ぶ
    s1mask = np.isfinite(df['Downlowd incremental(×10,000)'])
    s2mask = np.isfinite(df['Increment of positive registration'])
    s11mask = np.isfinite(df_copy['Downlowd incremental(×10,000)'])
    s22mask = np.isfinite(df_copy['Increment of positive registration'])

    #確認用
    #print(len(df_copy['Update']))
    #print(len(df_copy['Update'][s11mask]))

    #スプライン関数生成
    spline = spline_interp(df_copy['Update'][s11mask],df_copy['Downlowd incremental(×10,000)'][s11mask])

    #移動平均生成
    df_copy['Downlowd incremental(×10,000)']= df_copy['Downlowd incremental(×10,000)'].rolling(window=7).mean()
    #print(df_copy)
    s111mask = np.isfinite(df_copy['Downlowd incremental(×10,000)'])
    s222mask = np.isfinite(df_copy['Increment of positive registration'])
    rol = rol_meen(df_copy['Update'][s111mask],df_copy['Downlowd incremental(×10,000)'][s111mask])

    #確認用
    #print(df_copy['Update'][s111mask])
    #print(df_copy['Download(×10,000)'][s111mask])

    # 1つのaxesオブジェクトのlines属性に2つのLine2Dオブジェクトを追加
    ax1.plot(df['Update'][s1mask], df['Downlowd incremental(×10,000)'][s1mask],
             color=color_1, label="ダウンロード数", marker="o",zorder=2,markersize=1)
    
    ax1.grid(axis='y', color='black', lw=0.4)
    ax2 = ax1.twinx()
    
    #スプライン曲線
    #ax1.plot(spline[0],spline[1],color=color_1, label="",zorder=3)

    #移動平均線
    #ax1.plot(rol[0],rol[1],color=color_3, label="移動平均",zorder=4)

    #棒グラフ
    ax2.bar(df['Update'][s2mask], df['Increment of positive registration']
            [s2mask], color=color_2, label="陽性登録数",zorder=1)
    ax2.grid(None)
    
    # 軸の目盛りの最大値をしている
    ## axesオブジェクトに属するYaxisオブジェクトの値を変更
    #ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))
    #ax2.yaxis.set_major_locator(MaxNLocator(nbins=5))

    # Y-axis setting(edited 2021/1)
    nticks = 6
    mticks = 11

    ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
    ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))

    ax1.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(mticks))
    ax2.xaxis.set_major_locator(matplotlib.ticker.LinearLocator(mticks))

    # round()で四捨五入して丸める
    ax1.set_ylim(0,round(max(df['Downlowd incremental(×10,000)'][s1mask])+  20, -1))
    #ax1.set_xlim(0,10)
    ax2.set_ylim(0,round(max(df['Increment of positive registration'][s2mask])+ 20, -1))


    # 軸の縦線の色を変更している
    # axesオブジェクトに属するSpineオブジェクトの値を変更
    # 図を重ねてる関係で、ax2のみ
    ax2.spines['left'].set_color(color_1)
    ax2.spines['right'].set_color(color_2)

    ax1.spines['left'].set_color(color_1)
    ax1.spines['right'].set_color(color_2)

    # 軸の縦線の色を変更している
    ax1.tick_params(axis='y', colors=color_1, direction='in',length = 5,width = 1)
    ax2.tick_params(axis='y', colors=color_3, direction='in',length = 5,width = 1)
    ax1.tick_params(axis='x', which='major',direction='in',length = 5,width = 1)
    ax2.tick_params(axis='x', which='major',direction='in',length = 5,width = 1)

    ax1.tick_params(labelbottom=True)
    ax2.tick_params(labelbottom=True)
    #ax.tick_params(axis = 'both', length = 0 )

    # 軸の目盛りの単位を変更する
    # ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d件"))
    # ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d件"))

    #重ね順として折れ線グラフを前面
    #棒グラフに折れ線が隠れてしまうのを防ぐ
    ax1.set_zorder(2)
    ax2.set_zorder(1)

    #折れ線グラフの背景を透明
    #重ね順が後ろに設定した棒グラフが消えるのを防ぐ
    ax1.patch.set_alpha(0)

    # 凡例
    # グラフの本体設定時に、ラベルを手動で設定する必要があるのは、barplotのみ。plotは自動で設定される
    handler1, label1 = ax1.get_legend_handles_labels()
    handler2, label2 = ax2.get_legend_handles_labels()

    # Title
    ax1.text(x=0.5, y=1.1, s='COCOA 各更新日毎の変化量について', fontsize=16,
             weight='bold', ha='center', va='bottom', transform=ax1.transAxes)
    ax1.text(x=0.5, y=1.05, s='土日祝日データ欠損', fontsize=8, alpha=0.75,
             ha='center', va='bottom', transform=ax1.transAxes)
    ax1.set_ylabel('ダウンロード数[万件]')
    ax2.set_ylabel('陽性登録数[件]')
    ax1.set_xlabel('更新日')

    # 凡例をまとめて出力する
    ax1.legend(handler1 + handler2, label1 + label2,
               loc="upper left", borderaxespad=1)

    download_max = 1.2 * max(df['Downlowd incremental(×10,000)'])
    #positive_max = 1.2 * max(df['Increment of positive registration'])

    # 最大値設定
    #ax1.set_ylim([0, download_max])
    #ax2.set_ylim([0, positive_max])

    # ##以下をカスタマイズする
    ax1.xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=14, tz=None))
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

    print("Saving sheet_dy\n")
    file_name_date = os.path.normpath(os.path.join(os.path.dirname(__file__), '../chart_pool/sheet_dy' + str_date + '.png'))
    plt.savefig(file_name_date, dpi=400)
    #plt.show()

    print("Plot of the increase[finish]\n")
