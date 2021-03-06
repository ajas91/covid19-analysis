from tkinter import font
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read Covid-19 Dataset
data = pd.read_csv('DashboardCovid/data/owid-covid-data.csv')
formatData = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
formatData.drop('value',axis=1,inplace=True)

dataWithoutWorld = data.copy()
dataWithoutWorld = dataWithoutWorld.loc[~(dataWithoutWorld['continent'].isna())].groupby('location').tail(1).sort_values(by='total_cases',ascending=True).dropna(subset=['total_cases'])
dataDate = dataWithoutWorld.iloc[0]['date']
total_cases = data.loc[data['location']=='World','total_cases'].values[-1]
new_cases = data.loc[data['location']=='World','new_cases'].values[-1]
countryData = data.loc[data['location']=='Oman']

dataWithoutWorld = dataWithoutWorld[['location','iso_code','total_cases']]
dataWithoutWorld.columns = ['name','code3','value']
dataWithoutWorld = dataWithoutWorld.merge(formatData)
dataWithoutWorld.sort_values(by='name')['name'].to_clipboard()
# print(dataWithoutWorld.sort_values(by='name')['name'].to_list())
# print(formatData.head(5))
# print(dataWithoutWorld.sort_values(by='name').head(5).to_dict('records'))
# print(countryData.pivot_table(index = 'date',values = 'new_cases').reset_index())

# TOP 15 Countries with COVID-19 Cases
# dataWithoutContinent = topCountries = data.loc[~(data['continent'].isna())].groupby('location').tail(1).sort_values(by='total_cases',ascending=True).dropna(subset=['total_cases'])
# topCountries = dataWithoutContinent.tail(15)

# plt.style.use('seaborn')
# plt.barh(topCountries['location'],topCountries['total_cases']/1000000)

# plt.suptitle('Top 15 Countries with COVID-19 Cases as of 27/01/2022')
# plt.ylabel('Country')
# plt.xlabel('Number of Total Cases in Millions')

# plt.grid(visible=True, which='major', axis='both')
# plt.tight_layout()

# plt.savefig('figures/topCountries.png')
# plt.close()

# # COVID-19 Cases by Continents
# plt.style.use('seaborn')
# continents = set(data['continent'])
# explode = (0.03,0.03,0.03,0.03,0.03,0.03)
# covidInContinents = data.loc[(data['location'].isin(continents))].groupby('location').tail(1).sort_values(by='total_cases')
# plt.pie(covidInContinents['total_cases'],labels=covidInContinents['location'],autopct='%.1f%%', explode=explode)

# plt.suptitle('COVID-19 Cases by continents as of 27/01/2022')
# plt.tight_layout()

# plt.savefig('figures/byContinents.png')
# plt.close()

# # Top Countries with COVID-19 Cases in 100 people
# casesByDensity = dataWithoutContinent.loc[:,['date','location','total_cases','population']]
# casesByDensity['cases_density'] = casesByDensity['total_cases']/casesByDensity['population']
# casesByDensity.sort_values(by='cases_density',inplace=True)
# casesByDensity = casesByDensity.tail(15)

# plt.style.use('seaborn')
# plt.barh(casesByDensity['location'],casesByDensity['cases_density']*100)
# plt.ylabel('Country')
# plt.xlabel('Number of Cases in 100 people')

# plt.suptitle('Top Countries with COVID-19 Cases in 100 people as of 27/01/2022')
# plt.tight_layout()

# plt.savefig('figures/topCountriesIn100.png')
# plt.close()

# # Gulf Countries Cases per 100  people
# gulfCountries = ['Oman','Qatar','Bahrain','United Arab Emirates','Kuwait','Saudi Arabia']
# casesInGulf = dataWithoutContinent.loc[(dataWithoutContinent['location'].isin(gulfCountries)),
#                                        ['date','location','total_cases','population']]
# casesInGulf['cases_density'] = casesInGulf['total_cases']/casesInGulf['population']
# casesInGulf.sort_values(by='cases_density',inplace=True)

# plt.style.use('seaborn')
# plt.barh(casesInGulf['location'],casesInGulf['cases_density']*100)
# plt.ylabel('Country')
# plt.xlabel('Number of Cases in 100 people')

# plt.suptitle('Gulf Countries Cases per 100  people')
# plt.savefig('figures/gulfCountriesDensity.png')
# plt.close()

# # Gulf Countries Total Cases
# casesInGulf.sort_values(by='total_cases',inplace=True)

# plt.style.use('seaborn')
# plt.barh(casesInGulf['location'],casesInGulf['total_cases']/1000000)
# plt.ylabel('Country')
# plt.xlabel('Number of Total Cases in Million')

# plt.suptitle('Gulf Countries Total Cases')
# plt.savefig('figures/gulfCountriesCases.png')
# plt.close()

# # Gulf Countries cases Desnsity by date
# fullCasesInGulf = data.loc[(data['location'].isin(gulfCountries))]
# fullCasesInGulf['cases_density'] = fullCasesInGulf['total_cases']/fullCasesInGulf['population']*100

# pivotTabCases = fullCasesInGulf.pivot_table(index = 'date',values = 'cases_density',columns= 'location')
# pivotTabCases.plot()

# plt.ylabel('Cases Density')
# plt.xlabel('Date')
# plt.legend()
# plt.grid(visible=True, which='major', axis='both')

# plt.suptitle('Gulf Countries Cases per 100  people')
# plt.gcf().autofmt_xdate()
# plt.savefig('figures/gulfCountriesCasesPer100.png')
# plt.close()