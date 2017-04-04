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
'''
#不需要了，UI中搞定
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
'''

def doCrypto(mode,operation,des_key,des_IV,key_filename,sig_filename,rawfilename):
    #条件判断
    #DES
    if mode == 'DES':
        #rawfile = input('输入源文件路径：')
        if operation == '加密':
            print('DES加密中')
            mydes.desMode(rawfilename,mode,operation,des_key,des_IV)
        elif operation == '解密':
            mydes.desMode(rawfilename,mode,operation,des_key,des_IV)
        else:
            print('请选择正确的操作')

    #RSA
    elif mode == 'RSA':
        #rawfile = input('输入源文件路径：')
        #keyfile = input('密钥文件：')
        if operation == '加密':
            myrsa.encFile(rawfilename,key_filename,mode,operation)
        elif operation == '解密':
            myrsa.decFile(rawfilename,key_filename,mode,operation)
        else:
            print('请选择正确的操作')

    #混合
    elif mode == '混合模式':
        #rawfile = input('输入源文件路径：')
        #keyfile = input('密钥文件路径：')
        if operation == '加密':
            mymix.encMix(rawfilename,key_filename,mode,operation)
        elif operation == '解密':
            mymix.decMix(rawfilename,key_filename,mode,operation)
        else:
            print('请选择正确的操作')

    #签名
    elif mode == '数字签名':
        #rawfile = input('输入文件路径：')
        #keyfile = input('输入密钥文件路径：')
        hash_method = 'SHA-1'
        if operation == '签名':
            mysign.sigFile(rawfilename,key_filename,hash_method,mode,operation)
        elif operation == '验证':
            #signature = input('输入签名文件路径：')
            mysign.veriFile(rawfilename,key_filename,sig_filename,mode,operation)
        else:
            print('请选择正确的操作')

    else:
        return '请选择正确的模式'
    
    return '操作完成'