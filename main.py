from merchant import Merchant
from issuingBank import IssuingBank
from acquiringBank import AcquiringBank
from consumer import Consumer
import utilities

#Make csk and all xs same bit size.

if __name__ == '__main__':
    merchant = Merchant()
    acquiringBank = AcquiringBank()
    consumer = Consumer()
    issuingBank = IssuingBank()
    merchant.init(consumer,acquiringBank)
    acquiringBank.init(issuingBank,merchant)
    issuingBank.init(consumer,acquiringBank)
    consumer.init(merchant,issuingBank)