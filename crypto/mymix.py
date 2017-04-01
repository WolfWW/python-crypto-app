#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import string,random
import rsa,pyDes
import base

#加密
def encMix(keyfile,rawfile):
    #rsa加密DES密钥
    pub_key = base.getPubKey(keyfile) 
    des_key = input('输入8字节DES密钥:')
    # 随机生成8字节IV，加解密时均自动使用
    des_IV = ''.join(random.sample(string.ascii_letters+string.digits,8))
    des_data = des_key + des_IV
    enc_des = rsa.encrypt(des_data.encode('utf-8'),pub_key)
    des = pyDes.des(des_key,pyDes.CBC,des_IV,pad=None,padmode=pyDes.PAD_PKCS5)

    #DES加密文件
    with open(rawfile,'rb') as f:
        data = f.read()
        enc_data = des.encrypt(data)
        f.close()

    #密文文件命名
    newfile = base.newFileName(rawfile,mode='m',operation=0)    
     
    #密文写入
    with open(newname,'wb') as f:
        [f.write(x) for x in (enc_des,enc_data)]
        f.close()
        
    print('Done!密文文件是: %s' % newfile)

#计算DES密钥密文长度
def size_in_bytes(priv_key):
    #计算n模8的余数
    remainder = (int(len(bin(priv_key.n))) - 2) % 8
    bytes = (int(len(bin(priv_key.n))) - 2) / 8
    #模不为0则要在地板除的基础上加1
    if remainder:
        bytes = (int(len(bin(priv_key.n))) - 2) // 8 + 1
    return bytes
    
#解密
def decMix(keyfile,rawfile):
    #读取私钥
    priv_key = base.getPrivKey(keyfile)

    #计算DES密钥密文的长度
    len_of_enc_des = size_in_bytes(priv_key)

    #分别读取DES密钥密文和明文密文
    with open(rawfile,'rb') as f:
        wait_dec_des,wait_dec_data = [f.read(x) for x in (len_of_enc_des,-1)]
        #读取密钥密文，剩下的是明文密文
        f.close()
     
    #解密DES密钥和初始值
    dec_des = rsa.decrypt(wait_dec_des,priv_key).decode('utf-8')
    dec_des_key,dec_des_IV = dec_des[:8],dec_des[8:]
    des = pyDes.des(dec_des_key,pyDes.CBC,dec_des_IV,pad=None,padmode=pyDes.PAD_PKCS5)

    #明文文件命名
    newfile = base.newFileName(rawfile,mode='m',operation=1)
    
    #解密文件
    with open(newname,'wb') as f:
        dec_data = des.decrypt(wait_dec_data)
        f.write(dec_data)
        f.close()

    print('Done!明文文件是: %s' % newfile)