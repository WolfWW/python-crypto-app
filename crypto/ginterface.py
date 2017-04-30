#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import string,random
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
import base,myrsa,mydes,mymix,mysign,myaes

root = Tk()
root.title('Python Crypto')
root.resizable(False,False)  #禁止用户改变窗口大小

############################################################
#------------------------初始化区域------------------------#
############################################################
#初始化选择
init_frame = Frame(root)
init_frame.pack()

#Text组件输出方法
def textPrint(textVar):
    text['state'] = 'normal'
    text.insert(END,textVar + '\n')
    text.yview(MOVETO,1.0)
    text['state'] = 'disabled'

#所有输入框存放在一个列表中，用于清空和禁用
def entryList():
    entry_list = [des_key_entry,des_IV_entry,key_filename_entry,sig_filename_entry,aes_keys_entry]
    return entry_list
    
#下拉框放在一个列表
def choiceList():
    choice_list = [operation,rsa_keys,hash_method,aes_bits]
    return choice_list

#除模式选择框，所有输入框全部清空，用于模式判断
def clearAll():
    entry_list = entryList()
    for entry in entry_list:
        entry.delete(0,END)
    choice_list = choiceList()
    for choice in choice_list:
        choice.set('')

#除模式选择框、操作选择框、RSA选择，所有输入框都恢复禁用状态，用于模式判断    
def disabledAll():
    entry_list = entryList()
    for entry in entry_list:
        entry['state'] = 'disabled'
    aes_choice['state'] = 'disabled'
    hash_choice['state'] = 'disabled'

#根据模式显示可选操作，在judgMode中调用
def displayOperation():
    mode_list = ['DES','AES','RSA','混合模式']
    if mode.get() in mode_list:
        operation_choice['values'] = ['加密','解密']
    elif mode.get() == '数字签名':
        operation_choice['values'] = ['签名','验证']
        
#模式判断，模式选择框事件绑定
def judgMode(event):
    clearAll()
    disabledAll()
    displayOperation()
    if mode.get() == 'DES':
        des_key_entry['state'] = 'normal'
        des_IV_entry['state'] = 'normal'
    elif mode.get() == 'AES':
        aes_keys_entry['state'] = 'normal'    
    elif mode.get() in ['RSA','混合模式']:
        key_filename_entry['state'] = 'normal'
    elif mode.get() == '数字签名':
        key_filename_entry['state'] = 'normal'
            
#操作判断，操作选择框事件绑定   
def judgOperation(event):
    if mode.get() == 'AES':
        if operation.get() == '加密':
            aes_choice['state'] = 'readonly'
        elif operation.get() == '解密':
            aes_bits.set('')
            aes_choice['state'] = 'disabled'
    elif mode.get() == '数字签名':
        if operation.get() == '签名':
            hash_choice['state'] = 'readonly'
            sig_filename_entry.delete(0,END)
            sig_filename_entry['state'] = 'disabled'
        elif operation.get() == '验证':
            sig_filename_entry['state'] = 'normal'
            hash_method.set('')
            hash_choice['state'] = 'disabled'
        
        
#模式选择
mode_label = Label(init_frame,text='模式选择:')
mode_label.grid(row=0,column=0,padx=5,pady=5)
mode = StringVar()
mode_choice = ttk.Combobox(init_frame,textvariable=mode,values=['DES','AES','RSA','混合模式','数字签名'],width=18,state='readonly')
mode_choice.grid(row=0,column=1,padx=0,pady=5)
mode_choice.bind('<FocusIn>',judgMode)
#这里选择FocusIn绑定事件，是因为点击Combobox框时焦点其实是在下拉列表里
#选定一个选项后，焦点才会回到选择框内，此时是判断的完美时机

#操作选择
oper_label = Label(init_frame,text='    操作选择:')
oper_label.grid(row=0,column=2,padx=5,pady=5)
operation = StringVar()
operation_choice = ttk.Combobox(init_frame,textvariable=operation,values=[],width=18,state='readonly')
operation_choice.grid(row=0,column=3,padx=0,pady=5)
operation_choice.bind('<FocusIn>',judgOperation)

############################################################
#---------------------RSA和HASH选择区域--------------------#
############################################################

choice_frame = Frame(root)
choice_frame.pack()

#RSA密钥生成
rsa_bits_label = Label(choice_frame,text='RSA选择:')
rsa_bits_label.grid(row=0,column=0,padx=5,pady=15)
rsa_keys = StringVar()
rsa_keys.set('')  #设置默认值
rsa_keys_choice = ttk.Combobox(choice_frame,textvariable=rsa_keys,values=['1024','2048','3072','4096'],width=6,state='readonly')
rsa_keys_choice.grid(row=0,column=1,padx=0,pady=5)

#密钥生成方法，密钥生成按钮调用
def rsakey():
    try:
        textVar = base.geneKeys(int(rsa_keys_choice.get()))
    except:
        textVar = '请选择RSA位数'
    textPrint(textVar)

#密钥生成按钮
gene_key_button = Button(choice_frame,text='生成RSA密钥文件',command=rsakey,width=15)
gene_key_button.grid(row=0,column=2,padx=6,pady=15)

#Hash方法选择，提供MD5和SHA-1，只用于数字签名
hash_label = Label(choice_frame,text='HASH方法选择:',width=15,anchor=E)
hash_label.grid(row=0,column=3,padx=5,pady=15)
hash_method = StringVar()
hash_method.set('')  #设置默认值
hash_choice = ttk.Combobox(choice_frame,textvariable=hash_method,values=['MD5','SHA-1'],width=6,state='disabled')
hash_choice.grid(row=0,column=5,padx=0,pady=5)

#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

############################################################
#-----------------------密钥输入区域-----------------------#
############################################################

#密钥输入
key_frame = Frame(root)
key_frame.pack()

#验证DES密钥合法性，DES密钥输入框验证方法
#使用messagebox弹出密钥无效的提示
def valiDeskey():
    if len(des_key.get()) == 8 or not des_key.get():
        return True
    else:
        messagebox.showerror('提示','请输入8个字符DES密钥',default='ok',icon='warning')
        return False

#DES密钥
des_key_label = Label(key_frame,text='DES密钥:',anchor=E)
des_key_label.grid(row=0,column=0,padx=5,pady=5)
des_key = StringVar()
des_key_entry = Entry(key_frame,state='disabled',textvariable=des_key,validate='focusout',validatecommand=valiDeskey,width=10,show='*')
des_key_entry.grid(row=0,column=1)

#验证DES初始值合法性，DES初始值输入框验证方法
def valiDesIV():
    if len(des_IV.get()) == 8 or not des_IV.get():
        return True
    else:
        messagebox.showerror('提示','请输入8个字符DES初始值',default='ok',icon='warning')
        return False
        
#DES初始值
des_IV_label = Label(key_frame,text='DES初始值:',anchor=E)
des_IV_label.grid(row=1,column=0,padx=5,pady=5)
des_IV = StringVar()
des_IV_entry = Entry(key_frame,textvariable=des_IV,state='disabled',validate='focusout',validatecommand=valiDesIV,width=10,show='*')
des_IV_entry.grid(row=1,column=1)

#RSA密钥读取
key_file_label = Label(key_frame,text='密钥文件:',anchor=E)  #标签，这里只显示字符
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
sig_file_label = Label(key_frame,text='签名文件:',anchor=E)
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

#AES密钥位数选择
aes_bits_label = Label(key_frame,text='AES位数:',anchor=E)
aes_bits_label.grid(row=2,column=0,padx=5,pady=5)
aes_bits = StringVar()
aes_bits.set('')  #设置默认值
aes_choice = ttk.Combobox(key_frame,textvariable=aes_bits,values=['128','192','256'],width=8,state='disabled')
aes_choice.grid(row=2,column=1)

#AES密钥
aes_keys_label = Label(key_frame,text='AES密钥:',anchor=E)
aes_keys_label.grid(row=2,column=2,padx=20,pady=15)

#打印AES位数提醒
def aesTips(event):
    try:
        aes_keys_length = int(aes_choice.get())//8
        textVar = '您选择了%d位AES，将使用%d个字符的密码' % (int(aes_choice.get()),aes_keys_length)
        textPrint(textVar)
    except:
        pass

#AES密钥输入框
aes_keys = StringVar()
aes_keys_entry = Entry(key_frame,textvariable=aes_keys,state='disabled',width=20,show='*')
aes_keys_entry.grid(row=2,column=3)
aes_keys_entry.bind('<FocusIn>',aesTips)
        
#生成AES密钥
def aeskey():
    aes_keys_entry.focus_set()
    try:
        new_aes_key = ''.join(random.sample(string.ascii_letters+string.digits,int(aes_choice.get())//8))
        aes_keys_entry.delete(0,END)
        aes_keys_entry.insert(0,new_aes_key)
        textVar = '请牢记AES密钥：%s' % new_aes_key
    except:
        textVar = '请选择AES位数后再生成密钥'    
    textPrint(textVar)
Button(key_frame,text="生成密钥",command=aeskey).grid(row=2,column=4)

#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

############################################################
#-------------------------执行区域-------------------------#
############################################################

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

#获取所有参数
def doCrypto(mode,operation):
    #获取所有参数
    des_key = des_key_entry.get()
    des_IV = des_IV_entry.get()
    key_filename = key_filename_entry.get()
    sig_filename = sig_filename_entry.get()
    rawfilename = rawfilename_entry.get()
    hash_method = hash_choice.get()
    aes_bits = aes_choice.get()
    aes_keys = aes_keys_entry.get()
    #初始化一个返回信息
    textVar = '%s%s操作完成' % (mode,operation)
    #条件判断，执行操作
    #DES
    if mode == 'DES':
        if operation == '加密':
            mydes.desMode(rawfilename,mode,operation,des_key,des_IV)
        elif operation == '解密':
            mydes.desMode(rawfilename,mode,operation,des_key,des_IV)
        else:
            textVar = '请选择%s正确的操作' % mode
    #AES
    elif mode == 'AES':
        if operation == '加密':
            myaes.aesMode(rawfilename,mode,operation,aes_bits,aes_keys)
        elif operation == '解密':
            aes_bits = len(aes_keys)*8
            myaes.aesMode(rawfilename,mode,operation,aes_bits,aes_keys)
        else:
            textVar = '请选择%s正确的操作' % mode          
    #RSA
    elif mode == 'RSA':
        if operation == '加密':
            myrsa.encFile(rawfilename,key_filename,mode,operation)
        elif operation == '解密':
            myrsa.decFile(rawfilename,key_filename,mode,operation)
        else:
            textVar = '请选择%s正确的操作' % mode
    #混合
    elif mode == '混合模式':
        if operation == '加密':
            mymix.encMix(rawfilename,key_filename,mode,operation)
        elif operation == '解密':
            mymix.decMix(rawfilename,key_filename,mode,operation)
        else:
            textVar = '请选择%s正确的操作' % mode
    #签名
    elif mode == '数字签名':
        if operation == '签名':
            mysign.sigFile(rawfilename,key_filename,hash_method,mode,operation)
        elif operation == '验证':
            textVar = textVar + '\n' + mysign.veriFile(rawfilename,key_filename,sig_filename,mode,operation)
        else:
            textVar = '请选择%s正确的操作' % mode            
    else:
        textVar = '请选择模式'    
    return textVar
    
#执行按钮调用方法
def cryption():
    #点击按钮后，焦点移到源文件处，避免可能造成的DES密钥区错误
    rawfilename_entry.focus_set()
    #获取模式和操作，用于判断
    mode = mode_choice.get()
    operation = operation_choice.get()
    #执行操作
    #try:
    textVar = doCrypto(mode,operation)
    #except:
    #    textVar = '请正确输入各项参数'
    textPrint(textVar)
    #清空输入框
    if '操作完成' in textVar:
        mode_choice.set('')
        clearAll()
        disabledAll()
        rawfilename_entry.delete(0,END)

do_button = Button(final_frame,text='执行操作',command=cryption,width=20)
do_button.grid(row=0,column=3,padx=5,pady=5)

#退出按钮
exit_button = Button(final_frame,text='退出',command=root.quit,width=5)
exit_button.grid(row=0,column=4,padx=5,pady=5)

#分界线
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

############################################################
#-------------------------对话框区域-----------------------#
############################################################
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
