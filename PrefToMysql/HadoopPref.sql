/*
Navicat MySQL Data Transfer

Source Server         : 192.168.249.155
Source Server Version : 50095
Source Host           : 192.168.249.155:3306
Source Database       : HadoopPref

Target Server Type    : MYSQL
Target Server Version : 50095
File Encoding         : 65001

Date: 2013-09-10 11:40:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `DataNode_Jvm`
-- ----------------------------
DROP TABLE IF EXISTS `DataNode_Jvm`;
CREATE TABLE `DataNode_Jvm` (
  `memNonHeapUsedM` float(10,3) default NULL,
  `memNonHeapCommittedM` float(10,3) default NULL,
  `memHeapUsedM` float(10,3) default NULL,
  `memHeapCommittedM` float(10,3) default NULL,
  `gcCount` int(11) default NULL,
  `gcTimeMillis` int(11) default NULL,
  `threadsNew` int(11) default NULL,
  `threadsRunnable` int(11) default NULL,
  `threadsBlocked` int(11) default NULL,
  `threadsWaiting` int(11) default NULL,
  `threadsTimedWaiting` int(11) default NULL,
  `threadsTerminated` int(11) default NULL,
  `hostname` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `DataNode_Jvm_index_dt_host` USING BTREE (`hostname`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of DataNode_Jvm
-- ----------------------------

-- ----------------------------
-- Table structure for `DataNodeMetrics`
-- ----------------------------
DROP TABLE IF EXISTS `DataNodeMetrics`;
CREATE TABLE `DataNodeMetrics` (
  `G_written` float(10,3) default NULL,
  `G_read` float(10,3) default NULL,
  `blocks_written` int(11) default NULL,
  `blocks_read` int(11) default NULL,
  `blocks_replicated` int(11) default NULL,
  `blocks_removed` int(11) default NULL,
  `blocks_verified` int(11) default NULL,
  `block_verification_failures` int(11) default NULL,
  `blocks_get_local_pathinfo` int(11) default NULL,
  `reads_from_local_client` int(11) default NULL,
  `reads_from_remote_client` int(11) default NULL,
  `writes_from_local_client` int(11) default NULL,
  `writes_from_remote_client` int(11) default NULL,
  `readBlockOp_num_ops` int(11) default NULL,
  `readBlockOp_avg_time` float(10,3) default NULL,
  `writeBlockOp_num_ops` int(11) default NULL,
  `writeBlockOp_avg_time` float(10,3) default NULL,
  `ThreadCount` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `DataNodeMetrics_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of DataNodeMetrics
-- ----------------------------

-- ----------------------------
-- Table structure for `FSNamesystem`
-- ----------------------------
DROP TABLE IF EXISTS `FSNamesystem`;
CREATE TABLE `FSNamesystem` (
  `FilesTotal` int(11) default NULL,
  `BlocksTotal` int(11) default NULL,
  `CapacityTotalGB` int(11) default NULL,
  `CapacityUsedGB` int(11) default NULL,
  `NonDfsUsedSpace` int(11) default NULL,
  `CapacityRemainingGB` int(11) default NULL,
  `TotalLoad` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `FSNamesystem_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of FSNamesystem
-- ----------------------------

-- ----------------------------
-- Table structure for `Hbase_Master`
-- ----------------------------
DROP TABLE IF EXISTS `Hbase_Master`;
CREATE TABLE `Hbase_Master` (
  `nameAsString` varchar(255) default NULL,
  `readRequestsCount` int(11) default NULL,
  `requestsCount` int(11) default NULL,
  `rootIndexSizeKB` int(11) default NULL,
  `storefileIndexSizeMB` int(11) default NULL,
  `storefileSizeMB` int(11) default NULL,
  `storefiles` int(11) default NULL,
  `stores` int(11) default NULL,
  `totalCompactingKVs` int(11) default NULL,
  `totalStaticBloomSizeKB` int(11) default NULL,
  `totalStaticIndexSizeKB` int(11) default NULL,
  `writeRequestsCount` int(11) default NULL,
  `currentCompactedKVs` int(11) default NULL,
  `memStoreSizeMB` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `Hbase_Master_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Hbase_Master
-- ----------------------------

-- ----------------------------
-- Table structure for `Hbase_Master_Warning`
-- ----------------------------
DROP TABLE IF EXISTS `Hbase_Master_Warning`;
CREATE TABLE `Hbase_Master_Warning` (
  `Zookeeper` int(11) default NULL,
  `DeadRegion` int(5) default NULL,
  `DeadRegionServers` varchar(255) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `Hbase_Master_Warning_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Hbase_Master_Warning
-- ----------------------------

-- ----------------------------
-- Table structure for `JobTracker_Jvm`
-- ----------------------------
DROP TABLE IF EXISTS `JobTracker_Jvm`;
CREATE TABLE `JobTracker_Jvm` (
  `memNonHeapUsedM` float(10,3) default NULL,
  `memNonHeapCommittedM` float(10,3) default NULL,
  `memHeapUsedM` float(10,3) default NULL,
  `memHeapCommittedM` float(10,3) default NULL,
  `gcCount` int(11) default NULL,
  `gcTimeMillis` int(11) default NULL,
  `ThreadCount` int(11) default NULL,
  `threadsNew` int(11) default NULL,
  `threadsRunnable` int(11) default NULL,
  `threadsBlocked` int(11) default NULL,
  `threadsWaiting` int(11) default NULL,
  `threadsTimedWaiting` int(11) default NULL,
  `threadsTerminated` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `JobTracker_Jvm_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of JobTracker_Jvm
-- ----------------------------

-- ----------------------------
-- Table structure for `JobTracker_RPC`
-- ----------------------------
DROP TABLE IF EXISTS `JobTracker_RPC`;
CREATE TABLE `JobTracker_RPC` (
  `RpcQueueTime_num_ops` int(11) default NULL,
  `RpcQueueTime_avg_time` float(10,3) default NULL,
  `RpcProcessingTime_num_ops` int(11) default NULL,
  `RpcProcessingTime_avg_time` float(10,3) default NULL,
  `getSystemDir_num_ops` int(11) default NULL,
  `getSystemDir_avg_time` float(10,3) default NULL,
  `getStagingAreaDir_num_ops` int(11) default NULL,
  `getStagingAreaDir_avg_time` float(10,3) default NULL,
  `getNewJobId_num_ops` int(11) default NULL,
  `getNewJobId_avg_time` float(10,3) default NULL,
  `submitJob_num_ops` int(11) default NULL,
  `submitJob_avg_time` float(10,3) default NULL,
  `getJobStatus_num_ops` int(11) default NULL,
  `getJobStatus_avg_time` float(10,3) default NULL,
  `getTaskCompletionEvents_num_ops` int(11) default NULL,
  `getTaskCompletionEvents_avg_time` float(10,3) default NULL,
  `getJobCounters_num_ops` int(11) default NULL,
  `getJobCounters_avg_time` float(10,3) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `JobTracker_RPC_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of JobTracker_RPC
-- ----------------------------

-- ----------------------------
-- Table structure for `JobTracker_Warning`
-- ----------------------------
DROP TABLE IF EXISTS `JobTracker_Warning`;
CREATE TABLE `JobTracker_Warning` (
  `nodes` int(11) default NULL,
  `alive` int(11) default NULL,
  `deadnodes` int(11) default NULL,
  `map_slots_used` int(11) default NULL,
  `per_map_slots_used` float(10,3) default NULL,
  `reduce_slots_used` int(11) default NULL,
  `per_reduce_slots_used` float(10,3) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `JobTracker_warning_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of JobTracker_Warning
-- ----------------------------

-- ----------------------------
-- Table structure for `JobTrackerMetrics`
-- ----------------------------
DROP TABLE IF EXISTS `JobTrackerMetrics`;
CREATE TABLE `JobTrackerMetrics` (
  `map_slots` int(11) default NULL,
  `reduce_slots` int(11) default NULL,
  `maps_launched` int(11) default NULL,
  `maps_completed` int(11) default NULL,
  `maps_failed` int(11) default NULL,
  `reduces_launched` int(11) default NULL,
  `reduces_completed` int(11) default NULL,
  `reduces_failed` int(11) default NULL,
  `jobs_submitted` int(11) default NULL,
  `jobs_completed` int(11) default NULL,
  `waiting_maps` int(11) default NULL,
  `waiting_reduces` int(11) default NULL,
  `jobs_failed` int(11) default NULL,
  `jobs_killed` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `JobTracker_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of JobTrackerMetrics
-- ----------------------------

-- ----------------------------
-- Table structure for `NameNode_Jvm`
-- ----------------------------
DROP TABLE IF EXISTS `NameNode_Jvm`;
CREATE TABLE `NameNode_Jvm` (
  `memNonHeapUsedM` float(10,3) default NULL,
  `memNonHeapCommittedM` float(10,3) default NULL,
  `memHeapUsedM` float(10,3) default NULL,
  `memHeapCommittedM` float(10,3) default NULL,
  `gcCount` int(11) default NULL,
  `gcTimeMillis` int(11) default NULL,
  `threadsNew` int(11) default NULL,
  `threadsRunnable` int(11) default NULL,
  `threadsBlocked` int(11) default NULL,
  `threadsWaiting` int(11) default NULL,
  `threadsTimedWaiting` int(11) default NULL,
  `threadsTerminated` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `NameNode_Jvm_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of NameNode_Jvm
-- ----------------------------

-- ----------------------------
-- Table structure for `NameNode_RPC`
-- ----------------------------
DROP TABLE IF EXISTS `NameNode_RPC`;
CREATE TABLE `NameNode_RPC` (
  `getFileInfo_num_ops` int(11) default NULL,
  `getFileInfo_avg_time` float(10,3) default NULL,
  `getListing_num_ops` int(11) default NULL,
  `getListing_avg_time` float(10,3) default NULL,
  `delete_num_ops` int(11) default NULL,
  `delete_avg_time` float(10,3) default NULL,
  `mkdirs_num_ops` int(11) default NULL,
  `mkdirs_avg_time` float(10,3) default NULL,
  `create_num_ops` int(11) default NULL,
  `create_avg_time` float(10,3) default NULL,
  `renewLease_num_ops` int(11) default NULL,
  `renewLease_avg_time` float(10,3) default NULL,
  `addBlock_num_ops` int(11) default NULL,
  `addBlock_avg_time` float(10,3) default NULL,
  `blockReceived_num_ops` int(11) default NULL,
  `blockReceived_avg_time` float(10,3) default NULL,
  `setSafeMode_num_ops` int(11) default NULL,
  `setSafeMode_avg_time` float(10,3) default NULL,
  `getBlockLocations_num_ops` int(11) default NULL,
  `getBlockLocations_avg_time` float(10,3) default NULL,
  `fsync_num_ops` int(11) default NULL,
  `fsync_avg_time` float(10,3) default NULL,
  `RpcQueueTime_num_ops` int(11) default NULL,
  `RpcQueueTime_avg_time` float(10,3) default NULL,
  `RpcProcessingTime_num_ops` int(11) default NULL,
  `RpcProcessingTime_avg_time` float(10,3) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `NameNode_RPC_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of NameNode_RPC
-- ----------------------------

-- ----------------------------
-- Table structure for `NameNode_Warning`
-- ----------------------------
DROP TABLE IF EXISTS `NameNode_Warning`;
CREATE TABLE `NameNode_Warning` (
  `CorruptBlocks` int(11) default NULL,
  `ExcessBlocks` int(11) default NULL,
  `MissingBlocks` int(11) default NULL,
  `UnderReplicatedBlocks` int(11) default NULL,
  `DFS_PercentUsed` float(10,3) default NULL,
  `LiveNodes` int(11) default NULL,
  `DeadNodes` int(11) default NULL,
  `DeadNodesServer` varchar(255) default '',
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of NameNode_Warning
-- ----------------------------

-- ----------------------------
-- Table structure for `NameNodeMetrics`
-- ----------------------------
DROP TABLE IF EXISTS `NameNodeMetrics`;
CREATE TABLE `NameNodeMetrics` (
  `FilesCreated` int(11) default NULL,
  `FilesAppended` int(11) default NULL,
  `GetBlockLocations` int(11) default NULL,
  `FilesRenamed` int(11) default NULL,
  `GetListingOps` int(11) default NULL,
  `CreateFileOps` int(11) default NULL,
  `FilesDeleted` int(11) default NULL,
  `DeleteFileOps` int(11) default NULL,
  `FileInfoOps` int(11) default NULL,
  `AddBlockOps` int(11) default NULL,
  `Transactions_num_ops` int(11) default NULL,
  `Transactions_avg_time` float(10,3) default NULL,
  `Syncs_num_ops` int(11) default NULL,
  `Syncs_avg_time` float(10,3) default NULL,
  `JournalTransactionsBatchedInSync` int(11) default NULL,
  `blockReport_num_ops` int(11) default NULL,
  `blockReport_avg_time` float(10,3) default NULL,
  `fsImageLoadTime` int(11) default NULL,
  `FilesInGetListingOps` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `NameNodeMetrics_index_dt_host` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of NameNodeMetrics
-- ----------------------------

-- ----------------------------
-- Table structure for `RegionServerMetrics`
-- ----------------------------
DROP TABLE IF EXISTS `RegionServerMetrics`;
CREATE TABLE `RegionServerMetrics` (
  `ThreadCount` int(11) default NULL,
  `totalStaticIndexSizeM` float(10,3) default NULL,
  `blockCacheFree` float(10,3) default NULL,
  `memstoreSizeMB` int(11) default NULL,
  `blockCacheCount` int(11) default NULL,
  `blockCacheHitRatio` int(11) default NULL,
  `blockCacheHitCachingRatio` int(11) default NULL,
  `blockCacheHitCount` int(11) default NULL,
  `hdfsBlocksLocalityIndex` int(11) default NULL,
  `writeRequestsCount` int(11) default NULL,
  `compactionTimeMinTime` int(11) default NULL,
  `compactionTimeMaxTime` int(11) default NULL,
  `blockCacheSizeM` float(10,3) default NULL,
  `readRequestsCount` int(11) default NULL,
  `rootIndexSizeKB` float(11,0) default NULL,
  `blockCacheMissCount` int(11) default NULL,
  `blockCacheHitRatioPastNPeriods` int(11) default NULL,
  `blockCacheHitCachingRatioPastNPeriods` int(11) default NULL,
  `storefiles` int(11) default NULL,
  `blockCacheEvictedCount` int(11) default NULL,
  `stores` int(11) default NULL,
  `requests` int(11) default NULL,
  `hostName` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `RegionServerMetrics_index` USING BTREE (`hostName`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of RegionServerMetrics
-- ----------------------------

-- ----------------------------
-- Table structure for `TaskTracker_Jvm`
-- ----------------------------
DROP TABLE IF EXISTS `TaskTracker_Jvm`;
CREATE TABLE `TaskTracker_Jvm` (
  `memNonHeapUsedM` float(10,3) default NULL,
  `memNonHeapCommittedM` float(10,3) default NULL,
  `memHeapUsedM` float(10,3) default NULL,
  `memHeapCommittedM` float(10,3) default NULL,
  `gcCount` int(11) default NULL,
  `gcTimeMillis` int(11) default NULL,
  `threadsNew` int(11) default NULL,
  `threadsRunnable` int(11) default NULL,
  `threadsBlocked` int(11) default NULL,
  `threadsWaiting` int(11) default NULL,
  `threadsTimedWaiting` int(11) default NULL,
  `threadsTerminated` int(11) default NULL,
  `hostname` varchar(255) default NULL,
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `task_jvm` USING BTREE (`hostname`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TaskTracker_Jvm
-- ----------------------------

-- ----------------------------
-- Table structure for `TaskTrackerMetrics`
-- ----------------------------
DROP TABLE IF EXISTS `TaskTrackerMetrics`;
CREATE TABLE `TaskTrackerMetrics` (
  `RpcQueueTime_num_ops` int(11) default NULL,
  `RpcQueueTime_avg_time` float(10,3) default NULL,
  `RpcProcessingTime_num_ops` int(11) default NULL,
  `RpcProcessingTime_avg_time` float(10,3) default NULL,
  `getTask_num_ops` int(11) default NULL,
  `getTask_avg_time` float(10,0) default NULL,
  `getMapCompletionEvents_num_ops` int(11) default NULL,
  `getMapCompletionEvents_avg_time` float(10,3) default NULL,
  `commitPending_num_ops` int(11) default NULL,
  `commitPending_avg_time` float(10,3) default NULL,
  `ThreadCount` int(11) default NULL,
  `tasks_completed` int(11) default NULL,
  `tasks_failed_timeout` int(11) default NULL,
  `tasks_failed_ping` int(11) default NULL,
  `hostname` varchar(255) default '',
  `Dtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  KEY `index_dt_host` USING BTREE (`hostname`,`Dtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TaskTrackerMetrics
-- ----------------------------
