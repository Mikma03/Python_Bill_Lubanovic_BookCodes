import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print('Myję talerz na', dish)
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Wycieram talerz na', dish)
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishes = ['sałatkę', 'pieczywo', 'danie główne', 'deser']
washer(dishes, dish_queue)
dish_queue.join()
