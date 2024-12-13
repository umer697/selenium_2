from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Create a Service object for the Edge WebDriver
service = Service('C:/Users/Admin/Desktop/jupyter/msedgedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Edge(service=service)

# Open a website
driver.get("https://www.google.com")


