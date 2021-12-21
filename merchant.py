from datetime import datetime
from typing import Dict
import random
import utilities

class Merchant():
    status : int

    mAk : int
    pXb : int
    xB : int
    xB1 : int
    csk : int
    #Participants
    consumer : object
    acquiringBank : object
    def __init__(self):
        self.status = 1
        self.pXb = random.getrandbits(10)
        self.xB = random.getrandbits(10)
        self.xB1 = random.getrandbits(10)
        self.mAk = random.getrandbits(10)
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
            if message["op-code"] == 1:
                self.csk = message["Pxa"] ** self.xB % random.getrandbits(10)
                self.status = 3
                message2 = dict()
                message2["op-code"]=2;message2["Pxb"]=self.pXb;message2["2"]=(self.csk ^ self.xB1)
                mDate , mtime = self.getTimeData()
                shoppingMessage = ""; shoppingMessage += str(random.randint(0,100))+" "+message["shoppingList"]+" "+str(mDate)+" "+str(mtime)
                message2["3"]=utilities.en2(self.csk,self.xB1,shoppingMessage)
                message2["4"]=utilities.hmac(utilities.adderEncrypt(self.csk,self.xB1))
                self.consumer.send(message2)