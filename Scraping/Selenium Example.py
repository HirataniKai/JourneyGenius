# from selenium import webdriver

# # Sets path to the chromedriver program
# # In my case, its set in Program Files (x86)
# PATH = "c:\Program Files (x86)\chrome-win64\chrome.exe"
# # Driver var will use the webdriver function and use Chrome as the desired browser
# driver = webdriver.Chrome(PATH)

# # Get the mf URL
# driver.get("https://myanimelist.net/anime/17265/Log_Horizon")

from selenium import webdriver

# Specify the path to the ChromeDriver executable
chromedriver_path = "C:/Program Files (x86)/chrome-win64/chromedriver.exe"

# Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files (x86)\\chrome-win64\\chrome.exe"

# Set the path to the ChromeDriver executable
chrome_options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Get the desired URL
driver.get("https://myanimelist.net/anime/17265/Log_Horizon")
