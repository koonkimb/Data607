import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

full_url = "https://www.weather.gov/buf/BuffaloSnow"
print(full_url)
page = requests.get(full_url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}).text
soup = BeautifulSoup(page, "html.parser")

tags = []
index = 0

def returnTrue(tag):
    return tag.font;

allData = soup.find_all("tr")

for i in allData:
    tags.insert(len(tags),i.get_text().strip())

df = pd.DataFrame(columns = ['SEASON','JUL','AUG','SEP','OCT','NOV','DEC','JAN','FEB','MAR','APR','MAY','JUN','ANNUAL'])

for element in tags:
    row = element.strip().split('\n')
    #print(row)
    if len(row) == 14:
        df.loc[len(df)] = row
 

df.to_csv("buffalosnow.csv",sep =';',index=False)
