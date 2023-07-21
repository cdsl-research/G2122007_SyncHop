from esp import espnow

try:
  e = espnow.ESPNow()
  e.init()
  print("init")

  recv_from = ubinascii.unhexlify(di["esp32"]["esp006"]["mac"].encode())   # MAC address of peer's wifi interface
  send_to = ubinascii.unhexlify(di["esp32"]["esp002"]["mac"].encode())
  e.add_peer(recv_from)
  e.add_peer(send_to)
  print("add_peer: ", recv_from, send_to)
except:
  print("init_error")

#try:
while True:
  print("Receiving...")
  host, msg = e.irecv()     # Available on ESP32 and ESP8266
  if msg:             # msg == None if timeout in irecv()
    print(host, msg)
    ack=str(msg)
    if host==recv_from:
      e.send(send_to, msg, True)
      print("end")
    if msg == b'end':
      print("end")
      break
#except:
#  print("receive_error")

e.deinit()
print("deinit")
