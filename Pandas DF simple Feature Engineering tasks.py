# import required libraries
import numpy as np
import pandas as pd

#Create Dataframe from CSV file & parse dates
bets = pd.read_excel('file_name_cleaned.xlsx', parse_dates = True)
#create copy of orginal dataframe
data_copy = bets.copy(deep = True)

# pull out metdata into seperate dataframe
bets['DateUpdate'] = bets['Date'].str.split('T') # split pandas dataframe column based on sring value
bets['Clusters'] = bets['Host'].str.split('-bb-')
metadata = pd.DataFrame(bets['DateUpdate'].to_list(), columns=['DATE','TIME']) # create new df and convert 
metadata = pd.DataFrame(bets['Clusters'].to_list(), columns=['Cluster','EngineNode']) 

# drop columns
bets.drop(['DateUpdate'], axis=1, inplace=True)
bets.drop(['Host'], axis=1, inplace=True)
bets.drop(['Clusters'], axis=1, inplace=True)

# add metadata to original dataframe
bets['Cluster'] = metadata['Cluster']
bets['EngineNode'] = metadata['EngineNode']

#covert 'Date' column object to datetime object
bets['Date'] = pd.to_datetime(bets['Date'])