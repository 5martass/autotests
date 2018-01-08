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
        time.sleep(2)
        return self.find_element(*MainPageLocators.SEARCH_LIST).text

    def click_sign_up_button(self):
        self.find_element(*MainPageLocators.SIGNUP).click()
        time.sleep(2)
        return SignUpPage(self.driver)

    def click_sign_in_button(self):
        self.find_element(*MainPageLocators.LOGIN).click()
        time.sleep(2)
        return LoginPage(self.driver)

class LoginPage(Page):
    def enter_email(self, user):
        self.find_element(*LoginPageLocators.EMAIL).send_keys(users.get_user(user)["email"])

    def enter_password(self, user):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(users.get_user(user)["password"])

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
