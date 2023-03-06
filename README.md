## Changes 

#### **0.0.2 (2023-03-06)**

* Initialization of the first commands without bug fixing,
* Push the release on pypi.

## Sqlite Wrapper 

To use python 3.7 is required.  
 * To initialise a new connection instance the class: `SqliteWrap(<connexionName>)` ,
* To create a new table call the function: `create_table("<tableName>" , listFields=[("<name>",<type>), ..]>)`,
* To add items to the different tables: `read_rows("<tableName>" , listFields=[("<name>",<value>), ..]>)`, 
* To find the maximum of a field in a table: `max_index("<tableName>" , <fields="<nameFieds>">)`, 
* To display the content of a table: `read_rows("<tableName>",<listFields=["<name>", ..]>)` , 
* To delete information from a table: `delete_rows("<tableName>" , "<condition=("<field>",<value>)>")`, 
* To empty a table: `reset_table("<tableName>")` ,
* To close the connexion with the db: `close_db()` . 
