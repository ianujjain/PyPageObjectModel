class Page(object):
    def __init__(self, driver):
        self.Webdriver = driver

    def FindElement(self, *locator):
        return self.Webdriver.find_element(*locator)

    def FindElements(self, *locator):
        return self.Webdriver.find_element(*locator)