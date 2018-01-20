from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *
import users
from selenium.webdriver.support.ui import WebDriverWait
import time

class MainPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocators.LOGO) else False

    def search_item(self, item):
        self.find_element(*MainPageLocators.SEARCH).send_keys(item)
        self.find_element(*MainPageLocators.SEARCH).send_keys(Keys.RETURN)
        return self.find_element(*MainPageLocators.SEARCH_LIST).text

    def add_some_ducks(self):
        self.find_element(*ShoppingLocators.PURPLE_DUCK).click()
        self.find_element(*ShoppingLocators.QUANTITY).clear()
        self.find_element(*ShoppingLocators.QUANTITY).send_keys(5)
        self.find_element(*ShoppingLocators.ADD_PRODUCT).click()
        time.sleep(1)
        self.find_element(*ShoppingLocators.CART).click()
        return self.find_element(*ShoppingLocators.REMOVE).text

    def click_sign_up_button(self):
        self.find_element(*MainPageLocators.SIGNUP).click()
        return SignUpPage(self.driver)

    def sign_in(self):
        self.driver.get("http://localhost/litecart/en/login")
        return LoginPage(self.driver)

class LoginPage(Page):
    def enter_email(self, user):
        self.find_element(*LoginPageLocators.EMAIL).send_keys('Jonh@Dou.aa')

    def enter_password(self, user):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys('password123')

    def enter_in_valid_email(self, user):
        self.find_element(*LoginPageLocators.EMAIL).send_keys('invalidUser@test.com')

    def enter_in_valid_password(self, user):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys('qwert1235')

    def click_login_button(self):
        self.find_element(*LoginPageLocators.SUBMIT).click()

    def in_valid_login(self, user):
        self.enter_in_valid_email(user)
        self.enter_in_valid_password(user)
        self.click_login_button()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.MESSAGE).text

    def login_with_in_valid_user(self, user):
        self.in_valid_login(user)
        return self.find_element(*LoginPageLocators.MESSAGE).text

class HomePage(Page):
    pass

class SignUpPage(Page):
    pass

class AdminPage(Page):

    def login(self):
        self.driver.get("http://localhost/litecart/admin")
        self.find_element(*AdminPageLocators.USERNAME).send_keys('admin')
        self.find_element(*AdminPageLocators.PASSWORD).send_keys('admin')
        self.find_element(*AdminPageLocators.LOGINBUTTON).click()
        return AdminPage(self.driver)

    def navigation(self):
        self.find_element(*AdminPageLocators.APPEARENCE).click()
        self.find_element(*AdminPageLocators.APP_LOGO).click()
        self.find_element(*AdminPageLocators.APP_TEMPLATE).click()
        self.find_element(*AdminPageLocators.CATALOG).click()
        self.find_element(*AdminPageLocators.CAT_PG).click()
        self.find_element(*AdminPageLocators.CAT_S).click()
        self.find_element(*AdminPageLocators.CAT_M).click()
        self.find_element(*AdminPageLocators.CAT_DS).click()
        self.find_element(*AdminPageLocators.CAT_OG).click()
        self.find_element(*AdminPageLocators.CAT_CSV).click()
        self.find_element(*AdminPageLocators.CAT_SOS).click()
        self.find_element(*AdminPageLocators.CAT_QU).click()
        self.find_element(*AdminPageLocators.COUNTRIES).click()
