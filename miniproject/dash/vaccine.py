import pandas as pd

in_vaccine = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/India.csv')

in_vaccine['date'] = pd.to_datetime(in_vaccine['date'])
in_vaccine = in_vaccine.rename(columns={'total_vaccinations':'Total_Vaccinations','people_vaccinated':'Dose_1','people_fully_vaccinated':'Dose_2'})

in_vaccine['Daily_Total_Vaccinations'] = in_vaccine['Total_Vaccinations'].diff().fillna(0).astype(int)
in_vaccine['Daily_Dose_1'] = in_vaccine['Dose_1'].diff().fillna(0).astype(int)
in_vaccine['Daily_Dose_2'] = in_vaccine['Dose_2'].diff().fillna(0).astype(int)

in_vaccine.to_csv(r'./dash/static/data/'+'vaccine_time_series.csv')
