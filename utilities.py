import random
import string
import hmac
from typing import List

def xorEncrypt(p:int,k:int):
    return p ^ k

def xorDecrypt(c:int,k:int):
    return c ^ k

def adderEncrypt(p:int,k:int):
    pb = bitArray(p)
    pk = bitArray(k)
    if len(pb) == len(pk):
        retb = []
        for i in range(len(pb)):
            retb.append(pb[i]+pk[i])
        ret = 0
        for i in retb:
            ret = (ret << 1) | i
        return ret
    else:
        print("Failed, not same size")
        print(p)
        print(k)
        return -4

def sumer(p:int,k:int):
    pb = bitArray(p)
    pk = bitArray(k)
    ml = max(len(pb),len(pk))
    if len(pb) < ml:
        while(len(pb)<ml):
            pb.insert(0,0)
    if len(pk) < ml:
        while(len(pk)<ml):
            pk.insert(0,0)
    if len(pb) == len(pk):
        retb = []
        for i in range(len(pb)):
            aux = pb[i]+pk[i]
            if aux == 0:
                retb.append(0)
            elif aux == 1:
                retb.append(1)
            elif aux == 2:
                retb.append(0)
    ret = 0
    for i in retb:
        ret = (ret << 1) | i
    return ret

def rev(original:List,l):
    ret = original.copy()
    if len(ret) < l:
        while(len(ret)<l):
            ret.append(0)
    ret.reverse()
    return ret

def HMAC(message,key):
    return hmac.new(key,msg=bytes(message)).digest()
    

def adderDecrypt(c:int,k:int):
    if c >= k:
        return c - k
    else:
        return k - c
        kC = 0
        aux = [1 if i == 0 else 0 for i in bitArray(k)]
        print(aux)
        for i in aux:
            kC = (kC << 1) | i
        return c + 1 + kC

def rsaEncrypt(x:int,e:int,N:int):
    return x**e % N

def rsaDecrypt(y:int,d:int,N:int):
    return y**d % N

def aesEncrypt():
    pass

def aesDecrypt():
    pass

def en1(a:int,b:int,x:int):
    return sumer((x^a),b)

def invEn1(a:int,b:int,y:int):
    return adderDecrypt(y,b)^a

def en2(a:int,b:int,str:string):
    sl = [ord(i) for i in list(str)]
    print(sl)
    c = ""
    for i in sl:
        c += chr(sumer((i^a),b) )#% 256)
    return c

def invEn2(a:int,b:int,cstr:string):
    cl = [ord(i) for i in list(cstr)]
    print(cl)
    s = ""
    for i in cl:
        s += chr(adderDecrypt(i,b)^a % 256)
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

'''
#Binary adder is not consistent
#k = 5
#a = 6
k = 10
a = 6
c = sumer(a,k)
print(bitArray(c))
print("c: ",c)
p = adderDecrypt(c,k)
print(p)
print(a==p)
'''
'''
print(en1(10,3,112))
print(invEn1(10,3,218))
a = en2(10,3,"patatas,pepinos,huevos")
print(invEn2(10,3,a))
'''