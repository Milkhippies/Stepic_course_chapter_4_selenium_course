from selenium.webdriver.common.by import By

from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()

    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
