import time
import win32api
import requests
from datetime import datetime, timedelta
serversidekey = "oAayX9wXdv7RDs425pXXc8zTa9TqHqWKOQcs0qZKmFGwpomqmL87rLSSu81By2gZ"
dak = 0
pdat = datetime.now()
while True:
    dat = datetime.now()
    mak = win32api.GetLastInputInfo()
    print(mak)
    print(dak)
    print(dat)
    print(pdat)

    print(dat-pdat)
    print(timedelta(seconds=5))
#    if dak is not mak:
    print(f"{dak} {mak}")
    if dak == mak:
        print("yeah")
        if dat - pdat >  timedelta(seconds=5): print("idle")
#        requests.post("https://2.hy.pr/activity/mon", json={"lastActivity":dat.strftime(),"status":"idle"} headers={'Auth':serversidekey})
        else: print("active1")
    else:
        dak = mak
        pdat=dat
        print("active2")


    time.sleep(1)
