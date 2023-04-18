Hadoop dfs commands:
================
dfs -ls /hivedemos

Comments in Hive:
==============
-- This is script

Databases in hive:
=================

Default database is default database.

To create database:
===================
create database student;

To suppress already existing database warnings:
===================================
create database IF NOT EXISTS student;

Note: You can also use the keyword SCHEMA instead of database.

To see databases:
===============
Show databases;

Hive ==> create a directory for each database.

Tables in that database will be stored in sub directories of the database directory.

Note: The database directory is created under hive.metastore.warehouse.dir.

default location: /user/hive/warehouse/student.db

To add comment for database:
======================
create database student comment 'Holds all student tables';

To describe database:
====================
describe database student;

Note: Also shows the directory location for the database.

To associate key-value properties with the database:
===================================================
create database student WITH DBPROPERTIES ('creator' = 'subhashini' , 'date' = '2015-1-27');

describe database EXTENDED student;

Use command:
===========
sets a database as your working database.

use student;

Note: there is no command to show you which databse is your current working database.

To drop database:
================
drop database if exists student;


To Alter Database:
=============
Note: You can set key-value pairs in the DBPROPERTIES associated with a databse using Alter Database command. No other metadata about the database can be changed including its name and directory location.

alter database student SET DBPROPERTIES ('edited-by' = 'Subha');

Note: There is no way to delete or unset a DBPROPERTY.

Managing Tables in Hive:
=======================
Two kinds of tables:

1. Managed Table

2. External Table

====================================================================================================================

Dataset: Student.tsv

1001	John	45.0
1002	James	85.0
1003	John	45.0
1004	James	85.0
1005	Smith	60.0
1006	Scott	70.0
1007	Shoba	80.0
1008	Taanu	90.0
1009	Anbu	95.0
1010	Aruna	85.0

Managed Table:
=============

create table IF NOT EXISTS student_int (studID INT COMMENT 'Student ID',studName STRING, gpa FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

create table IF NOT EXISTS student(studID INT COMMENT 'Student ID',studName STRING, gpa FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

Note: Stored in warehouse folder. When you drop an internal table, it drops the data, and it also drops the metadata.

External Table:
==============

create EXTERNAL table IF NOT EXISTS student_ext (studID INT COMMENT 'Student ID',studName STRING, gpa FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION '/student_information';

Note: Create a new directory.

Note: When you drop an external table, it only drops the meta data. That means hive is ignorant of that data now. It does not touch the data itself.

Data Manipualtion in Hive:
=========================
Loading Data to Hive Tables:
===========================
LOAD DATA INPATH '/hivedemos/student.tsv' INTO TABLE student_int;

LOAD DATA LOCAL INPATH '/home/vagrant/bigdata/pigdemos/student.tsv' INTO TABLE student_int;

LOAD DATA LOCAL INPATH '/home/vagrant/bigdata/hivedemos/student.tsv' INTO TABLE student_ext;

Complex Data Types:
==================
student.csv
==========
John Smith,80.0,Joshi:Jack,English!24:EVS!25:Hindi!23
scott Tiger,90.0,James:Aruna,English!25:EVS!25:Hindi!22 
 
create table student_complex(name String,gpa FLOAT, classmates ARRAY<STRING>,marks MAP<STRING,INT>) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY ':'
MAP KEYS TERMINATED BY '!';

Describe student_complex;

LOAD DATA LOCAL INPATH '/home/vagrant/bigdata/pigdemos/student.csv' INTO TABLE student_complex;

select * from student_complex;

select name, classmates from student_complex;

select name, marks from student_complex;

select name, marks['English']  from student_complex;

Order by:
========
SELECT s.studID, s.studName,s.gpa                    
FROM student s
ORDER BY s.studName DESC;

select * from metastore.TBLS join metastore.COLUMNS_V2 on TBLS.TBL_ID=COLUMNS_V2.CD_ID;


Partition Table:
===============
  
1. Static Partition 
2. Dynamic Partition

Static Partition:
================
Static Partition (SP) columns:The columns whose values are known at COMPILE TIME (given by user).

CREATE TABLE student_sp(studID INT, studName STRING COMMENT 'Student Name')
PARTITIONED BY (gpa FLOAT);

INSERT OVERWRITE TABLE student_sp
PARTITION (gpa=45.0)
select studID,studName from student
where gpa=45.0;

show partitions student_sp;

alter table student_sp add partition(gpa=85.0);

INSERT OVERWRITE TABLE student_sp
PARTITION (gpa=85.0)
select studID,studName from student where gpa=85.0;

Dynamic Partition:
=================

CREATE TABLE student_dp(studID INT, studName STRING COMMENT 'Student Name')
PARTITIONED BY (gpa FLOAT);

SET hive.exec.dynamic.partition = true; -- enable dynamic partition
SET hive.exec.dynamic.partition.mode = nonstrict; - to disable static partition requirmnent for dp

Note: Dynamic partition strict mode requires at least one static partition column. To turn this off set hive.exec.dynamic.partition.mode=nonstrict

INSERT OVERWRITE TABLE student_dp
PARTITION (gpa)
select studID,studName,gpa from student;

select * from student_dp where gpa=45.0;

show partitions student_dp;

select * from student_dp where gpa=45.0;

Drop Table:
==========

Drop table [IF EXISTS] student;

