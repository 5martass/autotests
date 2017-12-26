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

def lookup(driver,query):
    driver.get("http://localhost/litecart/admin/login.php")

#login admin section
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
        print("Button not found")
#check nav menu
#appearence
    try:
        appearence = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/descendant::td[1]/div[3]/ul/li[1]/a/span[2]')))
        appearence.click()

    except TimeoutException:
        print("Appearence block not found")
#по сути 1 пункт уже открыт сразу после открытия списка можно было бы сразу проверку написать, но мало, лучше речекнуть
    try:
        appearence_template = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/descendant::td[1]/div[3]/ul/li[1]/ul/li[1]/a/span')))
        appearence_template.click()
        driver.find_element(By.XPATH, '/descendant::td[3]/h1').text == "Template"
    except TimeoutException:
        print("Template nav.block of header not found")

    try:
        appearence_logo = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/descendant::td[1]/div[3]/ul/li[1]/ul/li[2]/a/span')))
        appearence_logo.click()
        driver.find_element(By.XPATH, '/descendant::td[3]/h1').text == "Logotype"
    except TimeoutException:
        print("Logotype nav.block of header not found")
#Catalog
    try:
        catalog= driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/descendant::td[1]/div[3]/ul/li[2]/a/span[2]')))
        catalog.click()
    except TimeoutException:
        print("Catalog block not found")

    try:
        catalog_catalog = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/descendant::td[1]/div[3]/ul/li[2]/ul/li[1]/a/span')))
        catalog_catalog.click()
        driver.find_element(By.XPATH, '/descendant::td[3]/h1').text == "Catalog"
    except TimeoutException:
        print("Catalog nav.block of header not found")

    try:
        catalog_pg = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/descendant::td[1]/div[3]/ul/li[2]/ul/li[2]/a/span')))
        catalog_pg.click()
        driver.find_element(By.XPATH, '/descendant::td[3]/h1').text == "Product Groups"
    except TimeoutException:
        print("Product Groups nav.block of header not found")

#etc

driver = init_driver()
lookup(driver, "Selenium")
time.sleep(5)
driver.quit()
