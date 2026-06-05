from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators

from locators.logout_page_locators import LogoutageLocators
from locators.registration_page_locators import RegistrationPageLocators 

from helpers import register_user
from helpers import login_user
from locators.login_page_locators import LoginPageLocators as Locators

from locators.login_page_locators import LoginPageLocators

class TestLogout:

    def test_logout_from_personal_account(self, driver, user_data):

        register_user(driver, user_data)
        login_user(driver, user_data)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )
        
        # кликаем ЛК
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            LogoutageLocators.LOGOUT_BUTTON)).click()

        assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            RegistrationPageLocators.LOGIN_HEADER
        )
    )
        
    