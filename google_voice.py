import os
from urllib import parse
import requests

# 設定附檔名 + 預設網址 + 資料夾位置
extension = '.mp3'
url = 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q='
voice_dir = 'voice/'
read_file = 'all.txt'

# 建立資料夾
if not os.path.exists(voice_dir):
    os.mkdir(voice_dir)

# 開檔 + 讀檔 + 遍歷
file = open('all.txt', encoding="utf-8", mode="w+")
for now_download in file.readlines():
    # 存取網站(編碼轉譯)
    html = requests.get(url + parse.quote(now_download))

    # 設定儲存的路徑 + 主檔名
    full_path = os.path.join(voice_dir, now_download.rstrip())

    # 寫檔 + 補上副檔名 + 關檔
    with open(full_path + extension, 'wb') as f:
        f.write(html.content)
