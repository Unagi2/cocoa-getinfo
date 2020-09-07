# cocoa-getinfo:COCOA-appに関する公式情報取得

![GitHub top language](https://img.shields.io/github/languages/top/Unagi2/cocoa-getinfo?style=flat-square)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Unagi2/cocoa-getinfo?style=flat-square)
![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Unagi2/cocoa-getinfo?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/Unagi2/cocoa-getinfo?style=flat-square)
![Commit Msg](https://img.shields.io/badge/Commit%20message-Ja-brightgreen.svg?style=flat-square)
![Code Cmnt](https://img.shields.io/badge/code%20comment-Ja-brightgreen.svg?style=flat-square)

本システムは、厚生労働省が発表する接触確認アプリの「ダウンロード数」や「陽性登録数」の情報を取得する事が可能である。


またこれに付随し、本システムは取得したデータをGoogleスプレッドシートに出力、matplotlibによるグラフ生成と画像出力、Twitterへの自動投稿などの機能を有している。


情報取得先は厚生労働省の特設サイト「新型コロナウイルス接触確認アプリ（COCOA) COVID-19 Contact-Confirming Application」である。


本プロジェクトは，厚生労働省が公開する情報を収集するため，スクレイピングプログラムを搭載している。
そのため，厚生労働省のrobot.txt（<https://www.mhlw.go.jp/robots.txt>）によるクローラ許可範囲の確認，「利用規約・リンク・著作権等」に則り制作している。


また，アクセス先サーバへの負担軽減やDoS状態を防ぐため，プログラムは更新される時間帯のみに作動させ，アクセスリトライ間隔は余裕を持たせた「５分」に設定している。



-   「新型コロナウイルス接触確認アプリ」（厚生労働省）（<https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html>）を加工して作成

# DEMO(cocoa_webupdate_nitify.py実行時)

**1.  [Start]スクレイピングによる画像取得の進捗画面**

```
cd cocoa-getinfo
python3 webupdate_notify.py #基幹プログラム開始

holiday.py Start process #土日祝日判別プログラム

Weekday Mode #処理結果:平日

Web更新チェック開始

[！！更新検知！！] 

検知時刻:2020/09/07 17:11

==Start Main==

[1/5 Processing image acquisition...] #画像取得プログラム

[Completed!]
```

**2.  OCRプログラム稼働中の進捗画面**

```
[2/5 Processing OCR...] #OCR処理（画像->文字）

と 接触 確認 アブ プリ は 、iOS・Android と も に 、 現 在 、「1.1.2」 を 配布 し て いま す 。
古い バー ジョ ン の アブ リ を ご 利用 の 方 は 、App Store ま た は Googsle Play か ら 「 接 触 確
認 ア ブリ 」 を 検索 いた だ き 、 アッ プ デ ー ト を お 願い し ます 。

・ ダウ ン ロ ー ド 数 は 、9 月 7 日 17:00 現 在 、 合 計 で 約 1.631 万 件 で す 。
・ios、Android 両 方 の 合計 の 数 に な り ま す 。
・ ダ ウン ロー ド 後 に 削除 し 、 再 度 ダ ウン ロー ド し た 場合 は 、 複 数 回 カウ ント され る 場
合 が あり ます 。

・ 陽性 登録 件 数 は 、9 月 7 日 17:00 現 在 、 合 計 で 623 件 で す 。

[Completed!]
```

| 取得画像 | TesseractによるOCR後の出力 |
| ---|---|
| ![cocoa_info_0810](https://user-images.githubusercontent.com/34627350/89762922-618e9680-db2c-11ea-8d15-e53a7fc5c570.png) | ![DEMO2](https://user-images.githubusercontent.com/34627350/89762891-4d4a9980-db2c-11ea-8410-b460420d9b95.png) |

**3.  テキストの整形及びデータ抽出の進捗画面**

- 公式情報が更新される平日のモード
```
[3/5 Processing data extraction and output... ] #数値データの抽出とログ出力

と接触確認アブプリは、iOS・Androidともに、現在、「1.1.2」を配布しています。古いバージョンのアブリをご利用の方は、AppStoreまたはGoogslePlayから「接触確認アブリ」を検索いただき、アップデートをお願いします。・ダウンロード数は、9月7日17:00現在、合計で約1.631万件です。・ios、Android両方の合計の数になります。・ダウンロード後に削除し、再度ダウンロードした場合は、複数回カウントされる場合があります。・陽性登録件数は、9月7日17:00現在、合計で623件です。

データ取得日 : 2020/09/07

Mode : データ更新処理

ダウンロード数 : 1.631

陽性者登録数 : 623

経過日数 : 80
[Completed!]
```


- 公式情報の更新が無い土日祝日のモード
```
[Processing data extraction and output... ]

接触確認アプリは、iOS・Androidともに、現在、「1.1.2」を配布しています。古いバージョンのアプブリをご利用の方は、App StoreまたはGoogle Playから「接触確認アプリ」を検索いただき、 アップデートをお願いします。ダウンロード数は、8月7日17:00現在、 合計で約1.205万件です。・iOS、Android両方の合計の数になります。・ダウンロード後に削除し、再度ダウンロードした場合は、複 数回カウントされる場合があります。陽性登録件数は、8月7日17:00現在、合計で165件です。

データ取得日 : 08/10

Mode : 土日祝日処理

ダウンロード数 : N/A

陽性者登録数 : N/A

経過日数 : 52
[Completed data extraction and output processing]

```

**4.  Google Spreadsheetからデータを読み取り，グラフ生成時の進捗画面**
```

Plot of Accumulation[start] #累積グラフ作成
Saving #画像保存中
Plot of Accumulation[finish]

Plot of the increase[start]　#増加量グラフ作成
Saving
Plot of the increase[finish]

Plot of Download Moving Average[start] #移動平均グラフ（Test）
Saving
Plot of Download Moving Average[finish]

Plot of Positive Moving Average[start]#移動平均グラフ（Test）
Saving
Plot of Positive Moving Average[finish]

```

**5.  読み取ったデータと生成したグラフをツイートに送信する際の進捗画面**
```
[First tweet]

9月7日17:00現在
・ダウンロードは、合計1,631万件
・陽性登録件数は、合計623件

8/18より画像内の一部が乱れています。ご了承ください。

Google Data Portalにてレポート公開
https://datastudio.google.com/u/0/reporting/f9081247-b6d3-48b8-a6e2-82d3b0b018ce/page/EczbB

#COCOA #接触確認アプリ


[Second tweet]

9月7日17:00現在
更新日毎の増分変化についてのグラフ

8/18より画像内の一部が乱れています。ご了承ください。

Google Data Portalにてレポート公開
https://datastudio.google.com/u/0/reporting/f9081247-b6d3-48b8-a6e2-82d3b0b018ce/page/EczbB

#COCOA #接触確認アプリ

[Completed!]

==End Main==

更新チェック終了

holiday.py END process
```


**6.  出力状況（GoogleSheetの状況と、matplotlibにより生成したグラフの出力画像）**

| シートへの書き込み | グラフ作成 |
| ---|---|
| ![DEMO6](https://user-images.githubusercontent.com/34627350/89765181-c9df7700-db30-11ea-8f40-a9fc773907de.png) | ![sheet_date20200907](https://user-images.githubusercontent.com/34627350/92392694-9e64a200-f159-11ea-8479-9a1e6c79b9a3.png) |

# Features

厚生労働省から発表される掲載情報は、テキストデータが画像化されておりデータ抽出には文字認識を行う必要がある。
今回、文字認識（OCR）にはCloudVisionなどのクラウドサービスを使わずに、「Tesseract」を使用しており導入がしやすくなっている。

# Requirement

Tesseractの導入方法について

-   参考リンク:<https://rightcode.co.jp/blog/information-technology/python-tesseract-image-processing-ocr>

"cocoa-getinfo"を動かすのに必要なライブラリは以下に示す。

-   pyocr 0.7.2
-   tweepy 3.7.0
-   oauth2client 4.1.3
-   oauthlib 3.0.0
-   google-auth 1.20.1
-   google-auth-oauthlib 0.4.1
-   gspread 3.6.0
-   japanize-matplotlib 1.1.2
-   pandas 1.1.1
-   cycler 0.10.0
-   Pillow 7.2.0
-   matplotlib 3.3.1
-   numpy 1.19.1
-   scipy 1.5.2
-   seaborn 0.10.1

# Installation
まとめて必要ライブラリのインストールを行う方法
```bash
python3 -m pip install -r requirements.txt
```

個々のライブラリについては、適宜pipコマンドや，apt-getコマンド（推奨）でインストールを行う

```bash
python3 -m　pip install [ライブラリ名]
```

```bash
sudo apt-get install python3-[ライブラリ名]
```

Numpyに関して導入が上手くいかない方（Raspberry Pi 3B+）

```bash
sudo apt-get install libatlas-base-dev
pip3 uninstall numpy  # remove previously installed version
sudo apt install python3-numpy
```

# Usage

本システムの実行方法

```bash
git clone https://github.com/Unagi2/cocoa-getinfo
cd cocoa-getinfo
python webupdate_notify.py
```

各機能の個別実行方法

-   画像取得処理

```bash
cd cocoa-getinfo/sub_sys
python3 cocoa_fetch.py
```

-   OCR処理

```bash
cd cocoa-getinfo/sub_sys
python3 cocoa_ocr.py
```

-   データ抽出とGoogleスプレッドシートへの書き込み処理

```bash
cd cocoa-getinfo/sub_sys
python3 cocoa_wordsearch_datapush.py
```

-   Googleスプレッドシートのグラフ生成と画像出力処理(この機能を単独で利用する場合，一時的にcocoa_gspread_pull.py内の"from sub_sys"を消す必要あり)

```bash
cd cocoa-getinfo/sub_sys
python3 cocoa_gspread_pull.py
```

-   ツイート投稿処理

```bash
cd cocoa-getinfo/sub_sys
python3 cocoa_tweet.py
```

# Note

**注意点**
-   Googleスプレッドショートへの編集権限を必要とするため、「サービスアカウント」を作成する必要がある。また、作成した認証情報のjsonファイルは、key_poolディレクトリに入れること。
    <br>
    参考リンク：<https://qiita.com/akabei/items/0eac37cb852ad476c6b9><br>
-   Twitterへのツイート権限を必要とするため、Twitter APIを取得する必要がある。認証情報は、cocoa_tweet.py内の26行目を参照し、key_poolディレクトリに保存すること。<br>
-   Googleスプレッドシートのグラフの画像取得を可能にするため、事前に「グラフの公開」より 画像公開リンクを作成する必要がある。（2020/9/7 グラフ生成システムへの移行により本画像取得機能は廃止）

**出典・引用サイト**
-   新型コロナウイルス接触確認アプリ（COCOA) COVID-19 Contact-Confirming Application(厚生労働省)<br>
    <https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/cocoa_00138.html>
-   Webページ更新を自動チェックして通知させよう <br>
    <http://shinnandesu.hatenablog.com/entry/2018/05/26/172751>
-   【Windows】Pythonでスクリプトを自動実行する方法を現役エンジニアが解説【初心者向け】<br>
    <https://techacademy.jp/magazine/31962>
-   Raspberry PiのPythonライブラリはpipよりapt-getで入れるのが断然早い<br>
    <https://karaage.hatenadiary.jp/entry/2018/10/05/073000>
-   python 時系列データの補間<br>
    <https://qiita.com/kenichi-hamaguchi/items/3c5e63e195e06a21d1da>
-   Scipy.interpolate を使った様々な補間法<br>
    <https://qiita.com/maskot1977/items/913ef108ff1e2ba5b63f>
-   欠損値を処理する方法<br>
    <https://qiita.com/ground0state/items/40c2cf0295af53d1193e>
-   pandasで欠損値NaNを前後の値から補間するinterpolate<br>
    <https://note.nkmk.me/python-pandas-interpolate/>
-   matplotlib 54. ConciseDateFormatterで時系列グラフの軸ラベルをシンプルにする<br>
    <https://sabopy.com/py/matplotlib-54/>
-   Matplotlib-2軸グラフの書き方<br>
    <https://datumstudio.jp/blog/matplotlib-2%E8%BB%B8%E3%82%B0%E3%83%A9%E3%83%95%E3%81%AE%E6%9B%B8%E3%81%8D%E6%96%B9>
-   matplotlibで二軸のグラフを作成する<br>
    <https://www.so-wi.com/2019/12/11/two_axises_chart.html>
-   matplotlibでグラフのスムージング<br>
    <https://snova301.hatenablog.com/entry/2018/10/07/135233>

# Author

-   Unagi.
-   E-mail:30.unagi@gmail.com

# License

"cocoa-getinfo" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
