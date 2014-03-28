import time
import datetime
import re
import sys

balance="-$40,000.07"
#r=re.match(r"\$([\d\.]+)",balance)
balance=re.sub(r"[\$,]","",balance)
balance=float(balance)
if balance is not None:
    print balance
    #print r.group(0)
    #print r.group(1)
else:
    print "parse fail"

sys.exit()

r=re.sub(r'[$,]','','$228.16')
print r



