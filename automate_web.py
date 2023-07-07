from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Load the config from the JSON file
from selenium.webdriver.support.wait import WebDriverWait

with open("config.json") as f:
    config = json.load(f)

# Access the variables from the config
url = config["url"]
uname = config["username"]
password = config["password"]
card_no = config["card_number"]
exp_date = config["expiry_date"]
exp_year = config["expiry_year"]
cvv_no = config["cvv"]
name_on_card = config["name_on_card"]

driver = webdriver.Chrome()

# Load the webpage
driver.get(url)

# Find and click the login link to navigate to the login page


login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
login_link.click()

# Wait for the username field to be present on the login page
username = driver.find_element(By.NAME, "email")
# Input the username
username.send_keys(uname)

# Find the password field and input the password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)

# Submit the login form
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Find the container element for the featured items
featured_items_container = driver.find_element(By.XPATH, "//div[@class='features_items']")

# Find all the product elements within the container
product_elements = featured_items_container.find_elements(By.CLASS_NAME, "productinfo")

# Create a list to store the item details
item_details = []

# Iterate through each product element
for product_element in product_elements:
    # Find the label and price elements within each product element
    label_element = product_element.find_element(By.TAG_NAME, "p")
    price_element = product_element.find_element(By.TAG_NAME, "h2")

    # Get the text of the label and price elements
    label = label_element.text
    price = price_element.text

    # Append the label and price to the item_details list
    item_details.append((label, price))

# Sort the item_details list by price from low to high
sorted_item_details = sorted(item_details, key=lambda x: float(x[1].replace("Rs. ", "")))

# Print the sorted item details on the console
for label, price in sorted_item_details:
    print(f"Label: {label} | Price: {price}")


# Scroll up
scroll_element = driver.find_element(By.TAG_NAME, "body")
actions = ActionChains(driver)
actions.move_to_element(scroll_element).perform()

# Navigate to Women >> Dress >> Women – Tops Products
women_link = driver.find_element(By.XPATH, "//a[@data-toggle='collapse' and @data-parent='#accordian' and "
                                           "@href='#Women']")
dress_menu = driver.find_element(By.XPATH, "//div[@class='panel-body']")

tmenus = dress_menu.find_elements(By.CLASS_NAME, "panel-body")

for menu in tmenus:
    # Find the label and price elements within each product element
    element_l = menu.find_element(By.TAG_NAME, "a")

# Select the Fancy Green Top and add to cart
fancy_green_top = driver.find_element(By.XPATH, "//p[text()='Fancy Green Top']")
add_to_cart_button = fancy_green_top.find_element(By.XPATH, "//a[@data-product-id='8' and contains(@class, 'add-to-cart')]")
add_to_cart_button.click()
print("Added Fancy Green Top To Cart")

# Select the Summer White Top and add to cart
summer_white_top = driver.find_element(By.XPATH, "//p[text()='Summer White Top']")
add_to_cart_button = summer_white_top.find_element(By.XPATH, "//a[@data-product-id='6' and contains(@class, 'add-to-cart')]")
add_to_cart_button.click()
print("Added Summer White Top To Cart")

# Click on "View cart"
wait = WebDriverWait(driver, 10)  # Adjust the timeout value as needed
view_cart_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='text-center']/a[@href='/view_cart']")))
cart_link = view_cart_link.find_element(By.XPATH, "//p[@class='text-center']/a[@href='/view_cart']")
cart_link.click()


wait = WebDriverWait(driver, 30)
checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='container']/div[@class='row']/div[@class='col-sm-6']/a[@class='btn btn-default check_out']")))
checkout_button.click()


# Adding comments
wait = WebDriverWait(driver, 10)
comments_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='ordermsg']/textarea[@name='message']")))
comments_field = driver.find_element(By.XPATH, "//textarea[@class='form-control' and @name='message']")
comments_field.send_keys("Order placed.")

# Clicking on "Place Order"
place_order_button = driver.find_element(By.XPATH, "//div/a[@href='/payment' and contains(@class, 'btn') and contains(@class, 'check_out')]")
place_order_button.click()

# Enter card details
wait = WebDriverWait(driver, 10)
card_number_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-12 form-group card']/input[@name='card_number']")))
card_number_field = driver.find_element(By.XPATH, "//div[@class='col-sm-12 form-group card']/input[@name='card_number']")
card_number_field.send_keys(card_no)

wait = WebDriverWait(driver, 10)
expiry_date_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4 form-group expiration']/input[@name='expiry_month']")))
expiry_date_field = driver.find_element(By.XPATH, "//div[@class='col-sm-4 form-group expiration']/input[@name='expiry_month']")
expiry_date_field.send_keys(exp_date)

wait = WebDriverWait(driver, 10)
expiry_year_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4 form-group expiration']/input[@name='expiry_year']")))
expiry_year_field = driver.find_element(By.XPATH, "//div[@class='col-sm-4 form-group expiration']/input[@name='expiry_year']")
expiry_year_field.send_keys(exp_year)

wait = WebDriverWait(driver, 10)
cvv_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-4 form-group cvc']/input[@name='cvc']")))
cvv_field = driver.find_element(By.XPATH, "//div[@class='col-sm-4 form-group cvc']/input[@name='cvc']")
cvv_field.send_keys(cvv_no)

wait = WebDriverWait(driver, 10)
name_on_card_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-sm-12 form-group']/input[@name='name_on_card']")))
name_on_card_input = driver.find_element(By.XPATH, "//div[@class='col-sm-12 form-group']/input[@name='name_on_card']")
name_on_card_input.send_keys(name_on_card)

# Submit the form (Place Order)
wait = WebDriverWait(driver, 10)
pay_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='form-row']//button[@class='form-control btn btn-primary submit-button']")))
pay_button = driver.find_element(By.XPATH, "//div[@class='form-row']//button[@class='form-control btn btn-primary submit-button']")
pay_button.click()

# Find the element containing the text
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@style="font-size: 20px; font-family: garamond;"]')))
element = driver.find_element(By.XPATH, '//p[@style="font-size: 20px; font-family: garamond;"]')

# Get the text of the element
text = element.text

# Verify if the expected text is present/ Order is successfully placed
expected_text = "Congratulations! Your order has been confirmed!"
if expected_text == text:
    print("Text verification successful!")
else:
    print("Text verification failed!")

# Close the WebDriver
driver.quit()
