
##Task 1: Create database using SQLite¶

import sqlite3 

# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR.db')

# cursor object
cursor_obj = conn.cursor()



##Task 2: Create a table in the database¶

# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# Creating table
table = """ CREATE TABLE if not exists INSTRUCTOR (ID INTEGER PRIMARY KEY NOT NULL, 
FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2)); """

cursor_obj.execute(table)

print("table is ready")



##Task 3: Insert data into the table¶

cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')

cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')




##Task 4: Query data in the table¶

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print ("All the data")
#The  fetchall()  method in Python retrieves all the rows from the result set of a query and presents them as a list of tuples.
output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)
    
    
# Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)    


# Fetch only FNAME from the table

statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
    print(fetch)
    
    
# write and execute an update statement that changes the Rav's CITY to MOOSETOWN

query_update = ''' UPDATE INSTRUCTOR SET CITY = 'MOOSETOWN' WHERE FNAME = "Rav" '''  
cursor_obj.execute(query_update)  


statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_update = cursor_obj.fetchmany(2)
for update in output_update:
    print (update)
    
  

## Task 5: Retrieve data into Pandas¶    
import pandas as pd

#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("SELECT * FROM INSTRUCTOR;" , conn)

#print the dataframe
df

#print just the LNAME for first row in the pandas data frame
df.LNAME[0]

#Once the data is in a Pandas dataframe, you can do the typical pandas operations on it.
# see how many rows and columns are in the dataframe
df.shape


## Task 6: Close the Connection¶
conn.close()



