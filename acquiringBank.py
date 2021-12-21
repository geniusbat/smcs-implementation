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
        pass