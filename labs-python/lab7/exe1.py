import time
import random
import sys

def wait(x):
    time.sleep(x)

def time_cron():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    while(1):
        time_interval = random.uniform(a,b)
        # measure process time
        t0 = time.clock()
        wait(time_interval)
        print time.clock() - t0, "seconds process time"
        
        # measure wall time
        t0 = time.time()
        wait(time_interval)
        print time.time() - t0, "seconds wall time"

time_cron()
