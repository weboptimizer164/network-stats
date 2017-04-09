
import time
import datetime
import psutil
import json

def calc_ul_dl():
    t0 = time.time()
    counter = psutil.net_io_counters()
    tot = (counter.bytes_sent, counter.bytes_recv)

    # while True:
    last_tot = tot
    time.sleep(1)
    counter = psutil.net_io_counters()
    # t1 = time.time()
    tot = (counter.bytes_sent, counter.bytes_recv)
    ul, dl = [(now - last) / 1000.0
              for now, last in zip(tot, last_tot)]
    # rate.append((ul, dl))
    # t0 = time.time()
    date, time1 = str(datetime.datetime.now()).split()
    s1 = {"Download Speed": str(dl)+"KBps", "Upload Speed": str(ul)+"KBps", "Time": str(time1[:8])}
    s1 = json.dumps(s1)
    return s1
