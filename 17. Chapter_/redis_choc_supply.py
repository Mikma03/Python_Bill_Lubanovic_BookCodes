import redis
import random
from time import sleep

conn = redis.Redis()
varieties = ['mleczna', 'gorzka', 'karmelowa', 'orzechowa']
conveyor = 'czekolady'
while True:
    seconds = random.random()
    sleep(seconds)
    piece = random.choice(varieties)
    conn.rpush(conveyor, piece)
