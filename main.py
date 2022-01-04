from random import randint
from merchant import Merchant
from issuingBank import IssuingBank
from acquiringBank import AcquiringBank
from consumer import Consumer
import time

if __name__ == '__main__':
    stepTimes = dict()
    stepTimes["1.1"]=0
    stepTimes["1.2"]=0
    stepTimes["1.3"]=0
    stepTimes["1.4"]=0
    stepTimes["2.1"]=0
    stepTimes["2.2"]=0
    stepTimes["3.2"]=0
    stepTimes["4"]=0
    epochs = 100000
    average = 0
    for i in range(epochs):
        start = time.process_time()
        merchant = Merchant()
        acquiringBank = AcquiringBank()
        consumer = Consumer()
        issuingBank = IssuingBank()
        merchant.init(consumer,acquiringBank)
        acquiringBank.init(issuingBank,merchant)
        issuingBank.init(consumer,acquiringBank, merchant)
        consumer.init(merchant,issuingBank)
        end = time.process_time()
        while(not consumer.done):
            pass
        average = (average+((end-start)*1000000))/2
        stepTimes["1.1"] = (stepTimes["1.1"]+(consumer.times["1.1"]-start)*1000000)/2
        stepTimes["1.2"] = (stepTimes["1.2"]+(merchant.times["1.2"]-start)*1000000)/2 
        stepTimes["1.3"] = (stepTimes["1.3"]+(consumer.times["1.3"]-start)*1000000)/2
        stepTimes["1.4"] = (stepTimes["1.4"]+(merchant.times["1.4"]-start)*1000000)/2
        stepTimes["2.1"] = (stepTimes["2.1"]+(consumer.times["2.1"]-start)*1000000)/2
        stepTimes["2.2"] = (stepTimes["2.2"]+(issuingBank.times["2.2"]-start)*1000000)/2
        stepTimes["3.2"] = (stepTimes["3.2"]+(acquiringBank.times["3.2"]-start)*1000000)/2
        stepTimes["4"] = (stepTimes["4"]+(merchant.times["4"]-start)*1000000)/2
    #print("Total duration: ", (end-start)*1000000, " microseconds")
    print("Average duration: ",average," microseconds")
    print("Time to get to step")
    for key, value in stepTimes.items():
        print("Step ",key, ": ", value, "microseconds")
    #Relativize times to previous step
    print("Individual times")
    stepTimes["4"] = (merchant.times["4"]-acquiringBank.times["3.2"])
    stepTimes["3.2"] = (acquiringBank.times["3.2"]-issuingBank.times["2.2"])
    stepTimes["2.2"] = (issuingBank.times["2.2"]-consumer.times["2.1"])
    stepTimes["2.1"] = (consumer.times["2.1"]-merchant.times["1.4"])
    stepTimes["1.4"] = (merchant.times["1.4"]-consumer.times["1.3"])
    stepTimes["1.3"] = (consumer.times["1.3"]-merchant.times["1.2"])
    stepTimes["1.2"] = (merchant.times["1.2"]-consumer.times["1.1"])
    stepTimes["1.1"] = (consumer.times["1.1"]-start)

    for key, value in stepTimes.items():
        print("Step ",key, " took: ", value, "microseconds")