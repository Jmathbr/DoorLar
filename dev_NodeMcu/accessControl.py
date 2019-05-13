import time
from machine import Pin
from npControl import NpControl as npc
RELAY_OFF = 0
RELAY_ON = 1 


buttonState = False

class AcessControl:

    def __init__(self,GPIO_RELE,obj_np):
        
        self.relay = Pin(GPIO_RELE, Pin.OUT)
        #self.npc = self.npc(GPIO_np)
        self.npc = obj_np

    def denied(self):
        self.npc.denied()
        self.relay.value(RELAY_OFF)
        print("---------------")
        print("You Shall Not Pass.")
        print("---------------")
        #time.sleep(1)

    def granted(self,setDelay):
        self.npc.granted()
        self.relay.value(RELAY_ON)
        print("---------------")
        print("Welcome, You Shall Pass.")
        print("---------------")
        #time.sleep(setDelay)

    def programModeOn(self):
        self.npc.cycleLeds(2)
        self.relay(RELAY_OFF)

    def normalModeOn(self):
        self.npc.read()
        print("---------------")
        print("Normal Mode On.")
        print("---------------")
        self.relay(RELAY_OFF)