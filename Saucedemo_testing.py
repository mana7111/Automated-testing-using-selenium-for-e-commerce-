import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = None

def wait_and_click(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        element.click()
        print(f"Clicked element with {by}={value}")
    except Exception as e:
        print(f"Error clicking element {value}: {str(e)}")

def wait_and_send_keys(driver, by, value, keys):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
        element.send_keys(keys)
        print(f"Sent keys to element with {by}={value}")
    except Exception as e:
        print(f"Error sending keys to element {value}: {str(e)}")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.saucedemo.com/')
    print("Navigated to Sauce Demo website")
    
    # Log in
    wait_and_send_keys(driver, By.ID, 'user-name', 'standard_user')
    wait_and_send_keys(driver, By.ID, 'password', 'secret_sauce')
    wait_and_click(driver, By.ID, 'login-button')

    time.sleep(5)

    if "inventory" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")
        raise Exception("Login failed.")

    # Add items to cart
    def add_item_to_cart(driver, item_name):
        try:
            item_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item_name}']/../../following-sibling::div/button"))
            )
            item_button.click()
            print(f"Added {item_name} to cart")
        except Exception as e:
            print(f"Error adding item {item_name} to cart: {str(e)}")

    add_item_to_cart(driver, 'Sauce Labs Backpack')
    add_item_to_cart(driver, 'Sauce Labs Bike Light')
    time.sleep(3)

    # Navigate to cart
    wait_and_click(driver, By.CLASS_NAME, 'shopping_cart_link')
    time.sleep(3)

    # Proceed to checkout
    wait_and_click(driver, By.ID, 'checkout')
    time.sleep(3)

    # Fill in checkout information
    wait_and_send_keys(driver, By.ID, 'first-name', 'John')
    wait_and_send_keys(driver, By.ID, 'last-name', 'Doe')
    wait_and_send_keys(driver, By.ID, 'postal-code', '12345')
    wait_and_click(driver, By.ID, 'continue')
    time.sleep(3)

    # Finish checkout
    wait_and_click(driver, By.ID, 'finish')
    time.sleep(3)

    # Verify checkout completion
    try:
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'complete-header'))
        )
        if confirmation_message.text == 'THANK YOU FOR YOUR ORDER':
            print("Checkout successful!")
        else:
            print("Checkout failed.")
    except Exception as e:
        print(f"Error verifying checkout completion: {str(e)}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    if driver:
        driver.quit()
