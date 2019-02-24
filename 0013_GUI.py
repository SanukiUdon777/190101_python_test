#Tkinter(ティーキンター, ティーケーインター)
from tkinter import *
from tkinter import ttk



# コールバック関数の生成
#def make_cmd(n):
#    return lambda : buff.set('button %d pressed' % n)




root = Tk()
root.title('My First App')
root.geometry("400x300")

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")


#ラベル
Static1 = ttk.Label(text=u'test', foreground='#ff0000', background='#ffaacc')
Static1.place(x=200, y=200)
Static1.pack()

#エントリー
EditBox = ttk.Entry()
#EditBox.insert(ttk.END,"挿入する文字列")
EditBox.pack()


#button = Button(root, text = 'Button')
#button.pack()

# ボタンの生成
#for x in range(4):
#    button = Button(root, text = "Button %d" % x, command = make_cmd(x))
#    button.pack()

#frame1 = ttk.Frame(root)
#label1 = ttk.Label(frame1, text='Your name:')

root.mainloop()