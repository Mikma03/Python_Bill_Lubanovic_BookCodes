import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Wątek %s: %s" % (threading.current_thread(), what))

if __name__ == "__main__":
    whoami("jestem głównym programem")
    for n in range(4):
        p = threading.Thread(target=do_this,
          args=("jestem funkcją %s" % n,))
        p.start()

