from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to handle login testing
def test_login(driver, email, password, expected_url):
    try:
        # Wait for the email input to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )

        # Fill in the email and password
        email_input = driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys(email)

        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)

        # Submit the form
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Wait for the successful redirection (wait until the new page loads)
        WebDriverWait(driver, 10).until(
            EC.url_to_be(expected_url)
        )

        # Check if we reached the correct page
        if driver.current_url == expected_url:
            print(f"Login successful for {email}, redirected to: {expected_url}")
        else:
            print(f"Login failed or redirection error for {email}.")
    except Exception as e:
        print(f"An error occurred for {email}: {e}")

# Set up the WebDriver (make sure to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Use the correct WebDriver (e.g., ChromeDriver, FirefoxDriver)
driver.maximize_window()

# # Open the login page
# driver.get("http://127.0.0.1:8000/login/")  # Update the login URL if necessary

# # Test User Login
# test_login(driver, "biya@gmail.com", "Biya1234", "http://127.0.0.1:8000/")

# Test Admin Login
driver.get("http://127.0.0.1:8000/login/")  # Open login page again
test_login(driver, "admin@gmail.com", "Admin@2001", "http://127.0.0.1:8000/admin-dashboard/")

# Pause to see the result (for demonstration purposes)
time.sleep(3)

# Close the browser
driver.quit()
