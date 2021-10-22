from selenium import webdriver
from pages.main_page import MainPage
import geckodriver_autoinstaller
import chromedriver_binary

def run_chrome():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.send_digit(1, 100)
    main_page.send_special_word()

def run_firefox():
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    main_page = MainPage(driver)
    main_page.send_digit(1, 100)
    main_page.send_special_word()


run_chrome()
run_firefox()


