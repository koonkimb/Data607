import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   
import requests
import pandas as pd
import numpy as np
import time

user = input("Enter email: ")
print("\n")
pw = input("Enter password: ")
print("\n")

def get_selenium():                           
    options = webdriver.ChromeOptions()                      
    driver = webdriver.Chrome(options=options)
    return (driver)

driver = get_selenium()
login_url = "https://www.linkedin.com/learning-login/?redirect=%2Flearning%2F%3FupsellOrderOrigin%3Ddefault_guest_learning&upsellOrderOrigin=default_guest_learning&fromSignIn=true&trk=homepage-learning_nav-header-signin"
driver.get(login_url)

email = driver.find_element(By.NAME, "email")
email.send_keys(user)
email.send_keys(Keys.RETURN)

password = driver.find_element(By.NAME, "session_password")
password.send_keys(pw)
password.send_keys(Keys.RETURN)

time.sleep(6)


topics = ["Artificial-Intelligence-Foundations","Generative-AI","Machine-Learning","Natural-Language-Processing-nlp","Neural-Networks-and-Deep-Learning",
          "Data-Analysis","Data-Visualization","Business-Intelligence","Tech-Career-Skills","Data-Engineering",
          "Database-Development","Database-Administration","Data-Resource-Management","Data-Centers"]

#full_url = "https://www.linkedin.com/learning/topics/data-analysis?u=2006794"
for topic in topics:
    full_url = "https://www.linkedin.com/learning/topics/" + topic
    driver.get(full_url)

    scroll_pause_time = 3 # Pause between each scroll
    screen_height = driver.execute_script("return window.screen.height;")  # Browser window height
    i = 1
    while True:
        # Scroll down
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time)

        # Check if reaching the end of the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if screen_height * i > scroll_height:
            try:
                button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Show more topic results'][type='button']")
                button.click()
            except:
                break
            


    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    tags = []
    index = 0

    allData = soup.find_all("div", {"class" : "lls-card-detail-card-body__main"})

    for i in allData:
        tags.insert(len(tags),i.get_text().strip())
        #print(i.get_text())

    data = []

    for element in tags:
        row = element.strip().split('\n')
        data.append(row)
     
    df = pd.DataFrame(data)


    df = df.replace(r'^\s+|\s+$','', regex=True)
    df = df.map(lambda x: np.nan if isinstance(x, str) and x.strip() == '' else x)
    df = df.dropna(axis=1, how='all')
    filename = topic + ".csv"
    df.to_csv(filename,sep =';',index=False)

driver.quit()
