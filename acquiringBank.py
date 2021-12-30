from random import randint
from typing import Dict
from merchant import Merchant

class AcquiringBank():
    status : int
    #Participants
    merchant : Merchant
    issuingBank : object
    def __init__(self):
        pass
    def init(self,iss,mer):
        self.issuinBank=iss
        self.merchant=mer
    def send(self,message:Dict):
        #Step 3.2
        if message["op-code"] == 7:
            message8 = dict()
            message8["op-code"] = 7
            message8["1"] = message["2"]
            message8["2"] = message["3"]
            message8["authCode"] = randint(0,1000)
            self.merchant.send(message8)