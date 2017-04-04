#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import pyDes
import base

'''
纯DES中还是需要用户输入一个初始值，一定程度上增强一些安全性

'''

def desMode(rawfilename,mode,operation,des_key,des_IV):
    print(rawfilename,operation,des_key,des_IV)
    #以下数据初始化
    #key = input('请输入8字节密钥：')
    #IV = input('请输入8字节初始值：')
    des = pyDes.des(des_key,pyDes.CBC,des_IV,pad=None,padmode=pyDes.PAD_PKCS5)
    newname = base.newFileName(rawfilename,mode,operation)
    #以下根据用户选择进行加密或解密
    with open(rawfilename,'rb') as f1:  #以二进制只读模式打开源文件
        data = f1.read()  #读取文件数据
        #加密数据
        if operation == '加密':
            print('加密中，请稍候...')
            information = des.encrypt(data)
        #解密数据
        else:  #operation不是0，就只可能是1
            print('解密中，请稍候...')
            information = des.decrypt(data)
        with open(newname,'wb') as f2:
            f2.write(information)
            f2.close()  #操作完成后，打开的文件要关闭
        print('新文件是：%r' % newname)  #十分人性化告诉用户新文件是哪个 
        f1.close()
    return '操作完成'