import random
import string
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
from typing import List

def xorEncrypt(p:int,k:int):
    return p ^ k

def xorDecrypt(c:int,k:int):
    return c ^ k

def adderEncrypt(p:int,k:int):
    lp = bitArray(p); lp.reverse()
    lk = bitArray(k); lk.reverse()
    sum = []
    carry = 0
    pBigger = (len(lp)>=len(lk))
    if pBigger:
        for i in range(len(lp)):
            bp = lp[i]
            if i < len(lk):
                aux = bp + carry + lk[i]
                if aux == 2:
                    aux = 0
                    carry = 1
                elif aux ==3:
                    aux = 1
                    carry = 1
                else:
                    carry = 0
                sum.append(aux)
            else:
                aux = bp+carry
                carry = 0
                if aux == 2:
                    aux = 0
                    carry = 1
                sum.append(aux)
    else:
        for i in range(len(lk)):
            bk = lk[i]
            if i < len(lp):
                aux = bk + carry + lp[i]
                if aux == 2:
                    aux = 0
                    carry = 1
                elif aux ==3:
                    aux = 1
                    carry = 1
                else:
                    carry = 0
                sum.append(aux)
            else:
                aux = bk + carry
                carry = 0
                if aux == 2:
                    aux = 0
                    carry = 1
                sum.append(aux)
    #sumT = sum.copy()
    #sumT.reverse()
    ret = 0
    for i in range(len(sum)):
        bit = sum[i]
        if bit == 1:
            ret += 2**i
    return ret


def adderDecrypt(c:int,k:int):
    if c >= k:
        return c - k
    else:
        lkC = [1 if i == 0 else 0 for i in bitArray(k)]
        kC = 0
        lkC.reverse()
        for i in range(len(lkC)):
            bit = lkC[i]
            if bit == 1:
                kC += 2**i
        sum = c + kC + 1
        return sum



def rsaEncrypt(x:int,e:int,N:int):
    return x**e % N

def rsaDecrypt(y:int,d:int,N:int):
    return y**d % N

def aesEncrypt(data, key):
    key = Padding.pad(bytes(key), 16)
    if isinstance(data, str):
        paddedData = Padding.pad(bytes(data, encoding='utf8'), 16)
    else:
        newData = chr(data)
        paddedData = Padding.pad(bytes(newData, encoding='utf8'), 16)
    cipher = AES.new(key,AES.MODE_ECB)
    cText = cipher.encrypt(paddedData)
    return cText

def aesDecrypt(data, key):
    key = Padding.pad(bytes(key), 16)
    cipher = AES.new(key,AES.MODE_ECB)
    plain = cipher.decrypt(data)
    return Padding.unpad(plain,16).decode("utf-8")

def aesResToInt(res):
    return int.from_bytes(res, sys.byteorder)

def en1(a:int,b:int,x:int):
    return adderEncrypt(xorEncrypt(x,a),b)

def invEn1(a:int,b:int,y:int):
    return xorDecrypt(adderDecrypt(y,b),a)

def en2(a:int,b:int,str:string):
    sl = [ord(i) for i in list(str)]
    print(sl)
    for i in range(len(sl)):
        sl[i] = adderEncrypt(xorEncrypt(sl[i],a),b) % 256
    s=""
    for i in sl:
        s += chr(i)
    return s

def invEn2(a:int,b:int,cstr:string):
    cl = [ord(i) for i in list(cstr)]
    for i in range(len(cl)):
        cl[i] = xorDecrypt(adderDecrypt(cl[i],b),a) % 256
    s=""
    for i in cl:
        s += chr(i)
    return s

def hmac(message):
    return hash(message)

def bitArray(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]

def generateNumber(bits=10)-> int:
    num = random.getrandbits(10)
    if len(bitArray(num))==bits:
        return num
    else:
        while len(bitArray(num))!=bits:
            aux = bitArray(num)
            for i in range(bits-len(bitArray(num))):
                aux.append(1)
            num = 0
            for i in aux:
                num = (num << 1) | i
        return num