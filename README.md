# SyncHop
SyncHop is a software for ESP-NOW network.

This software is implemented by micropython.

#1 A simple example in data transmission from sender(sender.py) to receiver(receiver.py).

<img width="331" alt="スクリーンショット 2023-07-14 085422" src="https://github.com/cdsl-research/G2122007_03/assets/65758209/f2b62f00-a9e7-47f9-ae2a-693e2eff615a">

#2 An example in multihop data transmission via relay(relay.py).

<img width="514" alt="スクリーンショット 2023-07-14 090134" src="https://github.com/cdsl-research/G2122007_03/assets/65758209/9a93b6e7-77e0-4f3d-a3dd-7514994e0993">

# Usage
Setting MAC addresses in config.json and setting peers.
```
peer1 = ubinascii.unhexlify(di["esp32"]["esp004"]["mac"].encode())
```
Executing each programs in terminal.
```
execfile("sender.py") #(Role | sender, relay, receiver).py
```
