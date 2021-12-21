from datetime import datetime
from typing import Dict
from merchant import Merchant
from acquiringBank import AcquiringBank

class IssuingBank():
    status : int
    bAk : int
    #Participants
    consumer : object
    acquiringBank : AcquiringBank
    def __init__(self):
        pass
    def init(self,con,acq):
        self.consumer=con
        self.acquiringBank=acq
    def getTimeData():
        dt = datetime.utcnow()
        return [dt.date(),dt.time()]
    def send(self,message:Dict):
        pass