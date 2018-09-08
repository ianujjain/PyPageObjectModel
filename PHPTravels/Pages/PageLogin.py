from Entities.Login import Login
from WebBasePages.PageBase import Page


class PageLogin(Page):

    def __init__(self, driver):
        self.Locator = Login
        super().__init__(driver)

    def EnterEmail(self, email):
        self.FindElement(*self.Locator.Email).send_keys(email)

    def EnterPassword(self, password):
        self.FindElement(*self.Locator.Password).send_keys(password)

    def ClickOnSubmit(self):
        self.FindElement(*self.Locator.Submit).click()

    def Login(self, email, password):
        self.EnterEmail(email)
        self.EnterPassword(password)
        self.ClickOnSubmit();
