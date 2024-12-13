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

##ACCESS ELEMEN BY XPATH
# input = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
# input.send_keys("facebook")
# button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
# button.click()

##ACCESS ELEMEN BY CLASS_NAME
# input = driver.find_element(By.CLASS_NAME,'gLFyf')
# input.send_keys("facebook")
# button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
# button.click()

##ACCESS ELEMEN BY TAG_NAME
# input = driver.find_element(By.TAG_NAME,'textarea').send_keys("WHATSAPP")
# button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
# button.click()

# #ACCESS ELEMEN BY TAG_NAME
# input = driver.find_element(By.NAME,'q').send_keys("instagram")
# button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
# button.click()

#partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT,'Images').click()

#LINK TEXT
# GMAIL = driver.find_element(By.LINK_TEXT,'Gmail').click()


#ID
# GMAIL = driver.find_element(By.ID)

# CSS SELECTOR
# driver.find_element(By.CSS_SELECTOR)

input = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea').send_keys('primetidings')
button = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
















