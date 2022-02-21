from turtle import left
from django.shortcuts import render
from matplotlib.style import context
import pandas as pd
import firstUI.control as cnt

# Create your views here.
def indexPage(request):

    formatData = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    formatData.drop('value',axis=1,inplace=True)
    formatData.loc[formatData['name']=='Israel','name']='Palestine' 

    data, dataWithoutWorld,dataDate = cnt.readData()
    totalCases = data.loc[data['location']=='World','total_cases'].values[-1]
    newCases = data.loc[data['location']=='World','new_cases'].values[-1]
    countryWithMostCases = dataWithoutWorld['location'].values[-1]
    countryWithMostCasesDensity = dataWithoutWorld.sort_values(by='cases_density',ascending=False)['location'].values[0]
    minCases = dataWithoutWorld['total_cases'].values[0]
    maxCases = dataWithoutWorld['total_cases'].values[-1]


    dataWithoutWorld = dataWithoutWorld[['location','iso_code','total_cases']]
    dataWithoutWorld.columns = ['location','code3','value']
    dataWithoutWorld = dataWithoutWorld.merge(formatData).drop('location',axis=1)
    mapData = dataWithoutWorld.to_dict('records')
    countriesList = dataWithoutWorld.sort_values(by='name')['name'].to_list()
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
    return render(request, 'index.html',context)




def indivitualCountryData(request):
    data, dataWithoutWorld,dataDate = cnt.readData()
    countryName = request.POST.get('countryName')
    
    countryData = data.loc[data['location']==countryName]
    dateList = countryData['date'].to_list()
    totalCasesValues = countryData['total_cases'].to_list()
    newCasesValues = countryData['new_cases'].to_list()
    casesPer100 = (countryData['new_cases_density']*100000).to_list()
    countryTotalCount = data.loc[data['location']==countryName,'total_cases'].values[-1]
    worldCount = data.loc[data['location']=='World','total_cases'].values[-1]
    print(dateList)
    context={'dataDate':dataDate, 
             'dateList':dateList,
             'totalCasesValues':totalCasesValues,
             'newCasesValues':newCasesValues,
             'casesPer100':casesPer100,
             'countryTotalCount':countryTotalCount,
             'worldCount':worldCount,
            }
    return render(request,'countries.html',context)