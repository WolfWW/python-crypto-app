#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
import base
import crypto

root = Tk()
root.title('Python Crypto')
root.resizable(False,False)  #禁止用户改变窗口大小

#-------------------------初始化区域-------------------------#
#初始化选择
init_frame = Frame(root)
init_frame.pack()

#模式判断，模式选择框事件绑定
def judgMode(event):
    if mode.get() == 'DES':
        des_key_entry['state'] = 'normal'
        des_IV_entry['state'] = 'normal'
        key_filename_entry.delete(0,END)
        sig_filename_entry.delete(0,END)
        key_filename_entry['state'] = 'disabled'
        sig_filename_entry['state'] = 'disabled'
    elif mode.get() == 'RSA' or '混合模式':
        des_key_entry.delete(0,END)
        des_IV_entry.delete(0,END)
        sig_filename_entry.delete(0,END)
        des_key_entry['state'] = 'disabled'
        des_IV_entry['state'] = 'disabled'
        key_filename_entry['state'] = 'normal'
        sig_filename_entry['state'] = 'disabled'
    elif mode.get() == '混合模式':  
    #很无奈，不能和RSA合并，会出现未选择模式而密钥文件输入可用的BUG
        des_key_entry.delete(0,END)
        des_IV_entry.delete(0,END)
        sig_filename_entry.delete(0,END)
        des_key_entry['state'] = 'disabled'
        des_IV_entry['state'] = 'disabled'
        key_filename_entry['state'] = 'normal'
        sig_filename_entry['state'] = 'disabled'
    elif mode.get() == '数字签名':
        des_key_entry.delete(0,END)
        des_IV_entry.delete(0,END)
        sig_filename_entry.delete(0,END)
        des_key_entry['state'] = 'disabled'
        des_IV_entry['state'] = 'disabled'
        key_filename_entry['state'] = 'normal'
        sig_filename_entry['state'] = 'disabled'
        
#操作判断，操作选择框事件绑定   
def judgOperation(event):
    if mode.get() == '数字签名':
        des_key_entry.delete(0,END)
        des_IV_entry.delete(0,END)
        des_key_entry['state'] = 'disabled'
        des_IV_entry['state'] = 'disabled'
        if operation.get() == '签名':
            sig_filename_entry.delete(0,END)
            key_filename_entry['state'] = 'normal'
            sig_filename_entry['state'] = 'disabled'
        elif operation.get() == '验证':
            key_filename_entry['state'] = 'normal'
            sig_filename_entry['state'] = 'normal'    
        
        
#模式选择
mode_label = Label(init_frame,text='模式选择:')
mode_label.grid(row=0,column=0,padx=5,pady=5)
mode = StringVar()
mode_choice = ttk.Combobox(init_frame,textvariable=mode,values=['DES','RSA','混合模式','数字签名'],width=18,state='readonly')
mode_choice.grid(row=0,column=1,padx=0,pady=5)
mode_choice.bind('<FocusOut>',judgMode)

#操作选择
oper_label = Label(init_frame,text='操作选择:')
oper_label.grid(row=0,column=2,padx=10,pady=5)
operation = StringVar()
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

#密钥生成方法，密钥生成按钮调用
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

#-------------------------密钥输入区域-------------------------#
#密钥输入
key_frame = Frame(root)
key_frame.pack()

#验证DES密钥合法性，DES密钥输入框验证方法
#使用messagebox弹出密钥无效的提示
def valiDeskey():
    if len(des_key.get()) == 8:
        return True
    else:
        des_key_entry.delete(0,END)
        messagebox.showerror('输入错误','请输入8字节DES密钥',default='ok',icon='warning')
        return False

#DES密钥
des_key_label = Label(key_frame,text='DES密钥:')
des_key_label.grid(row=0,column=0,padx=5,pady=5)
des_key = StringVar()
des_key_entry = Entry(key_frame,state='disabled',textvariable=des_key,validate='focusout',validatecommand=valiDeskey,width=10,show='*')
des_key_entry.grid(row=0,column=1)

#验证DES初始值合法性，DES初始值输入框验证方法
def valiDesIV():
    if len(des_IV.get()) == 8:
        return True
    else:
        des_IV_entry.delete(0,END)
        messagebox.showerror('输入错误','请输入8字节DES初始值',default='ok',icon='warning')
        return False
        
#DES初始值
des_IV_label = Label(key_frame,text='DES初始值:')
des_IV_label.grid(row=1,column=0,padx=5,pady=15)
des_IV = StringVar()
des_IV_entry = Entry(key_frame,textvariable=des_IV,state='disabled',validate='focusout',validatecommand=valiDesIV,width=10,show='*')
des_IV_entry.grid(row=1,column=1)

#RSA密钥读取
key_file_label = Label(key_frame,text='密钥文件:')  #标签，这里只显示字符
key_file_label.grid(row=0,column=2,padx=20,pady=5)  #给标签定位

#输入密钥文件路径
key_filename = StringVar()      #实例化一个字符串变量
key_filename_entry = Entry(key_frame,textvariable=key_filename,state='disabled',width=20)
key_filename_entry.grid(row=0,column=3)

#选择密钥文件，密钥文件后的浏览文件按钮调用
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
sig_filename_entry = Entry(key_frame,textvariable=sig_filename,state='disabled',width=20)
sig_filename_entry.grid(row=1,column=3)

#选择签名文件，签名文件后的浏览文件按钮调用
def openSigFile():
    global sig_filename_entry
    fileName = filedialog.askopenfilename()
    sig_filename_entry.delete(0,END)
    sig_filename_entry.insert(0,fileName)
Button(key_frame,text="浏览文件",command=openSigFile).grid(row=1,column=4)

#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

#-------------------------执行区域-------------------------#

#执行操作框架
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

#执行按钮调用方法
def cryption():
    #点击按钮后，焦点移到源文件处，如果用户刚选择过模式，就会强制执行模式判断
    rawfilename_entry.focus_set()
    mode = mode_choice.get()
    operation = operation_choice.get()
    des_key = des_key_entry.get()
    des_IV = des_IV_entry.get()
    key_filename = key_filename_entry.get()
    sig_filename = sig_filename_entry.get()
    rawfilename = rawfilename_entry.get()
    try:
        textVar = crypto.doCrypto(mode,operation,des_key,des_IV,key_filename,sig_filename,rawfilename)
    except:
        textVar = '请正确输入各项参数'
    text['state'] = 'normal'
    text.insert(END,textVar)
    text.insert(END,'\n')
    text['state'] = 'disabled'
    #清空输入框
    if textVar == '操作完成':
        mode_choice.set('')
        operation_choice.set('')
        des_key_entry.delete(0,END)  #Entry组件没有set方法
        des_key_entry['state'] = 'disabled'
        des_IV_entry.delete(0,END)
        des_IV_entry['state'] = 'disabled'
        key_filename_entry.delete(0,END)
        key_filename_entry['state'] = 'disabled'
        sig_filename_entry.delete(0,END)
        sig_filename_entry['state'] = 'disabled'
        rawfilename_entry.delete(0,END)
do_button = Button(final_frame,text='执行操作',command=cryption,width=20)
do_button.grid(row=0,column=3,padx=5,pady=5)

#退出按钮
exit_button = Button(final_frame,text='退出',command=root.quit,width=5)
exit_button.grid(row=0,column=4,padx=5,pady=5)

#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

#-------------------------对话框区域-------------------------#
#对话框框架,此框架作用是方便排版
text_frame = Frame(root)
text_frame.pack()

#滚动条和对话框
textbar = Scrollbar(text_frame,takefocus=False)
textbar.pack(side=RIGHT,fill=Y)
text = Text(text_frame,height=10,width=60,bd=3,yscrollcommand=textbar.set,relief=SUNKEN,wrap=WORD,state='disabled')
#高度、宽度、边框宽度和样式、按单词换行
text.pack(side=RIGHT,fill=BOTH)
textbar['command'] = text.yview  #yview是Text组件自带方法

#清空对话框
def empty_text():
    text['state'] = 'normal'
    text.delete(1.0,END)
    text['state'] = 'disabled'
empty_button = Button(text='清空对话框',command=empty_text)
empty_button.pack(padx=15,pady=5,side=RIGHT)


mainloop()
