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


def test_shop(browser):
    browser.get("https://www.saucedemo.com/")
    WebDriverWait(browser, 40)
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
    browser.find_element(By.ID, "checkout").click()
    browser.find_element(By.ID, "first-name").send_keys("Даша")
    browser.find_element(By.ID, "last-name").send_keys("Артюнина")
    browser.find_element(By.ID, "postal-code").send_keys("180016")
    browser.find_element(By.ID, "continue").click()

    result = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_price = result.text.strip().replace("Total: $", "")

    expected_local = "58.29"
    assert total_price == expected_local
    print(f"Итого = ${total_price}")
