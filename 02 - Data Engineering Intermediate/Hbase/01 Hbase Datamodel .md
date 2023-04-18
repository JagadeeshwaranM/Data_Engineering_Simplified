![image](https://user-images.githubusercontent.com/42135673/232831533-3ae1903b-da2b-4531-a4cc-d0408729a163.png)

From HBase’s point of view, a row is a logical unit, not a physical one.

   In HBase, rows are subdivided along their column families.
   
   For the client and the user, however, a row appears as one logical unit.
   
   As data in a particular column family is stored together in one HFile, fetching a database row means to collect all cells (latest timestamp) 
   in all column families that are referenced by the same row key.
   
   For writing to a particular cell, this has similar implications as only the HFile that holds the column family containing the cell will be touched.
   
    In fact, a “row” is only one special way of viewing related data. The HBase reference states that HBase should rather be thought of 
    as a “multi-dimensional hash map”, where the combination (namespace, table, column family, column qualifier, time stamp) are the key to a particular value. 
    This how HBase relates to KV-based NoSQL solutions.
 
   Every data object stored in an HBase cell is interpreted as an array of bytes, even column qualifiers/names and row keys are considered as byte arrays.
   
   The mechanism can be used to easily store binary data (e.g. MOBs – medium sized objects, such as images, 10 KB – 10MB).
   
   While this gives a maximum of flexibility to the database developer, the validation of data types and correct value ranges must be done inside the application.
 


