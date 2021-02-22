import time
import config

def fail(msg=None):
    end = '->\n' if msg else ''
    print(time.ctime(), end=end)
    print(msg or '')
    time.sleep(config.debug.time_fail)

def succesful(msg=None):
    if msg:
        print(msg)
    time.sleep(config.debug.time_succesful)

