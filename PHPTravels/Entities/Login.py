from selenium.webdriver.common.by import By


class Login(object):
    Email = (By.CSS_SELECTOR, "input.form-control[placeholder='Email']")
    Password = (By.CSS_SELECTOR, "input.form-control[placeholder='Password']")
    Submit = (By.CSS_SELECTOR, "button[class='btn btn-primary btn-block ladda-button fadeIn animated']");
