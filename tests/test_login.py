
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators.login_page_locators import LoginPageLocators

from helpers import register_user
from locators.login_page_locators import LoginPageLocators as Locators

#вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main_page(driver, user_data):

    register_user(driver, user_data)
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    ).send_keys(user_data["email"])

    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )

    driver.quit()

#вход через кнопку «Личный кабинет»,

def test_login_from_personal_account_button(driver, user_data):

    register_user(driver, user_data)
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    ).send_keys(user_data["email"])

    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )

    driver.quit()

#вход через кнопку в форме регистрации

def test_login_from_registration_form(driver, user_data):

    register_user(driver, user_data)
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    driver.find_element(*Locators.REGISTER_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_LINK)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    ).send_keys(user_data["email"])

    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )

    driver.quit()

    
#вход через кнопку в форме восстановления пароля.

def test_login_from_password_recovery_form(driver, user_data):

    register_user(driver, user_data)
    

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_LINK)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT)
    ).send_keys(user_data["email"])

    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.ORDER_BUTTON)
    )

    driver.quit()



        




