import pandas as pd

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
death = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

#adjusting the column dates as a single date column
dates = confirmed.columns[4:]

confirmed_df_long = confirmed.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Confirmed'
)

deaths_df_long = death.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Deaths'
)

recovered_df_long = recovered.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    value_vars=dates, 
    var_name='Date', 
    value_name='Recovered'
)

# Merging confirmed_df_long and deaths_df_long
full_table = confirmed_df_long.merge(
  right=deaths_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)
# Merging full_table and recovered_df_long
full_table = full_table.merge(
  right=recovered_df_long, 
  how='left',
  on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long']
)


#creating a dataframe for India
time_series = full_table.loc[full_table['Country/Region']=='India'].copy()

#resetting index
time_series.reset_index(drop=True, inplace=True)
#dropping unwanted columns
time_series.drop(['Province/State','Lat','Long'], axis = 1, inplace=True)


time_series['Date'] = pd.to_datetime(time_series['Date'])
time_series['Recovered'] = time_series['Recovered'].fillna(0).astype(int)


#calculating active cases
time_series['Active'] = time_series['Confirmed']-time_series['Recovered']-time_series['Deaths']


#daily new cases, deaths, recovered, total
time_series['Daily Confirmed'] = time_series['Confirmed'].diff().fillna(0).astype(int).apply(lambda x: 0 if x<0 else x)
time_series['Daily Deaths'] = time_series['Deaths'].diff().fillna(0).astype(int).apply(lambda x: 0 if x<0 else x)
time_series['Daily Recovered'] = time_series['Recovered'].diff().fillna(0).astype(int).apply(lambda x: 0 if x<0 else x)
time_series['Daily Active'] = time_series['Active'].diff().fillna(0).astype(int).apply(lambda x: 0 if x<0 else x)


#exporting csv
time_series.to_csv(r'./dash/static/data/'+'cases_time_series.csv')

