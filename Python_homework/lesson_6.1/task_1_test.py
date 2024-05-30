from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from time import sleep
import pytest



driver.implicitly_wait(30)

def first_test(driver):
    driver.get(" https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    address = driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    zip = driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
    city = driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
    sleep()
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

zip_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")
assert zip_color == "alert py-2 alert-danger"

other_elements = driver.find_elements(By.CSS_SELECTOR, ".alert py-2 alert-success")
assert other_elements == "alert py-2 alert-success"











