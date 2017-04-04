#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import rsa
import base

#签名
def sigFile(rawfilename,key_filename,hash_method,mode,operation):
    message = open(rawfilename,'rb').read()
    priv_key = base.getPrivKey(key_filename)
    signature = rsa.sign(message,priv_key,hash_method)
    with open('signature.SIG','wb') as f:
        f.write(signature)
        f.close()
        print('签名文件已生成')
    
#验证
def veriFile(rawfilename,key_filename,sig_filename,mode,operation):
    message = open(rawfilename,'rb').read()
    pub_key = base.getPubKey(key_filename)
    signature = open(sig_filename,'rb').read()
    try:
        print(rsa.verify(message,signature,pub_key),'检测完毕！文件未被篡改') 
    except:
        print('危险！文件被篡改') 