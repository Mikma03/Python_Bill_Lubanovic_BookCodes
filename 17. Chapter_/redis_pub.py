import redis
import random

conn = redis.Redis()
cats = ['syjamski', 'perski', 'mainkun', 'norwerski leśny']
hats = ['cylinder', 'melonik', 'kapelusz myśliwski', 'kapelusz kowbojski']
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('Publikowanie komunikatu: kot %s nosi %s' % (cat, hat))
    #conn.publish(cat, hat)
