#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from tkinter import *
from tkinter import ttk


root = Tk()
root.title(u"Software Title")
root.geometry("400x300")

#
# ボタンが押されるとここが呼び出される
#
def DeleteEntryValue(event):
    #エントリーの中身を削除
    EditBox.delete(0, tk.END)


#エントリー
EditBox = ttk.Entry(width=10)
EditBox.insert(tk.END,"挿入する文字列")
EditBox.pack()

#ボタン
Button = ttk.Button(text=u'ボタンです', width=50)
Button.bind("<Button-1>",DeleteEntryValue) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button.pack()

root.mainloop()