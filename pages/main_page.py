import time
from .base_page import BasePage
from .locators import MainPageLocator
from selenium.common.exceptions import TimeoutException
from .right_number_page import RightNumberPage
import re
import base64
import chromedriver_binary

class MainPage(BasePage):

    def __init__(self, driver):
        super(). __init__(driver)
        self.url = "https://qahomework.dtoojyfrkrg7j.amplifyapp.com/homework.html"
        self.open(self.url)

    def send_digit(self, n_1, n_2):
        for i in range(n_1, n_2):
            text_field = self.find_element(MainPageLocator.TEXT_AREA_LOCATOR)
            text_field.clear()
            text_field.send_keys(i)
            button = self.find_element(MainPageLocator.BUTTON_SUBMIT_LOCATOR)
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            if not self.check_header_text():
                self.open(self.url)
                break
        

    def check_header_text(self):
        text = "Welcome to Homework Exercise"
        try:
            self.wait(MainPageLocator.PAGE_HEADER_LOCATOR, text)
            return True
        except TimeoutException:
            RightNumberPage(self.driver)
            return False

    @staticmethod
    def convert_word(word):
        encode_name = base64.b64encode(b'Stranger').decode("utf-8")
        l = re.findall(r'[A-Z0-9]', encode_name)
        return ''.join(l)
   
   
    def send_special_word(self):
        name = "Stranger"
        self.find_element(MainPageLocator.INPUT_NAME_LOCATOR).send_keys(name)
        self.find_element(MainPageLocator.TEXT_AREA_LOCATOR).send_keys(self.convert_word(name))
        button = self.find_element(MainPageLocator.BUTTON_SUBMIT_LOCATOR)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(5)
        self.driver.close()
        return 