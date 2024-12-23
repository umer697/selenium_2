from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException  # Import TimeoutException
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


# Create a Service object for the chrome WebDriver
service = Service('C:/Users/Admin/Desktop/jupyter/chromedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

driver.maximize_window()
# Open a website
driver.get("https://elyscents.pk/")

# Wait for the "View All" element to be clickable
try:
    view_all = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#CollectionSection-template--15297572077649__featured_collection_ECY4Bq > div.page-width.page-width--flush-small > div > div > div.grid__item.text-center.small--hide > a"))
    )
    # driver.execute_script("arguments[0].scrollIntoView();", view_all)  # Scroll into view
    view_all.click()
except TimeoutException:
    print("Element not found within the timeout period.")
time.sleep(10)

# name = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a/div/div[1]").text
# reg_price = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a/div/div[2]/span[2]").text
# disc_price = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a/div/div[2]/span[3]").text

    
# Function to wait for and retrieve element text
def get_element_text(driver, xpath, wait_time=10, element_name="element"):
    try:
        # Wait for the element to be present and visible
        element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text
    except TimeoutException:
        print(f"{element_name} not found within {wait_time} seconds")
        return f"{element_name} not found"
    except NoSuchElementException:
        print(f"{element_name} does not exist on the page")
        return f"{element_name} not found"

# Extract Name
name = get_element_text(
    driver, 
    "/html/body/div[2]/div/main/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a/div/div[1]", 
    element_name="Name"
)

# Extract Regular Price
reg_price = get_element_text(
    driver, 
    "/html/body/div[2]/div/main/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a/div/div[2]/span[2]", 
    element_name="Regular Price"
)

# Extract Discounted Price
disc_price = get_element_text(
    driver, 
    "/html/body/div[2]/div/main/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a/div/div[2]/span[3]", 
    element_name="Discounted Price"
)
    

print(f"Name: {name}")
print(f"Regular Price: {reg_price}")
print(f"Discounted Price: {disc_price}")

# Save the data to a pandas DataFrame
data = {'Name': [name], 'Regular Price': [reg_price], 'Discounted Price': [disc_price]}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('product_data.xlsx', index=False)

# Close the driver after completion
# driver.quit()
