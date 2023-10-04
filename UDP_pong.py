# UDP Pong
from socket import *
import time

pongPort = 12344

pongSocket = socket(AF_INET, SOCK_DGRAM)
pongSocket.bind(('', pongPort))
print("pong socket", pongSocket)

print("UDP Pong is ready to receive...")

number = 0

updatedNumber, pingAddress = pongSocket.recvfrom(2048)
number = int(updatedNumber.decode())
print(f"I've recieved {number} from {pingAddress}. I am sending back {number} + 1")

time.sleep(1)

pongSocket.sendto(str(number + 1).encode(), pingAddress)
updatedNumber, pingAddress = pongSocket.recvfrom(2048)
number = int(updatedNumber.decode())
print(f"I've recieved {number} from {pingAddress}. I am sending back {number} + 3")

time.sleep(1)

pongSocket.sendto(str(number + 3).encode(), pingAddress)

pongSocket.close()
