from selenium.webdriver.common.by import By

class MainPageLocator:
    TEXT_AREA_LOCATOR = (By.CSS_SELECTOR, "#contact_message")
    INPUT_NAME_LOCATOR = (By.CSS_SELECTOR, "#contact_name")
    INPUT_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#contact_email")
    BUTTON_SUBMIT_LOCATOR = (By.CSS_SELECTOR, "#button1")
    CHECKBUTTON_LOCATORS = (By.CSS_SELECTOR, "#useless-checkbox")
    CARS_IMAGE_LOCATOR = (By.XPATH, "//img[@src='img/cars.jpg']")
    HANDS_IMAGE_LOCATOR = (By.XPATH, "//img[@src='img/hands.jpg']")
    PAGE_HEADER_LOCATOR = (By.XPATH, "//h2")
