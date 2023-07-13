from esp import espnow
import utime
import ujson
import ubinascii

with open('config.json') as f:
  di = ujson.load(f)

#try:
e = espnow.ESPNow()
e.init()
print("init")
peer = ubinascii.unhexlify(di["esp32"]["esp001"]["mac"].encode())
print(peer)
e.add_peer(peer)
print("add_peer: ", peer)
#except:
#  print("init_error")

try:
  while True:
    print("Receiving...")
    host, msg = e.irecv()     # Available on ESP32 and ESP8266
    if msg:             # msg == None if timeout in irecv()
      print(host,msg)
      if msg == b'end':
        break
except:
  print("receive_error")

e.deinit()
print("deinit")



