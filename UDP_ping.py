# UDP Ping
from socket import *
import time

# pongName = 'catan.eecis.udel.edu'
# pongName = 'cisc450.cis.udel.edu'
pongName = "localhost"
pongPort = 12344

pingSocket = socket(AF_INET, SOCK_DGRAM)
print(pingSocket)

number = int(input('Enter an integer: '))

print(f"I am sending {number} to {pongName} on port {pongPort}")

time.sleep(1)

pingSocket.sendto(str(number).encode(), (pongName, pongPort))
updatedNumber, pongAddress = pingSocket.recvfrom(2048)
number = int(updatedNumber.decode())
print(f"I've recieved {number} from {pongAddress}. I am sending back {number} + 2")

time.sleep(1)

pingSocket.sendto(str(number + 2).encode(), (pongName, pongPort))
updatedNumber, pongAddress = pingSocket.recvfrom(2048)
number = int(updatedNumber.decode())
print(f"I've recieved {number} from {pongAddress}")

time.sleep(1)

pingSocket.close()
