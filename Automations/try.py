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

# Create Chrome options
options = Options()
options.add_experimental_option("detach", True) 

# Create a Chrome driver instance using WebDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options) # type: ignore

# Open the ebay website
driver.get("https://www.bestbuy.ca/en-ca")

# Maximize the browser window
driver.maximize_window()

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

# Wait for the Account button to be clickable
account_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/header/div/div/div[1]/div[2]/div/div[1]/a/span"))
)

# Click the Account button
account_button.click()

email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/form/fieldset/div[1]/div/div[1]/div/input"))
)
# Enter the email address
email_input.send_keys("rnithin@aol.com")

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/form/fieldset/div[2]/div/div[1]/div/input"))
)
# Enter the password
password_input.send_keys("Nithin@2004")

# Wait for the Sign In button to be clickable again
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='signIn']/div/button/span"))
)

# Click the Sign In button
sign_in_button.click()

# Find the search bar
search_bar = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "gh-search"))
)
search_bar.click()

# Input the search query
search_bar.send_keys("iphone 15 pro max")

# Click the search button
search_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "gh-btn"))
)
search_button.click()

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

time.sleep(5)

# Click on the 3rd option of shoes
product = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/main/div/div[1]/div[3]/div/div[2]/ul/div/div[6]/div/a/div/div/div[1]/div/div/div/img")
driver.execute_script('arguments[0].scrollIntoView(true)',product)
product.click()

# Add to cart
add_to_cart_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/section[4]/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/form/button'))
)
add_to_cart_button.click()

# Close the browser
driver.quit()

