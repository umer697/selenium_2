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
driver.get("https://www.flipkart.com/samsung-galaxy-fit3-amoled-display-aluminium-body-upto-13day-battery-5atm-ip68/p/itmc884180dbd9a8?pid=SMWGY6YRNHBBK8FP&lid=LSTSMWGY6YRNHBBK8FPDPQEGB&marketplace=FLIPKART&srno=s_1_33&otracker=search&otracker1=search&fm=Search&iid=226e103e-2f95-480f-aa88-43f968ed1637.SMWGY6YRYKY3GXQU.SEARCH&ppt=sp&ppn=sp&ssid=2mm4kdaxzk0000001734019004923&qH=87968ec020b2016b")

watch_name =  driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span').text
watch_price =  driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]').text
mrp_price =  driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[2]').text
discount =  driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[3]/span').text
stars = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]/div').text
rating = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1]').text
reviews = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3]').text

print("-----------------------------------------------------------------------------------------------------------")
print("Watch Name = ",watch_name)
print("Watch Price = ",watch_price)
print("Watch MRP Price = ",mrp_price)
print("Watch Discount = ",discount)
print("Start = ",stars)
print("Ratings = ",rating)
print("Number of Reviews = ",reviews)
print("-----------------------------------------------------------------------------------------------------------")
