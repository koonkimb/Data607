import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   
import requests
import pandas as pd
import numpy as np
import time

def get_selenium():                           
    options = webdriver.ChromeOptions()                      
    driver = webdriver.Chrome(options=options)
    return (driver)

driver = get_selenium()

time.sleep(1)

full_url = "https://mobalytics.gg/tft/team-comps"
driver.get(full_url)

scroll_pause_time = 2 # Pause between each scroll
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
# Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, "html.parser")

index = 0

allData = soup.find_all("div", {"class" : "m-1hi5yi4"})

row = []
champ_list = []
data = []

for i in allData:
    comp_name = i.find("a", {"class" : "m-tyi664"})
    row.append(comp_name.get_text())
    comp_patch = i.find("div", {"class" : "m-ttncf1"})
    row.append(comp_patch.get_text())
    comp_type = comp_patch.next_sibling
    row.append(comp_type.get_text())
    comp_rating = i.find("img", {"class" : "m-jmopu0"})
    row.append(comp_rating.attrs["alt"])
    champions = i.find_all("div", {"class" : "m-1lpv2x1"})
    for j in champions:
        champ = j.get_text()
        champ_list.append(champ)
    row.append(champ_list)
    data.append(row)
    row = []
    champ_list = []


df = pd.DataFrame(data)

filename = "top_comps.csv"
df.to_csv(filename,sep =';',index=False)

driver.quit()
