from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

#statewise cases
def state_cases():
    states = json.load(open('./dash/static/data/states_india.geojson','r'))
    cases_stats = pd.read_csv('./dash/static/data/state_cases_data.csv')

    fig = px.choropleth_mapbox(
        cases_stats,
        geojson=states,
        featureidkey='properties.ST_NM',
        locations='State_UT', color='Active_Cases',
        hover_name = 'State_UT',
        hover_data={'State_UT':False,'Active_Cases':False,'Active_Cases':':.3s','Recovered':':.3s','Deaths':':.3s','Total_Cases':':.3s'},
        color_continuous_scale='blues',
        mapbox_style="carto-positron",
        zoom=3.1, center = {"lat": 22.0000, "lon": 82.0000},
        opacity=0.5,
        #height=600
        #labels={'Dose_1':'First Dose','Dose_2':'Second Dose'}
    )
    fig.update_layout(margin={"r":0,"t":15,"l":0,"b":0})
    plt_div = plot(fig, output_type='div',config={'responsive': True})
    return plt_div


#statewise vaccine
def state_vaccine():
    states = json.load(open('./dash/static/data/states_india.geojson','r'))
    vaccine_stats = pd.read_csv('./dash/static/data/state_vaccine_data.csv')

    fig = px.choropleth_mapbox(
        vaccine_stats,
        geojson=states,
        featureidkey='properties.ST_NM',
        locations='State_UT', color='Total_Vaccination',
        hover_name = 'State_UT',
        hover_data={'State_UT':False,'Total_Vaccination':False,'Total_Vaccination':':.3s','Dose_1':':.3s','Dose_2':':.3s'},
        color_continuous_scale='blues',
        mapbox_style="carto-positron",
        zoom=3, center = {"lat": 22.0000, "lon": 82.0000},
        opacity=0.5,
        #height=600
        #labels={'Dose_1':'First Dose','Dose_2':'Second Dose'}
    )
    fig.update_layout(margin={"r":0,"t":15,"l":0,"b":0})
    plt_div = plot(fig, output_type='div',config={'responsive': True})
    return plt_div

def plot_cases_time_series(col1):
    time_series = pd.read_csv('./dash/static/data/cases_time_series.csv')
    fig = px.line(time_series,x='Date',y=col1)

    fig.update_layout(

        hovermode='x unified',
        updatemenus=[
            dict(
                type = "buttons",
                showactive=True,
                direction = "left",
                buttons=list([
                    dict(
                        args=[{"yaxis.type": "linear"}],
                        label="LINEAR",
                        method="relayout"
                    ),
                    dict(
                        
                        args=[{"yaxis.type": "log"}],
                        label="LOG",
                        method="relayout"
                    ),
                    dict(
                        args=[{'y':[time_series[col1]]}],
                        label="Cumulative",
                        method="update"
                    ),
                    dict(
                        args=[{'y':[time_series['Daily '+col1]]}],
                        label="Daily",
                        method="update"
                    )
                
                ]),
                pad={"r": 10, "t": 10},
                x=0,
                xanchor="left",
                y=1.2,
                yanchor="top"
            ),
        ]
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(margin={"r":0,"t":25,"l":0,"b":0})
    plt_div = plot(fig, output_type='div',config={'responsive': True})
    return plt_div

def plot_vaccine_time_series(col1):
    time_series = pd.read_csv('./dash/static/data/vaccine_time_series.csv')
    fig = px.line(time_series,x='date',y=col1)

    fig.update_layout(

        hovermode='x unified',
        updatemenus=[
            dict(
                type = "buttons",
                showactive=True,
                direction = "left",
                buttons=list([
                    dict(
                        args=[{"yaxis.type": "linear"}],
                        label="LINEAR",
                        method="relayout"
                    ),
                    dict(
                        
                        args=[{"yaxis.type": "log"}],
                        label="LOG",
                        method="relayout"
                    ),
                    dict(
                        args=[{'y':[time_series[col1]]}],
                        label="Cumulative",
                        method="update"
                    ),
                    dict(
                        args=[{'y':[time_series['Daily_'+col1]]}],
                        label="Daily",
                        method="update"
                    )
                
                ]),
                pad={"r": 10, "t": 10},
                x=0,
                xanchor="left",
                y=1.2,
                yanchor="top"
            ),
        ]
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(margin={"r":0,"t":25,"l":0,"b":0})
    plt_div = plot(fig, output_type='div',config={'responsive': True})
    return plt_div

