from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    search_input = driver.find_element(By.CSS_SELECTOR, "button")
    search_input.click()
    sleep(3)


delete = driver.find_element(By.CSS_SELECTOR, "button.added-manually").text
print(len(delete))

print(delete)


sleep(3)
driver.quit()
