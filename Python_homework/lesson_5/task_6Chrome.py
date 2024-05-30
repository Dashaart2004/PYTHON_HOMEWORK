from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
username.click()
username.send_keys("tomsmith")
sleep(3)


password = driver.find_element(By.ID, "password")
password.click()
password.send_keys("SuperSecretPassword!")
sleep(3)

button_login = driver.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in")
button_login.click()
