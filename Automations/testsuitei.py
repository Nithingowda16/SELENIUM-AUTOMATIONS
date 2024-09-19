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
driver.get("https://www.instagram.com/")

# Maximize the browser window
driver.maximize_window()

# Wait for the login form to load
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

# Enter your login credentials
username_input.send_keys("rnithin@aol.com")
password_input.send_keys("1234")

# Click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]'))
)
login_button.click()

# Wait for the login to complete
time.sleep(5)



