import time
import win32api
import requests
from datetime import datetime, timedelta
serversidekey = "REDACTED"
dak = 0
pdat = datetime.now()
lastPostTime = datetime.now() - timedelta(minutes=30)
prevstatus = "active"
while True:
    dat = datetime.now()
    mak = win32api.GetLastInputInfo()
    print(f"MASTER: ||||| {prevstatus} ||||||")
#    if dak is not mak:
    if dak == mak:
        if dat - pdat >  timedelta(minutes=10):
            print("idle")
            if dat - lastPostTime > timedelta(minutes=20) or prevstatus == "active":
                stri = "POST IDLE"
                print(f"\033[95m{stri}\033[0m")
                requests.post("https://2.hy.pr/activity/mon", json={"lastActivity":dat.strftime("%Y-%m-%d %H:%M:%S"),"status":"idle"}, headers={'Auth':serversidekey})
                lastPostTime = datetime.now()
            prevstatus = "idle"
            time.sleep(1)
            continue
        else: print("active1")
    else:
        dak = mak
        pdat=dat

        print("active2")

        if dat - lastPostTime > timedelta(minutes=10) or prevstatus == "idle":
            stri = "POST ACTIVE"
            print(f"\033[95m{stri}\033[0m")
            requests.post("https://2.hy.pr/activity/mon", json={"lastActivity":dat.strftime("%Y-%m-%d %H:%M:%S"),"status":"active"}, headers={'Auth':serversidekey})
            lastPostTime = datetime.now()
        prevstatus = "active"
    time.sleep(1)
