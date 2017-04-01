#! /usr/bin/env python3
# -*- coding:utf-8 -*-

##################################
#        mode==d:des             #
#        mode==r:rsa             #
#        mode==m:mix             #
#        mode==s:sign            #
# operation==0:encrypt OR sign   #
# operation==1:decrypt OR verify #
##################################

import base,myrsa,mydes,mymix,mysign

#按钮，生成密钥文件
#实测，输入1017-1023得到的文件大小和1024一样，输入1016得到的文件小1个字节
#即RSA密钥位数不足8的倍数会补足
bits_num = int(input('RSA密钥位数（0为不需要生成，可选1024、2048、3072、4096）:'))
while bits_num:
    base.geneKeys(bits_num)
    break

#用户选择mode和operation
mode = input('d代表DES，r代表rsa，m代表混合加密，s代表签名：')
operation = int(input('0表示加密或签名，1表示解密或验证：'))

#条件判断
#DES
if mode == 'd':
    rawfile = input('输入源文件路径：')
    if operation == 0:
        mydes.desMode(rawfile,operation)
    elif operation == 1:
        mydes.desMode(rawfile,operation)
    else:
        print('请选择正确的操作')

#RSA
elif mode == 'r':
    rawfile = input('输入源文件路径：')
    keyfile = input('密钥文件：')
    if operation == 0:
        myrsa.encFile(rawfile,keyfile)
    elif operation == 1:
        myrsa.decFile(rawfile,keyfile)
    else:
        print('请选择正确的操作')

#混合
elif mode == 'm':
    rawfile = input('输入源文件路径：')
    keyfile = input('密钥文件路径：')
    if operation == 0:
        mymix.encMix(keyfile,rawfile)
    elif operation == 1:
        mymix.decMix(keyfile,rawfile)
    else:
        print('请选择正确的操作')

#签名
elif mode == 's':
    rawfile = input('输入文件路径：')
    keyfile = input('输入密钥文件路径：')
    hash_method = 'SHA-1'
    if operation == 0:
        mysign.sigFile(keyfile,rawfile,hash_method)
    elif operation == 1:
        signature = input('输入签名文件路径：')
        mysign.veriFile(keyfile,rawfile,signature)
    else:
        print('请选择正确的操作')

else:
    print('请选择正确的模式')