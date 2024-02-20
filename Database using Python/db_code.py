import sqlite3
import pandas as pd

#create connection to the database
conn = sqlite3.connect('Staff.db')

table_name = 'Instructors'
attribute_list = ['ID',"FName",'LName','City','CCode']

file_path = '/Users/nombausr/Documents/Coursera/IBM DATA Engineering/Course3 Python Project/Database using Python/INSTRUCTOR.csv'
df = pd.read_csv(file_path,names=attribute_list)

df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready')

#Running Basic querries.
query_statement = f"select * from {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#view  the firstname column i.e FName

query_statement = f"select FName from {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#view the total number of entries in the Database
query_statement = f"select count(*) from {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#Insecting Data into the Database using Dataframe
data_dict = {"ID":[100],"FName":['Geraldine'],"LName":["Akinwale"],'City':['Lagos'],'CCode':['NG']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists='append', index=False)

# viewing the total number of entries in the table
query_statement = f"select count(*) from {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()

#Practise Problem
conn = sqlite3.connect('Staff.db')

table_name1 = 'Departments'
table_attribute = ["Dept_ID","Dept_Name","Manager_ID","Loc_ID"]

file_path = "/Users/nombausr/Documents/Coursera/IBM DATA Engineering/Course3 Python Project/Database using Python/Departments.csv"
df1 =pd.read_csv(file_path, names=table_attribute)

df1.to_sql(table_name1, conn, if_exists='replace', index=False)
# Running basic queries on data
query_statement = f"Select * from {table_name1}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"select Dept_Name from {table_name1}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# viewing the total number of entries in the table
query_statement = f"select count(*) from {table_name1}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

data_dict1 = {"Dept_ID":[9],"Dept_Name":['Quality Assurance'],"Manager_ID":[30010],"Loc_ID":['L0010']}

data_dict1_append = pd.DataFrame(data_dict1)

data_dict1_append.to_sql(table_name1,conn,if_exists='append',index=False)

# viewing the total number of entries in the table
query_statement = f"select count(*) from {table_name1}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)