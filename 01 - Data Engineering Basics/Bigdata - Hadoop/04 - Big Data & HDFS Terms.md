Semi Structured data -  Json

Unstructured data - Logs, Images, Audio & Videos

Monolithic - A powerful system with lot of resources. Hard to add resources after a certain limit

Distributed - Many smaller systems grouped together. Each system is node and entire group is cluster

Horizontal Scaling - 
Vertical Scaling - 

Resources means - RAM - 16 GB(Memory) , Hard Disk - 2 TB(Storage) & CPU Quad core (Compute)

Distributed Storage -  HDFS
Distributed Processing -  SPARK
Resource Management - YARN

Data Ingestion -  Sqoop transfers data between Relational Database and Hadoop

Data Query/Analysis -  DW tool for data analysis

Name Node - Master 

Data Nodes - Slaves where data is stored

Blocks - Breaking down the file into multiple parts as per block size

Block Size  - 128 MB  (With this size, each file is broken down into multiple chunks(blocks)

Meta Data - Namenode stores the information which says about each blocks locations in data node

Parity blocks in Hadoop 3

Data Nodes are made of commodity hardwares

However Name nodes are made of high quality hardwares

Failure Management:

Data Node:

	Fault Tolerance (Replication Factor Default 3 and can be changed)Name node will create one more copy to maintain the replication factor 
  when any data node is down with help of Heartbeat signal.
  
NameNode:
           SPOF - Single Point of Failure. In current version of hadoop, Namenode is no more SPOF
           
           fsimage -  snapshot of in-memory files at given time
           
           edit logs - all new changes after above snapshot taken
           
           Checkpointing -  Merging of both fsimage and edit logs to keep fsimage updated

Who does checkpointing -  Secondary Name Node 

   Client(Laptop) submits a job/ Request  --> Requests goes to Namenode --> Namenode sends back metadata info -->
   Client reads data from blocks of data node based on metadata 

Rack Awareness Mechanisms:
  The balance approach is to place replicas in two different racks.
  
  One replica in one rack and other two in a different rack or vice versa

Block Report
 Each data nodes sends a block report to the name node at a fixed frequency indication if any blocks are corrupted
 
Name Node High Availability:

   Active name nodes  sends the edit logs to the journal nodes and journal nodes keep updating the passive name nodes with latest edit logs.
   
   When Active name nodes goes down, passive name node takes over.
   
     Failure of (N-1)/2.
     
     Means 5 Nodes : (5-1)/2 ; 2 nodes can be failure
     
     In latest version of hadoop, we have can more than one name node.
     
Name node Scalability:

    We have previously discussed that about Secondary name node but it is for high availability and not to share the load.
    
    SO, we can have multiple name nodes which distribute or share the load.
    
    Different namenode can handle different name spaces

Name Node Federation:

    This concept scaling of namenode, dividing the load among name nodes is called as Name node federation

Gateway/Edge node  --> Where user logs in and access the cluster

