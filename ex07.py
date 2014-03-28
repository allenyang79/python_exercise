import os,sys
import json
import datetime
import time
import calendar
import arrow
import os
#Y-m-d H:i:s ms tz 
#print datetime.timedelta(3600*8)
import signal
import random

def long_function_call():
    n=0
    while(True):
        #donothing
        n+=1
        print "walking:{}".format(n)
        r=random.random()
        if r < 0.0000005:
            o=9/0
            print o
        if r < 0.00002:
            print "Done"
            break

class TimeoutException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "TIMEOUT:{}!!".format(self.value)
        #repr(self.value)

def signal_handler(signum, frame):
    print signum
    raise TimeoutException(1)


signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(1)   # Ten seconds
try:
    long_function_call()
except TimeoutException as ext:
    print ext
