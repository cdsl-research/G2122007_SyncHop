from esp import espnow
import utime

for i in range(1):
  e = espnow.ESPNow()
  e.init()
  print("init")
  peer = b'\xecb`\x84\x00\x00' # MAC address of peer's wifi interface

  e.add_peer(peer)
  print("add_peer: ", peer)

  e.send(b'start')       # Send to all peers
  print("Starting...")
  for j in range(10):
    f = open("network.txt", "a")
    for k in range(10):
      start=utime.ticks_ms()
      e.send(peer, str(i), True)
      f.write(str(utime.localtime()))
      f.write(",")
      f.write(str(e.stats()))
      f.write("\n")
      e.send(b'end')
    f.close()
    print("end")
    try:
      while True:
        f = open("network.txt", "a")
        print("Receiving...")
        host, msg = e.irecv()     # Available on ESP32 and ESP8266
        if msg:             # msg == None if timeout in irecv()
          stop=utime.ticks_ms()
          print(host, msg)
          f.write(str(utime.localtime()))
          f.write(",")
          f.write(str(e.stats()))
          f.write(",")
          f.write(str(e.peers))
          f.write("\n")
          if msg == b'end':
            print("end")
            f.close()
            break
        f.close()
    except:
      print("receive_error")
    print(stop-start)
    f = open("result.txt", "a")
    f.write(str(stop-start))
    f.write("\n")
    f.close()
    utime.sleep(1)
  e.deinit()
