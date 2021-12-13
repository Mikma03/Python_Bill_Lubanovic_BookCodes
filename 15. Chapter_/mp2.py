import multiprocessing
import time
import os

def whoami(name):
    print("Jestem %s, proces %s" % (name, os.getpid()))
    
def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tObieg %s z %s." % (num, stop))
        time.sleep(1)
        
if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
