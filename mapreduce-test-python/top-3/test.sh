#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /top-3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /top-3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/top-3/mapper.py -mapper ../../mapreduce-test-python/top-3/mapper.py \
-file ../../mapreduce-test-python/top-3/reducer.py -reducer ../../mapreduce-test-python/top-3/reducer.py \
-input /top-3/input/* -output /top-3/output/
/usr/local/hadoop/bin/hdfs dfs -cat /top-3/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /top-3/output/
../../stop.sh
