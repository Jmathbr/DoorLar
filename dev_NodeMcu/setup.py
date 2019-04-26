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
                IdMaster = {"ID": "okok"} #str(rf.get())

                if IdMaster != "SemTag":
                    break

            data = [{"ID":IdMaster}]
            arq.write(ujson.dumps(data))
            arq.close()



    def findCard(self, tag):

        arq = open("ID.json").read() #abrindo arquivo listas    
        arqload = ujson.loads(arq)  
        amount = int(len(arqload)) #tamanho da lista

        findTag = tag
        
        for i in range (amount):
            if arqload[i]["ID"] == findTag :
                print("Tag ", findTag," encontrada na posicao", i)
                arq.close()
                return (True,i)

        arq.close()
        print("Tag", findTag, "não encontrada")
        return (False,i)


    def addCard(self, tag):

        arq = open("ID.json").read()                 #abrindo arquivo listas    
        arqload = ujson.loads(arq)
        newdata = {"ID":"newssid"} #str(rf.get())
        arqload.append(newdata)                 #add novo dado a lista redes
        arq = open("ID.json","w")
        arq.write(ujson.dumps(arqload))                 #sobrecrevendo lista antiga com a nova lista atualizada
        arq.close()
    


    def rmCard(self,tag):

        (std,pos) = self.findCard(tag) 
        arq = open("ID.json").read()                 #abrindo arquivo listas    
        arqload = ujson.loads(arq)
        arqload.pop(pos)
        arq = open("ID.json","w")
        arq.write(ujson.dumps(arqload))                 #sobrecrevendo lista antiga com a nova lista atualizada
        arq.close()



    def IsMaster(self,tag):

        arq = open("ID.json").read()
        arqload = ujson.loads(arq)
        amount = int(len(arqload))

        for i in range (amount):
            if arqload[i]["ID"] == tag:
                 return True
            else:
                return False

