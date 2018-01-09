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
        time.sleep(1)
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
        time.sleep(1)
        return SignUpPage(self.driver)

    def click_sign_in_button(self):
        self.driver.get("http://localhost/litecart/en/login")
        time.sleep(1)
        return LoginPage(self.driver)

class LoginPage(Page):
    def enter_email(self, user):
        self.find_element(*LoginPageLocators.EMAIL).send_keys('Jonh@Dou.aa')

    def enter_password(self, user):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys('password123')

    def click_login_button(self):
        self.find_element(*LoginPageLocators.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE).text

class HomePage(Page):
    pass

class SignUpPage(Page):
    pass
