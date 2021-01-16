# -*- coding: utf-8 -*-
from sub_sys import cocoa_fetch
from sub_sys import cocoa_pyocr
from sub_sys import cocoa_wordsearch_datapush
from sub_sys import cocoa_sheet_load
from sub_sys import cocoa_tweet
from sub_sys import cocoa_gspread_pull
from sub_sys import cocoa_create_plot
from sub_sys import cocoa_rolling_plot
import time


def main_process():
    print("\n==Start Main==\n")

    # print("\n[Image Get...]\n")
    cocoa_fetch.fetch_image()

    # print("[OCR Process...]\n")
    cocoa_pyocr.py_ocr()

    # print("[Data Sample & GoogleSheet DataPush Process... ]\n")
    cocoa_wordsearch_datapush.search_and_push(1)

    print("\nInterval Time 5sec\n")
    time.sleep(5)

    # print("[GoogleSheet Downloads Process... ]\n")
    #cocoa_sheet_load.sheet_load()

    ###新ver.画像取得システム###

    #DataFlame Get
    df = cocoa_gspread_pull.sheet_pull()
    #df = pd.read_csv('df.csv')
    #print(df)
    #print(gspread_pull())

    # Plot of Accumulation
    cocoa_create_plot.graph_date(df[0])

    # Plot of the increase
    cocoa_create_plot.graph_dy(df[0])

    # Moving average
    ## download
    cocoa_rolling_plot.graph_dl_rol(df[0],df[1])

    ## positive
    cocoa_rolling_plot.graph_posi_rol(df[0],df[1])


    print("\nInterval Time 1sec\n")
    time.sleep(1)

    # Tweet Process(Test ver.)
    cocoa_tweet.tweet()

    print("\n==End Main==\n")


if __name__ == "__main__":
    main_process()
