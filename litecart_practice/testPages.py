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
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/litecart/en/")
        print ("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print ("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        search_result = page.search_item("Duck")
        self.assertIn("Duck", search_result)

    def test_sign_up_button(self):
        print ("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        signUpPage = page.click_sign_up_button()
        self.assertIn("create_account", signUpPage.get_url())

    def test_sign_in_with_valid_user(self):
        print ("\n" + str(test_cases(4)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.sign_in()
        result = loginPage.login(email = 'Jonh@Dou.aa', password = 'password123')
        self.assertIn("You are now logged in", result)

    def test_sign_in_with_in_valid_user(self):
        print ("\n" + str(test_cases(5)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.sign_in()
        result = loginPage.login(email = 'invalidUser@test.com', password = 'qwert1235')
        self.assertIn("Wrong password or the account is disabled, or does not exist", result)

    def test_shopping_cart(self):
        #print ("\n" + str(test_cases(6)))
        page = MainPage(self.driver)
        search_result = page.search_item("Duck")
        self.assertIn("Duck", search_result)
        add_ducks = page.add_some_ducks()
        self.assertIn("Remove", add_ducks)

    def test_admin_navigation_check(self):
        #print ("\n" + str(test_cases(7)))
        page = AdminPage(self.driver)
        login = page.login()
        self.assertIn("admin", signUpPage.get_url())
        check_nav_menu = page.navigation()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
