from BaseTestCase.BaseTC import BaseTC
import unittest
import HtmlTestRunner
import time

from Pages.PageLogin import PageLogin


class Test_TCLogin(BaseTC):

    def test_A_ValidateUsernameCannotBeEmptyErrorMessage(self):
        ObjPageLogin = PageLogin(self.driver)
        ErrorMessage = ObjPageLogin.UsernameCannotBeEmptyLogin()
        time.sleep(5)
        self.assertEqual(ErrorMessage, "Username cannot be empty", 'Incorrect Error Message: Username cannot be empty')

    def test_B_ValidateLoginWithInValidUser(self):
        ObjPageLogin = PageLogin(self.driver)
        ErrorMessage = ObjPageLogin.InvalidCredentialsLogin("Admin1", "admin1231")
        time.sleep(5)
        self.assertEqual(ErrorMessage, "Invalid credentials", 'Incorrect Error Message: Invalid credentials')

    def test_C_ValidateLoginWithValidUser(self):
        ObjPageLogin = PageLogin(self.driver)
        ObjPageLogin.Login("Admin","admin123")



