from datetime import datetime

class Merchant():
    mAk : int
    xB : int
    xB1 : int

    def dynamicAuthCode():
        pass
    def getTimeData():
        dt = datetime.utcnow()
        return [dt.date(),dt.time()]


print(Merchant.getTimeData())