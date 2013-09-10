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
    
    #修改接口ip多
    data=os.popen("curl -s http://nameip:50070/jmx > ./namedata.txt").readlines()
    f = file('namedata.txt')
    source=f.read().strip()
    ddata=json.JSONDecoder().decode(source)
    target=ddata['beans']
    
    int_FilesTotal = target[2]["FilesTotal"]
    int_BlocksTotal = target[2]["BlocksTotal"]
    int_CapacityTotalGB = target[2]["CapacityTotalGB"]
    int_CapacityUsedGB = target[2]["CapacityUsedGB"]
    float_NonDfsUsedSpaceGB = target[20]["NonDfsUsedSpace"]
    int_NonDfsUsedSpaceGB = float_NonDfsUsedSpaceGB/(1024*1024*1024)
    int_CapacityRemainingGB = target[2]["CapacityRemainingGB"]
    int_TotalLoadB = target[2]["TotalLoad"]
    str_hostName = target[2]["tag.hostName"]


    cursor.execute("insert into FSNamesystem (FilesTotal,BlocksTotal,CapacityTotalGB, \
    CapacityUsedGB,NonDfsUsedSpace,CapacityRemainingGB,TotalLoad,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_FilesTotal,int_BlocksTotal,int_CapacityTotalGB,int_CapacityUsedGB, \
    int_NonDfsUsedSpaceGB,int_CapacityRemainingGB,int_TotalLoadB,str_hostName))
    res = cursor.fetchall()
    
    float_memNonHeapUsedM = target[8]["memNonHeapUsedM"]
    float_memNonHeapCommittedM = target[8]["memNonHeapCommittedM"]
    
    float_memHeapUsedM = target[8]["memHeapUsedM"]
    float_memHeapCommittedM = target[8]["memHeapCommittedM"]
    
    int_gcCount = target[8]["gcCount"]
    int_gcTimeMillis = target[8]["gcTimeMillis"]
    
    int_threadsNew = target[8]["threadsNew"]
    int_threadsRunnable = target[8]["threadsRunnable"]
    
    int_threadsBlocked = target[8]["threadsBlocked"]
    int_threadsWaiting = target[8]["threadsWaiting"]
    
    int_threadsTimedWaiting = target[8]["threadsTimedWaiting"]
    int_threadsTerminated = target[8]["threadsTerminated"]
    
    
    cursor.execute("insert into NameNode_Jvm (memNonHeapUsedM,memNonHeapCommittedM,memHeapUsedM, \
    memHeapCommittedM,gcCount,gcTimeMillis,threadsNew,threadsRunnable,threadsBlocked,threadsWaiting, \
    threadsTimedWaiting,threadsTerminated,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(float_memNonHeapUsedM,float_memNonHeapCommittedM,float_memHeapUsedM,float_memHeapCommittedM, \
    int_gcCount,int_gcTimeMillis,int_threadsNew,int_threadsRunnable,int_threadsBlocked,int_threadsWaiting, \
    int_threadsTimedWaiting,int_threadsTerminated,str_hostName))
    res = cursor.fetchall()
    
    int_getFileInfo_num_ops = target[5]["getFileInfo_num_ops"]
    float_getFileInfo_avg_time = target[5]["getFileInfo_avg_time"]
    
    int_getListing_num_ops = target[5]["getListing_num_ops"]
    float_getListing_avg_time = target[5]["getListing_avg_time"]
    
    int_delete_num_ops = target[5]["delete_num_ops"]
    float_delete_avg_time = target[5]["delete_avg_time"]
    
    int_mkdirs_num_ops = target[5]["mkdirs_num_ops"]
    float_Rmkdirs_avg_time = target[5]["mkdirs_avg_time"]
    
    int_create_num_ops = target[5]["create_num_ops"]
    float_create_avg_time = target[5]["create_avg_time"]
    
    int_renewLease_num_ops = target[5]["renewLease_num_ops"]
    float_renewLease_avg_time = target[5]["renewLease_avg_time"]
    
    int_addBlock_num_ops = target[5]["addBlock_num_ops"]
    float_addBlock_avg_time = target[5]["addBlock_avg_time"]
    
    int_blockReceived_num_ops = target[5]["blockReceived_num_ops"]
    float_blockReceived_avg_time = target[5]["blockReceived_avg_time"]
    
    int_setSafeMode_num_ops = target[5]["setSafeMode_num_ops"]
    float_setSafeMode_avg_time = target[5]["setSafeMode_avg_time"]
    
    int_getBlockLocations_num_ops = target[5]["getBlockLocations_num_ops"]
    float_getBlockLocations_avg_time = target[5]["getBlockLocations_avg_time"]
    
    int_fsync_num_ops = target[5]["fsync_num_ops"]
    float_fsync_avg_time = target[5]["fsync_avg_time"]
    
    int_RpcQueueTime_num_ops = target[7]["RpcQueueTime_num_ops"]
    float_RpcQueueTime_avg_time = target[7]["RpcQueueTime_avg_time"]
    
    int_RpcProcessingTime_num_ops = target[7]["RpcProcessingTime_num_ops"]
    float_RpcProcessingTime_avg_time = target[7]["RpcProcessingTime_avg_time"]
    
    cursor.execute("insert into NameNode_RPC (getFileInfo_num_ops,getFileInfo_avg_time,getListing_num_ops,\
    getListing_avg_time,delete_num_ops,delete_avg_time,mkdirs_num_ops,mkdirs_avg_time,create_num_ops, \
    create_avg_time,renewLease_num_ops,renewLease_avg_time,addBlock_num_ops,addBlock_avg_time,blockReceived_num_ops, \
    blockReceived_avg_time,setSafeMode_num_ops,setSafeMode_avg_time,getBlockLocations_num_ops,getBlockLocations_avg_time, \
    fsync_num_ops,fsync_avg_time,RpcQueueTime_num_ops,RpcQueueTime_avg_time,RpcProcessingTime_num_ops,RpcProcessingTime_avg_time,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_getFileInfo_num_ops,float_getFileInfo_avg_time,int_getListing_num_ops,float_getListing_avg_time,int_delete_num_ops, \
    float_delete_avg_time,int_mkdirs_num_ops,float_Rmkdirs_avg_time,int_create_num_ops,float_create_avg_time, \
    int_renewLease_num_ops,float_renewLease_avg_time,int_addBlock_num_ops,float_addBlock_avg_time,int_blockReceived_num_ops, \
    float_blockReceived_avg_time,int_setSafeMode_num_ops,float_setSafeMode_avg_time,int_getBlockLocations_num_ops, \
    float_getBlockLocations_avg_time,int_fsync_num_ops,float_fsync_avg_time,int_RpcQueueTime_num_ops,float_RpcQueueTime_avg_time, \
    int_RpcProcessingTime_num_ops,float_RpcProcessingTime_avg_time,str_hostName))
    res = cursor.fetchall()
    
    int_FilesCreated = target[10]["FilesCreated"]
    int_FilesAppended = target[10]["FilesAppended"]
        
    int_GetBlockLocations = target[10]["GetBlockLocations"]
    int_FilesRenamed = target[10]["FilesRenamed"]
        
    int_GetListingOps = target[10]["GetListingOps"]
    int_CreateFileOps = target[10]["CreateFileOps"]
    
    int_FilesDeleted = target[10]["FilesDeleted"]
    int_DeleteFileOps = target[10]["DeleteFileOps"]
    
    int_FileInfoOps = target[10]["FileInfoOps"]
    int_AddBlockOps = target[10]["AddBlockOps"]
    
    int_Transactions_num_ops = target[10]["Transactions_num_ops"]
    float_Transactions_avg_time = target[10]["Transactions_avg_time"]
    
    int_Syncs_num_ops = target[10]["Syncs_num_ops"]
    float_Syncs_avg_time = target[10]["Syncs_avg_time"]
    
    int_JournalTransactionsBatchedInSync = target[10]["JournalTransactionsBatchedInSync"]
    
    int_blockReport_num_ops = target[10]["blockReport_num_ops"]
    float_blockReport_avg_time = target[10]["blockReport_avg_time"]
    
    int_fsImageLoadTime = target[10]["fsImageLoadTime"]
    int_FilesInGetListingOps = target[10]["FilesInGetListingOps"]

    cursor.execute("insert into NameNodeMetrics (FilesCreated,FilesAppended,GetBlockLocations,FilesRenamed,GetListingOps,CreateFileOps,\
    FilesDeleted,DeleteFileOps,FileInfoOps,AddBlockOps,Transactions_num_ops,Transactions_avg_time,Syncs_num_ops,Syncs_avg_time, \
    JournalTransactionsBatchedInSync,blockReport_num_ops,blockReport_avg_time,fsImageLoadTime,FilesInGetListingOps,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_FilesCreated,int_FilesAppended,int_GetBlockLocations,int_FilesRenamed,int_GetListingOps,int_CreateFileOps,int_FilesDeleted, \
    int_DeleteFileOps,int_FileInfoOps,int_AddBlockOps,int_Transactions_num_ops,float_Transactions_avg_time,int_Syncs_num_ops,
    float_Syncs_avg_time,int_JournalTransactionsBatchedInSync,int_blockReport_num_ops,float_blockReport_avg_time,int_fsImageLoadTime, \
    int_FilesInGetListingOps,str_hostName))
    res = cursor.fetchall()
    
    int_CorruptBlocks = target[2]["CorruptBlocks"]
    int_ExcessBlocks = target[2]["ExcessBlocks"]
    int_MissingBlocks = target[2]["MissingBlocks"]   
    int_UnderReplicatedBlocks = target[2]["UnderReplicatedBlocks"]      
    
    pre_DFS_PercentUsed = 100 - target[20]["PercentRemaining"]
    
    list_livenodes = target[20]["LiveNodes"]
    json_livenodes = json.loads(list_livenodes)
    int_LiveNodes = len(json_livenodes)
    
    list_DeadNodes = target[20]["DeadNodes"]
    json_DeadNodes = json.loads(list_DeadNodes)
    int_DeadNodes = len(json_DeadNodes)
    str_list_DeadNodesServer = json_DeadNodes.keys()
    
    if str_list_DeadNodesServer==[]:
        str_DeadNodesServer=""
    else:
        str_DeadNodesServer = ("".join(str(str_list_DeadNodesServer).split('\''))).strip('[]')
    
    cursor.execute("insert into NameNode_Warning (CorruptBlocks,ExcessBlocks,MissingBlocks,UnderReplicatedBlocks,DFS_PercentUsed, \
    LiveNodes,DeadNodes,DeadNodesServer,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,'%s','%s');" \
    %(int_CorruptBlocks,int_ExcessBlocks,int_MissingBlocks,int_UnderReplicatedBlocks,pre_DFS_PercentUsed,int_LiveNodes,int_DeadNodes,str_DeadNodesServer,str_hostName))
    res = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    
except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
