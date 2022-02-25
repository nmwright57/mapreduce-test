#!/usr/bin/python
from operator import itemgetter
import sys


for line in sys.stdin: 
  line = line.strip()
  hour_ip, count = line   
  hour, ip, count = line.split(' ')
  print '%s\t%s' % ('['+hour+']' +ip, count)
