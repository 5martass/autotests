import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def lookup(driver, query):
    driver.get("http://localhost/litecart/admin/login.php")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "username")))
        box1 = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "password")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "login")))
        box.send_keys("admin")
        box1.send_keys("admin")
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located(
                (By.NAME, "login")))
            button.click()
    except TimeoutException:
        print("Box or Button not found")

driver = init_driver()
lookup(driver, "Selenium")
time.sleep(5)
driver.quit()
