from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get(" http://uitestingplayground.com/classattr")
for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    blue_button.click()
    sleep(1)

    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass


driver.quit()
