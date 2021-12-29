import random
import string
import hmac
from typing import List

def xorEncrypt(p:int,k:int):
    return p ^ k

def xorDecrypt(c:int,k:int):
    return c ^ k

def adderEncrypt(p:int,k:int):
    return p+k

def adderDecrypt(c:int,k:int):
    return c-k

def rsaEncrypt(x:int,e:int,N:int):
    return x**e % N

def rsaDecrypt(y:int,d:int,N:int):
    return y**d % N

def aesEncrypt():
    pass

def aesDecrypt():
    pass

def en1(a:int,b:int,x:int):
    return x+a

def invEn1(a:int,b:int,y:int):
    return y-a

def en2(a:int,b:int,str:string):
    sl = [ord(i) for i in list(str)]
    for i in range(len(sl)):
        sl[i] = sl[i]+1 % 256
    s=""
    for i in sl:
        s += chr(i)
    return s

def invEn2(a:int,b:int,cstr:string):
    cl = [ord(i) for i in list(cstr)]
    for i in range(len(cl)):
        cl[i] = cl[i]-1 % 256
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