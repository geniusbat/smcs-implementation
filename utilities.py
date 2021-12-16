import string
import hmac

def orEncrypt(p:int,k:int):
    return p ^ k

def orDecrypt(c:int,k:int):
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
        return -4

def sumer(p:int,k:int):
    pb = bitArray(p)
    pk = bitArray(k)
    if len(pb) == len(pk):
        retb = []
        for i in range(len(pb)):
            retb.append(pb[i]+pk[i])
    elif len(pb) < len(pk):
        retb = []
        for i in range(len(pk)):
            if i < len(pb):
                retb.append(pb[i]+pk[i])
            else:
                retb.append(pk[i])
    elif len(pb) > len(pk):
        retb = []
        for i in range(len(pb)):
            if i < len(pk):
                retb.append(pk[i]+pb[i])
            else:
                retb.append(pb[i])
    ret = 0
    for i in retb:
        ret = (ret << 1) | i
    return ret

def HMAC(message,key):
    return hmac.new(key,msg=bytes(message)).digest()
    

def adderDecrypt(c:int,k:int):
    if c >= k:
        return c - k
    else:
        kC = 0
        aux = [1 if i == 0 else 0 for i in bitArray(k)]
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
    c = ""
    for i in sl:
        c += chr(sumer((i^a),b) % 256)
    return c

def invEn2(a:int,b:int,cstr:string):
    cl = [ord(i) for i in list(cstr)]
    s = ""
    for i in cl:
        s += chr(adderDecrypt(i,b)^a % 256)
    return s

def hmac(message):
    return hash(message)

def bitArray(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]

#TODO: Check en2

print(HMAC(1,3))