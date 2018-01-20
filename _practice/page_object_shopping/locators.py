from selenium.webdriver.common.by import By


class MainPageLocators(object):
  LOGO          = (By.XPATH, '/html/body/div[1]/div/header/div[1]/a/img')
  SIGNUP        = (By.XPATH, '//*[contains(text(), "New customers click here")]')
  LOGIN         = (By.NAME, 'login')
  SEARCH        = (By.NAME, 'query')
  SEARCH_LIST   = (By.XPATH, '//*[contains(text(), "Purple Duck")]')

class LoginPageLocators(object):
  EMAIL         = (By.NAME, 'email')
  PASSWORD      = (By.NAME, 'password')
  SUBMIT        = (By.NAME, 'login')
  MESSAGE       = (By.CSS_SELECTOR, '.notice')

class ShoppingLocators(object):
  PURPLE_DUCK   = (By.XPATH, '//*[contains(text(), "Purple Duck")]')
  QUANTITY      = (By.NAME, 'quantity')
  ADD_PRODUCT   = (By.NAME, 'add_cart_product')
  CART          = (By.ID, 'cart')
  REMOVE        = (By.NAME, 'remove_cart_item')

class AdminPageLocators(object):
#login
  USERNAME      = (By.NAME, 'username')
  PASSWORD      = (By.NAME, 'password')
  LOGINBUTTON   = (By.NAME, 'login')
#navigation menu
  APPEARENCE    = (By.XPATH, '//*[contains(text(), "Appearence")]')
  APP_LOGO      = (By.ID, 'doc-logotype')
  APP_TEMPLATE  = (By.ID, 'doc-template')
  CATALOG       = (By.XPATH, '//*[contains(text(), "Catalog")]')
  CAT_CATALOG   = (By.ID, 'doc-catalog')
  CAT_PG        = (By.ID, 'doc-product_groups')
  CAT_OG        = (By.ID, 'doc-option_groups')
  CAT_M         = (By.ID, 'doc-manufacturers')
  CAT_S         = (By.ID, 'doc-suppliers')
  CAT_DS        = (By.ID, 'doc-delivery_statuses')
  CAT_SOS       = (By.ID, 'doc-sold_out_statuses')
  CAT_QU        = (By.ID, 'doc-quantity_units')
  CAT_CSV       = (By.ID, 'doc-csv')
  COUNTRIES     = (By.XPATH, '//*[contains(text(), "Countries")]')
