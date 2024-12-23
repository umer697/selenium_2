from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
# Open a website
driver.implicitly_wait(5)
driver.get("https://google.com")

input = driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
input.send_keys("facebook")

search_button = driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()