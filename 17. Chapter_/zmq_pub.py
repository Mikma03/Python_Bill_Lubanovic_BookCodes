import zmq
import random
import time

host = '*'
port = 6789
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))
cats = ['syjamski', 'perski', 'mainkun', 'norwerski leśny']
hats = ['cylinder', 'melonik', 'kapelusz myśliwski', 'kapelusz kowbojski']
time.sleep(1)
for msg in range(10):
    cat = random.choice(cats)
    cat_bytes = cat.encode('utf-8')
    hat = random.choice(hats)
    hat_bytes = hat.encode('utf-8')
    print('Publikowanie komunikatu: kot %s nosi %s' % (cat, hat))
    pub.send_multipart([cat_bytes, hat_bytes])
