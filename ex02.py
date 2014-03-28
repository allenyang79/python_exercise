import time
import datetime
import re



r=re.sub(r'[$,]','','$228.16')
print r



t=time.time()
print datetime.datetime.fromtimestamp(t).strftime('%m/%d/%Y')

print "=====GOGO================="
now=time.time()
today= datetime.date.today()
today= today.strftime('%m/%d/%Y')
print today

yesterday = datetime.date.today() - datetime.timedelta(1)
yesterday= yesterday.strftime('%m/%d/%Y')
print yesterday


print "==={}===".format("ZZZZ")


o={}
if o.get('data') is None:
    o['data']={"total":None,"rows":{}}

o['data']['rows']['aa']="BBB"
print o
