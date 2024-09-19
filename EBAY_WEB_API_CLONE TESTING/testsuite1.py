from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait #type: ignore
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# Create Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Create a Chrome driver instance using WebDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) #type: ignore

try:
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
    password_input.send_keys("nithin@1234")

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

    # Wait for the search bar to be clickable
    search_bar = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "gh-ac"))
    )

    # Click the search bar
    search_bar.click()

    # Input the search query
    search_bar.send_keys("sneakers")

    # Click the search button
    search_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "gh-btn"))
    )
    search_button.click()