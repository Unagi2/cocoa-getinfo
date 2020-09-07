# -*- coding: utf-8 -*-
from sub_sys import cocoa_fetch
from sub_sys import cocoa_pyocr
from sub_sys import cocoa_wordsearch_datapush
from sub_sys import cocoa_sheet_load
from sub_sys import cocoa_tweet
from sub_sys import gspread_pull
from sub_sys import create_plot
from sub_sys import rolling_plot
import time


def main_process():
    print("\n==Start Main==\n")

    # print("\n[Image Get...]\n")
    cocoa_fetch.fetch_image()

    # print("[OCR Process...]\n")
    cocoa_pyocr.py_ocr()

    # print("[Data Sample & GoogleSheet DataPush Process... ]\n")
    cocoa_wordsearch_datapush.search_and_push()

    print("\nInterval Time 5sec\n")
    time.sleep(5)

    # print("[GoogleSheet Downloads Process... ]\n")
    #cocoa_sheet_load.sheet_load()

    ###新ver.画像取得システム###

    #DataFlame Get
    df = gspread.sheet_pull()
    #print(df)
    #print(gspread_pull())

    # Plot of Accumulation
    create_plot.graph_date(df)

    # Plot of the increase
    create_plot.graph_dy(df)

    # Moving average
    # download
    rolling_plot.graph_dl_rol(df)

    # positive
    rolling_plot.graph_posi_rol(df)
    #####

    print("\nInterval Time 5sec\n")
    time.sleep(1)

    # Tweet Process(Test ver.)
    cocoa_tweet.tweet()

    print("\n==End Main==\n")


if __name__ == "__main__":
    main_process()
