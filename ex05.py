import os,sys
import json
import datetime
import time
import calendar
import arrow
#Y-m-d H:i:s ms tz 
#print datetime.timedelta(3600*8)


print arrow.utcnow()

print "==GMT+08:00 now==="
dt1=arrow.get().to("+08:00").floor('hour')
dt2=arrow.get().to("+08:00").floor('day')
print "{},{}".format(dt1,dt1.timestamp)
print "{},{}".format(dt2,dt2.timestamp)

print "======"
f='YYYY-MM-DD HH:mm:ssZZ'
print arrow.get("2014-01-13T00:00:00+08:00")
print arrow.get("2014-01-13 00:00:00+08:00",f)



###
print "======"
dt1=arrow.get('2014-02-12 00:00:00+08:00',f)
dt2=arrow.get('2014-02-11 16:00:00+00:00',f)
dt3=arrow.get("2014-02-11T16:00:00Z")
dt4=arrow.get(2014,02,12)

print dt1
print dt2
print dt3
print dt4

print "======"
print dt1.timestamp
print dt2.timestamp
print dt3.timestamp

print "======"
print dt1.datetime.timetuple()
print dt2.datetime.timetuple()

print "======"
print int(time.mktime(dt1.datetime.timetuple()))
print int(time.mktime(dt2.datetime.timetuple()))

print "====="
print dt1.datetime.utctimetuple()
print dt2.datetime.utctimetuple()

print "======"
print int(time.mktime(dt1.datetime.utctimetuple()))
print int(time.mktime(dt2.datetime.utctimetuple()))


       



