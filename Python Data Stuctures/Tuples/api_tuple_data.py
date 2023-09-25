import numpy as np
import pandas as pd

# Website
website = ['https://apipheny.io/free-api/#apis-without-key']

# Api's
mlb_api = ['https://appac.github.io/mlb-data-api-docs/#game-data']
flight_api = ['https://travelpayouts.github.io/slate/?shell#']
airlines_data_api = ['https://rapidapi.com/vacationist/api/iata-and-icao-codes/details']

# Test Endpoints
test_endpoints = ("https://api.coindesk.com/v1/bpi/currentprice.json","https://datausa.io/api/data?drilldowns=Nation&measures=Population",
             "https://api.zippopotam.us/us/33162") # tuple data structure
print(test_endpoints[0])
print(type(test_endpoints[0]))

# Api's (data container)
api_tup = (mlb_api,flight_api,airlines_data_api)
print(api_tup[-1])
print(type(api_tup[-1]))

# add (api) to tuple
x = ['https://site.financialmodelingprep.com/developer/docs/']
xy = list(api_tup) # convert tuple to list
xy.append(x) 
#
print("")
print(xy)
print(type(xy))

# convert list -> tuple (after main tuple updated)
api_tup = tuple(xy)
print("")
print(api_tup)
print(type(api_tup))
# 





