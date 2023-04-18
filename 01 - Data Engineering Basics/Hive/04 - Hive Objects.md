![image](https://user-images.githubusercontent.com/42135673/232810358-d3d98eee-6d38-4a68-b190-c8f896f12a8e.png)


**Databases**

  Namespaces that separate tables and other data units from naming conflicts. 

**Tables**

  Homogeneous units of data which have the same schema.
  
    Managed Tables:
        When you create a table in Hive, by default Hive will manage the data, which means that Hive moves the data into its warehouse directory. 
    External Tables:
        Alternatively, you may create an external table, which tells Hive to refer to the data that is at an existing location outside the warehouse directory. 
 
 **Partitions**
 
Each Table can have one or more Partition keys which determine how the data is stored. 
Partitions - apart from being storage units – can be used inside queries just like regular columns.

**Buckets**

Data in each partition may in turn be divided into Buckets based on the value of a hash function of some column of the Table. 
Buckets can be used to efficiently sample the data.
Note that buckets do not require Partitions.

**Files**

The data itself can be stored in several different file formats:

  - TEXTFILE (default)
  - SEQUENCEFILE (binary)
  - RCFILE (column-oriented)
  - ORC (opt. column-oriented)
  - PARQUET (Apache)
  - AVRO (Apache)

**Records/Rows**

Single records respectively rows in tables are read/written using so-called SerDe’s (Serializer/De-serializer).
They parse raw byte input into records/rows.



