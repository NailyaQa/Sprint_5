

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators

from locators.registration_page_locators import RegistrationPageLocators as Locators

#Регистрацция пользователя 
def register_user(driver, user_data):

    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    driver.find_element(*Locators.REGISTER_LINK).click()

    driver.find_element(*Locators.NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])

    driver.find_element(*Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.LOGIN_HEADER)
    )

#вход пользователя 
def login_user(driver, user_data):

    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.MAIN_LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(user_data["email"])

    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()