from datetime import datetime
from typing import Dict
import random
import newUtilities as utilities

class Merchant():
    status : int

    mAk : int #Merchant auth key
    pXb : int #Unused
    xB1 : int 
    #Diffie
    xB : int
    g : int
    p : int
    csk : int
    #Participants
    consumer : object
    acquiringBank : object
    def __init__(self):
        self.status = 1
        self.pXb = random.getrandbits(5)
        self.xB = 4
        self.xB1 = 12
        self.mAk = random.getrandbits(5)
    def init(self,con,acq):
        self.consumer=con
        self.acquiringBank=acq
    def dynamicAuthCode(self):
        pass
    def getTimeData(self):
        dt = datetime.utcnow()
        return [dt.date(),dt.time()]
    def send(self,message:Dict):
        if message["op-code"]==self.status:
            #step 1.2
            if message["op-code"] == 1:
                self.csk = message["A"] ** self.xB % message["p"]
                self.status = 3
                message2 = dict()
                message2["op-code"]=2
                message2["B"]= message["g"] ** self.xB % message["p"]
                message2["2"]= utilities.xorEncrypt(self.xB1, self.csk)
                mDate , mtime = self.getTimeData()
                shoppingMessage = ""; shoppingMessage += str(random.randint(0,10))+" "+message["shoppingList"]+" "+str(mDate)+" "+str(mtime)
                message2["3"]=utilities.en2(self.csk,self.xB1,shoppingMessage)
                message2["4"]=utilities.hmac(utilities.adderEncrypt(self.csk,self.xB1))
                self.consumer.send(message2)
            #1.4
            elif message["op-code"] == 3:
                xA1 = utilities.invEn1(self.csk, self.xB1, message["3"])
                if message["5"] == utilities.hmac(utilities.adderEncrypt(xA1,self.csk)):
                    consumerInfo = utilities.invEn2(self.csk, xA1, message["4"])
                    print("Consumer info: ", consumerInfo)
                    self.status=7 
                    message4 = dict()
                    message4["op-code"]=4
                    shoppingAssociationMessage = consumerInfo + " , businessCert 40$ bankCode-10222, AvdManuelAltolaguirre, " + str(utilities.aesEncrypt(utilities.xorEncrypt(xA1,self.mAk),self.csk))
                    message4["1"]=utilities.en2(xA1,self.xB1,shoppingAssociationMessage)
                    message4["2"]=utilities.hmac(utilities.adderEncrypt(utilities.xorEncrypt(self.csk,self.xB1), xA1))
                    self.consumer.send(message4)
            #4
            elif message["op-code"] == 7:
                self.status = 9
                message9 = dict()
                message9["op-code"] = 8
                invoice = "This is the invoice"
                message9["1"] = invoice
                message9["2"] = utilities.hmac(utilities.adderEncrypt(self.csk, utilities.xorEncrypt(self.consumer.xA1,self.xB1)))
                self.consumer.send(message9)
        else:
            print("Merchant's status not equal to op-code, status: ", self.status, " op-code: ",message["op-code"])