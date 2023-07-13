from esp import espnow
import utime
import random

#execfile("ntptime.py")

for i in range(1):
  e = espnow.ESPNow()
  e.init()
  print("init")
  peer = b'\xff\xff\xff\xff\xff\xff' # MAC address of peer's wifi interface
  e.add_peer(peer)
  peer1 = b'\xecb`\x84\x00\x00'
  e.add_peer(peer1)
  print("add_peer: ", peer)

  e.send(peer,"Starting...")       # Send to all peers
  print("Starting...")
  #for j in range(1000):
    #f = open("network.txt", "a")
    #start=utime.ticks_ms()
    #e.send(peer, str(random.random()), True)
    #stop=utime.ticks_ms()
    #f.write(str(stop-start))
    #f.write("\n")
    #utime.sleep(0.1)
    #f.close()
  for i in range(10):
    e.send(b'end')
  print("end")
  e.deinit()
  

