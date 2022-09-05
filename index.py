from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


s = Service('/Users/eromelus/Desktop/solarbot/chromedriver')
everbright_url = "https://engine.goeverbright.com/usage/93d18200-28dd-49d6-9a47-ee8bfb5f1dd9"

USERNAME = "edwinsromelus@gmail.com"
PASSWORD = "Codingjefe12!"


# Logs into Everbright


def login_everbright():
    driver.get(everbright_url)
    user_field = driver.find_element(By.ID, "authEmail")
    pass_field = driver.find_element(By.ID, "authPassword")
    log_in_button = driver.find_element(By.TAG_NAME, "button")

    user_field.send_keys(USERNAME)
    pass_field.send_keys(PASSWORD)
    time.sleep(2)
    log_in_button.click()

# Logs into Enerflo


def login_enerflo():
    user_field = driver.find_element(By.ID, "email")
    next_button = driver.find_element(By.ID, "ssoCheck")
    user_field.send_keys(USERNAME)

    next_button.click()
    time.sleep(2)

    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys(PASSWORD)
    log_in_button = driver.find_element(
        By.XPATH, '//*[@id="loginBlock"]/div/button')
    time.sleep(2)
    log_in_button.click()


def open_tab():
    driver.switch_to.new_window('tab')


os.system('clear')
print("What is the enerflo URL?")
enerflo_url = input()

driver = webdriver.Chrome(service=s)

login_everbright()
open_tab()
driver.get(enerflo_url)
login_enerflo()


driver.quit()
