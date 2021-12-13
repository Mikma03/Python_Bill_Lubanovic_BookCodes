from invoke import task
@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Bieżący czas:", timestr)
