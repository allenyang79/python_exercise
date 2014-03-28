import itertools

c={}
c['aa']="AAA"
c['bb']="BBB"
for i,obj in c:
    print i
    print obj
    print "===="




#print itertools.count(10)
#print itertools.count(2.5,0.5)
"""
for i in itertools.chain([1,2,3,],['a','b','c'],['q1','q2','q3']):
    print i


for i in itertools.count(2.5,0.5):
    print i
    if i > 100:
        break
"""
for i in itertools.compress('ABCDEF', [1,0,1,0,1,1]):
    print i
