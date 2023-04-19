- Hive uses table schemata at read time thus enabling flexible data handling.

- Hive doesn't verify the data when it is loaded, but rather when a query is issued.

- Schema on read makes for a very fast initial load, since the data does not have to be read, parsed, and serialized to disk in the database's internal format. 

- The load operation is just a file copy or move. 

- It is more flexible, too: consider having two schemas for the same underlying data, depending on the analysis being performed. 

- Furthermore, there are many scenarios where the schema is not known at load time, so there are no indexes to apply, because the queries have not been formulated yet. 




