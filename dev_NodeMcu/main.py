from rfidPorteiro import RfidPorteiro as rf
from setup import Setup as stp
import time
import ujson

import time
import machine, neopixel
from machine import Pin


#Defining constants
RELAY_OFF = 0
BUTTON_OFF = 1
RELAY_ON = 1 
BUTTON_ON = 0
NP_OFF = (0, 0, 0)

ORANGE = (255, 127, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0,255,255)
VIOLET =(255,0,255)

LEDELAY = 50

WHITE = (128, 128, 128)

#NeoPixel Pin
np = neopixel.NeoPixel(machine.Pin(13), (1))
#Relay Pin
relay = Pin(15, Pin.OUT)
#Button Pin
button = Pin(12, Pin.IN, Pin.PULL_UP)

#Variables
programMode = False
buttonState = False
t_ult = 0
t_atual = 0

#Sleep
def sleep(t_ult, t_atual, time_ms):
    if t_ult + t_atual >= time_ms:
        return True
    else:
        return False

#Led cycle
def cycleLeds(cycles):
    i = 0 
    while(i < cycles): 
        np[0] = ORANGE
        np.write()
        time.sleep_ms(LEDELAY)
        np[0] = RED
        np.write()
        time.sleep_ms(LEDELAY)
        np[0] = YELLOW
        np.write()
        time.sleep_ms(LEDELAY)
        np[0] = GREEN
        np.write()
        time.sleep_ms(LEDELAY)
        np[0] = CYAN
        np.write()
        time.sleep_ms(LEDELAY)
        np[0] = BLUE
        np.write()
        time.sleep_ms(LEDELAY)
        np[0] = VIOLET
        np.write()
        time.sleep_ms(LEDELAY)
        i = i + 1
    #np[0] = WHITE
    #np.write()
    #time.sleep(0.2)
    #np[0] = NP_OFF
    #np.write()

#Startup Led
def startLed():
    cycleLeds(4)

#Led configuration for normal mode
def normalModeOn():
    np[0] = WHITE
    np.write()
    print("---------------")
    print("Normal Mode On.")
    print("---------------")
    relay(RELAY_OFF)

#Led configuratios for program mode
def programModeOn():
    cycleLeds(2)
    #np[0] = BLUE
    #np.write()
    relay(RELAY_OFF)

#Acess granted
def granted(setDelay):
    #Suavisa ao acender a luz
    global t_ult = time.ticks_ms()
    for i in range(0,256):
        np[0] = (0,i,0)
        np.write()
        time.sleep_ms(2)

    #np[0] = GREEN
    #np.write()
    relay.value(RELAY_ON)
    print("---------------")
    print("Welcome, You Shall Pass.")
    print("---------------")
    sleep(t_ult, timesetDelay*1000)

#Access denied
def denied():
    #Suavisa ao acender a luz
    for i in range(0,256):
        np[0] = (i,0,0)
        np.write()
        time.sleep_ms(2)

    #np[0] = RED
    #np.write()
    relay.value(RELAY_OFF)
    print("---------------")
    print("You Shall Not Pass.")
    print("---------------")
    time.sleep(1)

#Write Sucess
def sucessWrite():
    np[0] = NP_OFF
    np.write()
    time.sleep_ms(100)
    i = 0
    while(i < 3):
        np[0] = GREEN
        np.write()
        time.sleep_ms(100)
        np[0] = NP_OFF
        np.write()
        time.sleep_ms(100)
        i = i + 1 

#Write Failed
def failedWrite():
    np[0] = NP_OFF
    np.write()
    time.sleep(0.2)
    i = 0
    while(i < 3):
        np[0] = RED
        np.write()
        time.sleep(0.2)
        np[0] = NP_OFF
        np.write()
        time.sleep(0.2)
        i = i + 1 

#Delete Sucess
def sucessDelete():
    np[0] = NP_OFF
    np.write()
    time.sleep(0.2)
    i = 0
    while(i < 3):
        np[0] = YELLOW
        np.write()
        time.sleep(0.2)
        np[0] = NP_OFF
        np.write()
        time.sleep(0.2)
        i = i + 1 

#Setup
stp = stp()
rf = rf()
startLed()
print(".\n.\n.\n    Access Control v0.1     \n.\n.\n.")



#Main Loop
while(True):
    cardTag = str(rf.get())

    while(cardTag == "SemTag"):
        if button.value() == BUTTON_ON:

            #np[0] = GREEN
            #np.write()
            
            print("Button Pressed, Opening Door")
            granted(1)
        if programMode == True:
            programModeOn()
        else:
            normalModeOn()
        cardTag = str(rf.get())
    #Caso não esteja lendo nenhum cartão, não proseguirá
    
    if programMode == True:
        if stp.IsMaster(cardTag):
            print("Master Card Scanned")
            print("Exiting Program Mode and Opening Door")
            print("-----------------------------")
            granted(1)
            programMode = False
        else:
            if stp.findCard(cardTag)[0]:
                print("I know this CARD, removing...")
                stp.rmCard(cardTag)
                #add retorno visual
                np[0] = RED
                np.write()
                time.sleep_ms(3000)
                #fim do retorno visual
                print("-----------------------------")
                print("Scan a CARD to ADD or REMOVE from memory")
            else:
                print("I do not know this CARD, adding...")
                stp.addCard(cardTag)
                #add retorno visual
                np[0] = GREEN
                np.write()
                time.sleep_ms(3000)
                #fim do retorno visual
                print("-----------------------------")
                print("Scan a CARD to ADD or REMOVE from memory")
    else:

        if stp.IsMaster(cardTag):
            programMode = True
            print("Hello Master - Entered Program Mode")
            amount = stp.amount()
            print("I have", amount, "card(s) on memory.\n")
            print("Scan a CARD to ADD or REMOVE from memory")
            print("Scan Master Card again to Exit Program Mode")
            print("-----------------------------")
        else:
            if stp.findCard(cardTag)[0]:
                granted(1)
            else:
                denied()
            
