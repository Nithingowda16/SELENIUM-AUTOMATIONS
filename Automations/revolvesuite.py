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
driver.get("https://www.coggles.com/")

# Maximize the browser window
driver.maximize_window()

# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div[2]/div/button/p"))
)

# Click the Sign In button
sign_in_button.click()  

email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/main/astro-island[1]/div/div[1]/div/div/div/form/div[2]/div[1]/input"))
)
# Enter the email address
email_input.send_keys("rnithin@aol.com")

time.sleep(0.5)  # wait for 0.5 seconds

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/main/astro-island[1]/div/div[1]/div/div/div/form/div[2]/div[2]/input"))
)

# Enter the password
password_input.send_keys("Nithin@2004")

time.sleep(0.5)  # wait for 0.5 seconds

# Find the login button
login_button = driver.find_element(By.XPATH, '/html/body/main/astro-island[1]/div/div[1]/div/div/div/form/button') 

# Click the login button
login_button.click()

time.sleep(0.5)  # wait for 0.5 seconds

# Find the "Man" button on the top of the page
EC.element_to_be_clickable((By.LINK_TEXT, 'Man'))
man_button = driver.find_element(By.CSS_SELECTOR, '#site-header-nav > div:nth-child(3) > div.relative.nav-controls.peer > a')

# Click the "Man" button
man_button.click()

actions = ActionChains(driver)
man_button = driver.find_element(By.CSS_SELECTOR, '#site-header-nav > div:nth-child(3) > div.relative.nav-controls.peer > a')
actions.move_to_element(man_button).click().perform()