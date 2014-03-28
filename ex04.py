import os,sys
import json
import datetime
import time
import calendar
import pytz
from pprint import pprint
import dateutil.tz
#Y-m-d H:i:s ms tz 
#print datetime.timedelta(3600*8)

f='%Y-%m-%d %H:%M:%S %z'

"""
#datetime.datetime(2011, 8, 24, 13, 39, tzinfo=tzoffset(None, 28800))
print datetime.datetime.now()
print datetime.datetime.now(dateutil.tz.tzoffset("APPLE",3600*0))
dt=datetime.datetime.now(dateutil.tz.tzoffset("APPLE",3600*8))
#print dt.utcfromtimestamp()
print calendar.timegm(dt.utctimetuple())
"""
print "=============================="


dt=datetime.datetime(2014,1,1,0,0,0,tzinfo=dateutil.tz.tzoffset('GMT+8',3600*3))
print dt
print calendar.timegm(dt.utctimetuple())

#dt.astimezone(tz.tzoffset(3600*0))


#dt.astimezone(tzoffset(None, 3600))
