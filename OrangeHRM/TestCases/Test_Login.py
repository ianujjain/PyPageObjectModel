import sys

sys.path.append('D:\\Python\\PyPageObjectModel\\OrangeHRM\\BaseTestCase')
from BaseTestCase.BaseTC import BaseTC

sys.path.append("D:\\Python\\PyPageObjectModel\\POM\\WebBasePages")
from Pages.PageLogin import PageLogin

import time


class Test_Login(BaseTC):

    def test_A_ValidateUsernameCannotBeEmptyErrorMessage(self):
        ObjPageLogin = PageLogin(self.driver)
        ErrorMessage = ObjPageLogin.UsernameCannotBeEmptyLogin()
        time.sleep(5)
        self.assertEqual(ErrorMessage, "Username cannot be empty", 'Validate Error Message: Username cannot be empty')

    def test_B_ValidateLoginWithInValidUser(self):
        ObjPageLogin = PageLogin(self.driver)
        ErrorMessage = ObjPageLogin.InvalidCredentialsLogin("Admin1", "admin1231")
        time.sleep(5)
        self.assertEqual(ErrorMessage, "Invalid credentials", 'Validate Error Message: Invalid credentials')

    def test_C_ValidateLoginWithValidUser(self):
        ObjPageLogin = PageLogin(self.driver)
        ObjPageLogin.Login("Admin", "admin123")
