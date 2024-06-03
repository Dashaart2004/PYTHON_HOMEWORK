from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get(" http://uitestingplayground.com/dynamicid")
for i in range(3):
    search_input = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    search_input.click()
    sleep(3)


driver.quit()