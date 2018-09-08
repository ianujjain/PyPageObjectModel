from Entities.Login import Login
from WebBasePages.PageBase import Page


class PageLogin(Page):

    def __init__(self, driver):
        self.Locator = Login
        super().__init__(driver)

    def EnterUserName(self, username):
        self.FindElement(*self.Locator.UserName).send_keys(username)

    def EnterPassword(self, password):
        self.FindElement(*self.Locator.Password).send_keys(password)

    def ClickOnSubmit(self):
        self.FindElement(*self.Locator.Submit).click()

    def ErrorMsgInvalidCredentials(self):
        return self.FindElement(*self.Locator.ErrorMessage).text

    def ErrorMsgUsernameCannotBeEmpty(self):
        return self.FindElement(*self.Locator.ErrorMessage).text

    def UsernameCannotBeEmptyLogin(self):
        self.ClickOnSubmit();
        return self.ErrorMsgUsernameCannotBeEmpty();

    def InvalidCredentialsLogin(self, username, password):
        self.Login(username, password)
        return self.ErrorMsgUsernameCannotBeEmpty();

    def Login(self, username, password):
        self.EnterUserName(username)
        self.EnterPassword(password)
        self.ClickOnSubmit();
