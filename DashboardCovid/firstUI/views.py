from django.shortcuts import render
from matplotlib.style import context
import pandas as pd

# Create your views here.
def indexPage(request):

    data = pd.read_csv('data/owid-covid-data.csv')
    totalCount = data.loc[data['location']=='World']['total_cases'].values[-1]

    continents = set(data['continent'])
    covidInContinents = data.loc[(data['location'].isin(continents))].groupby('location').tail(1).sort_values(by='total_cases')
    countries = covidInContinents['location'].to_list()
    counts = covidInContinents['total_cases'].to_list()

    context={'totalCount':totalCount, 'countries':countries,'counts':counts}
    return render(request, 'index.html',context)