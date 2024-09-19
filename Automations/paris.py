from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to Google
driver.get('https://www.google.com')
driver.maximize_window()

# Scroll to the bottom of the page to load all content
def scroll_to_bottom():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

scroll_to_bottom()


driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(1)  # wait for 1 second


# Send search query
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('what is software testing?? ')
search_box.send_keys(Keys.RETURN)

# Show search results details for a few seconds
time.sleep(5)

# Scroll slowly down for some time
def slow_scroll(duration=10):
    for _ in range(duration):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

slow_scroll(10)
 # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0.5)  
# Come back to the code page after a few seconds
time.sleep(5)
# Close the browser window
driver.quit()


# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to Google
driver.get('https://www.google.com')
driver.maximize_window()

# Scroll to the bottom of the page to load all content
def scroll_to_bottom():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

scroll_to_bottom()


driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(1)  # wait for 1 second


# Send search query
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Robotics automation Images')
search_box.send_keys(Keys.RETURN)

# Show search results details for a few seconds
time.sleep(5)

# Scroll slowly down for some time
def slow_scroll(duration=10):
    for _ in range(duration):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

slow_scroll(10)
 # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0.5)  
# Come back to the code page after a few seconds
time.sleep(5)

# Close the browser window
driver.quit()