from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

# Create Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a Chrome driver instance using WebDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options) # type: ignore

# Open the ebay website
driver.get("https://sephora.in/")

# Maximize the browser window
driver.maximize_window()

# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="header-account"]/div[2]/div/div[1]'))
)

# Click the Sign In button
sign_in_button.click()

# Find the mobile number input field and enter the phone number
phone_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/input")))
phone_field.send_keys("81234 56789")

# Find the "Get OTP" button and click on it
get_otp_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[3]/div/div/div[2]/div/div[3]/button")))
get_otp_button.click()

# Find the checkbox for the terms and conditions and click it
checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div[3]/div/div/div/div[3]/div/div/div[4]/input")))
checkbox.click()

# You can add additional steps here to interact with the page further, 
# such as waiting for the OTP to be sent, entering the OTP, and completing the process.

# Close the browser
driver.quit()