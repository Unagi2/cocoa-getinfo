# -*- coding: utf-8 -*-
from sub_sys import cocoa_fetch
from sub_sys import cocoa_pyocr
from sub_sys import cocoa_wordsearch_datapush
from sub_sys import cocoa_sheet_load
from sub_sys import cocoa_tweet
import time


def main_process():
    print("\n==土日祝日用　Start Main==\n")

    # print("\n[Image Get...]\n")
    cocoa_fetch.fetch_image()

    # print("[OCR Process...]\n")
    cocoa_pyocr.py_ocr()

    # print("[Data Sample & GoogleSheet DataPush Process... ]\n")
    cocoa_wordsearch_datapush.search_and_push(0)

    print("\n==End Main==\n")


if __name__ == "__main__":
    main_process()
