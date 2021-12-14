from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 4096

print('Czas uruchomienia serwera', datetime.now())
print('Oczekiwanie na połączenie od klienta.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)
data, client = server.recvfrom(max_size)
print('Dane odebrane', datetime.now(), 'od klienta', client, ':', data)
server.sendto(b'Witaj, kliencie!', client)
server.close()
