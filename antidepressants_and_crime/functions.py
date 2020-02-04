import pandas as pd
import numpy as np
import json
import requests

def readCsv ():
    df = pd.read_csv("FOI_Request_(07853).csv")
    return df

def getCrime (x, y):

    url = f"https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date={x}-{y}"
    response = requests.get(url)
    data = response.json()
    
    return data

def years(año):
    
    counter = 0
    
    for i in range(4,13):
        counter += len(getCrime(str(año), str(i)))
    for e in range(1,4):
        counter += len(getCrime(str(año+1), str(e)))
    return counter
                       
print(f"Crime in 2017: {years(2017)}")
print(f"Crime in 2018: {years(2018)}")