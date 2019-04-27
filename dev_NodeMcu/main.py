from rfidPorteiro import RfidPorteiro as rf
from setup import Setup as stp
import time
import ujson

import time
import machine, neopixel
from machine import Pin

#Defining constants
RELAY_OFF = 0
RELAY_ON = 1
NP_OFF = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (128, 128, 128)


#Pinnig state NeoPixel
np = neopixel.NeoPixel(machine.Pin(13)(1))
#Relay Pin
relay = Pin(12, Pin.OUT)

#Led cycle
def cycleLeds(cycles):
    i = 0 
    while(i < cycles): 
        np[0] = GREEN
        np.write()
        time.sleep(0.2)
        np[0] = YELLOW
        np.write()
        time.sleep(0.2)
        np[0] = RED
        np.write()
        time.sleep(0.2)
        i = i + 1
    np[0] = WHITE
    np.write()
    time.sleep(0.2)
    np[0] = NP_OFF
    np.write()

#Startup Led
def startLed():
    cycleLeds(4)

#Led configuration for normal mode
def normalModeOn():
    np[0] = YELLOW
    np.write()
    print("---------------")
    print("Normal Mode On.")
    print("---------------")
    relay(RELAY_OFF)

#Led indication that program mode is on
def programModeOn():
    cycleLeds(2)
    np[0] = WHITE
    np.write()
    print("---------------")
    print("Program Mode On.")
    print("---------------")
    relay(RELAY_OFF)

#Acess granted
def granted(setDelay):
    np[0] = GREEN
    np.write()
    relay.value(RELAY_ON)
    print("---------------")
    print("Access Granted.")
    print("---------------")
    time.sleep(setDelay)

#Access denied
def denied():
    np[0] = RED
    np.write()
    relay.value(RELAY_OFF)
    print("---------------")
    print("Access Denied.")
    print("---------------")
    time.sleep(1)

#Write Sucess
def sucessWrite():
    np[0] = NP_OFF
    np.write()
    time.sleep(0.2)
    i = 0
    while(i < 3):
        np[0] = GREEN
        np.write()
        time.sleep(0.2)
        np[0] = NP_OFF
        np.write()
        time.sleep(0.2)
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
stp()

startLed()
print(".\n.\n.\n    Access Control v0.1     \n.\n.\n.")

#Main Loop
while(True):
    

