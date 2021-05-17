from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.mygov.in/covid-19'

driver = webdriver.Edge(r'msedgedriver.exe')
driver.get(url)

timeout = 30

#
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="statewise-data"]/a[1]')))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()

button1 = driver.find_element(By.XPATH,'//*[@id="statewise-vaccine-data"]/a[1]')
button1.click()

button2 = driver.find_element(By.XPATH,'//*[@id="statewise-data"]/a[1]')
button2.click()


js= '''var remove_up = document.getElementsByClassName('data-up');
    for(var i = i=remove_up.length-1;i >= 0;i--){
    remove_up[i].parentNode.removeChild(remove_up[i])
    }
    var remove_down = document.getElementsByClassName('data-down');
    for(var i = i=remove_down.length-1;i >= 0;i--){
    remove_down[i].parentNode.removeChild(remove_down[i])
    }
    '''

driver.execute_script(js)

soup = BeautifulSoup(driver.page_source,'html.parser')
vaccine_stats = [] 
vaccine_rows = soup.find_all('tr')

extract_contents = lambda row: [x.text.replace(',', '') for x in row]

for row in vaccine_rows:
    stat = extract_contents(row.find_all('td')) 
    if len(stat) == 5:
        vaccine_stats.append(stat)

#print(vaccine_stats)
vaccine_col = ['State_UT','Dose_1','Dose_2','Total_Vaccination','Total_Vaccination_Yesterday']
state_vaccine_data = pd.DataFrame(data = vaccine_stats, columns = vaccine_col)


state_vaccine_data['Dose_1'] = state_vaccine_data['Dose_1'].map(int)
state_vaccine_data['Dose_2'] = state_vaccine_data['Dose_2'].map(int)
state_vaccine_data['Total_Vaccination'] = state_vaccine_data['Total_Vaccination'].map(int)
state_vaccine_data['Total_Vaccination_Yesterday'] = state_vaccine_data['Total_Vaccination_Yesterday'].map(int)


state_cols = ['State_UT','Total_Cases','Active_Cases','Recovered','Deaths','Active Ratio','Recovered Ratio','Death Ratio']
cases_stats = [] 
cases_rows = soup.find_all('tr')

for row in cases_rows:
    stat = extract_contents(row.find_all('td')) 
    if len(stat) == 8:
        cases_stats.append(stat)

#print(cases_stats)
state_cases_data = pd.DataFrame(data = cases_stats, columns = state_cols)


state_cases_data['Total_Cases'] = state_cases_data['Total_Cases'].map(int)
state_cases_data['Active_Cases'] = state_cases_data['Active_Cases'].map(int)
state_cases_data['Recovered'] = state_cases_data['Recovered'].map(int)
state_cases_data['Deaths'] = state_cases_data['Deaths'].map(int)

state_cases_data['State_UT'] = state_cases_data['State_UT'].replace(['Telengana'],'Telangana')

dataset = pd.merge(state_vaccine_data,state_cases_data, on='State_UT')

state_vaccine_data.to_csv('./dash/static/data/'+'state_vaccine_data.csv')
state_cases_data.to_csv('./dash/static/data/'+'state_cases_data.csv')
dataset.to_csv(r'./dash/static/data/'+'dataset.csv')

driver.quit()
