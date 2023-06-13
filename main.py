# coding: utf -8
from urllib import response
import PySimpleGUI as sg  
import urllib.request as req
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL

sg.theme('BrightColors')

# レイアウト
layout = [
    [sg.Text('URLを入力'), sg.InputText(key='-Input1-')],
    [sg.Button('タイトルを取得', key='title'), sg.Text('', key='output')],
    [sg.Text('保存先を指定'), sg.FolderBrowse(key='-Input2-')],
    [sg.Text('※保存先を指定しない場合、実行ファイルと同じ階層に保存されます', size=55)],
    [sg.Button('mp4形式で保存', key='btn1'), sg.Button('mp3形式で保存', key='btn2'), sg.Button('終了',key='close')]
]
# ウィンドウ作成
window = sg.Window('YT Downloader by asa', layout,)


while True:
    event, values = window.read()
    
    try:
        if event == 'title':
            url = values['-Input1-']
            response = req.urlopen(url)
            parse_html = BeautifulSoup(response, "html.parser")
            window['output'].update(parse_html.title.string)
        # webスクレイピングによるタイトルの確認。キーはtitle
        

        if event == 'btn1':
            url = values['-Input1-']
            path = values['-Input2-']
            print(path)
            ydl_opts = {
                'format': 'best',
                'outtmpl': f'{path}/%(title)s.%(ext)s'
                }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        if event == 'btn2':
            url = values['-Input1-']
            path = values['-Input2-']
            print(path)
            ydl_opts = {
                'outtmpl': f'{path}/%(title)s.%(ext)s',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                    }],
                }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
        if event == sg.WIN_CLOSED or event == 'close':
            break
        
    except:
        print('エラーが発生しました')
        
    else:
        print('完了しました')
        
print('終了します。')
window.close()