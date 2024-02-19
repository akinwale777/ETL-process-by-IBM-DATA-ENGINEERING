# The code in this folder show a practical steps oof how to create an ETL process to extract data from JSON, CSV and XML files, and transform and load them into a single CSV file for analysis

The steps that can be followed to achieve this are stated bellow.
the files to extract from were gotteen from the web by running this code in the terminal.
This i did by first runing the code 
# brew install wget
on my terminal. This allows me todownload file from the internet.

# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip 

after the Download, The file need to be unzip by typeing the command unzip filename

# unzip source.zip

Then i installed all the library i will need in the terminal using the code
# python3 -m pip install pandas

Task one is to create the function to extract the data from the various file
then create the function where to append all the extracted files too. This will involve calling all the previous extract functions for extracting from the various files.

Task two is to create the transformation function

Task three is to the create the Log and load function

Task for is to then combined all the function for the etl process as can been seen in the etl.py code
