
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Tkinter 有自己的变量类，通过使用类里的get()和set()实例方法来操作变量

import Tkinter as tk
from diary import *

root = tk.Tk()
root.title("DEXION'S LOG DIARY")
root.geometry('400x400')
labHello=tk.Label(root,text="This is your notepad",pady=20).pack()  #pady是padding
strVarIntro = tk.StringVar(value="This is Python Magic Tkinter")

txtInput = tk.Entry(root,textvariable=strVarIntro,width=36)
txtInput.pack()


def print_content():
    textCheck = strVarIntro.get()
    if(textCheck=="clear"):
        delete_text()
    else:
        
        append_text(strVarIntro.get())  #调用diary.py的函数 将输入信息更新到diary.log里

    txtOutput.config(text=get_text()) #通过config更新message里要显示的信息
    #print strVarIntro.get() #获取输入值
    strVarIntro.set('') #设空

#btnView = tk.Button(root,text="View",command=print_content).pack()
root.bind('<Return>',lambda event:print_content())


txtOutput = tk.Message(root,text='',width=360, pady=20)
txtOutput.pack()
'''
txtOutput = tk.Message(root,textvariable = strVarIntro)
txtOutput.pack()
'''
root.mainloop()
