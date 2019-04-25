from rfidPorteiro import RfidPorteiro as rf
import ujson
import time


class Setup:
    def __init__(self):
        print("Setup started")
        #Colocar no boot
        try:
            arq = open("ID.json").read()
            print("Found ID Master")
            arqload = ujson.loads(arq)
            arq.close()

        except:
            print("Not Found ID Master")
            print("Scan A RFID Card to Define as Master Card: ")

            while(True):
                time.sleep_ms(100)
                IdMaster = str(rf.get())

                if IdMaster != "SemTag":
                    break

            data = [{"ID":IdMaster}]
            arq.write(ujson.dumps(data))
            arq.close()

