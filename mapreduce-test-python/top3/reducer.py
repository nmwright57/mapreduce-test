
   
#!/usr/bin/python
from operator import itemgetter
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


dict_hour_ip = {}

for hour_ip, count in dict_ip_count.items():
  hour = hour_ip[1:6]
        ip = hour_ip[7:]
        count = int(count)
        if hour not in dict_hour_ip.keys():
            dict_hour_ip[hour] = [(ip,count)]
        else:
            dict_hour_ip[hour].append((ip, count))

for hour, ip_count in dict_hour_ip.items():
    top_3_ip = sorted(list(ip_count), key = lambda x:x[1], reverse=True)[0:3]
    print(hour,"top 3 ip", top_3_ip)
    for ip, count in top_3_ip:
        print ('%s\t%s' % ('['+hour+']' +ip, count))

sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
for ip, count in sorted_dict_ip_count:
    print '%s\t%s' % (hour,ip, count)
