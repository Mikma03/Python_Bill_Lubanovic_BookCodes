import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 4096

print('Czas uruchomienia klienta', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Witaj, serwerze!', server_address)
data, server = client.recvfrom(max_size)
print('Dane odebrane', datetime.now(), 'z serwera', server, ':', data)
client.close()
