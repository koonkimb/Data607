import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

full_url = "https://vlab.noaa.gov/web/mdl/historic-storms"
print(full_url)
page = requests.get(full_url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}).text
soup = BeautifulSoup(page, "html.parser")

pre_tags = []
index = 0

allData = soup.find_all('pre')

for i in allData:
    pre_tags.insert(len(pre_tags),i.get_text().strip())
    index += 1

num_rows = int(index/7)
num_columns = 7

df = pd.DataFrame(np.array(pre_tags).reshape(num_rows, num_columns))

df.columns = ['Storm','Date','Storm-Tide','Obs','Guidance','Cat,Pres,Dead,$bn','Area']

df.to_csv("stormdata.csv",sep =';',index=False)

