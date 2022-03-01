# Database README

---------------------------------------------------------------

# HallBotDB Class Functions

Database Object

Acts as a folder holding the tables within the database

---------------------------------------------------------------

### \_\_init\_\_

Initialize the database with just a name which will be the name of the folder.

Creates the list of tables, named database.

If the folder already exists it will load the database from memory.

Parameters:
* name - string
  * The name of your database. Acts as the name of the folder.

Code Example:
```python
test_db = HallBotDB("Test")
```

---------------------------------------------------------------

### create_table

Adds a table to your database.

Your table will automatically have "ID" as the first header.

Parameters:
* name - string
  * The name of your table. Will act as the file name for your table.
* headers - list
  * A list of the headers for each column in your table.

Code Example:
```python
test_db.create_table("Players", ["Name", "RPS Score"])
```

---------------------------------------------------------------

### delete_table - Not functional yet

Deletes the named table from your database.

Parameters:
* name - string
  * The name of the table you would like to delete from the database.

Code Example:
```python
test_db.delete_table("Players")
```

---------------------------------------------------------------

### get_table

Fetches a table object from your database.

Returns a table object.

Returns False if the table is not found.

Parameters:
* name - string
  * The name of the table you would like to fetch from the database.

Code Example:
```python
test_db.get_table("Players")
```

---------------------------------------------------------------

### dumpdb

Saves the database to memory.

Will overwrite any files or folders with the same names.

Code Example:
```python
test_db.dumpdb()
```

---------------------------------------------------------------

# Table Class Functions

Table Object

Acts as a .txt file holding rows of attributes

Member Variables:
* name - string
  * The name of the table. Acts as the name of the .txt file when saved to memory.
* attributes - list
  * A list of attribute objects.
* ID - string
  * A random sequence of characters used as a unique identifier for the table

---------------------------------------------------------------

### \_\_init\_\_

Initializes a table to put in the database.

Creates a list of attributes and adds the headers as the first attribute.

Your table will automatically have "ID" as the first header.

create_table Database function automatically calls this function and adds the table to your database.

Parameters:
* name - string
  * The name of the table. Acts as the name of the .txt file when saved to memory.
* headers - list
  * A list of the headers for each column in your table.

Code Example: 
```python
test_table = Table("Players", ["Name", "RPS Score"])
```

---------------------------------------------------------------

### add_attribute

Adds an attribute to the attributes list.

Effectively adds a row to your table.

Attribute must have same number of values as the header for your table.

Parameters:
* attribute - Attribute
  * The attribute that you are adding to the table.

Code Examples: 

Adding to a table.
```python
test_table.add_attribute(Attribute(["test_name1", 2], False))
```
Adding to a table in a database.
```python
test_db.get_table("Players").add_attribute(Attribute(["test_name1", 2], False))
```

---------------------------------------------------------------

### remove_attribute - Not functional yet

Removes an attribute from the attributes list.

Effectively removes a row from your table.

Parameters:
* ID - string
  * The ID of the attribute you would like to remove.

Code Example:
```python
test_table.remove_attribute("1234567890abcdef")
```

---------------------------------------------------------------

# Attribute Class Functions

Attribute Object

Acts as a row in your table .txt file.

Member Variables:
* values - list
  * A list of the values in your attribute
* ID - string
  * A random sequence of characters used as a unique identifier for the attribute

---------------------------------------------------------------

### \_\_init\_\_

Initializes an attribute to put in your table.

Copies a list of values and stores that in the attribute.

Automatically adds a unique ID as the first value in attribute.

If this is the header attribute it will add "ID" as the first value.

Parameters:
* values - list
  * A list of values that is being added to the attribute.
* header - bool
  * Specifies whether or not this attribute is the header.
    * True - Attribute is header
    * False - Attribute is not header

Code Example:
```python
test_attribute = Attribute(["test_name1", 2], False)
```
