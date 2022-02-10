from tkinter import font
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read Covid-19 Dataset
data = pd.read_csv('data/owid-covid-data.csv')

# TOP 15 Countries with COVID-19 Cases
topCountries = data.loc[~(data['continent'].isna())].groupby('location').tail(1).sort_values(by='total_cases',ascending=True).dropna(subset=['total_cases']).tail(15)

plt.style.use('seaborn-darkgrid')
plt.barh(topCountries['location'],topCountries['total_cases']/1000000)

plt.suptitle('Top 15 Countries with COVID-19 Cases as of 27/02/2022')
plt.ylabel('Country')
plt.xlabel('Number of Total Cases in Millions')

plt.grid(visible=True, which='major', axis='both')
plt.tight_layout()

plt.savefig('figures/topCountries.png')
plt.show()