from selenium import webdriver
from fixture.session import session_control
from fixture.group import group_control

class Application(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.session = session_control(self)
        self.group = group_control(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.driver.close()
