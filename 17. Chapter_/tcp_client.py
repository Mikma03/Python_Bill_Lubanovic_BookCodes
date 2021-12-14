import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000

print('Czas uruchomienia klienta:', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Witaj, serwerze!')
data = client.recv(max_size)
print('Dane odebrane', datetime.now(), ':', data)
client.close()
