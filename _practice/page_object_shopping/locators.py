from selenium.webdriver.common.by import By


class MainPageLocators(object):
  LOGO          = (By.XPATH, '/html/body/div[1]/div/header/div[1]/a/img')
#  ACCOUNT       = (By.CSS_SELECTOR, '')
  SIGNUP        = (By.XPATH, '//*[contains(text(), "New customers click here")]')
  LOGIN         = (By.NAME, 'login')
  SEARCH        = (By.NAME, 'query')
  SEARCH_LIST   = (By.XPATH, '//*[contains(text(), "Purple Duck")]')

class LoginPageLocators(object):
  EMAIL         = (By.NAME, 'email')
  PASSWORD      = (By.NAME, 'password')
  SUBMIT        = (By.NAME, 'login')
  ERROR_MESSAGE = (By.CSS_SELECTOR, '.notice')
