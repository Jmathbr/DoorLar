from rfidPorteiro import RfidPorteiro as rf
import ujson
import time

#Setup
class Setup:
    def __init__(self):
        print("Setup started")
        
        try:
            arq = open("ID.json").read()
            print("Found ID Master")
            arqload = ujson.loads(arq)

        except:
            print("Not Found ID Master")
            print("Scan A RFID Card to Define as Master Card: ")
            arq = open("ID.json","w")
            
            while(True):
                time.sleep_ms(100)
                IdMaster = str(rf.get())

                if IdMaster != "SemTag":
                    break

            data = [{"ID":IdMaster}]
            arq.write(ujson.dumps(data))
            arq.close()

