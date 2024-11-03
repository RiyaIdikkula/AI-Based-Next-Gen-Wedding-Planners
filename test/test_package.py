from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Function to handle adding a package
def test_add_package(driver, package_name, package_price, expected_url):
    try:
        # Open the add package page
        driver.get('http://127.0.0.1:8000/add-package/')

        # Wait for the package name input to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "name"))
        )

        # Fill in the package name and price
        package_name_input = driver.find_element(By.ID, 'name')
        package_name_input.clear()
        package_name_input.send_keys(package_name)

        package_price_input = driver.find_element(By.ID, 'price')
        package_price_input.clear()
        package_price_input.send_keys(package_price)

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        # Wait for the successful redirection
        WebDriverWait(driver, 10).until(
            EC.url_to_be(expected_url)
        )

        # Check if we reached the correct page
        if driver.current_url == expected_url:
            print(f"Package '{package_name}' added successfully and redirected to: {expected_url}")
        else:
            print(f"Package addition failed or redirection error for '{package_name}'.")
    except Exception as e:
        print(f"Already addeed '{package_name}': {e}")

# Set up the WebDriver
driver = webdriver.Chrome()  # Use the correct WebDriver (e.g., ChromeDriver, BraveDriver)
driver.maximize_window()

# Test User Login


# Test Admin Login
driver.get("http://127.0.0.1:8000/login/")  # Open login page again
test_login(driver, "admin@gmail.com", "Admin@2001", "http://127.0.0.1:8000/admin-dashboard/")

# Test Adding a Package
driver.get("http://127.0.0.1:8000/add-package/")  # Open add package page
test_add_package(driver, "Diamond", "200000", "http://127.0.0.1:8000/view-packages/")

# Pause to see the result (for demonstration purposes)
time.sleep(3)

# Close the browser
driver.quit()
