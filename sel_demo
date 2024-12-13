import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://www.flipkart.com/q/smart-watches?otracker=undefined_footer_footer&page=1")

watch_name = []
current_price = []
mrp_price = []
discount = []
delivery_charge = []
stars = []
rating = []
review = []


for i in range(2,26):

    try:
        watch_name_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[1]'.format(i))
        watch_name.append(watch_name_element.text)
    except:
        watch_name.append("")

    try:
        current_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]'.format(i))
        current_price.append(current_price.text)
    except:
        current_price.append("")

    try:
        mrp_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]'.format(i))
        mrp_price.append(mrp_price_element.text)
    except:
        mrp_price.append("")

    try:
        discount_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[3]/span'.format(i))
        discount.append(discount_element.text)
    except:
        discount.append("")

    try:
        delivery_charge_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[2]/div/div'.format(i))
        delivery_charge.append(delivery_charge_element.text)
    except:
        delivery_charge.append("")

    try:
        stars_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div'.format(i))
        stars.append(stars_element.text)
    except:
        stars.append("")

    try:
        rating_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[1]'.format(i))
        rating.append(rating_element.text)
    except:
        rating.append("")

    try:
        review_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[3]'.format(i))
        review.append(review_element.text)
    except:
        review.append("")

next_page_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]/span')
next_page = next_page_element.click()

for i in range(1,9):
    for i in range(2,26):

        try:
            watch_name_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[1]'.format(i))
            watch_name.append(watch_name_element.text)
        except:
            watch_name.append("")

        try:
            current_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]'.format(i))
            current_price.append(current_price.text)
        except:
            current_price.append("")

        try:
            mrp_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]'.format(i))
            mrp_price.append(mrp_price_element.text)
        except:
            mrp_price.append("")

        try:
            discount_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[3]/span'.format(i))
            discount.append(discount_element.text)
        except:
            discount.append("")

        try:
            delivery_charge_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[2]/div/div'.format(i))
            delivery_charge.append(delivery_charge_element.text)
        except:
            delivery_charge.append("")

        try:
            stars_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div'.format(i))
            stars.append(stars_element.text)
        except:
            stars.append("")

        try:
            rating_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[1]'.format(i))
            rating.append(rating_element.text)
        except:
            rating.append("")

        try:
            review_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[3]'.format(i))
            review.append(review_element.text)
        except:
            review.append("")

    next_page_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[12]/span')
    next_page = next_page_element.click()

for i in range(2,26):

    try:
        watch_name_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[1]'.format(i))
        watch_name.append(watch_name_element.text)
    except:
        watch_name.append("")

    try:
        current_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]'.format(i))
        current_price.append(current_price.text)
    except:
        current_price.append("")

    try:
        mrp_price_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[2]'.format(i))
        mrp_price.append(mrp_price_element.text)
    except:
        mrp_price.append("")

    try:
        discount_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[3]/span'.format(i))
        discount.append(discount_element.text)
    except:
        discount.append("")

    try:
        delivery_charge_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[2]/div[1]/div[2]/div/div'.format(i))
        delivery_charge.append(delivery_charge_element.text)
    except:
        delivery_charge.append("")

    try:
        stars_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div'.format(i))
        stars.append(stars_element.text)
    except:c
        stars.append("")

    try:
        rating_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[1]'.format(i))
        rating.append(rating_element.text)
    except:
        rating.append("")

    try:
        review_element = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[{0}]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[3]'.format(i))
        review.append(review_element.text)
    except:
        review.append("")

data_records = {'Watch_Name': watch_name, 'Current_price':current_price, 'MRP_Price':mrp_price, 'Discount':discount, 'Delivery_Charge':delivery_charge, 'Stars':stars, 'Rating':rating, 'Review':review}
df = pd.DataFrame(data_records)
df.to_csv('Output_records.csv', index=False)
    
# driver.quit()