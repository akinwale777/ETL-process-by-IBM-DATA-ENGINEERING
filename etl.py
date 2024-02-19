import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = 'log_file.txt'
target_file = 'transformed_data.csv'

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['name','height','weight'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name,"height":height,"weight":weight}])],ignore_index=True)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight'])

    #process all CSV files
    for csvfile in glob.glob('*.csv'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))],ignore_index=True)

    #Proceess all json file
    for jsonfile in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))],ignore_index=True)

    #process all xml file:
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))],ignore_index=True)
    
    return extracted_data

def transform(extracted_data):
    '''
    Convert inches to meters and round off to two decimal
    1 inch is 0.0254 meters
    '''
    extracted_data['height'] = round(extracted_data.height * 0.0254, 2)

    '''
    Convert pounds to kilograms and round off to two decimal
    1 pound is 0.45359237 kilograms
    '''

    extracted_data['weight'] = round(extracted_data.weight * 0.45359237, 2)

    return extracted_data

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

def log_process(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' #year-monthname-Day-Hour-Minute-Second
    now = datetime.now() #get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(log_file,"a") as f:
        f.write(timestamp + ',' + message + '\n')


# Testing ETL operations aand Log progress        
# Log the initialization of the ETL process 
log_process("ETL Job started")

# log the beginning of the Extraction process
log_process("Extract phase Started")
extracted_data = extract()

# Log the beginning of the Transformation process
log_process('Transformation process')
transformed_data = transform(extracted_data)
print("Traansformed Data")
print(transformed_data)

# Log the completion of the transformation proceess
log_process("Transformation phase Ended")

# Log the beginning of the loading process
log_process("load phase Started")
load_data(target_file,transformed_data)

#log the complettion of the Loading process
log_process("Load phase Ended")

# Log the completion of the ETL process
log_process("ETL Job Ended")
