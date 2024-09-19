from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService


# Create Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a Chrome driver instance using WebDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) # type: ignore

# Open the ebay website
driver.get("https://tutorialsninja.com/demo/")

# Maximize the browser window
driver.maximize_window()

# Scroll from top to bottom slowly
x = 0
while True:
    driver.execute_script('scrollBy(0,30)')  # scroll down by 50 pixels
    time.sleep(0.1)  # wait for 0.5 seconds
    x += 1
    if x > 100:  # stop after 100 iterations (adjust as needed)
        break

    # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0)  # wait for 1 second

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for 3 seconds to allow the page to load
time.sleep(3)

# Navigate to the next page (if there is a "Next" button)
next_button = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[4]/div/div[3]/button[1]/i")
if next_button:
    next_button.click()

# Wait for 3 seconds to allow the page to load
time.sleep(5)

next_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
if next_button:
    next_button.click()



# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/div[2]/ul/li[5]/a/span "))
)

# Click the Sign In button
sign_in_button.click()

# Wait for 3 seconds to allow the page to load
time.sleep(2)


# Close the browser
driver.quit()