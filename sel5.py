from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Create a Service object for the Chrome WebDriver
service = Service('C:/Users/Admin/Desktop/jupyter/chromedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.adamchoi.co.uk/overs/detailed")

# Click the "All Matches" button
all_matches_button = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_matches_button.click()
time.sleep(10)

# Collect match data
matches = driver.find_elements(By.TAG_NAME, 'tr')
date = []
home_team = []
score = []
away_team = []

for match in matches:
    try:
        # Check if the row has the required number of columns (e.g., 4)
        columns = match.find_elements(By.TAG_NAME, 'td')
        if len(columns) >= 4:  # Ensure there are enough `td` elements
            date.append(columns[0].text)  # First column
            home_team.append(columns[1].text)  # Second column
            score.append(columns[2].text)  # Third column
            away_team.append(columns[3].text)  # Fourth column
    except Exception as e:
        print(f"Error processing match: {e}")

# Save data to CSV and Excel
df = pd.DataFrame({"Date": date, "Home Team": home_team, "Score": score, "Away Team": away_team})
df.to_csv('football_data.csv', index=False)
df.to_excel('football_data.xlsx', index=False)

# Print messages
print(f"Scraped {len(date)} rows of data.")
print("CSV and Excel files have been saved successfully.")

# Close the WebDriver
driver.quit()
