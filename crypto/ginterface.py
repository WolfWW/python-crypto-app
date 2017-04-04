#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import base,crypto


root = Tk()
root.title('Python Crypto')
root.resizable(False,False)  #禁止用户改变窗口大小

#初始化选择
init_frame = Frame(root)
init_frame.pack()

def judgMode(event):
    if mode.get() == 'DES':
        des_key_entry['state'] = 'normal'
        des_IV_entry['state'] = 'normal'
        key_filename_entry['state'] = 'disabled'
        sig_filename_entry['state'] = 'disabled'
    elif mode.get() == 'RSA' or '混合模式':
        des_key_entry['state'] = 'disabled'
        des_IV_entry['state'] = 'disabled'
        key_filename_entry['state'] = 'normal'
        sig_filename_entry['state'] = 'disabled'
    elif mode.get() == '数字签名':
        des_key_entry['state'] = 'disabled'
        des_IV_entry['state'] = 'disabled'
       
def judgOperation(event):
    if operation.get() == '签名':
        key_filename_entry['state'] = 'normal'
        sig_filename_entry['state'] = 'disabled'
    elif operation.get() == '验证':
        key_filename_entry['state'] = 'normal'
        sig_filename_entry['state'] = 'normal'
       
#模式选择
mode_label = Label(init_frame,text='模式选择:')
mode_label.grid(row=0,column=0,padx=5,pady=5)
mode = StringVar()
mode.set('DES')  #设置默认值
mode_choice = ttk.Combobox(init_frame,textvariable=mode,values=['DES','RSA','混合模式','数字签名'],width=18,state='readonly')
mode_choice.grid(row=0,column=1,padx=0,pady=5)
mode_choice.bind('<FocusOut>',judgMode)

#操作选择
oper_label = Label(init_frame,text='操作选择:')
oper_label.grid(row=0,column=2,padx=10,pady=5)
operation = StringVar()
operation.set('加密')  #设置默认值
operation_choice = ttk.Combobox(init_frame,textvariable=operation,values=['加密','解密','签名','验证'],width=18,state='readonly')
operation_choice.grid(row=0,column=3,padx=0,pady=5)
operation_choice.bind('<FocusOut>',judgOperation)

#RSA密钥生成
rsa_bits_label = Label(init_frame,text='RSA选择:')
rsa_bits_label.grid(row=1,column=0,padx=5,pady=15)
keys = StringVar()
keys.set('1024')  #设置默认值
keys_choice = ttk.Combobox(init_frame,textvariable=keys,values=['1024','2048','3072','4096'],width=18,state='readonly')
keys_choice.grid(row=1,column=1,padx=0,pady=5)

def rsakey():
    textVar = base.geneKeys(int(keys_choice.get()))
    text.insert(END,textVar)
    text.insert(END,'\n')

#密钥生成按钮
gene_key_button = Button(init_frame,text='生成RSA密钥文件',command=rsakey,width=20)
gene_key_button.grid(row=1,column=3,padx=0,pady=20)

#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)


#密钥输入
key_frame = Frame(root)
key_frame.pack()


#DES密钥
des_key_label = Label(key_frame,text='DES密钥:')
des_key_label.grid(row=0,column=0,padx=5,pady=5)
des_key = StringVar()
des_key_entry = Entry(key_frame,textvariable=des_key,width=10,show='*')
des_key_entry.grid(row=0,column=1)


#DES初始值
des_IV_label = Label(key_frame,text='DES初始值:')
des_IV_label.grid(row=1,column=0,padx=5,pady=15)
des_IV = StringVar()
des_IV_entry = Entry(key_frame,textvariable=des_IV,width=10,show='*')
des_IV_entry.grid(row=1,column=1)

#RSA密钥读取
key_file_label = Label(key_frame,text='密钥文件:')  #标签，这里只显示字符
key_file_label.grid(row=0,column=2,padx=20,pady=5)  #给标签定位
#输入密钥文件路径
key_filename = StringVar()      #实例化一个字符串变量
key_filename_entry = Entry(key_frame,textvariable=key_filename,width=20)
key_filename_entry.grid(row=0,column=3)
#选择密钥文件
def openKeyFile():
    global key_filename_entry  #如果要在函数中复制，就要声明全局变量
    fileName = filedialog.askopenfilename()
    key_filename_entry.delete(0,END) #清空输入框已有内容
    key_filename_entry.insert(0,fileName)  #将文件路径填入输入框
Button(key_frame,text="浏览文件",command=openKeyFile).grid(row=0,column=4)

#签名文件
sig_file_label = Label(key_frame,text='签名文件:')
sig_file_label.grid(row=1,column=2,padx=20,pady=15)
#输入签名文件路径
sig_filename = StringVar()
sig_filename_entry = Entry(key_frame,textvariable=sig_filename,width=20)
sig_filename_entry.grid(row=1,column=3)
#选择签名文件
def openSigFile():
    global sig_filename_entry
    fileName = filedialog.askopenfilename()
    sig_filename_entry.delete(0,END)
    sig_filename_entry.insert(0,fileName)
Button(key_frame,text="浏览文件",command=openSigFile).grid(row=1,column=4)


#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)



#执行操作
final_frame = Frame(root)
final_frame.pack()
#源文件选择
raw_file_label = Label(final_frame,text='源文件:')
raw_file_label.grid(row=0,column=0,padx=5,pady=5)
#输入源文件路径
rawfilename = StringVar()
rawfilename_entry = Entry(final_frame,textvariable=rawfilename,width=20)
rawfilename_entry.grid(row=0,column=1)
#选择源文件
def openRawFile():
    global rawfilename_entry
    fileName = filedialog.askopenfilename()
    rawfilename_entry.delete(0,END)
    rawfilename_entry.insert(0,fileName)
Button(final_frame,text="浏览文件",command=openRawFile).grid(row=0,column=2)

#执行按钮
def cryption():
    mode = mode_choice.get()
    operation = operation_choice.get()
    des_key = des_key_entry.get()
    des_IV = des_IV_entry.get()
    key_filename = key_filename_entry.get()
    sig_filename = sig_filename_entry.get()
    rawfilename = rawfilename_entry.get()
    textVar = crypto.doCrypto(mode,operation,des_key,des_IV,key_filename,sig_filename,rawfilename)
    text.insert(END,textVar)
    text.insert(END,'\n')
do_button = Button(final_frame,text='执行操作',command=cryption,width=20)
do_button.grid(row=0,column=3,padx=5,pady=5)
#退出按钮
exit_button = Button(final_frame,text='退出',command=root.quit,width=5)
exit_button.grid(row=0,column=4,padx=5,pady=5)
#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

#进度显示
text = Text(height=20,width=60,bd=3,relief=SUNKEN)
text.pack(padx=5,pady=5)



mainloop()
