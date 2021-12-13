from concurrent import futures
import math
import time
import sys

def calc(val):
    time.sleep(1)
    result = math.sqrt(float(val))
    return result

def use_threads(num, values):
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as tex:
        results = tex.map(calc, values)
    t2 = time.time()
    return t2 - t1

def use_processes(num, values):
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as pex:
        results = pex.map(calc, values)
    t2 = time.time()
    return t2 - t1

def main(workers, values):
    print(f"Liczba wywołań: {workers}, liczba wartości: {len(values)}")
    t_sec = use_threads(workers, values)
    print(f"Czas realizacji za pomocą wątków: {t_sec:.4f} s")
    p_sec = use_processes(workers, values)
    print(f"Czas realizacji za pomocą procesów: {p_sec:.4f} s")

if __name__ == '__main__':
    workers = int(sys.argv[1])
    values = list(range(1, 6)) # 1 .. 5
    main(workers, values)
