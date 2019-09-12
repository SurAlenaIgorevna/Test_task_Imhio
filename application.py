from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Application(object):

    def __init__(self):

        from methods.methods import Methods

        self.Methods = Methods(self)
        self.init_driver()

    def init_driver(self):
        options = Options()
        self.driver = webdriver.Chrome( options=options )