from SubSys import cocoa_get
from SubSys import cocoa_pyocr
from SubSys import cocoa_wordsearch_datapush
from SubSys import cocoa_sheetDL
from SubSys import cocoa_tweet
import time

def main_process():
    print("\n==Start Main==\n")

    # print("\n[Image Get...]\n")
    cocoa_get.get_image()

    # print("[OCR Process...]\n")
    cocoa_pyocr.py_ocr()

    # print("[Data Sample & GoogleSheet DataPush Process... ]\n")
    cocoa_wordsearch_datapush.search_and_push()

    print("\nInterval Time 5sec\n")
    time.sleep(5)

    # print("[GoogleSheet Downloads Process... ]\n")
    cocoa_sheetDL.sheet_dl()

    print("\nInterval Time 5sec\n")
    time.sleep(1)

    # Tweet Process(Test ver.)
    cocoa_tweet.tweet()

    print("\n==End Main==\n")


if __name__ == "__main__":
    main_process()
