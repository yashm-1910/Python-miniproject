from django.shortcuts import render
from . import plot
import pandas as pd
import json

# Create your views here.
def cases(request):
    df1 = pd.read_csv('dash/static/data/cases_time_series.csv')
    recent_cases = df1.iloc[-1,:]

    df = pd.read_csv('dash/static/data/state_cases_data.csv')
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    return render(
        request,'dash/cases.html', 
        context={
            'plot_div1':plot.state_cases(),
            'plot_div2':plot.plot_cases_time_series('Confirmed'),
            'plot_div3':plot.plot_cases_time_series('Active'),
            'plot_div4':plot.plot_cases_time_series('Recovered'),
            'plot_div5':plot.plot_cases_time_series('Deaths'),
            'confirmed': recent_cases['Confirmed'],
            'recovered': recent_cases['Recovered'],
            'active': recent_cases['Active'],
            'deaths': recent_cases['Deaths'],
            'data': data,
            'title':'Covid-19'
            }
            
    )

def vaccine(request):
    df2 = pd.read_csv('dash/static/data/vaccine_time_series.csv')
    recent_vaccine = df2.iloc[-1,:]

    df = pd.read_csv('dash/static/data/state_vaccine_data.csv')
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    return render(
        request,'dash/vaccine.html', 
        context={
            'plot_div1':plot.state_vaccine(),
            'plot_div2':plot.plot_vaccine_time_series('Total_Vaccinations'),
            'plot_div3':plot.plot_vaccine_time_series('Dose_1'),
            'plot_div4':plot.plot_vaccine_time_series('Dose_2'),
            'Total_Vaccinations': recent_vaccine['Total_Vaccinations'],
            'Dose_1': recent_vaccine['Dose_1'],
            'Dose_2': recent_vaccine['Dose_2'],
            'data': data,
            'title':'Vaccine'
            }
    )