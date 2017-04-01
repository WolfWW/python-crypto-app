#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from rsa.bigfile import *
import base

#加密大文件
def encFile(rawfile,keyfile):
    '''
    读取公钥文件
    密文文件命名
    使用库提供的方法加密文件
    '''
    pub_key = base.getPubKey(keyfile)
    newfile = base.newFileName(rawfile,mode='r',operation=0)
    with open(rawfile,'rb') as infile, open(newfile,'wb') as outfile:        
        encrypt_bigfile(infile,outfile,pub_key)
        infile.close()
        outfile.close()
    print('加密完成！密文文件是：%s' % newfile)

#解密大文件
def decFile(rawfile,keyfile):
    '''
    读取私钥文件
    明文文件命名
    使用库提供的方法解密文件
    '''
    priv_key = base.getPrivKey(keyfile)
    newfile = base.newFileName(rawfile,mode='r',operation=1)
    with open(rawfile,'rb') as infile, open(newfile,'wb') as outfile:        
        decrypt_bigfile(infile,outfile,priv_key)
        infile.close()
        outfile.close()
    print('解密完成！明文文件是：%s' % newfile)
