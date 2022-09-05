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


def clear():
    os.system('clear')


def get_enerflo_url():
    clear()

    print("What is the enerflo URL?")
    enerflo_url = input()
    return enerflo_url


def login_everbright():
    driver.get(everbright_url)
    user_field = driver.find_element(By.ID, "authEmail")
    pass_field = driver.find_element(By.ID, "authPassword")
    log_in_button = driver.find_element(By.TAG_NAME, "button")

    user_field.send_keys(USERNAME)
    pass_field.send_keys(PASSWORD)
    time.sleep(2)
    log_in_button.click()


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


def has_numbers(string):
    return any(char.isdigit() for char in string)


def get_customer_info(element_text):
    customer_info = []
    customer_name = []
    customer_address = []
    slice_index = 0

    for val in element_text.split():
        if val.find('@') != -1 or val.find('(') != -1:
            break

        customer_info.append(val)

    for index, val in enumerate(customer_info):
        if has_numbers(val):
            slice_index = int(index)
            break

    customer_name = ' '.join(customer_info[:slice_index])
    customer_address = ' '.join(customer_info[slice_index:])

    return (customer_name, customer_address)

# initialize bot


enerflo_url = get_enerflo_url()
driver = webdriver.Chrome(service=s)

driver.get(enerflo_url)
login_enerflo()

time.sleep(2)
customer_info_text = driver.find_element(
    By.XPATH, '/html/body/div[1]/main/div[3]/div/div[7]/div[1]/div[1]/div/div[1]/h5').text


# TODO refactor info object (solar design with name and address attributes)

customer_name, customer_address = get_customer_info(customer_info_text)

print(customer_name, customer_address)

open_tab()
login_everbright()


# wait 3 seconds before quit
time.sleep(3)
driver.quit()
