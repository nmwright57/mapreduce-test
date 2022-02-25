#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /top-3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /top-3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/top-3/mapper1.py -mapper ../../mapreduce-test-python/top-3/mapper1.py \
-file ../../mapreduce-test-python/top-3/reducer1.py -reducer ../../mapreduce-test-python/top-3/reducer1.py \
-input /top-3/input/* -output /top-3/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/top-3/mapper-2.py -mapper ../../mapreduce-test-python/top-3/mapper-2.py \
-file ../../mapreduce-test-python/top-3/reducer-2.py -reducer ../../mapreduce-test-python/top-3/reducer-2.py \
-input /top-3/output/* -output /top-3-2/output/





/usr/local/hadoop/bin/hdfs dfs -cat /top-3-2/output/part-00000 | tail -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3-2/output/
../../stop.sh
