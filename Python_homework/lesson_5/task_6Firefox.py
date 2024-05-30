from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

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
sleep(3)

driver.quit()
