import gc
import ujson
gc.collect()
try:
    pritn(" . ")
    arq = open("ID.json").read()
    print("Found IDs list")

except:
    print("Not found IDs list")
    print("...")
    print("Creating IDs list")
    arq = open("ID.json","w")
    print("List of created IDs")
    arq.close()