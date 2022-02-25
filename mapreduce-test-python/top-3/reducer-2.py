#!/usr/bin/python
from operator import itemgetter
import sys


for line in sys.stdin: 
  line = line.strip().split('\t')
  hour, ip, count = line
  hour,ip = line.split('\t')    
  print '%s\t%s' % ('['+hour+']' +ip, count)
