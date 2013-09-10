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
    
    #修改接口
    data=os.popen("curl -s http://HMasterip:60010/jmx?qry=hadoop:service=Master,name=Master > ./Masterdata.txt").readlines()
    
    f = file('Masterdata.txt')
    source=f.read().strip()
    ddata=json.JSONDecoder().decode(source)
    target=ddata['beans']
    list_hostName = target[0]["ServerName"].split(',')
    str_hostName = list_hostName[0]
    
    str_nameAsString=os.popen("cat Masterdata.txt|grep nameAsString|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_readRequestsCount=os.popen("cat Masterdata.txt|grep readRequestsCount|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_requestsCount=os.popen("cat Masterdata.txt|grep requestsCount|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_rootIndexSizeKB=os.popen("cat Masterdata.txt|grep rootIndexSizeKB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_storefileIndexSizeMB=os.popen("cat Masterdata.txt|grep storefileIndexSizeMB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_storefileSizeMB=os.popen("cat Masterdata.txt|grep storefileSizeMB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_storefiles=os.popen("cat Masterdata.txt|grep storefiles|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_stores=os.popen("cat Masterdata.txt|grep stores|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_totalCompactingKVs=os.popen("cat Masterdata.txt|grep totalCompactingKVs|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_totalStaticBloomSizeKB=os.popen("cat Masterdata.txt|grep totalStaticBloomSizeKB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_totalStaticIndexSizeKB=os.popen("cat Masterdata.txt|grep totalStaticIndexSizeKB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_writeRequestsCount=os.popen("cat Masterdata.txt|grep writeRequestsCount|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_currentCompactedKVs=os.popen("cat Masterdata.txt|grep currentCompactedKVs|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()
    str_memStoreSizeMB=os.popen("cat Masterdata.txt|grep memStoreSizeMB|sed -e 's/\"//g'|awk -F \, '{print $1}'|awk '{print $3}'").readlines()


    inti=0
    while inti < len(str_nameAsString):
        cursor.execute("insert into Hbase_Master (nameAsString,readRequestsCount,requestsCount,rootIndexSizeKB,storefileIndexSizeMB,storefileSizeMB,storefiles,\
        stores,totalCompactingKVs,totalStaticBloomSizeKB,totalStaticIndexSizeKB,writeRequestsCount,currentCompactedKVs,memStoreSizeMB,hostName) \
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s');" \
        %("'"+str_nameAsString[inti].strip()+"'", \
        "'"+str_readRequestsCount[inti].strip()+"'", \
        "'"+str_requestsCount[inti].strip()+"'", \
        "'"+str_rootIndexSizeKB[inti].strip()+"'", \
        "'"+str_storefileIndexSizeMB[inti].strip()+"'", \
        "'"+str_storefileSizeMB[inti].strip()+"'", \
        "'"+str_storefiles[inti].strip()+"'", \
        "'"+str_stores[inti].strip()+"'", \
        "'"+str_totalCompactingKVs[inti].strip()+"'", \
        "'"+str_totalStaticBloomSizeKB[inti].strip()+"'", \
        "'"+str_totalStaticIndexSizeKB[inti].strip()+"'", \
        "'"+str_writeRequestsCount[inti].strip()+"'", \
        "'"+str_currentCompactedKVs[inti].strip()+"'", \
        "'"+str_memStoreSizeMB[inti].strip()+"'",str_hostName))  
        res = cursor.fetchall()
        inti = inti + 1

    str_ZookeeperQuorum=os.popen("cat Masterdata.txt|grep ZookeeperQuorum|sed 's/[ /,/]*$//'|sed -e 's/\"//g'|sed 's/,/\\n/g'|sed -e 's/\]//g'|awk '{print $3}'").readlines()
    int_ZookeeperQuorum=len(str_ZookeeperQuorum)


    str_json_DeadRegionServers = target[0]["DeadRegionServers"]

    if str_json_DeadRegionServers==[]:
        int_DeadRegionServers=0
        str_DeadRegionServers=""
    else:
        int_DeadRegionServers=len(str_json_DeadRegionServers)
        str_DeadRegionServers = ("".join(str(str_json_DeadRegionServers).split('\''))).strip('[]')

    cursor.execute("insert into Hbase_Master_Warning (Zookeeper,DeadRegion,DeadRegionServers,hostName) values (%s,%s,'%s','%s');" %(int_ZookeeperQuorum,int_DeadRegionServers,str_DeadRegionServers,str_hostName))
    res = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
