from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Create a Service object for the Edge WebDriver
service = Service('C:/Users/Admin/Desktop/jupyter/geckodriver-v0.33.0-win64/geckodriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Firefox(service=service)

# Open a website
driver.get("https://www.google.com")