from tkinter import font
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read Covid-19 Dataset
data = pd.read_csv('data/owid-covid-data.csv')

# TOP 15 Countries with COVID-19 Cases
dataWithoutContinent = topCountries = data.loc[~(data['continent'].isna())].groupby('location').tail(1).sort_values(by='total_cases',ascending=True).dropna(subset=['total_cases'])
topCountries = dataWithoutContinent.tail(15)

plt.style.use('seaborn')
plt.barh(topCountries['location'],topCountries['total_cases']/1000000)

plt.suptitle('Top 15 Countries with COVID-19 Cases as of 27/01/2022')
plt.ylabel('Country')
plt.xlabel('Number of Total Cases in Millions')

plt.grid(visible=True, which='major', axis='both')
plt.tight_layout()

plt.savefig('figures/topCountries.png')
plt.close()

# COVID-19 Cases by Continents
plt.style.use('seaborn')
continents = set(data['continent'])
explode = (0.03,0.03,0.03,0.03,0.03,0.03)
covidInContinents = data.loc[(data['location'].isin(continents))].groupby('location').tail(1).sort_values(by='total_cases')
plt.pie(covidInContinents['total_cases'],labels=covidInContinents['location'],autopct='%.1f%%', explode=explode)

plt.suptitle('COVID-19 Cases by continents as of 27/01/2022')
plt.tight_layout()

plt.savefig('figures/byContinents.png')
plt.close()

# Top Countries with COVID-19 Cases in 100 people
casesByDensity = dataWithoutContinent.loc[:,['date','location','total_cases','population']]
casesByDensity['cases_density'] = casesByDensity['total_cases']/casesByDensity['population']
casesByDensity.sort_values(by='cases_density',inplace=True)
casesByDensity = casesByDensity.tail(15)

plt.barh(casesByDensity['location'],casesByDensity['cases_density']*100)
plt.ylabel('Country')
plt.xlabel('Number of Cases in 100 people')

plt.suptitle('Top Countries with COVID-19 Cases in 100 people as of 27/01/2022')
plt.tight_layout()

plt.savefig('figures/topCountriesIn100.png')
plt.close()