# import required libraries
import numpy as np
import pandas as pd

#Create Dataframe from CSV file & parse dates
data = pd.read_excel('file_name_cleaned.xlsx', parse_dates = True)
#create copy of orginal dataframe
data_copy = data.copy(deep = True)

# pull out metdata into seperate dataframe
data['DateUpdate'] = data['Date'].str.split('T') # split pandas dataframe column based on sring value
data['Clusters'] = data['Host'].str.split('-bb-')
metadata = pd.DataFrame(data['DateUpdate'].to_list(), columns=['DATE','TIME']) # create new df and convert 
metadata = pd.DataFrame(data['Clusters'].to_list(), columns=['Cluster','EngineNode']) 

# drop columns
data.drop(['DateUpdate'], axis=1, inplace=True)
data.drop(['Host'], axis=1, inplace=True)
data.drop(['Clusters'], axis=1, inplace=True)

# add metadata to original dataframe
data['Cluster'] = metadata['Cluster']
data['EngineNode'] = metadata['EngineNode']

#covert 'Date' column object to datetime object
data['Date'] = pd.to_datetime(data['Date'])

# strng strip (remove right side of string required string removal in comma's)
data['SaveTime'] = data['SaveTime'].str.rstrip('ms')
data['SendTime'] = data['SendTime'].str.rstrip('ms')
data['TotalTime'] = data['TotalTime'].str.rstrip('ms')

# Data Type Conversion 
data['FixtureID'] = data['Fixture'].astype('object') 
data['SaveTime'] = data['SaveTime'].astype('int')
data['SendTime'] = data['SendTime'].astype('int')
data['TotalTime'] = data['TotalTime'].astype('int')

# remove white space
data['Client'] = data['Client'].str.strip()

# new column seconds = 1ms / 1000
data['TotalSeconds'] = data['TotalTime'] / 1000
