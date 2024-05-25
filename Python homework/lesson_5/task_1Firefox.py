from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    search_input = driver.find_element(By.CSS_SELECTOR, "button")
    search_input.click()
    sleep(3)


delete = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(delete))
for button in delete:
	print(button.text)

sleep(3)
driver.quit()
