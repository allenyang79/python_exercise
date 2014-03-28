import os,sys
print "GO TMP 2"
import json

o={
		"a":"AAA",
		"b":"BBB"
}

print "fix by MASTER"

print "fix by MASTER2"
print "fix by TMP"
print o
print o["a"]

print "fix by MASTER"

print o.get("a","AAAA")
print o.get("c","CCCC")
print o["c"]

print "FIX BY TMP"
