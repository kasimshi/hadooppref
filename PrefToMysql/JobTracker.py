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
    
    #修改接口ip
    data=os.popen("curl -s http://jobip:50030/jmx > ./jobdata.txt").readlines()
    f = file('jobdata.txt')
    source=f.read().strip()
    ddata=json.JSONDecoder().decode(source)
    target=ddata['beans']
    
    int_RpcQueueTime_num_ops = target[3]["RpcQueueTime_num_ops"]
    float_RpcQueueTime_avg_time = target[3]["RpcQueueTime_avg_time"]
    
    int_RpcProcessingTime_num_ops = target[3]["RpcProcessingTime_num_ops"]
    float_RpcProcessingTime_avg_time = target[3]["RpcProcessingTime_avg_time"]

    int_getSystemDir_num_ops = target[8]["getSystemDir_num_ops"]
    float_getSystemDir_avg_time = target[8]["getSystemDir_avg_time"]
    
    int_getStagingAreaDir_num_ops = target[8]["getStagingAreaDir_num_ops"]
    float_getStagingAreaDir_avg_time = target[8]["getStagingAreaDir_avg_time"]
    
    int_getNewJobId_num_ops = target[8]["getNewJobId_num_ops"]
    float_getNewJobId_avg_time = target[8]["getNewJobId_avg_time"]
    
    int_submitJob_num_ops = target[8]["submitJob_num_ops"]
    float_submitJob_avg_time = target[8]["submitJob_avg_time"]
    
    int_getJobStatus_num_ops = target[8]["getJobStatus_num_ops"]
    float_getJobStatus_avg_time = target[8]["getJobStatus_avg_time"]
    
    int_getTaskCompletionEvents_num_ops = target[8]["getTaskCompletionEvents_num_ops"]
    float_getTaskCompletionEvents_avg_time = target[8]["getTaskCompletionEvents_avg_time"]
    
    #int_getTaskDiagnostics_num_ops = target[8]["getTaskDiagnostics_num_ops"]
    #float_getTaskDiagnostics_avg_time = target[8]["getTaskDiagnostics_avg_time"]
    
    int_getJobCounters_num_ops = target[8]["getJobCounters_num_ops"]
    float_getJobCounters_avg_time = target[8]["getJobCounters_avg_time"]
    
    #int_killJob_num_ops = target[8]["killJob_num_ops"]
    #float_killJob_avg_time = target[8]["killJob_avg_time"]
    
    str_hostName = target[8]["tag.hostName"]
    

    cursor.execute("insert into JobTracker_RPC (RpcQueueTime_num_ops,RpcQueueTime_avg_time,RpcProcessingTime_num_ops, \
    RpcProcessingTime_avg_time,getSystemDir_num_ops,getSystemDir_avg_time,getStagingAreaDir_num_ops,getStagingAreaDir_avg_time, \
    getNewJobId_num_ops,getNewJobId_avg_time,submitJob_num_ops,submitJob_avg_time,getJobStatus_num_ops,getJobStatus_avg_time, \
    getTaskCompletionEvents_num_ops,getTaskCompletionEvents_avg_time,getJobCounters_num_ops,getJobCounters_avg_time,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_RpcQueueTime_num_ops,float_RpcQueueTime_avg_time,int_RpcProcessingTime_num_ops,float_RpcProcessingTime_avg_time, \
    int_getSystemDir_num_ops,float_getSystemDir_avg_time,int_getStagingAreaDir_num_ops,float_getStagingAreaDir_avg_time,\
    int_getNewJobId_num_ops,float_getNewJobId_avg_time,int_submitJob_num_ops,float_submitJob_avg_time,\
    int_getJobStatus_num_ops,float_getJobStatus_avg_time,int_getTaskCompletionEvents_num_ops,float_getTaskCompletionEvents_avg_time,\
    int_getJobCounters_num_ops,float_getJobCounters_avg_time,str_hostName))
    res = cursor.fetchall()

    float_memNonHeapUsedM = target[17]["memNonHeapUsedM"]
    float_memNonHeapCommittedM = target[17]["memNonHeapCommittedM"]
    
    float_memHeapUsedM = target[17]["memHeapUsedM"]
    float_memHeapCommittedM = target[17]["memHeapCommittedM"]
    
    int_gcCount = target[17]["gcCount"]
    int_gcTimeMillis = target[17]["gcTimeMillis"]
    
    int_ThreadCount = target[16]["ThreadCount"]
    int_threadsNew = target[17]["threadsNew"]
    
    int_threadsRunnable = target[17]["threadsRunnable"]
    int_threadsBlocked = target[17]["threadsBlocked"]
    
    int_threadsWaiting = target[17]["threadsWaiting"]
    int_threadsTimedWaiting = target[17]["threadsTimedWaiting"]
    int_threadsTerminated = target[17]["threadsTerminated"]
    
    cursor.execute("insert into JobTracker_Jvm (memNonHeapUsedM,memNonHeapCommittedM,memHeapUsedM,memHeapCommittedM,gcCount,gcTimeMillis,ThreadCount,threadsNew,\
    threadsRunnable,threadsBlocked,threadsWaiting,threadsTimedWaiting,threadsTerminated,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(float_memNonHeapUsedM,float_memNonHeapCommittedM,float_memHeapUsedM,float_memHeapCommittedM,int_gcCount,int_gcTimeMillis,int_ThreadCount,int_threadsNew,\
    int_threadsRunnable,int_threadsBlocked,int_threadsWaiting,int_threadsTimedWaiting,int_threadsTerminated,str_hostName))
    res = cursor.fetchall()    

    str_SummaryJson = target[5]["SummaryJson"]
    json_SummaryJson = json.loads(str_SummaryJson)
    
    int_nodes = json_SummaryJson["nodes"]
    int_alive = json_SummaryJson["alive"]
    int_deadnodes = int_nodes - int_alive
    
    int_reduce_slots = json_SummaryJson["slots"]["reduce_slots"]
    int_reduce_slots_used = json_SummaryJson["slots"]["reduce_slots_used"]
    per_reduce_slots_used = float(int_reduce_slots_used)*100/int_reduce_slots
    
    int_map_slots = json_SummaryJson["slots"]["map_slots"]
    int_map_slots_used = json_SummaryJson["slots"]["map_slots_used"]
    per_map_slots_used = float(int_map_slots_used)*100/int_map_slots


    cursor.execute("insert into JobTracker_Warning (nodes,alive,deadnodes,map_slots_used,per_map_slots_used,reduce_slots_used,per_reduce_slots_used,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_nodes,int_alive,int_deadnodes,int_map_slots_used,per_map_slots_used,int_reduce_slots_used,per_reduce_slots_used,str_hostName))
    res = cursor.fetchall()
    
    int_map_slots = target[12]["map_slots"]
    int_reduce_slots = target[12]["reduce_slots"]
    
    int_maps_launched = target[12]["maps_launched"]
    int_maps_completed = target[12]["maps_completed"]
    int_maps_failed = target[12]["maps_failed"]
    
    int_reduces_launched = target[12]["reduces_launched"]
    int_reduces_completed = target[12]["reduces_completed"]
    int_reduces_failed = target[12]["reduces_failed"]
    
    int_jobs_submitted = target[12]["jobs_submitted"]
    int_jobs_completed = target[12]["jobs_completed"]
    
    int_waiting_maps = target[12]["waiting_maps"]
    int_waiting_reduces = target[12]["waiting_reduces"]
    
    int_jobs_failed = target[12]["jobs_failed"]
    int_jobs_killed = target[12]["jobs_killed"]
    
    cursor.execute("insert into JobTrackerMetrics (map_slots,reduce_slots,maps_launched,maps_completed,maps_failed,reduces_launched, \
    reduces_completed,reduces_failed,jobs_submitted,jobs_completed,waiting_maps,waiting_reduces,jobs_failed,jobs_killed,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_map_slots,int_reduce_slots,int_maps_launched,int_maps_completed,int_maps_failed,int_reduces_launched,int_reduces_completed, \
    int_reduces_failed,int_jobs_submitted,int_jobs_completed,int_waiting_maps,int_waiting_reduces,int_jobs_failed,int_jobs_killed,str_hostName))
    res = cursor.fetchall()
    
    
    conn.commit()
    cursor.close()
    conn.close()
    
except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
