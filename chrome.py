from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create a Service object for the Edge WebDriver
service = Service('C:/Users/Admin/Desktop/jupyter/chromedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://")


