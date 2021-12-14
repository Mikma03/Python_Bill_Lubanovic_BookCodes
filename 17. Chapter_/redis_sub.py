import redis

conn = redis.Redis()
topics = ['maine coon', 'persian']
sub = conn.pubsub()
sub.subscribe(topics)
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subskrypcja komunikatu: kod %s nosi %s' % (cat, hat))
