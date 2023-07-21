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

for i in range(100):
  preamble = "AB"
  data=str(i)+str(utime.mktime(utime.localtime()))+":esp006:"+str(random.random())
  pre_num = 0
  for j in range(10):
    pre_num = j
    tmp = e.stats()[2]
    e.send(peer1,preamble,True)
    print(j)
    if tmp == e.stats()[2]:
      print(f"{tmp}:{e.stats()[2]},preamble was sended")
      utime.sleep(1)
      break
    utime.sleep(1)
  tmp2 = e.stats()[2]
  e.send(peer1,data,True)
  if tmp2 == e.stats()[2]:
    print(f"{tmp}:{e.stats()[2]},success")
    with open("result.csv","a") as f:
      data = str(i)+","+str(pre_num)+",SUCCESS"
      f.write(data)
  else:
    print(f"{tmp}:{e.stats()[2]},failed")
    with open("result.csv","a") as f:
      data = str(i)+","+str(pre_num)+",FAILED"
      f.write(data)
  print(data)
  utime.sleep(1)

e.deinit()
print("deinit")

