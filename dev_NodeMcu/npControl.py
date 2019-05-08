import time
import machine, neopixel
from machine import Pin

#Defining constants
NP_OFF = (0, 0, 0)
ORANGE = (125, 30, 0)
RED = (50, 0, 0)
YELLOW = (50, 50, 0)
GREEN = (0, 50, 0)
BLUE = (0, 0, 50)
CYAN = (0, 50, 50)
VIOLET =(50, 0, 50)
WHITE = (150, 150, 150)

time_ms = 50

class NpControl:

    def __init__(self, GPIO_np:int):

        self.np = neopixel.NeoPixel(machine.Pin(GPIO_np), (1))

    #Led cycle
    def cycleLeds(self,cycles):

        for i in range(cycles+1):
            self.np[0] = ORANGE
            self.np.write()
            time.sleep_ms(time_ms)
            
            self.np[0] = RED
            self.np.write()
            time.sleep_ms(time_ms)
            
            self.np[0] = YELLOW
            self.np.write()
            time.sleep_ms(time_ms)
            
            self.np[0] = GREEN
            self.np.write()
            time.sleep_ms(time_ms)
            
            self.np[0] = CYAN
            self.np.write()
            time.sleep_ms(time_ms)
            
            self.np[0] = BLUE
            self.np.write()
            time.sleep_ms(time_ms)
            
            self.np[0] = VIOLET
            self.np.write()
            time.sleep_ms(time_ms)


    #Startup Led
    def startLed(self, cycles):
        self.cycleLeds(4)

    def granted(self):
        self.np[0] = GREEN
        self.np.write()
        time.sleep_ms(time_ms)
    
    def read(self):
        self.np[0] = WHITE
        self.np.write()
        time.sleep_ms(time_ms)
    
    def add(self):
        self.np[0] = BLUE
        self.np.write()
        time.sleep_ms(time_ms)

    def rm(self):
        self.np[0] = ORANGE
        self.np.write()
        time.sleep_ms(time_ms)
