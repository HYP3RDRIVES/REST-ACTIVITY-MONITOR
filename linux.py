import time
import requests
import subprocess
from datetime import datetime, timedelta
serversidekey = "REDACTED"

while True:
    dat = datetime.now()
    try:
        result = subprocess.run("xprintidle", shell=True, check=True, stdout=subprocess.PIPE)
        if result.returncode != 0: print("an error occured")
        result=result.stdout.decode("utf-8")
        if int(result) > 600000: requests.post("https://hy.pr/activity/mon", json={"lastActivity":dat.strftime("%Y-%m-%d %H:%M:%S"),"status":"idle"}, headers={'Auth':serversidekey})
        else: requests.post("https://hy.pr/activity/mon", json={"lastActivity":dat.strftime("%Y-%m-%d %H:%M:%S"),"status":"active"}, headers={'Auth':serversidekey})
    except: print("an error occured")
    time.sleep(1)

