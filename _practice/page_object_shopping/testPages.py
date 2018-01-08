import unittest
from selenium import webdriver
from pages import *
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By


class TestPages(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost/litecart/en/")
        print ("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    @unittest.skip('done')
    def test_search_item(self):
        print ("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        search_result = page.search_item("Duck")
        self.assertIn("Duck", search_result)

    @unittest.skip('done')
    def test_sign_up_button(self):
        print ("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        signUpPage = page.click_sign_up_button()
        self.assertIn("create_account", signUpPage.get_url())

    @unittest.skip('done')
    def test_sign_in_button(self):
        print ("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        loginPage = page.click_sign_in_button()
        self.assertIn("login", loginPage.get_url())

    def test_sign_in_with_valid_user(self):
        print ("\n" + str(test_cases(4)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_valid_user("valid_user")
        self.assertIn("login", result.get_url())

    @unittest.skip(' ')
    def test_sign_in_with_in_valid_user(self):
        print ("\n" + str(test_cases(5)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.click_sign_in_button()
        result = loginPage.login_with_in_valid_user("invalid_user")
        self.assertIn("Wrong password or the account is disabled, or does not exist", result)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
