from esp import espnow
import utime
import random
import ujson
import ubinascii

with open('config.json') as f:
  di = ujson.load(f)

e = espnow.ESPNow()
e.init()
print("init")
peer1 = ubinascii.unhexlify(di["esp32"]["esp004"]["mac"].encode())
print(peer1)
e.add_peer(peer1)
print("add_peer: ", peer1)

while True:
  host, msg = e.recv()
  if msg:             # msg == None if timeout in recv()
    print(host, msg)
    if msg == b'end':
      break
