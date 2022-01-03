from datetime import datetime
import time
from typing import Dict
import newUtilities as utilities
from Cryptodome import Util
from merchant import Merchant
from acquiringBank import AcquiringBank

class IssuingBank():
    status : int
    bAk : int
    #Participants
    consumer : object
    acquiringBank : AcquiringBank
    merchant : object
    def __init__(self):
        pass
    def init(self,con,acq,mer):
        self.consumer=con
        self.acquiringBank=acq
        self.merchant = mer
    def send(self,message:Dict):
        #Step 2.2
        if message["op-code"] == 5:
            print("Step 2.2:")
            print("Card issuing bank checks if request is done before now")
            if time.time() - message["tnonce"] < 1000:
                xA2 = utilities.rsaDecrypt(message["3"],self.consumer.d, self.consumer.N)
                xA3 = utilities.invEn1(xA2, utilities.xorEncrypt(xA2, self.consumer.kPW), message["4"])
                paymentRequestMessage = utilities.invEn2(xA2, utilities.xorEncrypt(xA3, int(message["tnonce"])), message["5"])
                print("Payment Request Message: ", paymentRequestMessage)
                if utilities.hmac(utilities.adderEncrypt(utilities.xorEncrypt(self.consumer.csk, xA2), xA3)) == message["7"]:
                    aes = paymentRequestMessage.split(", ")[6]
                    if aes == str(utilities.aesEncrypt(utilities.xorEncrypt(self.consumer.xA1,self.merchant.mAk),self.consumer.csk)):
                        cardAuthCode = utilities.xorDecrypt(self.consumer.xA1, message["6"])
                        if cardAuthCode == utilities.aesResToInt(utilities.aesEncrypt(utilities.xorEncrypt(xA3, self.consumer.cAk),xA2)):
                            print("Checking if consumer can be allowed the payment")
                            print("Payment request accepted, doing payment")
                            message6 = dict()
                            message6["op-code"] = 6
                            confirmationMessage = "This is the confirmation message"
                            tradingResult = "accepted"
                            message6["1"] = utilities.en2(self.consumer.csk, self.consumer.xA1, confirmationMessage+", "+tradingResult)
                            message6["2"] = utilities.hmac(utilities.xorEncrypt(xA2,xA3))
                            self.consumer.send(message6)
                            message7 = dict()
                            message7["op-code"] = 7
                            message7["1"] = confirmationMessage
                            message7["2"] = tradingResult
                            message7["3"] = paymentRequestMessage
                            self.acquiringBank.send(message7)
