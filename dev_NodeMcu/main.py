from rfidPorteiro import RfidPorteiro as rf
from accessControl import AcessControl as acs
from npControl import NpControl as npc
from setup import Setup as stp
import ujson
from machine import Pin
import time

t_ult = 0
stp = stp()
rf = rf()
npc = npc(13)
acs = acs(15,npc)

GPIO_BUTTON = 12
programMode = False
buttonstate = False
#startLed()

print(".\n.\n.\n    Access Control v0.1     \n.\n.\n.")




def checkTime(t_ult, time_ms):
    if (time.ticks_ms() - t_ult) <= time_ms:
        return True
    else:
        return False

def interrupt(t_ult):
    t_ult = time.ticks_ms()

button = Pin(GPIO_BUTTON, Pin.IN, Pin.PULL_UP)
button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt(t_ult))

def check_rfid(cardTag):
    if stp.IsMaster(cardTag):#Verifica se o cartao e o master
        while True:
            npc.cycleLeds(1)
            newtag = str(rf.get())

            if(stp.IsMaster(newtag)):
                acs.granted(1)
                break
            
            if(stp.findCard(newtag)[0]):
                stp.rmCard(newtag)

            else:
                stp.addCard(newtag)

    if cardTag == "SemTag":
        npc.read()
        print("SEMTAG")

    elif (stp.findCard(cardTag)[0]):  #verifica se o cartao esta cadastrado
        global t_ult
        t_ult = time.ticks_ms()
        
while True:

    cardTag = str(rf.get())
    check_rfid(cardTag)

    if checkTime(t_ult,3000):
        acs.granted(1)
    else:
        acs.denied()    
            
