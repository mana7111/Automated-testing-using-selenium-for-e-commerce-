# Automated-testing-using-selenium-for-e-commerce-
This project involves automating interactions with the Amazon website using the Selenium WebDriver, leveraging Python for scripting and webdriver-manager for managing the ChromeDriver dependencies. 
The script is designed to perform a series of automated tasks on the Amazon platform, including logging in, searching for products, sorting results, adding items to the cart, and proceeding to the checkout page.

Objectives
Automate Login Process: Simulate the user login process by entering email and password, and verifying successful login.
Search for Products: Perform searches for different product categories (e.g., headphones, toys, whey proteins) and navigate back to the homepage.
Sort Search Results: Interact with the sorting dropdown to change the order of search results.
Cart Interaction: Add a specific product to the cart, navigate to the cart page, and proceed to the checkout page.
Scroll and Navigation: Implement scrolling to the bottom of the page and navigating to different sections of the site.
Key Features
Automated Login:

Navigate to the Amazon sign-in page.
Enter user credentials and submit the login form.
Verify successful login based on the current URL.
Product Search:

Search for specified product categories.
Clear the search box and enter new queries.
Submit search forms and navigate back to the homepage.
Result Sorting:

Interact with the sorting dropdown to reorder search results.
Cart Operations:

Navigate to a specific product page and add the product to the cart.
Go to the cart page and proceed to the checkout.
Scrolling and Page Navigation:

Scroll to the bottom of the page to simulate user browsing.
Navigate between different sections of the Amazon website.
Technologies Used
Python: The primary programming language for writing the automation script.
Selenium WebDriver: For web browser automation and interaction.
webdriver-manager: To manage and automatically download the appropriate version of ChromeDriver.
Google Chrome: The web browser used for automation.
Code Structure
Setup: Configure Chrome options and initialize the WebDriver using webdriver-manager.
Helper Functions: Define functions for common actions such as waiting for elements, clicking, and sending keys.
Main Automation Script: Implement the sequence of actions to interact with the Amazon website.
Prerequisites
Python installed on your machine.
Required Python packages (selenium, webdriver-manager) installed.
Google Chrome browser installed.
How to Run
Install Dependencies:

bash
Copy code
pip install selenium webdriver-manager
Execute the Script:

bash
Copy code
python amazon_automation.py
The script will automate the login process, search for products, sort results, add items to the cart, and proceed to the checkout page, mimicking typical user interactions on the Amazon website.
