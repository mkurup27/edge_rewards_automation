from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random

df = pd.read_csv('books.csv')

options = webdriver.EdgeOptions()
options.add_argument('--ignore-certificate-error')
options.add_argument('--ignore-ssl-error')
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options = options)
counter = 0

for i in df['Books'].sample(n=30):

    driver.get("https://bing.com")

    time.sleep(random.randint(2, 6))

    search = driver.find_element(by=By.ID, value='sb_form_q')
    search.send_keys(i)
    search.submit()

    time.sleep(3)

driver.quit()
