# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 03:55:03 2022

@author: X4btc
"""
import secrets
from eth_keys import keys
import time

file1=open("ethereum_addresses.txt","r")
fl=file1.read()

start=time.time()

a=1
while a<=100000:
    tm=time.time()-start
    private_key="{:064x}".format(secrets.randbits(256))
    private_key_bytes=bytes.fromhex(private_key)
    public_key_hex=keys.PrivateKey(private_key_bytes).public_key
    public_key_bytes=bytes.fromhex(str(public_key_hex)[2:])
    public_address=keys.PublicKey(public_key_bytes).to_address()
    
    found=fl.find(public_address)
    if found !=-1:
        print("private key is founded")
        file2=open("founded.txt","a")
        file2.write(public_address+" "+private_key+"\n")
        file2.close()
        print("private key ="+private_key)
        print("address   ="+public_address)
    else:
        print(str(a)+" private key = " +"Ethereum Address = "+public_address)
    a=a+1
    
    
file1.close()
print("Total Time = %s"%tm)
        
