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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value))).click()

def wait_and_send_keys(driver, by, value, keys):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value))).send_keys(keys)

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.amazon.com/')
    
    # Navigate to sign-in page
    wait_and_click(driver, By.ID, 'nav-link-accountList-nav-line-1')
    wait_and_send_keys(driver, By.ID, 'ap_email', 'enter ur email') // pls enter the email
    driver.find_element(By.ID, 'continue').click()
    wait_and_send_keys(driver, By.ID, 'ap_password', 'enter ur password') //pls enter the password
    driver.find_element(By.ID, 'signInSubmit').click()

    time.sleep(5)

    if "amazon.com" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed.")

    # Function to perform search and return to homepage
    def search_amazon(driver, query):
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()
        time.sleep(3)
        driver.get('https://www.amazon.com/')
        time.sleep(3)

    # Search for items
    search_amazon(driver, 'headphones')
    search_amazon(driver, 'toys')
    search_amazon(driver, 'whey proteins')

    # Sort the results (optional example)
    sort_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'a-autoid-0-announce')))
    sort_dropdown.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 's-result-sort-select_4'))).click()
    time.sleep(3)
    driver.get('https://www.amazon.com/')
    time.sleep(3)

    # Navigate to cart
    wait_and_click(driver, By.ID, 'nav-cart')
    time.sleep(3)
    driver.get('https://www.amazon.com/')
    time.sleep(3)

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.get('https://www.amazon.com/')
    time.sleep(3)

    # Add item to cart (example product URL)
    driver.get('https://www.amazon.in/Fire-TV-Stick-Alexa-Voice-Remote-3rd-Gen/dp/B08R6QR863')
    add_to_cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'add-to-cart-button')))
    add_to_cart_button.click()
    time.sleep(3)

    # Proceed to buy from cart
    driver.get('https://www.amazon.com/')
    time.sleep(3)
    cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nav-cart')))
    cart_button.click()
    time.sleep(3)
    proceed_to_buy_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'proceedToRetailCheckout')))
    proceed_to_buy_button.click()
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    if driver:
        driver.quit()
