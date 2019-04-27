from rfidPorteiro import RfidPorteiro as rf
from setup import Setup as stp
import time
import ujson

import time
from machine import Pin

#Defining constants
LED_OFF = RELAY_OFF = 0
LED_ON = RELAY_ON = 1

#Pinnig state LEDS
redLed = Pin(12, Pin.OUT) 
yellowLed = Pin(13, Pin.OUT) 
greenLed = Pin(15, Pin.OUT)
#Relay Pin
relay = Pin(16, Pin.OUT)

#Led cycle
def cycleLeds(cycles):
    i = 0 
    while(i < cycles): 
        redLed.value(LED_OFF)
        yellowLed.value(LED_OFF)
        greenLed.value(LED_ON)
        time.sleep(0.2)
        redLed.value(LED_OFF)
        yellowLed.value(LED_ON)
        greenLed.value(LED_OFF)
        time.sleep(0.2)
        redLed.value(LED_ON)
        yellowLed.value(LED_OFF)
        greenLed.value(LED_OFF)
        time.sleep(0.2)
        i = i + 1
    redLed.value(LED_ON)
    yellowLed.value(LED_ON)
    greenLed.value(LED_ON)
    time.sleep(0.2)
    redLed.value(LED_OFF)
    yellowLed.value(LED_OFF)
    greenLed.value(LED_OFF)

#Startup Led
def startLed():
    cycleLeds(4)

#Led configuration for normal mode
def normalModeOn():
    greenLed.value(LED_OFF)
    yellowLed.value(LED_ON)
    redLed.value(LED_OFF)
    print("---------------")
    print("Normal Mode On.")
    print("---------------")
    relay(RELAY_OFF)

#Led indication that program mode is on
def programModeOn():
    cycleLeds(2)
    greenLed.value(LED_ON)
    yellowLed.value(LED_ON)
    redLed.value(LED_ON)
    print("---------------")
    print("Program Mode On.")
    print("---------------")
    relay(RELAY_OFF)

#Acess granted
def granted(setDelay):
    greenLed.value(LED_ON)
    yellowLed.value(LED_OFF)
    redLed.value(LED_OFF)
    relay.value(RELAY_ON)
    print("---------------")
    print("Access Granted.")
    print("---------------")
    time.sleep(setDelay)

#Access denied
def denied():
    greenLed.value(LED_OFF)
    yellowLed.value(LED_OFF)
    redLed.value(LED_ON)
    relay.value(RELAY_OFF)
    print("---------------")
    print("Access Denied.")
    print("---------------")
    time.sleep(1)

#Write Sucess
def sucessWrite():
    greenLed.value(LED_OFF)
    yellowLed.value(LED_OFF)
    redLed.value(LED_OFF)
    time.sleep(0.2)
    i = 0
    while(i < 3):
        greenLed.value(LED_ON)
        time.sleep(0.2)
        greenLed.value(LED_OFF)
        time.sleep(0.2)
        i = i + 1 

#Write Failed
def failedWrite():
    greenLed.value(LED_OFF)
    yellowLed.value(LED_OFF)
    redLed.value(LED_OFF)
    time.sleep(0.2)
    i = 0
    while(i < 3):
        redLed.value(LED_ON)
        time.sleep(0.2)
        redLed.value(LED_OFF)
        time.sleep(0.2)
        i = i + 1 

#Delete Sucess
def sucessDelete():
    greenLed.value(LED_OFF)
    yellowLed.value(LED_OFF)
    redLed.value(LED_OFF)
    time.sleep(0.2)
    i = 0
    while(i < 3):
        yellowLed.value(LED_ON)
        time.sleep(0.2)
        yellowLed.value(LED_OFF)
        time.sleep(0.2)
        i = i + 1 

#Setup
stp()

startLed()
print(".\n.\n.\n    Access Control v0.1     \n.\n.\n.")

#Main Loop
while(True):
    normalModeOn()
    time.sleep(3)
    granted(2)
    time.sleep(1)
    denied()
    programModeOn()
    time.sleep(2)
    sucessWrite()
    time.sleep(1)
    failedWrite()
    time.sleep(1)
    sucessDelete()
    time.sleep(2)

