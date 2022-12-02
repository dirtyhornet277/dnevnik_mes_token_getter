from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def get_token(login, password):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://login.mos.ru/sps/login/methods/password?bo=/sps/oauth/ae?response_type=code%26access_type=offline%26client_id=dnevnik.mos.ru%26scope=openid+profile+birthday+contacts+snils+blitz_user_rights+blitz_change_password%26redirect_uri=https%3A%2F%2Fschool.mos.ru%2Fv3%2Fauth%2Fsudir%2Fcallback")
    time.sleep(2)
    login_input = driver.find_element(By.XPATH, '//*[@id="login"]') # type: ignore
    login_input.send_keys(login)
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys(password)
    button = driver.find_element(By.XPATH, '//*[@id="bind"]')
    button.click()
    time.sleep(1)
    return driver.get_cookie("aupd_token")["value"]
    driver.close()