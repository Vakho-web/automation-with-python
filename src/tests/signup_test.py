from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from datetime import datetime

def screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
    driver.save_screenshot(f"screenshot_{timestamp}.png")

driver = webdriver.Chrome()
driver.get("https://www.thetestingworld.com/testings/index.php?message=1")

username_field = driver.find_element(By.NAME, "fld_username")
email_field = driver.find_element(By.NAME, "fld_email")
password_field = driver.find_element(By.NAME, "fld_password")
confirm_password_field = driver.find_element(By.NAME, "fld_cpassword")
dob = driver.find_element(By.NAME, "dob")
phone = driver.find_element(By.NAME, "phone")
address = driver.find_element(By.NAME, "address")
radio_home = driver.find_element(By.XPATH, "//input[@name='add_type' and @value='home']")
gender_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='sex' and @required='']"))
country_dropdown = Select(driver.find_element(By.NAME, "country"))
state_dropdown = Select(driver.find_element(By.NAME, "state"))
city_dropdown = Select(driver.find_element(By.NAME, "city"))
zip_field = driver.find_element(By.NAME, "zip")
terms_tic = driver.find_element(By.NAME, "terms")

actions = ActionChains(driver)
actions.click(username_field) \
       .send_keys("SomeUserName") \
       .double_click(username_field) \
       .key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL) \
       .click(email_field) \
       .key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL) \
       .send_keys("@email.com") \
       .send_keys_to_element(password_field, "P@ssw0rd") \
       .send_keys_to_element(confirm_password_field, "P@ssw0rd") \
       .send_keys_to_element(dob, "11/13/1993") \
       .send_keys(Keys.TAB) \
       .perform()

time.sleep(1)

actions.send_keys_to_element(phone, "111222333") \
       .send_keys_to_element(address, "City, Street, Building, APN") \
       .click(radio_home) \
       .perform()

gender_dropdown.select_by_value("1")
country_dropdown.select_by_value("105")
time.sleep(3.5)
state_dropdown.select_by_value("1753")
time.sleep(3.5)
city_dropdown.select_by_value("21887")

actions.send_keys_to_element(zip_field, "15010").click(terms_tic).perform()
screenshot()
actions.send_keys(Keys.ENTER).perform()
screenshot()
driver.quit()
