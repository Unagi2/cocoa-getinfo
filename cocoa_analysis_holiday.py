from SubSys import cocoa_fetch
from SubSys import cocoa_pyocr
from SubSys import cocoa_wordsearch_datapush
from SubSys import cocoa_sheet_load
from SubSys import cocoa_tweet
import time


def main_process():
    print("\n==土日祝日用　Start Main==\n")

    # print("\n[Image Get...]\n")
    cocoa_fetch.fetch_image()

    # print("[OCR Process...]\n")
    cocoa_pyocr.py_ocr()

    # print("[Data Sample & GoogleSheet DataPush Process... ]\n")
    cocoa_wordsearch_datapush.search_and_push()

    print("\n==End Main==\n")


if __name__ == "__main__":
    main_process()
