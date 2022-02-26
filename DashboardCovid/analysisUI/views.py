from itertools import count
from turtle import left
from django.shortcuts import render
from matplotlib.style import context
import pandas as pd
import analysisUI.control as cnt

data, dataWithoutWorld,dataDate = cnt.readData()
countriesList = dataWithoutWorld.sort_values(by='location')['location'].to_list()
# Create your views here.
def indexPage(request):

    formatData = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    formatData.drop('value',axis=1,inplace=True)
    formatData.loc[formatData['name']=='Israel','name']='Palestine' 

    totalCases = data.loc[data['location']=='World','total_cases'].values[-1]
    newCases = data.loc[data['location']=='World','new_cases'].values[-1]
    countryWithMostCases = dataWithoutWorld['location'].values[-1]
    countryWithMostCasesDensity = dataWithoutWorld.sort_values(by='cases_density',ascending=False)['location'].values[0]
    minCases = dataWithoutWorld['total_cases'].values[0]
    maxCases = dataWithoutWorld['total_cases'].values[-1]


    dataWithoutWorld_modified = dataWithoutWorld[['location','iso_code','total_cases']]
    dataWithoutWorld_modified.columns = ['location','code3','value']
    dataWithoutWorld_modified = dataWithoutWorld_modified.merge(formatData).drop('location',axis=1)
    dataWithoutWorld_modified.dropna(subset=['value'],inplace=True)
    mapData = dataWithoutWorld_modified.to_dict('records')
    
    # continents = set(data['continent'])
    # covidInContinents = data.loc[(data['location'].isin(continents))].groupby('location').tail(1).sort_values(by='total_cases')
    # countries = covidInContinents['location'].to_list()
    # counts = covidInContinents['total_cases'].to_list()

    context={'dataDate':dataDate, 
             'totalCases':int(totalCases),
             'newCases':int(newCases),
             'mapData':mapData,
             'countryWithMostCases':countryWithMostCases,
             'countryWithMostCasesDensity':countryWithMostCasesDensity,
             'minCases': minCases,
             'maxCases': maxCases,
             'countriesList': countriesList,
             }
    return render(request, 'analysisUI/index.html',context)




def indivitualCountryData(request, country):
    print(request.POST.get('countryName'))
    if request.POST.get('countryName'):
        countryName = request.POST.get('countryName')
    else:
        countryName = country
    startDate = request.POST.get('startDate')
    print(startDate)
    print(countryName)
    
    countryData = data.loc[data['location']==countryName]
    dateList = countryData['date'].to_list()
    totalCases = countryData['total_cases'].values[-1]
    newCases = countryData['new_cases'].values[-1]
    totalCasesValues = countryData['total_cases'].to_list()
    newCasesValues = countryData['new_cases'].to_list()
    countryData[['new_deaths']] = countryData[['new_deaths']].fillna(value=0)
    newDeathsValues = countryData['new_deaths'].to_list()
    casesPer100 = (countryData['new_cases_density']*100000).to_list()
    countryTotalCount = data.loc[data['location']==countryName,'total_cases'].values[-1]
    worldCount = data.loc[data['location']=='World','total_cases'].values[-1]

    context={'dataDate':dataDate, 
             'countryName':countryName,
             'dateList':dateList,
             'totalCases':int(totalCases),
             'newCases':int(newCases),
             'totalCasesValues':totalCasesValues,
             'newCasesValues':newCasesValues,
             'newDeathsValues':newDeathsValues,
             'casesPer100':casesPer100,
             'countryTotalCount':countryTotalCount,
             'worldCount':worldCount,
             'countriesList': countriesList,
            }
    return render(request,'analysisUI/countries.html',context)