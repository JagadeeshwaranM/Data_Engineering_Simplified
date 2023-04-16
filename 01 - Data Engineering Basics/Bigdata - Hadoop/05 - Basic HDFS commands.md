
Lists the files from the directory:

      Hadoop fs -ls /

Create a directory:

    Hadoop fs -mkdir /user/jaga/

Create a parent directory even if doesn't exist

    Hadoop fs -mkdir -p /user/jaga/data

Delete the file

    Hadoop fs -rm /user/jaga/data/file1.txt

Delete the files from directory recursively

    Hadoop fs -rm -R /user/jaga/data

Copy the file from local system to hdfs

    hadoop fs -copyFromLocal Desktop/file1.txt /user/jaga/data

Copy the file from hdfs to local system

    hadoop fs -copyToLocal <hdfspath> <localpath>

Copy the file from hdfs source to target directory
  
    Hadoop fs -cp <hdfs source file path>  <hdfs target directory>

Move the file from hdfs source to target directory
  
    Hadoop fs -mv <hdfs source file path>  <hdfs target directory>
    
Check the disk usage in HDFS:
  
    Hadoop fs -df -h /user/cloudera   --> disk free
  
    Hadoop fs -du -h /user/cloudera  --> disk usage
  
    Hadoop fs -du -s -h  /user/cloudera  --> summary

