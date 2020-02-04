from functions.py import *

def titles ():

    df.columns = df.columns.str.title()
    df.columns = df.columns.str.strip()
    return df

def drop ():
    df = df.drop(columns = ["Practice Code", "Practice Name", "Drug Group"], axis=1)
    return df

def rename ():
    df = df.rename(columns={'Ccg': 'Clinical Commissioning Groups', 'No. Of Identifiable Patients': 'Number Of Patients', 'No. Of Items Prescribed To Identifiable Patients': 'Items Prescribed'})
    return df