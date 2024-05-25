from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(" http://uitestingplayground.com/dynamicid")
for i in range(3):
    search_input = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    search_input.click()
    sleep(3)


driver.quit()
