import urllib.request
import os

path = os.getcwd() + '/website/static/images'

url1 = 'https://mausam.imd.gov.in/Satellite/Converted/WV.gif'
r = urllib.request.urlopen(url1)
with open(path + '/WV.gif', "wb") as f:
    f.write(r.read())

url2 = 'https://mausam.imd.gov.in/Satellite/Converted/VIS.gif'
r = urllib.request.urlopen(url2)
with open(path+'/VIS.gif', "wb") as f:
    f.write(r.read())

url3 = 'https://mausam.imd.gov.in/Satellite/Converted/IR1.gif'
r = urllib.request.urlopen(url3)
with open(path + '/IR1.gif', "wb") as f:
    f.write(r.read())