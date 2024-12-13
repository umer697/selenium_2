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
driver.get("https://www.flipkart.com/q/smart-watches?otracker=undefined_footer_footer&page=1")


for i in range(2,26):

    try:
        watch_name_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[1]'.format(i))
        watch_name.append(watch_name_element.text)
    except:
        watch_name("")

    try:
        current_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]'.format(i))
        current_price(current_price.text)
    except:
        current_price("")

    try:
        mrp_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]'.format(i))
        mrp_price(mrp_price_element.text)
    except:
        mrp_price("")

    try:
        discount_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[3]/span'.format(i))
        discount(discount_element.text)
    except:
        discount("")

    try:
        delivery_charge_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[2]/div/div'.format(i))
        delivery_charge(delivery_charge_element.text)
    except:
        delivery_charge("")

    try:
        stars_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div'.format(i))
        stars(stars_element.text)
    except:
        stars("")

    try:
        rating_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[1]'.format(i))
        rating(rating_element.text)
    except:
        rating("")

    try:
        review_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[3]'.format(i))
        review(review_element.text)
    except:
        review("")



print("--------------------------------------------------------------------------------------")
print("Watch Name = ",watch_name)
print("Current Price = ",current_price)
print("MRP Price = ",mrp_price)
print("Discount = ",discount)
print("Delivery Charges = ",delivery_charges)
print("Starts = ",starts)
print("Ratings = ",rating)
print("Reviews = ",review)
print("--------------------------------------------------------------------------------------")