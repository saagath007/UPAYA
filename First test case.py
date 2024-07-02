from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

inputval = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
inputval.send_keys("youtube")
time.sleep(2)
a=driver.find_element(By.XPATH,"//span[normalize-space()='youtube']")
a.click()
time.sleep(2)

d = driver.find_element(By.XPATH, "//h3[normalize-space()='YouTube: Home']").click()
search = driver.find_element(By.XPATH, "//input[@id='search']").send_keys("timi bhane barasinghe")
sclick = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']//div").click()
time.sleep(2)
vid = driver.find_element(By.XPATH, "//ytd-thumbnail[@class='style-scope ytd-video-renderer']//img[@class='yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded']").click()

time.sleep(5)
full = driver.find_element(By.XPATH, "//button[@title='Full screen (f)']").click()
time.sleep(50)
