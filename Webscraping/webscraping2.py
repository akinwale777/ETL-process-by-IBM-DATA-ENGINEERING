import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_25'
csv_path = '/Users/nombausr/Documents/Coursera/IBM DATA Engineering/Course3 Python Project/Webscraping/top_25_films.csv'
df = pd.DataFrame(columns=["Film","Year","Rotten Tomatoes top 100"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page,'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count <25:
        cols = row.find_all('td')
        if len(cols) !=0:
            data_dict = {"Film":cols[1].string,
                         "Year":cols[2].string,
                         "Rotten Tomatoes top 100":cols[3].contents[0]}
            df1 = pd.DataFrame(data_dict,index=[0])
            df = pd.concat([df,df1],ignore_index=True)
            count +=1
    else:
        break

print(df)
df['Year']=df['Year'].astype(int)

print("\n\nThis is the filtered Dataframe for movies above the year 2000")
final_df = df[df['Year']>=2000]
print(final_df)