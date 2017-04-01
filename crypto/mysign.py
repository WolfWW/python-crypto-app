#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import rsa
import base

#签名
def sigFile(keyfile,rawfile,hash_method):
    message = open(rawfile,'rb').read()
    priv_key = base.getPrivKey(keyfile)
    signature = rsa.sign(message,priv_key,hash_method)
    with open('signature.SIG','wb') as f:
        f.write(signature)
        f.close()
        print('签名文件已生成')
    
#验证
def veriFile(keyfile,rawfile,sigfile):
    message = open(rawfile,'rb').read()
    pub_key = base.getPubKey(keyfile)
    signature = open(sigfile,'rb').read()
    try:
        print(rsa.verify(message,signature,pub_key),'检测完毕！文件未被篡改') 
    except:
        print('危险！文件被篡改') 
