# Ikariam script
# Made by vukasiN.
# 13.03.2018

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Username
user = "@gmail.com"

# Password
pwd = "password"

# Chrome Driver
driverpath = "location for chromedriver.exe"

# Open Chrome
driver = webdriver.Chrome(driverpath)
driver.maximize_window()

# Open website
driver.get("https://ikariam.gameforge.com/")
time.sleep(3)

# Login
button1 = driver.find_element_by_xpath("//*[@id='btn-login']").click()
time.sleep(1)

scrooldown = driver.find_element_by_xpath("//*[@id='logServer']").send_keys("Theta")
time.sleep(1)

email = driver.find_element_by_id("loginName").send_keys(user)
time.sleep(1)

sifra = driver.find_element_by_id("loginPassword").send_keys(pwd)
time.sleep(1)

dugme = driver.find_element_by_id("loginBtn").click()
time.sleep(3)

# Click on object
tvrdjava = driver.find_element_by_xpath("//*[@id='js_CityPosition17Link']").click()
time.sleep(2)

tvrdjava2 = driver.find_element_by_xpath("//*[@id='pirateCaptureBox']/div[1]/table/tbody/tr[1]/td[5]/a").click()
time.sleep(5)

# Close web browser
driver.close()
