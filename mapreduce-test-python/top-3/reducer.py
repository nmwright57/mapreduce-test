#!/usr/bin/python
from operator import itemgetter
#from collections import defaultdict
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    hour_ip, num = line.split('\t')

    try:
        num = int(num)
        dict_ip_count[hour_ip] = dict_ip_count.get(hour_ip, 0) + num

    except ValueError:
        pass



dict_hour_count = {}


for hour_ip, count in dict_ip_count.items():
        hour = hour_ip[1:6]
        ip = hour_ip[7:]
        count = int(count)

        if hour not in dict_hour_count.keys():
            dict_hour_count[hour] = [(ip,count)]

        else:
            dict_hour_count[hour].append((ip, count))



for hour, ip_count in dict_hour_count.items():
    top3 = sorted(list(ip_count), key = lambda x:x[1], reverse=True)[0:3]
    print(hour,top3)
