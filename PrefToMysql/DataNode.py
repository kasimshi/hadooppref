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
    
    #修改接口ip,多个data必须指定不同的文件名
    data=os.popen("curl -s http://datanode:50075/jmx > ./datanode.txt").readlines()
    f = file('datanode.txt')
    source=f.read().strip()
    ddata=json.JSONDecoder().decode(source)
    target=ddata['beans']
    
    float_memNonHeapUsedM = target[18]["memNonHeapUsedM"]
    float_memNonHeapCommittedM = target[18]["memNonHeapCommittedM"]
    
    float_memHeapUsedM = target[18]["memHeapUsedM"]
    float_memHeapCommittedM = target[18]["memHeapCommittedM"]
    
    int_gcCount = target[18]["gcCount"]
    int_gcTimeMillis = target[18]["gcTimeMillis"]
    
    int_threadsNew = target[18]["threadsNew"]
    int_threadsRunnable = target[18]["threadsRunnable"]
    
    int_threadsBlocked = target[18]["threadsBlocked"]
    int_threadsWaiting = target[18]["threadsWaiting"]
    
    int_threadsTimedWaiting = target[18]["threadsTimedWaiting"]
    int_threadsTerminated = target[18]["threadsTerminated"]
    
    str_hostName = target[18]["tag.hostName"]
    
    cursor.execute("insert into DataNode_Jvm (memNonHeapUsedM,memNonHeapCommittedM,memHeapUsedM,memHeapCommittedM,gcCount,gcTimeMillis, \
    threadsNew,threadsRunnable,threadsBlocked,threadsWaiting,threadsTimedWaiting,threadsTerminated,hostname) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(float_memNonHeapUsedM,float_memNonHeapCommittedM,float_memHeapUsedM,float_memHeapCommittedM,int_gcCount,int_gcTimeMillis, \
    int_threadsNew,int_threadsRunnable,int_threadsBlocked,int_threadsWaiting,int_threadsTimedWaiting,int_threadsTerminated,str_hostName))
    res = cursor.fetchall()
    
    float_G_written = float(target[5]["bytes_written"])/(1024*1024*1024)
    float_G_read = float(target[5]["bytes_read"])/(1024*1024*1024)
    
    int_blocks_written = target[5]["blocks_written"]
    int_blocks_read = target[5]["blocks_read"]
    
    int_blocks_replicated = target[5]["blocks_replicated"]
    int_bblocks_removed = target[5]["blocks_removed"]

    int_blocks_verified = target[5]["blocks_verified"]
    int_block_verification_failures = target[5]["block_verification_failures"]
    
    int_blocks_get_local_pathinfo = target[5]["blocks_get_local_pathinfo"]
    
    int_reads_from_local_client = target[5]["reads_from_local_client"]
    int_reads_from_remote_client = target[5]["reads_from_remote_client"]
    
    int_writes_from_local_client = target[5]["writes_from_local_client"]
    int_writes_from_remote_client = target[5]["writes_from_remote_client"]
    
    int_readBlockOp_num_ops = target[5]["readBlockOp_num_ops"]
    float_readBlockOp_avg_time = target[5]["readBlockOp_avg_time"]
    
    int_writeBlockOp_num_ops = target[5]["writeBlockOp_num_ops"]
    float_writeBlockOp_avg_time = target[5]["writeBlockOp_avg_time"]
    
    int_ThreadCount = target[15]["ThreadCount"]
    str_hostName = target[5]["tag.hostName"]
    
    cursor.execute("insert into DataNodeMetrics (G_written,G_read,blocks_written,blocks_read,blocks_replicated,blocks_removed, \
    blocks_verified,block_verification_failures,blocks_get_local_pathinfo,reads_from_local_client,reads_from_remote_client, \
    writes_from_local_client,writes_from_remote_client,readBlockOp_num_ops,readBlockOp_avg_time,writeBlockOp_num_ops, \
    writeBlockOp_avg_time,ThreadCount,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(float_G_written,float_G_read,int_blocks_written,int_blocks_read,int_blocks_replicated,int_bblocks_removed,int_blocks_verified, \
    int_block_verification_failures,int_blocks_get_local_pathinfo,int_reads_from_local_client,int_reads_from_remote_client, \
    int_writes_from_local_client,int_writes_from_remote_client,int_readBlockOp_num_ops,float_readBlockOp_avg_time,int_writeBlockOp_num_ops, \
    float_writeBlockOp_avg_time,int_ThreadCount,str_hostName))
    res = cursor.fetchall()
    
    
    conn.commit()
    cursor.close()
    conn.close()
        
except MySQLdb.Error,e:
       print "Mysql Error %d: %s" % (e.args[0], e.args[1])
