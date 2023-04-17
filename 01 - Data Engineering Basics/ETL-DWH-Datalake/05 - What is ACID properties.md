What are the 𝗔𝗖𝗜𝗗 𝗣𝗿𝗼𝗽𝗲𝗿𝘁𝗶𝗲𝘀 𝗼𝗳 𝗗𝗕𝗠𝗦

Transaction is a sequence of steps performed on a database as a single logical unit of work

The ACID database transaction model ensures that a performed transaction is always consistent by ensuring
 
- 𝗔𝘁𝗼𝗺𝗶𝗰𝗶𝘁𝘆 - Each transaction is either properly carried out or the database reverts back to the state before the transaction started
- 𝗖𝗼𝗻𝘀𝗶𝘀𝘁𝗲𝗻𝗰𝘆 - The database must be in a consistent state before and after the transaction
- I𝘀𝗼𝗹𝗮𝘁𝗶𝗼𝗻 - Multiple transactions occur independently without interference
- 𝗗𝘂𝗿𝗮𝗯𝗶𝗹𝗶𝘁𝘆 - Successful transactions are persisted even in the case of system failure

 ACID guarantees will be ensured by the most Relational Databases such as MySQL , PostgreSQL
 
 NoSQL databases not follows ACID instead BASE transaction model which leads eventual consistency. Eg: Cassandra, MongoDB
