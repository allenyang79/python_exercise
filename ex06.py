import os,sys
import json
import datetime
import time
import calendar
import arrow
import os
#Y-m-d H:i:s ms tz 
#print datetime.timedelta(3600*8)

#print result
html=""
for line in open("test.html"):
    html+=line
#print html


import slimmer

html=slimmer.js_slimmer(html)
html=slimmer.html_slimmer(html)
print html



