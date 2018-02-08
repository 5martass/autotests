from selenium import webdriver

class Application(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def open_home_page(self):
        webdriver = self.driver
        webdriver.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        webdriver = self.driver
        self.open_home_page()
        webdriver.find_element_by_name('user').click()
        webdriver.find_element_by_name('user').send_keys(username)
        webdriver.find_element_by_name('pass').click()
        webdriver.find_element_by_name('pass').send_keys(password)
        webdriver.find_element_by_css_selector('input[type=\"submit\"]').click()

    def open_groups_page(self):
        webdriver = self.driver
        webdriver.find_element_by_link_text('groups').click()

    def create_group(self, group):
        webdriver = self.driver
        self.open_groups_page()
        webdriver.find_element_by_name('new').click()
        webdriver.find_element_by_name('group_name').click()
        webdriver.find_element_by_name('group_name').send_keys(group.name)
        webdriver.find_element_by_name('group_header').click()
        webdriver.find_element_by_name('group_header').send_keys(group.header)
        webdriver.find_element_by_name('group_footer').click()
        webdriver.find_element_by_name('group_footer').send_keys(group.footer)
        webdriver.find_element_by_name('submit').click()
        self.return_groups_page()

    def return_groups_page(self):
        webdriver = self.driver
        webdriver.find_element_by_link_text('group page').click()

    def logout(self):
        webdriver = self.driver
        webdriver.find_element_by_link_text('Logout').click

    def destroy(self):
        self.driver.close()
