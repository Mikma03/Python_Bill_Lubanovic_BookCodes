from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 1000

print('Czas uruchomienia serwera', datetime.now())
print('Oczekiwanie na połączenie od klienta.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print('Dane odebrane', datetime.now(), 'od klienta', client, ':', data)
client.sendall(b'Witaj, kliencie!')
client.close()
server.close()
