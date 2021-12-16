from datetime import datetime

class IssuingBank():
    bAk : int

    def getTimeData():
        dt = datetime.utcnow()
        return [dt.date(),dt.time()]