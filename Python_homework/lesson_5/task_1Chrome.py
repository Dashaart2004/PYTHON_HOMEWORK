from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
