**HDFS Architecture**

![image](https://user-images.githubusercontent.com/42135673/232320089-dc36a589-4a02-4efd-babe-3786b81d5f06.png)

Name Node - Master

Data Nodes - Slaves where data is stored

Blocks - Breaking down the file into multiple parts as per block size

    Block Size - 128 MB (With this size, each file is broken down into multiple chunks(blocks)

Meta Data - Namenode stores the information which says about each blocks locations in data node

Data Nodes are made of commodity hardwares and Name nodes are made of high quality hardwares

Client(Laptop) submits a job/ Request --> Requests goes to Namenode --> Namenode sends back metadata info --> Client reads data from blocks of data node based on metadata

Datanodes store actual data in blocks and perform actual processing


