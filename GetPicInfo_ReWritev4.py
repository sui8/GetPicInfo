# Made by suiken-Developer
import tkinter as tk # メイン描画用
from tkinter import * # メイン描画用
from tkinter import ttk # メイン描画用
from tkinter import messagebox as msgbox # ダイアログ用
from tkinter import filedialog as fd # パス関係
from PIL import Image # 画像ファイルの扱い
import os, sys # パス関係
import glob # パス関係
import imghdr # 現在未使用
import webbrowser as web # ハイパーリンク用

root = tk.Tk()

root.geometry("500x125")
root.title("GetPicInfo ReWrite Ver 4.0.0")
root.iconbitmap("./icon.ico")

SaveName = "Export.txt"

# パスの取得
def dir_get():
    Dir = os.path.abspath(os.path.dirname(__file__))
    Dir_Path = fd.askdirectory(initialdir = Dir)
    entry.set(Dir_Path)

# メイン処理
def run():
    global SaveName
    text = ""
    exts = [".jpg", ".jpeg", ".jpe",
            ".jfif", ".pjpeg", ".pjp",
            ".png", ".gif", ",svg",
            ".svgz", ".tif", ".tiff",
            ".bmp", ".dib", ".ico"]
    dir_Path = entry.get()
    if not os.path.isdir(dir_Path):
        msgbox.showerror("GetPicInfo", "指定されたパスは存在しません。")
    if len(os.listdir(dir_Path)) == 0:
        msgbox.showerror("GetPicInfo", "指定されたパスにファイルが存在しません。")

    os.chdir(dir_Path)
    dir_Files = glob.glob("./*")
    Outs = []

    for i in dir_Files:
        try:
            Img_ext = os.path.splitext(i)
            Img_ext = str.lower(Img_ext[1])
            if not Img_ext in exts:
                pass
            else:
                im = Image.open(i)
                ImgW, ImgH = im.size
                Out = str(i) + " 1 0 0 " + str(ImgW) + " " + str(ImgH)
                Out = Out[2:]
                Outs.append(Out)
        except:
            pass

    with open(SaveName, mode="w") as f:
        f.write("\n".join(Outs))

    msgbox.showinfo("GetPicInfo", "処理が正常に終了しました。")

# GitHubを開く
def open_github(e):
    web.open_new(e.widget.cget("text"))
    

# この部分で描画関係

# 参照ボタンの設置

## Frameの作成
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=1, sticky=E)

## ラベルの作成
Dir_Label = ttk.Label(frame, text="実行するフォルダを参照してください", padding=(5, 2))
Dir_Label.pack(side=LEFT)

## 参照エントリーの作成
entry = StringVar()
Dir_Entry = ttk.Entry(frame, textvariable=entry, width=30)
Dir_Entry.pack(side=LEFT)

## 参照ボタンの設置→パスの取得
Dir_Button = ttk.Button(frame, text="参照", command=dir_get)
Dir_Button.pack(side=LEFT)


# 実行ボタンの設置

## Frame2の作成
frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=20,column=1,sticky=W)

## 実行ボタンの設置
Run_Button = ttk.Button(frame2, text="実行", command=run)
Run_Button.pack(fill="x", padx=30)


# GitHubリンク設置

## Frame3の作成
frame3 = ttk.Frame(root, padding=10)
frame3.grid(row=30,column=1,sticky=W)

GitHub_Button = tk.Label(frame3, text=r"https://github.com/suiken-Developer/GetPicInfo", fg="blue", cursor="hand2")
GitHub_Button.pack(fill="x", side=LEFT)
GitHub_Button.bind("<Button-1>", open_github)

# 画面の描画
root.mainloop()
