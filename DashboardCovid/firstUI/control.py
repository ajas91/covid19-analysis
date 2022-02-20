import pandas as pd

def readData():
    '''
    Read COVID 19 Dataset and returns to df
    1: data read
    2: dataframe with countries only
    '''

    data = pd.read_csv('data/owid-covid-data.csv')
    data.loc[data['location']=='Israel','location']='Palestine' 
    data['cases_density'] = data['total_cases']/data['population']
    data['new_cases_density'] = data['new_cases']/data['population']
    dataWithoutWorld = data.copy()
    dataWithoutWorld = dataWithoutWorld.loc[~(dataWithoutWorld['continent'].isna())].groupby('location').tail(1) \
                        .sort_values(by='total_cases',ascending=True).dropna(subset=['total_cases'])
    dataWithoutWorld['cases_density'] = dataWithoutWorld['total_cases']/dataWithoutWorld['population']
    dataDate = dataWithoutWorld.iloc[0]['date']

    return data, dataWithoutWorld, dataDate