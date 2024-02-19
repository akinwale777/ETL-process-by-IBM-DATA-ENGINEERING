This Director contains the file for the IBM labs on web scraping

Scenario
Consider that you have been hired by a Multiplex management organization to extract the information of the top 50 movies with the best average rating from the web link shared below.

https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

The information required is Average Rank, Film, and Year.
You are required to write a Python script webscraping_movies.py that extracts the information and saves it to a CSV file top_50_films.csv. You are also required to save the same information to a database Movies.db under the table name Top_50.

Initial step involves instlling the need packages which are pandas, Beautifulsoup, requests, and sqlite3 using the code:
python3.xx -m pip install <package>

# code setup
we then import all the packages we need in the script we will beusing to contin the code for the webscraping. This script can be called webscrapping.py
'
The packages to be imported are requests, sqlite3, pandas, and BeautifulSoup from bs4. 

Once all the needed packages have been imported, we create variables to hold the url, database, table_name as seen bellow.

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/project/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

- I used pwd command in the terminal to get my current working directory 

the next step is to create the respond object and then use beautiful soup to parse the object.

the  next step was to visit the websitte and inspect the page and determine the table to extract the data from.
I then created a list called tables to hold all the table tag in the page ('tbody')
I then created another list call rows to hold all the rows in the table table. the row have the tag 'tr'

Then the df is saved as csv file and also saved in a db using sqlite3 aas seen in the webscraping.py file



