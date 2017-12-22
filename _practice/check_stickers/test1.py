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
    driver.get("http://localhost/litecart/")

#open products section
    try:
        rubber_ducks = driver.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/descendant::a[text()="Rubber Ducks"]')))
        rubber_ducks.click()
    except ElementNotVisibleException:
        rubber_ducks.click()
    except TimeoutException:
        print("Category not found")
#stickers check
    try:
        prod1 = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//ul[2]/li[1]/a[1]/div[1]/div')))
    except TimeoutException:
        print("Purple duck have no sticker")

    try:
        prod1 = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//ul[2]/li[2]/a[1]/div[1]/div')))
    except TimeoutException:
        print("Yellow duck have no sticker")
#тут типо ловится эксепшн просто проверить
    try:
        prod1 = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//ul[2]/li[12]/a[1]/div[1]/div')))
    except TimeoutException:
        print("Black duck have no sticker")

# etc

driver = init_driver()
lookup(driver, "Selenium")
time.sleep(5)
driver.quit()
