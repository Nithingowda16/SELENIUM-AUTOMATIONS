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
driver.get("https://www.kijiji.ca/h-city-of-toronto/1700273")

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

# Wait for the Sign In button to be clickable
sign_in_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='global-header']/div/div[1]/div[3]/div/button"))
)

# Click the Sign In button
sign_in_button.click()

email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/form/section[1]/div[1]/input"))
)
# Enter the email address
email_input.send_keys("rnithin@aol.com")

password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/form/section[2]/div[2]/input"))
)
# Enter the password
password_input.send_keys("Nithin@2004")

# Wait for the Sign In button to be clickable again
sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/form/section[3]/button"))
)

# Click the Sign In button
sign_in_button.click()

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

# Click on the 3rd option of shoes
shoes = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[3]/div/div[2]/div/div/div[15]/div/a/div[1]/div[1]/span/img")
driver.execute_script('arguments[0].scrollIntoView(true)',shoes)
shoes.click()

# Wait for the logout button to be clickable
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, ""))  # Update with the correct XPath
)

# Wait for the "Log Out" button to be clickable
wait = WebDriverWait(driver, 10)
log_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div/div/div/header/div[3]/div/div[3]/div/div[4]/div/div/ul/li[11]/button")))

# Click the "Log Out" button
log_out_button.click()

# Close the browser
driver.quit()















