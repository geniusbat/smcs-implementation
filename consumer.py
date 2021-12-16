from _typeshed import Self
import string
import random
#from Crypto.Cipher import AES

class Consumer():
    selfId : int
    status : int
    #RSA
    e : int
    d : int
    N : int
    cardNumber : int
    cAk : int
    pw : string
    kPW : int
    #Xes are random dynamic keys
    x : int
    x1 : int
    x2 : int
    x3 : int
    def __init__(self):
        self.selfId = random.randint(0,10000)
        self.status = 0
        self.e 
        self.d 
        self.N
        self.cardNumber = 4916632844825070 #TODO: Aleatorize
        self.cAk
        self.pw = "password"
        self.kPW = hash(self.pw)
        self.x = random.randint(0,10000)
        self.x1 = random.randint(0,10000)
        self.x2 = random.randint(0,10000)
        self.x3 = random.randint(0,10000)
    def init(self):
        pass
    def cardAuthCode(self):
        pass
    def getConsumerData(self):
        return (self.selfId,self.e,self.N,self.kPW,self.cAk)