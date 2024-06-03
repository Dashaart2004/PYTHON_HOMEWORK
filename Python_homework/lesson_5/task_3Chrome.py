from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
