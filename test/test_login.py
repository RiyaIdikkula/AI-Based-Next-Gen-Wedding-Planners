from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (make sure to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Use the correct WebDriver (e.g., ChromeDriver, FirefoxDriver)
driver.maximize_window()

# Open the login page
driver.get("http://127.0.0.1:8000/login/")  # Update the login URL if necessary

try:
    # Wait for the email input to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    # Fill in the email and password
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("biya@gmail.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Biya1234")

    # Submit the form
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Wait for the successful redirection (wait until the new page loads)
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://127.0.0.1:8000/")
    )

    # Check if we reached the index page
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Login successful, reached the index page!")
    else:
        print("Login failed or redirection error.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Pause to see the result (for demonstration purposes)
    time.sleep(3)
    # Close the browser
    driver.quit()
