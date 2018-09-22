import unittest
from selenium import webdriver


class BaseTC(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(r"D:\Python\VS\PyPOM\POM\Drivers\chromedriver.exe")
        inst.driver.maximize_window()
        inst.driver.get('https://opensource-demo.orangehrmlive.com/')


    @classmethod
    def tearDownClass(inst):
        if (inst.driver != None):
            inst.driver.close();
            inst.driver.quit();