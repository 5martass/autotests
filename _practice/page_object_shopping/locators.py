from selenium.webdriver.common.by import By


class MainPageLocators(object):
  LOGO          = (By.XPATH, '/html/body/div[1]/div/header/div[1]/a/img')
  ACCOUNT       = (By.LINK_TEXT, 'account')
  SIGNUP        = (By.LINK_TEXT, 'create_account')
  LOGIN         = (By.NAME, 'login')
  SEARCH        = (By.NAME, 'query')
  SEARCH_LIST   = (By.XPATH, '//*[contains(text(), "Purple Duck")]')

class LoginPageLocators(object):
    pass
