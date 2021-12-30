from datetime import time
import time
import string
import random
from typing import Dict, List
import newUtilities as utilities
from Cryptodome.Cipher import AES
from merchant import Merchant
from issuingBank import IssuingBank

class Consumer():
    selfId : int
    status : int

    #Diffie
    xA : int
    g : int
    p : int
    csk : int

    #RSA
    e : int
    d : int
    N : int

    cardNumber : int
    cAk : int #Consumer Auth number
    pw : string #Password
    kPW : int #Password hash
    pXa : int #Unused
    #Xes are random dynamic keys
    xA1 : int
    xA2 : int
    xA3 : int
    #Participants
    merchant : Merchant
    issuinBank : IssuingBank
    def __init__(self):
        self.selfId = random.randint(0,10000)
        self.status = 1
        self.csk = 0
        self.e = 7
        self.d = 3
        self.N = 33
        self.g = 6
        self.p = 13
        self.cardNumber = 4916632844825070 #TODO: Aleatorize
        self.cAk = random.getrandbits(2)
        self.pw = "password"
        self.kPW = hash(self.pw)
        self.pXa = random.getrandbits(5)
        self.xA = 5
        self.xA1 = 12
        self.xA2 = random.getrandbits(5)
        self.xA3 = random.getrandbits(5)
        self.xB1 = 0
    def init(self,mer,iss):
        self.merchant=mer
        self.issuinBank=iss
        #Start 1.1
        self.status = 2
        message1 = dict()
        message1["op-code"] = 1; message1["A"] = self.g ** self.xA % self.p
        shoppingList = "patatas,pepinos,huevos"
        message1["shoppingList"] = shoppingList
        message1["g"]=self.g
        message1["p"]=self.p
        print("Message-1:",message1)
        self.merchant.send(message1)
    def cardAuthCode(self):
        pass
    def getConsumerData(self):
        return (self.selfId,self.e,self.N,self.kPW,self.cAk)
    def send(self,message:Dict):    
        if message["op-code"]==self.status:
            if message["op-code"]==2:
                #Step 1.3
                self.csk = message["B"] ** self.xA % self.p
                self.xB1 = utilities.xorDecrypt(int(message["2"]),self.csk)
                if message["4"]==utilities.hmac(utilities.adderEncrypt(self.csk,self.xB1)):
                    shoppingMessage = utilities.invEn2(self.csk,self.xB1,message["3"])
                    print("Shopping message received: ", shoppingMessage)
                    self.status = 4
                    message3 = dict()
                    message3["op-code"]=3; message3["consumerOrder"]=shoppingMessage.split(" ")[0]
                    message3["deliveryAddress"] = "Avenida Reina Mercedes"
                    message3["3"] = utilities.en1(self.csk, self.xB1, self.xA1)
                    message3["4"] = utilities.en2(self.csk, self.xA1, "Gustavo Molina, Avenida Reina Mercedes")
                    message3["5"] = utilities.hmac(utilities.adderEncrypt(self.xA1, self.csk))
                    self.merchant.send(message3)
            elif message["op-code"]==4:
                #Step 2.1
                if utilities.hmac(utilities.adderEncrypt(utilities.xorEncrypt(self.csk, self.xB1),self.xA1)) == message["2"]:
                    shoppingAssociationMessage = utilities.invEn2(self.xA1, self.xB1, message["1"])
                    print("Shopping association message: ", shoppingAssociationMessage)
                    print("Request user's password: ")
                    print("Password inputed")
                    if hash(self.pw) == self.kPW:
                        self.status=6
                        message5 = dict()
                        message5["op-code"]=5
                        message5["tnonce"] = time.time(); message5["id"] = self.selfId
                        message5["3"] = utilities.rsaEncrypt(self.xA2, self.e, self.N)
                        message5["4"] = utilities.en1(self.xA2, utilities.xorEncrypt(self.xA2, self.kPW), self.xA3)
                        paymentRequestMessage = str(self.csk) +", "+ str(self.xA1) +", "+ shoppingAssociationMessage
                        message5["5"] = utilities.en2(self.xA2, utilities.xorEncrypt(self.xA3, int(time.time())),paymentRequestMessage)
                        message5["6"] = utilities.xorEncrypt(self.xA1, utilities.aesResToInt(utilities.aesEncrypt(utilities.xorEncrypt(self.xA3, self.cAk),self.xA2)))
                        message5["7"] = utilities.hmac(utilities.adderEncrypt(utilities.xorEncrypt(self.csk, self.xA2), self.xA3))
                        self.issuinBank.send(message5)
                    else:
                        print("Password was wrong")
            elif message["op-code"]==6:
                if utilities.hmac(utilities.xorEncrypt(self.xA2, self.xA3)) == message["2"]:
                    result = utilities.invEn2(self.csk, self.xA1, message["1"]).split(", ")[1]
                    print("The result of the request was: ", result)
                    self.status = 8
            elif message["op-code"]==8:
                if message["2"] == utilities.hmac(utilities.adderEncrypt(self.csk, utilities.xorEncrypt(self.xA1, self.xB1))):
                    self.status = 9
                    print("The invoice for payment was: ", message["1"])
        else:
            print("Consumer's status not equal to op-code, status: ", self.status, " op-code: ",message["op-code"])