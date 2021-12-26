import gevent
from gevent import socket
hosts = ['www.helion.pl', 'www.gov.pl', 'www.facebook.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)