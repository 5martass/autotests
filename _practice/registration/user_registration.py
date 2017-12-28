import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def lookup(driver,query):
    driver.get("http://localhost/litecart/en/create_account")
    try:
        firsname = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "firstname")))
        firsname.click()
        firsname.send_keys("Jonh")

        lastname = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "lastname")))
        lastname.click()
        lastname.send_keys("Dou")

        address1 = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "address1")))
        address1.click()
        address1.send_keys("Anywhere")

        postcode = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "postcode")))
        postcode.click()
        postcode.send_keys("12345")

        city = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "city")))
        city.click()
        city.send_keys("Wonderland")

        email = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "email")))
        email.click()
        email.send_keys("Jonh@Dou.aa")

        phone = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "phone")))
        phone.click()
        phone.send_keys("+0123456789")

        select_country_field = select_country = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/form/table/tbody/tr[5]/td[1]/span[2]')))
        select_country_field.click()
        country_search = driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/span/span/span[1]/input')))
        country_search.send_keys("United States")
        country_search.send_keys(Keys.ENTER)

        password = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "password")))
        password.click()
        password.send_keys("password123")

        confirmed_password = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "confirmed_password")))
        confirmed_password.click()
        confirmed_password.send_keys("password123")
        '''тут ввод капчи ручками,
        я мог бы полезть в исходники и отрубить ее,
        но не буду'''
        time.sleep(10)

        create_account = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "create_account")))
        create_account.click()

    except TimeoutException:
        print("Something wrong!")

driver = init_driver()
lookup(driver, "Selenium")
time.sleep(5)
driver.quit()
