# cocoa-getinfo:COCOA-appに関する公式情報取得
![GitHub top language](https://img.shields.io/github/languages/top/Unagi2/cocoa-getinfo?style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Unagi2/cocoa-getinfo?style=flat-square)
![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Unagi2/cocoa-getinfo?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/Unagi2/cocoa-getinfo?style=flat-square)
![Commit Msg](https://img.shields.io/badge/Commit%20message-Ja-brightgreen.svg?style=flat-square)
![Code Cmnt](https://img.shields.io/badge/code%20comment-Ja-brightgreen.svg?style=flat-square)

本システムは、厚生労働省が発表する接触確認アプリの「ダウンロード数」や「陽性登録数」の情報を取得する事が可能である。またこれに付随し、本システムは取得したデータをGoogleスプレッドシートに出力、グラフ画像の取得、Twitterへの自動投稿などの機能を有している。

情報取得先は厚生労働省の特設サイト「新型コロナウイルス接触確認アプリ（COCOA) COVID-19 Contact-Confirming Application」である。
* https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html

# DEMO
1.  [Program Start]スクレイピングによる画像取得の進捗画面

'''
==Start Main==


[Processing image acquisition...]

[Image acquisition processing completed]
'''

2.  OCRプログラム稼働中の進捗画面

|　取得画像　|　TesseractによるOCR後の出力　|
|---|---|
|![cocoa_info_0810](https://user-images.githubusercontent.com/34627350/89762922-618e9680-db2c-11ea-8d15-e53a7fc5c570.png)|![DEMO2](https://user-images.githubusercontent.com/34627350/89762891-4d4a9980-db2c-11ea-8410-b460420d9b95.png)|

3. テキストの整形及びデータ抽出の進捗画面
'''
[Processing data extraction and output... ]

接触確認アプリは、iOS・Androidともに、現在、「1.1.2」を配布しています。古いバージョンのアプブリをご利用の方は、App StoreまたはGoogle Playから「接触確認アプリ」を検索いただき、 アップデートをお願いします。ダウンロード数は、8月7日17:00現在、 合計で約1.205万件です。・iOS、Android両方の合計の数になります。・ダウンロード後に削除し、再度ダウンロードした場合は、複 数回カウントされる場合があります。陽性登録件数は、8月7日17:00現在、合計で165件です。

データ取得日 : 08/10

Mode : 土日祝日処理

ダウンロード数 : N/A

陽性者登録数 : N/A

経過日数 : 52
[Completed data extraction and output processing]

'''

4. [Program End]Google Spreadsheetからのグラフ取得(画像)の進捗画面
'''
[Google Sheet download in progress... ]

[Google Sheet download process complete]


==End Main==

'''

5. 出力状況（GoogleSheetの状況と生成したグラフの画像取得）

| シートへの書き込み | グラフ作成 |
|---|---|
|![DEMO6](https://user-images.githubusercontent.com/34627350/89765181-c9df7700-db30-11ea-8f40-a9fc773907de.png)|![sheet_date0810](https://user-images.githubusercontent.com/34627350/89763552-ba126380-db2d-11ea-8f75-0ad5d2d800d6.png)|

# Features

厚生労働省から発表される情報は、画像化されておりデータ抽出には文字認識を行う必要がある。
今回、文字認識（OCR）にはCloudVisionなどのクラウドサービスを使わずに、「Tesseract」を使用しており導入がしやすくなっている。

# Requirement
* Tesseractの導入方法:https://rightcode.co.jp/blog/information-technology/python-tesseract-image-processing-ocr

"cocoa-getinfo"を動かすのに必要なライブラリは以下に示す。

* pyocr 0.7.2
* tweepy 3.7.0
* oauth2client 4.1.3
* oauthlib 3.0.0
* google-auth 1.20.1
* google-auth-oauthlib 0.4.1
* gspread 3.6.0
* Pillow 7.2.0

# Installation

未インストールのライブラリについては、適宜pipコマンドでインストールを行う

```bash
pip install [ライブラリ名]
```

# Usage

本システムの実行方法

```bash
git clone https://github.com/Unagi2/cocoa-getinfo
cd cocoa-getinfo
python COCOA_Analysis.py
```
各機能の個別実行方法
* 画像取得処理
```bash
cd cocoa-getinfo/SubSys
python cocoa_get.py
```
* OCR処理
```bash
cd cocoa-getinfo/SubSys
python cocoa_ocr.py
```
* データ抽出とGoogleスプレッドシートへの書き込み処理
```bash
cd cocoa-getinfo/SubSys
python cocoa_wordsearch_datapush.py
```
* Googleスプレッドシートのグラフ画像のダウンロード処理
```bash
cd cocoa-getinfo/SubSys
python cocoa_sheetDL.py
```
* ツイート投稿処理
```bash
cd cocoa-getinfo/SubSys
python cocoa_tweet.py
```
# Note

注意点
* Googleスプレッドショートへの編集権限を必要とするため、「サービスアカウント」を作成する必要がある。また、作成した認証情報のjsonファイルは、key_poolディレクトリに入れること。
参考リンク：https://qiita.com/akabei/items/0eac37cb852ad476c6b9
* Twitterへのツイート権限を必要とするため、Twitter APIを取得する必要がある。
* Googleスプレッドシートのグラフの画像取得を可能にするため、事前に「グラフの公開」より 画像公開リンクを作成する必要がある。

# Author

* Unagi.
* E-mail:30.unagi@gmail.com

# License

"cocoa-getinfo" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
