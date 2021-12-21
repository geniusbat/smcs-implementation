import string
import random
from typing import Dict, List
import utilities
from Crypto.Cipher import AES
from merchant import Merchant
from issuingBank import IssuingBank

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
    pXa : int
    #Xes are random dynamic keys
    x : int
    x1 : int
    x2 : int
    x3 : int
    #Participants
    merchant : Merchant
    issuinBank : IssuingBank
    def __init__(self):
        self.selfId = random.randint(0,10000)
        self.status = 1
        self.e = 7
        self.d = 3
        self.N = 33
        self.cardNumber = 4916632844825070 #TODO: Aleatorize
        self.cAk = random.getrandbits(10)
        self.pw = "password"
        self.kPW = hash(self.pw)
        self.pXa = random.getrandbits(10)
        self.xA = random.getrandbits(10)
        self.xA1 = random.getrandbits(10)
        self.xA2 = random.getrandbits(10)
        self.xA3 = random.getrandbits(10)
    def init(self,mer,iss):
        self.merchant=mer
        self.issuinBank=iss
        #Start
        self.status = 2
        message1 = dict()
        message1["op-code"] = 1; message1["Pxa"] = self.pXa
        shoppingList = "patatas,pepinos,huevos"
        message1["shoppingList"] = shoppingList
        print(message1)
        self.merchant.send(message1)
    def cardAuthCode(self):
        pass
    def getConsumerData(self):
        return (self.selfId,self.e,self.N,self.kPW,self.cAk)
    def send(self,message:Dict):
        print(message)