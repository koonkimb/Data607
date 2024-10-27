import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests
import pandas as pd
import numpy as np
import time


def get_selenium():                           
    options = webdriver.ChromeOptions()                      
    driver = webdriver.Chrome(options=options)
    return (driver)

driver = get_selenium()
##topics = ["Artificial-Intelligence-Foundations","Generative-AI","Machine-Learning","Natural-Language-Processing-nlp","Neural-Networks-and-Deep-Learning",
##          "Data-Analysis","Data-Visualization","Business-Intelligence","Tech-Career-Skills","Data-Engineering",
##          "Database-Development","Database-Administration","Data-Resource-Management","Data-Centers"]
##

topics = ["Data-Science"]
for topic in topics:
    csv_name = topic + "_links.csv"
    with open(csv_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        lines = [line.strip() for line in file]

    data = []

    for url in lines:
        driver.execute_script(f"window.open('{url}','_blank');")
        
        driver.switch_to.window(driver.window_handles[-1])
        response = requests.get(url)
        individualSoup = BeautifulSoup(response.content, 'html.parser')
        
        allData = individualSoup.find("script", {"type" : "application/ld+json"})
        data.append(allData.get_text().strip())
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])



    df = pd.DataFrame(data)
    
    filename =  topic + "_json.csv"
    df.to_csv(filename,sep =';',index=False)

driver.quit()
