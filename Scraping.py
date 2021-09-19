## スクレイピング
## https://qiita.com/Kenta-Han/items/83a23bc3a0c53cc170a2
from bs4.element import SoupStrainer
import requests  ##スクレイピング用
from bs4 import BeautifulSoup  ##スクレイピング用
import json  ##Python3 で JSON 形式のデータを扱う方法
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning) ##エラー消す

import sys
sys.path.append("lib.bs4")
from bs4 import BeautifulSoup

##html = ...
##soup = BeautifulSoup(html, "html.parser")


min_page = 1
max_page = 898
data_list = [] ##1体ずつデータを入れる

f = open('myfile.txt', 'w', encoding='UTF-8')

while min_page <= max_page:
    target_url = "https://zukan.pokemon.co.jp/detail/" + str(min_page).zfill(3)
    print(target_url)  ## url表示

    r = requests.get(target_url,verify=False)         ##　requestsを使って、webから取得
    soup = BeautifulSoup(r.content, "html.parser") ##　要素の抽出

    ## 特定のタグの取得　(scriptタグのtypeのapplication/ld+jsonを指定)
    ##title_part = soup.find_all("script", {"type": "application/ld+json"}) 
    title_part = soup.find_all("span","div")
    for i in title_part:
        title = i.get_text() ##タグの中のtext部分のみを指定
        print(title)
        a = json.loads(title)
        ## JSON ファイルを load 関数で読み込むと、Python で扱いやすいように辞書型で保存されます。
        ## 辞書型なら要素の取り出しなどが容易に出来て便利です．

        data_list.append[title] ##リストにデータ入れてる
        f.write(*data_list,sep=",") ##カンマ区切りで出力
        data_list.clear()   ##リスト初期化

        min_page += 1   ##ページ数を1追加