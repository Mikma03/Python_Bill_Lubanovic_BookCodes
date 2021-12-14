import socket
from datetime import datetime
from time import sleep

address = ('localhost', 6789)
max_size = 4096

print('Czas uruchomienia klienta:', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sleep(5)
    client.sendto(b'time', address)
    data, server_addr = client.recvfrom(max_size)
    print('Odebrana odpowiedź:', data)
client.close()