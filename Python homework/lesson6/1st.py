from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# FireFox = webdriver.Firefox(  
# service=FirefoxService(GeckoDriverManager().install()))
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))\


# def make_screenshot(browser):
#     browser.maximize_window()
#     browser.get("https://ya.ru/")
#     sleep(3)
#     browser.save_screenshot("./ya_"+browser.name+".png")
#     browser.quit()


# make_screenshot(FireFox)
# make_screenshot(Chrome)

# Chrome.get("https://ya.ru/")

# current_title = Chrome.title
# print(current_title)

# Chrome.quit()

# Chrome.get("http://ya.ru/")
# url = Chrome.current_url
# print(url)
# 

Chrome.maximize_window()
Chrome.minimize_window()
Chrome.fullscreen_window()

