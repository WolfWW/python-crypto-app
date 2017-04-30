#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import pyaes
import base

############################################################
#-----------------------AES采用CTR模式---------------------#
############################################################

        
def aesMode(rawfilename,mode,operation,aes_bits,aes_keys):
    aes_mode = mode + '%s位' % aes_bits
    newfile = base.newFileName(rawfilename,aes_mode,operation)
    key = aes_keys.encode("utf-8")
    AES = pyaes.AESModeOfOperationCTR(key)
    file_in = open(rawfilename,'rb')
    file_out = open(newfile,'wb')
    if operation == '加密':
        pyaes.encrypt_stream(AES,file_in,file_out)
    elif operation == '解密':
        pyaes.decrypt_stream(AES,file_in,file_out)
    file_in.close()
    file_out.close()