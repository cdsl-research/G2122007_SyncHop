# SyncHop
SyncHop is a software for ESP-NOW network.

This software is implemented by micropython.

#1 A simple example in data transmission from sender(sender.py) to receiver(receiver.py).

<img width="331" alt="スクリーンショット 2023-07-14 085422" src="https://github.com/cdsl-research/G2122007_SyncHop/assets/65758209/52e10a5e-3cbc-4b6d-abf2-46ff4ac4bd25">


#2 An example in multihop data transmission via relay(relay.py).

<img width="514" alt="スクリーンショット 2023-07-14 090134" src="https://github.com/cdsl-research/G2122007_SyncHop/assets/65758209/e9f2dc37-456e-4197-b7ef-ac86b97105a7">

# Usage
Setting MAC addresses in config.json and setting peers.
```config.json
{
  "esp32":{
    "esp001":{
      "mac" : "<MAC_ADDRESS>"
    },
  }
}
```
```
peer1 = ubinascii.unhexlify(di["esp32"]["esp001"]["mac"].encode())
```
Executing each programs on terminal.
```
execfile("sender.py") #(Role | sender, relay, receiver).py
```
