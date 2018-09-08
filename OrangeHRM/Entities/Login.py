from selenium.webdriver.common.by import By


class Login(object):
    UserName = (By.CSS_SELECTOR, '#txtUsername')
    Password = (By.CSS_SELECTOR, '#txtPassword')
    Submit = (By.CSS_SELECTOR, '#btnLogin');
    ErrorMessage = (By.CSS_SELECTOR, "#spanMessage")
