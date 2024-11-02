from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
    driver.save_screenshot(f"screenshot_{timestamp}.png")

driver = webdriver.Chrome()
driver.get("https://www.thetestingworld.com/testings/index.php?message=1")

driver.find_element(By.NAME, "fld_username").send_keys("SomeUserName")
driver.find_element(By.NAME, "fld_email").send_keys("SomeEmail@Email.com")
driver.find_element(By.NAME, "fld_password").send_keys("P@ssw0rd")
driver.find_element(By.NAME, "fld_cpassword").send_keys("P@ssw0rd")
driver.find_element(By.NAME, "dob").send_keys("11/13/1993")
driver.find_element(By.NAME, "dob").send_keys(Keys.TAB)
driver.find_element(By.NAME, "phone").send_keys("111222333")
driver.find_element(By.NAME, "address").send_keys("City, Street, Building, APN")
driver.find_element(By.XPATH, "//input[@name='add_type' and @value='home']").click()
driver.find_element(By.XPATH, "//select[@name='sex' and @required='']").click()
driver.find_element(By.XPATH, "//option[@value='1']").click()
driver.find_element(By.XPATH, "//select[@name='country']").click()
driver.find_element(By.XPATH, "//option[@value='105']").click()
driver.find_element(By.NAME, "dob").send_keys(Keys.TAB)
time.sleep(3.5)
driver.find_element(By.XPATH, "//select[@name='state']").click()
driver.find_element(By.XPATH, "//option[@value='1753']").click()
time.sleep(3.5)
driver.find_element(By.XPATH, "//select[@name='city']").click()
driver.find_element(By.XPATH, "//option[@value='21887']").click()
driver.find_element(By.NAME, "zip").send_keys("15010")
driver.find_element(By.NAME, "terms").click()
screenshot()
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Sign up']").click()
screenshot()
driver.quit()

