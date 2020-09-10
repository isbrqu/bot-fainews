import time
from decouple import config

def fail(msg=None):
    end = '->\n' if msg else ''
    print(time.ctime(), end=end)
    print(msg or '')
    time.sleep(config('TIME_SLEEP_FAIL', cast=int))

def succesful(msg=None):
    if msg:
        print(msg)
    time.sleep(config('TIME_SLEEP', cast=int))

