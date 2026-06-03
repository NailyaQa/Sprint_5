from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators

from helpers import register_user
from helpers import login_user
from locators.login_page_locators import LoginPageLocators as Locators

from locators.login_page_locators import LoginPageLocators


def test_go_to_personal_account(driver, user_data):

    register_user(driver, user_data)
    
    login_user(driver, user_data)
    

    # ждём входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
    )
    
    # кликаем ЛК
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        LoginPageLocators.PERSONAL_ACCOUNT_BUTTON
    )
).click()
    
    # проверяем профиль
    assert WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        ProfilePageLocators.PROFILE_TAB
    )
)

      

