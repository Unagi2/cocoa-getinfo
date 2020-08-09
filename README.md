# cocoa-getinfo:COCOA-appに関する公式情報取得

本システムは、厚生労働省が発表する接触確認アプリの「ダウンロード数」や「陽性登録数」の情報を取得する事が可能である。またこれに付随し、本システムは取得したデータをGoogleスプレッドシートに出力、グラフ画像の取得、Twitterへの自動投稿などの機能を有している。

# DEMO

作成中

# Features

厚生労働省から発表される情報は、画像化されておりデータ抽出には文字認識を行う必要がある。
今回、文字認識（OCR）にはCloudVisionなどのクラウドサービスを使わずに、「Terrasect」を使用しており導入がしやすくなっている。

# Requirement

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
* Googleスプレッドショートへの編集権限を必要とするため、「サービスアカウント」を作成する必要がある。
参考リンク：https://qiita.com/akabei/items/0eac37cb852ad476c6b9
* Twitterへのツイート権限を必要とするため、Twitter APIを取得する必要がある。
* Googleスプレッドシートのグラフの画像取得を可能にするため、事前に「グラフの公開」より 画像公開リンクを作成する必要がある。

# Author

* Unagi.
* E-mail:30.unagi@gmail.com

# License

"cocoa-getinfo" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
