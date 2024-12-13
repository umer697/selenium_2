from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)


# Create a Service object for the Edge WebDriver
# service = Service('C:/Users/Admin/Desktop/jupyter/chromedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Open a website
driver.get("https://www.google.com")


