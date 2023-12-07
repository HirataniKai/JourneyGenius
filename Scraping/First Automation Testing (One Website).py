from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup as BS
import csv


# Create Chrome options with headless mode
# chrome_options = Options()
# chrome_options.add_argument('--headless')

chromedriver_path = "C:/Program Files (x86)/chromedriver-win64/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()

chrome_options.binary_location = "c:\Program Files\Google\Chrome Beta\Application\chrome.exe"

# Create a WebDriver object with the specified options
driver = webdriver.Chrome(options=chrome_options, service=ChromeService(executable_path=chromedriver_path))

# Navigate to the Google search website
driver.get("https://www.google.com")

# Find the search input field by name
search_input = driver.find_element(By.NAME, "q")

# Enter the search query
search_input.send_keys("San Francisco Activities")

# Submit the form (you can use Keys.RETURN instead of finding the button)
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(5)

# Verify that the search results are displayed
assert "San Francisco" in driver.page_source

# Use WebDriverWait to wait for the presence of the fifth result link
try:
    fifth_result_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div[13]/div/div[2]/div[2]/div/div/div[3]"))
    )
    print("Fifth result link found")
except Exception as e:
    print(f"Exception: {e}")

# Click on the fifth search result link if found
if 'fifth_result_link' in locals():
    fifth_result_link.click()
    print("Clicked on the fifth result link")

# Now you are on the clicked website

# s initializes the html and parses it
s = BS(driver.content, 'html.parser')

# From here you have to go ahead and inspect the website to find the correct div id of where the information is coming from
# In this case, the div id is 'body-copy'
results = s.find(id='body-copy')


# This is where the actual information is located
# It's located in the div header, and the class is called 'h3'
Activity = results.find_all('div', class_='h3')

# Because BeautifulSoup is array based, you print out the desired number of the information
# In this case, there is only one anime title, so the array is at 0
print(Activity[0].text)

# This is where the actual information is located
# It's located in the div header, and the class is called 'h3'
activities = results.find_all('div', class_='h3')

# Create a CSV file and write the header
csv_filename = 'activities_data.csv'
csv_header = ['Activity']
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)

    # Write each activity to the CSV file
    for activity in activities:
        csv_writer.writerow([activity.text.strip()])

# Close the browser
driver.quit()
