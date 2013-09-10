yum install mysqldb
yum update python
yum install python*
yum install MySQL-python

导入DB脚本（库名称HadoopPref），配置好DB用户和权限。
修改代码的数据库IP帐号密码，修改访问的IP地址和保存的文件名称（task,datanode,region有多台所以保存的txt需要修改名称）




一、FSNamesystem
		FilesTotal：HDFS文件总数
		BlocksTotal：HDFS的Block总数
		CapacityTotalGB：HDFS文件系统总容量
		CapacityUsedGB：HDFS已使用的容量
		NonDfsUsedSpace：HDFS未使用但是已占用的容量
		CapacityRemainingGB：HDFS空余容量
		TotalLoad：HDFS连接数
二、NameNode_RPC
		getFileInfo_num_ops：查询文件信息的数次
		getFileInfo_avg_time：查询文件信息的平均时间
		getListing_num_ops：查询文件列表的数次
		getListing_avg_time：查询文件列表的平均时间
		delete_num_ops：删除文件的次数
		delete_avg_time：删除的平均时间
		mkdirs_num_ops：新建目录的次数
		mkdirs_avg_time：新建目录的时间
		create_num_ops：创建文件的数次
		create_avg_time：创建文件的平均时间
		renewLease_num_ops：重命名的次数
		renewLease_avg_time：重命名的平均时间
		addBlock_num_ops：写入block的数次
		addBlock_avg_time：写入的平均时间
		blockReceived_num_ops：block响应的次数
		blockReceived_avg_time：响应的平均时间
		setSafeMode_num_ops：安全模式的次数
		setSafeMode_avg_time：处于安全模式的平均时间
		getBlockLocations_num_ops：获取block位置的次数
		getBlockLocations_avg_time：该操作的平均时间
		fsync_num_ops：文件同步的次数
		fsync_avg_time：同步的平均时间
		RpcQueueTime_num_ops：rpc队列中完成rpccap做的数目
		RpcQueueTime_avg_time：该操作的平均时间
		RpcProcessingTime_num_ops：RPC在交互中的连接数
		RpcProcessingTime_avg_time：交互的平均时间
三、NameNodeMetrics
		FilesCreated：已创建的文件个数
		FilesAppended：已插入的文件个数
		GetBlockLocations：获取block位置的操作数
		FilesRenamed：重命名文件个数
		GetListingOps：查询列表的数次
		CreateFileOps：创建文件的数次
		FilesDeleted：已删除文件个数
		DeleteFileOps：删除文件次数
		FileInfoOps：查看文件信息的数次
		AddBlockOps：插入block的次数
		Transactions_num_ops：传输的次数
		Transactions_avg_time：传输平均时间
		Syncs_num_ops：同步次数
		Syncs_avg_time：同步平均时间
		JournalTransactionsBatchedInSync：定期同步处理的传输量
		blockReport_num_ops：block报告次数
		blockReport_avg_time：报告平均时间
		fsImageLoadTime：加载fsImage的时间
		FilesInGetListingOps：getlist操作次数
四、NameNode_Warning
		CorruptBlocks：损坏的block
		ExcessBlocks：多余的block 
		MissingBlocks：丢失的block
		UnderReplicatedBlocks：副本数量不足的block
		PercentRemaining：空间使用百分比
		LiveNodes：存活的节点个数
		DeadNodes：出问题的节点个数
		DeadNodesServer：出问题的节点名称
五、HMaster
		nameAsString：表名称
		readRequestsCount：读取请求个数（readRequestCount与客户端读取数据的个数不等价，而且大部分情况下readRequestCount 远小于客户端读取数据个数，因为next(1000)只算一次请求）
		requestsCount：请求次数
		rootIndexSizeKB：根索引容量
		storefileIndexSizeMB：storefile索引的大小
		storefileSizeMB：storefile文件大小
		storefiles：storefiles文件个数
		stores：stores的文件个数
		totalCompactingKVs：压缩的KeyValue数量
		totalStaticBloomSizeKB：store上所有bloom容量
		totalStaticIndexSizeKB：静态索引大小
		writeRequestsCount：写入请求个数（riteRequestCount与客户端写操作个数不完全等价，批量写只记做一次请求，大部分情况下writeRequestCount远小于客户端写操作的个数(尤其批量写频繁的情况下）
		currentCompactedKVs：当前压缩完成的KeyValue数量
		memStoreSizeMB：RegionServer中所有HRegion中的memstore大小的总和
六、Hbase_Master_Warning
		Zookeeper：Zookeeper的个数
		DeadRegion：出问题的节点个数
		DeadRegionServers：出问题的节点名称
七、JobTracker_RPC
		RpcQueueTime_num_ops：rpc队列中完成rpccap做的数目
		RpcQueueTime_avg_time：该操作的平均时间
		RpcProcessingTime_num_ops：RPC在交互中的连接数
		RpcProcessingTime_avg_time：交互的平均时间
		getSystemDir_num_ops:访问系统目录的次数
		getSystemDir_avg_time：访问系统目录的平均时间
		getStagingAreaDir_num_ops：访问等待区目录的次数
		getStagingAreaDir_avg_time：访问等待区目录的平均时间
		getNewJobId_num_ops：创建新jobid的次数
		getNewJobId_avg_time；平均时间
		submitJob_num_ops：提交job的次数
		submitJob_avg_time：平均时间
		getJobStatus_num_ops：获取job状态次数
		getJobStatus_avg_time：平均时间
		getTaskCompletionEvents_num_ops：完成的task次数
		getTaskCompletionEvents_avg_time：平均时间
		getJobCounters_num_ops：job数量
		getJobCounters_avg_time：平均时间
八、JobTrackerMetrics
		map_slots：全局map_slots的资源数量
		reduce_slots：全局reduce_slots的资源数量
		maps_launched：启动的map数量
		maps_completed：完成的数量
		maps_failed：失败的数量
		reduces_launched：启动的reduces数量
		reduces_completed：完成的数量
		reduces_failed：失败的数量
		waiting_maps：等待的map
		waiting_reduces：等待的reduces
		jobs_failed：失败的job
		jobs_killed：kill的job
九、TaskTrackerMetrics
		RpcQueueTime_num_ops：rpc队列中完成rpccap做的数目
		RpcQueueTime_avg_time：该操作的平均时间
		RpcProcessingTime_num_ops：RPC在交互中的连接数
		RpcProcessingTime_avg_time：交互的平均时间
		getTask_num_ops：当子进程启动后，获取jvmtask的次数
		getTask_avg_time：当子进程启动后，获取jvmtask的平均时间
		getMapCompletionEvents_num_ops： reduce获取已经完成的map输出地址事件的次数
		getMapCompletionEvents_avg_time：reduce获取已经完成的map输出地址事件的平均时间
		commitPending_num_ops：提交挂起的次数
		commitPending_avg_time：平均时间
		tasks_completed：已完成的task次数
		tasks_failed_timeout：失败超时的task次数
		tasks_failed_ping：因tasktracker与task交互失败导致的失败的task数目
十、DataNodeMetrics
		bytes_written：写入字节数
		bytes_read：读取字节数
		blocks_written：硬盘写入block的次数
		blocks_read：硬盘读取block的次数
		blocks_replicated：block的复制总数
		blocks_removed：删除block的数量
		blocks_verified：blcok验证的次数
		block_verification_failures：block验证失败的次数
		blocks_get_local_pathinfo：blcok获取本地路径信息的次数
		reads_from_local_client：从本地读取block的次数
		reads_from_remote_client：远程读取block的次数
		writes_from_local_client：写入本地的次数
		writes_from_remote_client：写入远程的次数
		readBlockOp_num_ops：读块总次数 一般和dfs.datanode.blocks_read一致，先从硬盘读入输入流，增加dfs.datanode.blocks_read计数，然后再增加该计数 
		readBlockOp_avg_time：读块的平均时间
		writeBlockOp_num_ops：写块总次数一般和dfs.datanode.blocks_written一致，先从硬盘，增加dfs.datanode.blocks_read计数，然后再增加该计数 
		writeBlockOp_avg_time：写块的平均时间
		ThreadCount：线程数
十一、	RegionServerMetrics
		ThreadCount：线程数
		totalStaticIndexSizeKB： HRegionServer上每个HFile文件的IndexSize的大小，这是指未压缩的，不带有其它信息的所有HFileBlockIndex信息的总和
		blockCacheFree：block cache中空闲的内存大小
		memstoreSizeMB：memstore大小的总和
		blockCacheCount：RegionServer中缓存到blockcache中block的个数
		blockCacheHitRatio： blockCache命中比例
		blockCacheHitCachingRatio：HitCache表示因为读取不到而cacheblock的行为，blockCacheHitCachingRatio表示发生该行为的比率
		blockCacheHitCount：blockCache命中次数
		hdfsBlocksLocalityIndex：统计RegionServer所在机器的数据本地化的概率
		writeRequestsCount：写请求的数量：writeRequestCount与客户端写操作个数不完全等价，批量写只记做一次请求，大部分情况下writeRequestCount远小于客户端写操作的个数(尤其批量写频繁的情况下)
		compactionTimeMinTime：压缩的最短时间
		compactionTimeMaxTime：压缩的最大时间
		blockCacheSize：blockCache大小
		readRequestsCount：读请求的数量：readRequestCount与客户端读取数据的个数不等价，而且大部分情况下readRequestCount 远小于客户端读取数据个数，因为next(1000)只算一次请求
		rootIndexSizeKB： storefileIndex的大小，和storefileIndexSizeMB相同
		blockCacheMissCount：blockCache非命中比例
		blockCacheHitRatioPastNPeriods：周期内的缓存命中率
		blockCacheHitCachingRatioPastNPeriods：周期内读取不到而cacheblock的行为的比率
		storefiles：Storefiles的个数
		blockCacheEvictedCount：BlockCache中被换出的Block的个数
		stores： RegionServer包含的Store的个数
		requests：请求的数量
十二、JVM
		memNonHeapUsedM： JVM已使用的非堆的大小
		memNonHeapCommittedM：JVM分配给非堆的大小
		memHeapUsedM：jvm使用堆内存大小 
		memHeapCommittedM：JVM分配的堆大小
		gcCount：JVM进行GC的次数
		gcTimeMillis：GC花费的时间，单位为微妙
		ThreadCount：线程数
		threadsNew：处于NEW状态线程数量
		threadsRunnable：处于RUNNABLE状态线程数量
		threadsBlocked：处于BLOCKED状态线程数量
		threadsWaiting：处于WAITING状态线程数量
		threadsTimedWaiting：处于TIMED_WAITING状态线程数量
		threadsTerminated：处于TERMINATED状态线程数量
		