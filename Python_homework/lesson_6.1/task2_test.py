import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_information(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    browser.find_element(By.XPATH, "//span[text() = '7']").click()
    browser.find_element(By.XPATH, "//span[text() = '+']").click()
    browser.find_element(By.XPATH, "//span[text() = '8']").click()
    browser.find_element(By.XPATH, "//span[text() = '=']").click()
    WebDriverWait(browser, 46).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)
    result_text = browser.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"
