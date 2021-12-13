import multiprocessing
import os
def whoami(what):
    print("Proces %s: %s" % (os.getpid(), what))

if __name__ == "__main__":
    whoami("jestem głównym programem")
    for n in range(4):
        p = multiprocessing.Process(target=whoami,
          args=("jestem funkcją %s" % n,))
        p.start()
