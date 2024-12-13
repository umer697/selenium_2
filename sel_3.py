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
driver.get("https://www.google.com")

ps = driver.page_source
# print(ps)

title = driver.title 
print("Title:", title)

current_url = driver.current_url
print("Current URL",current_url)

window_position = driver.get_window_position(windowHandle='current')
print("Window Position = ",window_position)

window_rec = driver.get_window_rect()
print("Window Rect: ",window_rec)

window_size = driver.get_window_size()
print("Window Size = ",window_size)

driver.minimize_window()

driver.quit()