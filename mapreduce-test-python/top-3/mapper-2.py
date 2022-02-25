#!/usr/bin/python
from operator import itemgetter
import sys

dict_hour_ip_count = {}

for line in sys.stdin: 
  line = line.strip()
  hour_ip, count = line
  hour,ip = line.split('\t')
  
  try:
    hour = int(hour)
    count = int(count)
    dict_hour_ip_count[hour].append([ip,count])
   
 except ValueError:
    pass
    
    
 for hour, ip_count in dict_hour_ip_count.items():
    top3 = sorted(list(ip_count), key = lambda x:x[1], reverse=True)[0:3]
    for ip, count in top3:
        print ('%s\t%s' % ('['+hour+']' +ip, count))
