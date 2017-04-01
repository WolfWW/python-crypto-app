#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import rsa

# 给新文件命名,不论加密还是解密
# 参数有源文件、选择模式、选择操作
def newFileName(rawfile,mode,operation):
    pathname = rawfile.split('.')[0] #获得源文件名
    lastname = rawfile.split('.')[1] #获得源文件后缀，选取第一个后缀
    rawpathname = pathname.split('-')[0] #去掉可能存在的上一次加解密操作的命名
    count = 0  #自增变量，文件名查重后生成新文件名
    #新文件名=源文件名+加解密模式+count+后缀
    newname = rawpathname +  '-mode-%s-operation-%d'%(mode,operation) + '.' + lastname
    #查重后生成新文件名
    while os.path.isfile(newname):
        count += 1
        newname = rawpathname + '-mode-%s-operation-%d-(%d)'%(mode,operation,count) + '.' + lastname
    return newname

#生成密钥对，并记录在文件中
def geneKeys(bits_num):
    '''
    生成相应的文件分别存放公钥和私钥，在对应场景时直接读取文件内
    引用的库定义了PublicKey数据类型，只能使用save_pkcs1()转换密钥后二进制写入文件
    '''
    (pub_key,priv_key) = rsa.newkeys(bits_num)
    # 密钥文件默认保存在当前目录
    with open('pub_key.pem','wb') as f1,open('priv_key.pem','wb') as f2:
        f1.write(rsa.PublicKey.save_pkcs1(pub_key))
        f1.close()
        f2.write(rsa.PrivateKey.save_pkcs1(priv_key))
        f2.close()
    print('Done!密钥文件已生成')

#读取密钥文件中的公钥
def getPubKey(keyfile):
    '''
    使用库作者提供的load_pkcs1()方法转换密钥
    二进制读出
    '''
    keydata = open(keyfile,'rb').read()
    pub_key = rsa.PublicKey.load_pkcs1(keydata)
    print('公钥已读取')
    return pub_key

#读取密钥文件中的私钥
def getPrivKey(keyfile):
    keydata = open(keyfile,'rb').read()
    priv_key = rsa.PrivateKey.load_pkcs1(keydata)
    print('私钥已读取')
    return priv_key