from random import randint
from typing import Dict
from merchant import Merchant
import time

class AcquiringBank():
    status : int
    #Participants
    merchant : Merchant
    issuingBank : object
    def __init__(self):
        pass
    def init(self,iss,mer):
        self.times = dict()
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
            self.times["3.2"]=time.process_time()
            self.merchant.send(message8)