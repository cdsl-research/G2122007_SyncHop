from esp import espnow
import utime
ack=""
try:
  e = espnow.ESPNow()
  e.init()
  print("init")

  peer = b'x!\x84\x9c\xaa\\'   # MAC address of peer's wifi interface
  e.add_peer(peer)
  print("add_peer: ", peer)
except:
  print("init_error")
for i in range(100):
  try:
    while True:
      print("Receiving...")
      host, msg = e.irecv()     # Available on ESP32 and ESP8266
      if msg:             # msg == None if timeout in irecv()
        print(host,msg)
        ack=str(msg)
        if msg == b'end':
          print("end")
          break
  except:
    print("receive_error")
  utime.sleep(3)
  if host==peer:
    for j in range(10):
      e.send(peer, "ack", True)
      e.send(peer, b'end')
    print("end")
e.deinit()
print("deinit")

