import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
#    options.add_argument("--headless")
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
##topics = ["Machine-Learning","Natural-Language-Processing-nlp","Neural-Networks-and-Deep-Learning",
##          "Data-Analysis","Data-Visualization","Business-Intelligence","Tech-Career-Skills","Data-Engineering",
##          "Database-Development","Database-Administration","Data-Resource-Management","Data-Centers"]

#topics = ["Generative-AI"]
#full_url = "https://www.linkedin.com/learning/design-thinking-data-intelligence"
#full_url = "https://www.linkedin.com/learning/topics/data-analysis?entityType=COURSE"

for topic in topics:
    full_url = "https://www.linkedin.com/learning/topics/" + topic + "?entityType=COURSE&u=2006794"
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
                time.sleep(6)
            except:
                break

              
    links = driver.find_elements(By.CSS_SELECTOR, "[class='ember-view entity-link']")
    unique_elements = set()
    for link in links:
            # Get the desired attribute (e.g., href) or text
            unique_key = link.get_attribute('href')  # or element.text

            # Add to the set; sets automatically handle duplicates
            unique_elements.add(unique_key)

        # Convert the set back to a list if needed
    distinct_links = list(unique_elements)

    df = pd.DataFrame(distinct_links)

    filename = topic + "_links.csv"
    df.to_csv(filename,sep =';',index=False)

driver.quit()


