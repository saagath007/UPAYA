from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
username.click()

password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
password.click()

loginb = driver.find_element(By.ID,"login-button")
loginb.click()
time.sleep(2)
menu = driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
logout = driver.find_element(By.ID, "logout_sidebar_link").click()

time.sleep(5)