from esp import espnow
import utime

ack=""
try:
  e = espnow.ESPNow()
  e.init()
  print("init")

  peer1 = b'\xecb`\x83\xbc\x10'   # MAC address of peer's wifi interface
  peer2 = b'\xfc\xf5\xc4=;,'
  e.add_peer(peer1)
  e.add_peer(peer2)
  print("add_peer: ", peer1, peer2)
except:
  print("init_error")

#try:
while True:
  print("Receiving...")
  host, msg = e.irecv()     # Available on ESP32 and ESP8266
  start=utime.ticks_ms()
  if msg:             # msg == None if timeout in irecv()
    print(host, msg)
    ack=str(msg)
    if host==peer1:
      stop=utime.ticks_ms()
      f=open("result.txt","a")
      f.write(str(stop-start))
      f.write("\n")
      f.close()
      e.send(peer2, ack, True)
      print("end")
    if host==peer2:
      stop=utime.ticks_ms()
      f=open("result.txt","a")
      f.write(str(stop-start))
      f.write("\n")
      f.close()
      e.send(peer1, ack, True)
      print("end")
    if msg == b'end':
      print("end")
      break
#except:
#  print("receive_error")

e.deinit()
print("deinit")
