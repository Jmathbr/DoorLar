from rfidPorteiro import RfidPorteiro as rf
from setup import Setup as stp
import time
import ujson

#void Setup
stp()


#void loop
#while(True):
#
#    tag = "teste"#str(rf.get())
#    time.sleep_ms(100)
#    cont = 0
#    for cont in range (amount):
#        if str(tag) == str(arqload[cont]["ID"]):
#            key = True
#            break
#
#    if key == True:
#        print("deu bom")
#        break

    #if tag != "SemTag":
    #    print(tag)
    #    print ("okok")
    #    url = "http://10.6.3.114:8012/?Matricula="+tag
    #    #url = "http://10.6.3.114:8012/?Tag="+tag
    #    response = urequests.get(url)
