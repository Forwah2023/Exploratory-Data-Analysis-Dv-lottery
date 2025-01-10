from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set up Chrome options
options = webdriver.ChromeOptions()
# Set up the download directory relative to the script location
script_dir = os.path.dirname(os.path.abspath(__file__))
download_dir = os.path.join(script_dir, "downloads")
os.makedirs(download_dir, exist_ok=True)

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)
# Initiate driver
driver = webdriver.Chrome(options=options)

# Navigate to the website
try:
    driver.get("https://dvcharts.xarthisius.xyz/ceacFY24.html")
    time.sleep(3) 
    element = driver.find_element(By.ID, "currentCsv")
    element.click()
    time.sleep(10) 
except:
    print("Invalid URL")
finally:
    # Close the browser
    driver.quit()