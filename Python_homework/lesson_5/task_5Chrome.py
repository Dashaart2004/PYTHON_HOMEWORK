from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.TAG_NAME, "input")
input.click()
input.send_keys("1000")
sleep(3)

input.clear()

input.send_keys("999")
sleep(3)

driver.quit()
