import redis
from datetime import datetime
from time import sleep

conn = redis.Redis()
timeout = 10
conveyor = 'czekolady'
while True:
    sleep(0.5)
    msg = conn.blpop(conveyor, timeout)
    remaining = conn.llen(conveyor)
    if msg:
        piece = msg[1]
        print('Zdjęta czekolada', piece, 'o godz.', datetime.utcnow(),
        ', pozostało sztuk:', remaining)
