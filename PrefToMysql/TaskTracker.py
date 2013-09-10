#! /usr/bin/env python
#coding=utf-8
#by kasim&Mango 20130910
import MySQLdb
import os
import time
import simplejson as json

try:    
    #修改mysql连接信息    
    conn = MySQLdb.connect(host="ip", \
            user="user", \
            passwd="pwd", \
            db="HadoopPref")
    global cursor
    cursor = conn.cursor()

    #修改接口ip多个task必须指定不同的文件名
    data=os.popen("curl -s http://taskip:50060/jmx > ./taskdata.txt").readlines()
    f = file('taskdata.txt')
    source=f.read().strip()
    ddata=json.JSONDecoder().decode(source)
    target=ddata['beans']
    
    float_memNonHeapUsedM = target[19]["memNonHeapUsedM"]
    float_memNonHeapCommittedM = target[19]["memNonHeapCommittedM"]
    
    float_memHeapUsedM = target[19]["memHeapUsedM"]
    float_memHeapCommittedM = target[19]["memHeapCommittedM"]
    
    int_gcCount = target[19]["gcCount"]
    int_gcTimeMillis = target[19]["gcTimeMillis"]
    
    int_threadsNew = target[19]["threadsNew"]
    int_threadsRunnable = target[19]["threadsRunnable"]
    
    int_threadsBlocked = target[19]["threadsBlocked"]
    int_threadsWaiting = target[19]["threadsWaiting"]
    
    int_threadsTimedWaiting = target[19]["threadsTimedWaiting"]
    int_threadsTerminated = target[19]["threadsTerminated"]
    
    str_hostName = target[19]["tag.hostName"]
    
    cursor.execute("insert into TaskTracker_Jvm (memNonHeapUsedM,memNonHeapCommittedM,memHeapUsedM,memHeapCommittedM,gcCount,gcTimeMillis, \
    threadsNew,threadsRunnable,threadsBlocked,threadsWaiting,threadsTimedWaiting,threadsTerminated,hostname) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(float_memNonHeapUsedM,float_memNonHeapCommittedM,float_memHeapUsedM,float_memHeapCommittedM,int_gcCount,int_gcTimeMillis, \
    int_threadsNew,int_threadsRunnable,int_threadsBlocked,int_threadsWaiting,int_threadsTimedWaiting,int_threadsTerminated,str_hostName))
    res = cursor.fetchall()
    
    int_RpcQueueTime_num_ops = target[7]["RpcQueueTime_num_ops"]
    float_RpcQueueTime_avg_time = target[7]["RpcQueueTime_avg_time"]
    
    int_RpcProcessingTime_num_ops = target[7]["RpcProcessingTime_num_ops"]
    float_RpcProcessingTime_avg_time = target[7]["RpcProcessingTime_avg_time"]
    
    int_getTask_num_ops = target[8]["getTask_num_ops"]
    float_getTask_avg_time = target[8]["getTask_avg_time"]
    
    int_getMapCompletionEvents_num_ops = target[8]["getMapCompletionEvents_num_ops"]
    float_getMapCompletionEvents_avg_time = target[8]["getMapCompletionEvents_avg_time"]
    
    int_commitPending_num_ops = target[8]["commitPending_num_ops"]
    float_commitPending_avg_time = target[8]["commitPending_avg_time"]
    
    int_ThreadCount = target[15]["ThreadCount"]
    
    int_tasks_completed = target[17]["tasks_completed"]
    int_tasks_failed_timeout = target[17]["tasks_failed_timeout"]
    int_tasks_failed_ping = target[17]["tasks_failed_ping"]
    str_hostname = target[17]["tag.hostName"]
    
    cursor.execute("insert into TaskTrackerMetrics (RpcQueueTime_num_ops,RpcQueueTime_avg_time,RpcProcessingTime_num_ops,RpcProcessingTime_avg_time, \
    getTask_num_ops,getTask_avg_time,getMapCompletionEvents_num_ops,getMapCompletionEvents_avg_time,commitPending_num_ops,commitPending_avg_time, \
    ThreadCount,tasks_completed,tasks_failed_timeout,tasks_failed_ping,hostname) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_RpcQueueTime_num_ops,float_RpcQueueTime_avg_time,int_RpcProcessingTime_num_ops,float_RpcProcessingTime_avg_time,int_getTask_num_ops,float_getTask_avg_time, \
    int_getMapCompletionEvents_num_ops,float_getMapCompletionEvents_avg_time,int_commitPending_num_ops,float_commitPending_avg_time,int_ThreadCount,int_tasks_completed, \
    int_tasks_failed_timeout,int_tasks_failed_ping,str_hostname))
    res = cursor.fetchall()
    
    
    conn.commit()
    cursor.close()
    conn.close()
        
except MySQLdb.Error,e:
       print "Mysql Error %d: %s" % (e.args[0], e.args[1])