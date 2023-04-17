What are slowly changing dimensions?

When organising a datawarehouse into Kimball-style star schemas, you relate fact records to a specific dimension record with its related attributes. But what if the information in the dimension changes? Do you now associate all fact records with the new value? Do you ignore the change to keep historical accuracy? Or do you treat facts before the dimension change differently to those after?
It is this decision that determines whether to make your dimension a slowly changing one. There are several different types of SCD depending on how you treat incoming change.

We have a very simple ‘customer’ dimension, with just 2 attributes – Customer Name and Country:

![image](https://user-images.githubusercontent.com/42135673/232538232-81168a0f-bfc5-422d-ae4a-b438305f829e.png)


• Type 0 – Fixed Dimension
No changes allowed, dimension never changes
• Type 1 – No History
Update record directly, there is no record of historical values, only current state

![image](https://user-images.githubusercontent.com/42135673/232538298-9ffe306e-22c4-48be-951d-cabbaee18c4f.png)


• Type 2 – Row Versioning
Track changes as version records with current flag & active dates and other metadata
In order to support type 2 changes, we need to add four columns to our table:
· Surrogate Key – the original ID will no longer be sufficient to identify the specific record we require, we therefore need to create a new ID that the fact records can join to specifically.
· Current Flag – A quick method of returning only the current version of each record
· Start Date – The date from which the specific historical version is active
· End Date – The date to which the specific historical version record is active
With these elements in place, our table will now look like:

![image](https://user-images.githubusercontent.com/42135673/232538387-42653281-b1ff-437a-b558-3fdd50f663b0.png)


This method is very powerful – you maintain the history for the entire record and can easily perform change-over-time analysis. However, it also comes with more maintenance overhead, increased storage requirement and potential performance impacts if used on very large dimensions.
Type 2 is the most common method of tracking change in data warehouses.

• Type 3 – Previous Value column
Track change to a specific attribute, add a column to show the previous value, which is updated as further changes occur
Here, we add a new column called “Previous Country” to track what the last value for our attribute was.

![image](https://user-images.githubusercontent.com/42135673/232538443-2c7e8818-5e81-4fad-bb4e-b328149f4ee0.png)


Note how this will only provide a single historical value for Country. If the customer changes his name, we will not be able to track it without adding a new column. Likewise, if Bob moved country again, we would either need to add further “Previous Previous Country” columns or lose the fact that he once lived in the United Kingdom.

• Type 4 – History Table
Show current value in dimension table but track all changes in separate table
There is no change to our existing table here, we simply update the record as if a Type 1 change had occurred. However, we simultaneously maintain a history table to keep track of these changes:
Our Dimension table reads:

![image](https://user-images.githubusercontent.com/42135673/232538506-7f5e5b8f-a208-479c-8ece-4d5b7c6a96de.png)

Whilst our Type 4 historical table is created as:

![image](https://user-images.githubusercontent.com/42135673/232538558-2a01302e-57f0-4282-87a4-94759d627a5d.png)

Depending on your requirements, you may place both ID and Surrogate Key onto the fact record so that you can optimise performance whilst maintaining functionality.
Separating the historical data makes your dimensions smaller and therefore reduces complexity and improves performance if the majority of uses only need the current value.
However, if you do require historical values, this structure adds complexity and data redundancy overheads. It is generally assumed that the system will use Type 1 or Type 2 rather than Type 4.

• Type 6 – Hybrid SCD
Utilise techniques from SCD Types 1, 2 and 3 to track change
The ‘Hybrid’ method simply takes SCD types 1, 2 and 3 and applies all techniques. We would maintain a history of all changes whilst simultaneously updating a “current value” column on all records.

![image](https://user-images.githubusercontent.com/42135673/232538629-edff6039-d3d3-40c1-a229-e9089ab11e23.png)

 
This gives you the ability to provide an element of change comparison without additional calculation, whilst still maintaining a full, detailed history of all changes in the system.
Personally, if this requirement came up, I would avoid the data redundancy of this extra column and simply calculate the current value using the “LAST_VALUE()” window function at run-time. Although this depends on your priorities between data storage and direct querying performance.


