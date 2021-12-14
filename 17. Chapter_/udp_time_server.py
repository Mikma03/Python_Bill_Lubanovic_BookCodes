from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

print('Czas uruchomienia serwera:', datetime.now())
print('Oczekiwanie na zapytania klienta.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)
while True:
    data, client_addr = server.recvfrom(max_size)
    if data == b'time':
        now = str(datetime.utcnow())
        data = now.encode('utf-8')
        server.sendto(data, client_addr)
        print('Odpowiedź serwera:', data)
server.close()