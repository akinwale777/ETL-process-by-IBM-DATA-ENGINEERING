import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/Users/nombausr/Documents/Coursera/IBM DATA Engineering/Course3 Python Project/Webscraping/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# I used pwd command in the terminal to get my current working directory

html_page = requests.get(url).text
data = BeautifulSoup(html_page,'html.parser')

tables = data.find_all('tbody') # to find all the table element and save them in a list called tables
rows = tables[0].find_all('tr') # to find all the row in a specific table and save them in a list called rows

# Loping through the rows list to extract 
for row in rows:
    if count < 50:
        cols = row.find_all('td')
        if len(cols) != 0:
            data_dict = {"Average Rank":cols[0].contents[0],
                         "Film":cols[1].contents[0],
                         "Year":cols[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1],ignore_index=True)
            count += 1
    else:
        break

# printing the df
print("The Dtaframe (df):\n",df)


#storing the data
df.to_csv(csv_path)

#to store the data to a database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()



