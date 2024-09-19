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

# Create Chrome optionsPIP
options = Options()
options.add_experimental_option("detach", True) 

# Create a Chrome driver instance using WebDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Open the ebay website
driver.get("https://www.ebay.com/")

# Maximize the browser window
driver.maximize_window()

# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"gh-ug\"]/a"))
)

# Click the Sign In button
sign_in_button.click()

# Wait for the email or username input field to be visible
email_input = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.ID, "userid"))
)

# Input the email or username
email_input.send_keys("rnithin@aol.com")

# Wait for the Continue button to be clickable
continue_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "signin-continue-btn"))
)

# Click the Continue button
continue_button.click()

# Wait for the password input field to be visible
password_input = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.ID, "pass"))
)

# Input the password
password_input.send_keys("aol@2024")

# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "sgnBt"))
)

# Click the Sign In button
sign_in_button.click()

try:
    # Wait for the Skip for now button to be clickable
    skip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"passkeys-cancel-btn\"]"))
    )

    # Click the Skip for now button
    skip_button.click()
except TimeoutException:
    # If the Simplify Sign-In page does not appear, continue with the rest of the script
    pass

# Scroll from top to bottom slowly
x = 0
while True:
    driver.execute_script('scrollBy(0,50)')  # scroll down by 50 pixels
    time.sleep(0.5)  # wait for 0.5 seconds
    x += 1
    if x > 100:  # stop after 100 iterations (adjust as needed)
        break

    # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(1)  # wait for 1 second

# Wait for the search bar to be clickable
search_bar = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "gh-ac"))
)

# Click the search bar
search_bar.click()

# Input the search query
search_bar.send_keys("bags")

# Click the search button
search_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "gh-btn"))
)
search_button.click()

# Wait for the search results to load
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "srp-results"))
)

# Scroll from top to bottom slowly
x = 0
while True:
    driver.execute_script('scrollBy(0,50)')  # scroll down by 50 pixels
    time.sleep(0.5)  # wait for 0.5 seconds
    x += 1
    if x > 100:  # stop after 100 iterations (adjust as needed)
        break

    # Scroll back to top
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)  # type: ignore
time.sleep(0.5)  # wait for 1 second

time.sleep(5)

# Click on the 3rd option of shoes
shoes = driver.find_element(By.XPATH, "//*[@id=\"item24413cc968\"]/div/div[1]/div/a/div/img")
driver.execute_script('arguments[0].scrollIntoView(true)',shoes)
shoes.click()

time.sleep(5)

# Close the browser
driver.quit()




