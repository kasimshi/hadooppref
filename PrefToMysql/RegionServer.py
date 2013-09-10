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
    
    #修改接口ip多个reg必须指定不同的文件名
    data=os.popen("curl -s http://regip:60030/jmx > ./regiondata.txt").readlines()
    f = file('regiondata.txt')
    source=f.read().strip()
    ddata=json.JSONDecoder().decode(source)
    target=ddata['beans']
    
    int_ThreadCount = target[8]["ThreadCount"]
    
    float_totalStaticIndexSizeM = float(target[15]["totalStaticIndexSizeKB"])/1024
    
    float_blockCacheFree = float(target[15]["blockCacheFree"])/(1024*1024)
    
    int_memstoreSizeMB= target[15]["memstoreSizeMB"]
    
    int_blockCacheCount = target[15]["blockCacheCount"]
    
    int_blockCacheHitRatio = target[15]["blockCacheHitRatio"]
    
    int_blockCacheHitCachingRatio = target[15]["blockCacheHitCachingRatio"]
    
    int_blockCacheHitCount = target[15]["blockCacheHitCount"]
    
    int_hdfsBlocksLocalityIndex = target[15]["hdfsBlocksLocalityIndex"]
    
    int_writeRequestsCount = target[15]["writeRequestsCount"]
    
    int_compactionTimeMinTime = target[15]["compactionTimeMinTime"]
    
    int_compactionTimeMaxTime = target[15]["compactionTimeMaxTime"]
    
    float_blockCacheSizeM = float(target[15]["blockCacheSize"])/(1024*1024)
    
    int_readRequestsCount = target[15]["readRequestsCount"]
    
    float_rootIndexSize = target[15]["rootIndexSizeKB"]
    
    int_blockCacheMissCount = target[15]["blockCacheMissCount"]
    
    int_blockCacheHitRatioPastNPeriods = target[15]["blockCacheHitRatioPastNPeriods"]
    
    int_blockCacheHitCachingRatioPastNPeriods = target[15]["blockCacheHitCachingRatioPastNPeriods"]
    
    int_storefiles = target[15]["storefiles"]
    
    int_blockCacheEvictedCount = target[15]["blockCacheEvictedCount"]
    
    int_stores = target[15]["stores"]
    
    int_requests = round(target[15]["requests"])
    
    list_hostName = str(target[5]["Name"]).split('@')
    str_hostName = list_hostName[1]
    

    
    cursor.execute("insert into RegionServerMetrics (ThreadCount,totalStaticIndexSizeM,blockCacheFree,memstoreSizeMB,blockCacheCount,blockCacheHitRatio, \
    blockCacheHitCachingRatio,blockCacheHitCount,hdfsBlocksLocalityIndex,writeRequestsCount,compactionTimeMinTime,compactionTimeMaxTime,blockCacheSizeM, \
    readRequestsCount,rootIndexSizeKB,blockCacheMissCount,blockCacheHitRatioPastNPeriods,blockCacheHitCachingRatioPastNPeriods,storefiles,blockCacheEvictedCount, \
    stores,requests,hostName) \
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
    %(int_ThreadCount,float_totalStaticIndexSizeM,float_blockCacheFree,int_memstoreSizeMB,int_blockCacheCount,int_blockCacheHitRatio,int_blockCacheHitCachingRatio,\
    int_blockCacheHitCount,int_hdfsBlocksLocalityIndex,int_writeRequestsCount,int_compactionTimeMinTime,int_compactionTimeMaxTime,float_blockCacheSizeM,\
    int_readRequestsCount,float_rootIndexSize,int_blockCacheMissCount,int_blockCacheHitRatioPastNPeriods,int_blockCacheHitCachingRatioPastNPeriods,int_storefiles,\
    int_blockCacheEvictedCount,int_stores,int_requests,str_hostName))
    res = cursor.fetchall()
    
    
    
    conn.commit()
    cursor.close()
    conn.close()
        
except MySQLdb.Error,e:
       print "Mysql Error %d: %s" % (e.args[0], e.args[1])
