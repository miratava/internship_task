from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by:tuple):
        return self.driver.find_element(by[0], by[1]) 

    def open(self, url):
        return self.driver.get(url)
    
    def wait(self, locator, header_text):
        return WebDriverWait(self.driver, 3).until(EC.text_to_be_present_in_element(locator, header_text))
