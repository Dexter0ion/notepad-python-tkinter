#coding=utf-8

import os

def append_text(text):
    f = open('diary.log','a')
    f.write(text+'\n')
    f.close()

def get_text():
    if not os.path.exists('diary.log'):
        append_text('')
    else:
        f = open('diary.log')
        text = f.read()
        f.close()
        return text
    
def delete_text():
    f = open('diary.log','w')
    f.write('')
    f.close()
    
if __name__ == '__main__':
    while True:
        text_input = raw_input('写点什么？：\n>')
        if text_input.lower() in ['quit','q','exit']:break
        if text_input.lower() in ['clear']:delete_text()
        append_text(text_input)
        print "嗯哼：\n",get_text()
