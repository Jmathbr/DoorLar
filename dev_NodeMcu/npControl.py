import time
import machine, neopixel
from machine import Pin

#Defining constants
NP_OFF = (0, 0, 0)
ORANGE = (255, 127, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET =(255, 0, 255)
WHITE = (128, 128, 128)

LED_DELAY = 50

class npControl:

    def __init__(self, GPIO_np:int):
        #NeoPixel Pin
        np = neopixel.NeoPixel(machine.Pin(GPIO_np), (1))

    #Led cycle
    def cycleLeds(cycles):
        i = 0 
        while(i < cycles): 
            np[0] = ORANGE
            np.write()
            time.sleep_ms(LED_DELAY)
            np[0] = RED
            np.write()
            time.sleep_ms(LED_DELAY)
            np[0] = YELLOW
            np.write()
            time.sleep_ms(LED_DELAY)
            np[0] = GREEN
            np.write()
            time.sleep_ms(LED_DELAY)
            np[0] = CYAN
            np.write()
            time.sleep_ms(LED_DELAY)
            np[0] = BLUE
            np.write()
            time.sleep_ms(LED_DELAY)
            np[0] = VIOLET
            np.write()
            time.sleep_ms(LED_DELAY)
            i = i + 1

    #Startup Led
    def startLed():
        cycleLeds(4)
    
