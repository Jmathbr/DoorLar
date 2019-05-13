# ************ DEFAULT ************
# NeoPixel GPIO = 13
# Rele  GPIO = 15
# Button GPIO = 12

# (Em rfidPorteiro.py, GPIOs):
# sck = 0
# mosi = 2
# miso = 4 
# rst = 5 
# cs = 14

from rfidPorteiro import RfidPorteiro as rf
from accessControl import AcessControl as acs
from npControl import NpControl as npc
from setup import Setup as stp
import ujson
from machine import Pin
import time

# Constantes
NP_GPIO = 13
RELE_GPIO = 16 #LED Test
GPIO_BUTTON = 12 #Interrupt Test

# Variáveis Globais 
t_ult = 0
stp = stp()
rf = rf()
npc = npc(NP_GPIO)
acs = acs(RELE_GPIO, npc)
i = 0

programMode = False
buttonstate = False

print(".\n.\n.\n    Access Control v0.1     \n.\n.\n.")

# Funcoes
def checkTime(t_ult, time_ms):
    if (time.ticks_ms() - t_ult) >= time_ms:
        return True
    else:
        return False

def interrupt():
    global t_ult
    t_ult = time.ticks_ms()
    print("Interrupt active...")

def check_rfid(cardTag):
    npc.reading()
    if stp.IsMaster(cardTag):          # Verifica se o cartao eh o master
        if(stp.IsMaster(cardTag)):
            global t_ult
            t_ult = time.ticks_ms()
            
        elif(stp.findCard(cardTag)[0]):
            stp.rmCard(cardTag)

        else:
            stp.addCard(cardTag)
    
    elif (stp.findCard(cardTag)[0]):   # Verifica se o cartao estah cadastrado
        global t_ult
        t_ult = time.ticks_ms()

# MAIN SETUP
button = Pin(GPIO_BUTTON, Pin.IN, Pin.PULL_UP)
button.irq(trigger=Pin.IRQ_RISING, handler=interrupt())

# MAIN LOOP
while True:
    cardTag = str(rf.get())
    if (cardTag != "SemTag"):
        check_rfid(cardTag)
    print(cardTag)
    
    if checkTime(t_ult,3000):
        acs.granted(1)
    else:
        acs.denied()    
            
