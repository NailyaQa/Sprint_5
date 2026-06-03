from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators
from locators.constructor_page_locators import ConstructorPageLocators


from locators.logout_page_locators import LogoutageLocators
from locators.registration_page_locators import RegistrationPageLocators 

from helpers import register_user
from helpers import login_user
from locators.login_page_locators import LoginPageLocators as Locators

from locators.login_page_locators import LoginPageLocators


def test_go_to_constructor_from_personal_account(driver, user_data):
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
        ConstructorPageLocators.CONSTRUCTOR_BUTTON)).click()
    
    
    assert WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        ConstructorPageLocators.BURGER_HEADER
    )
)
    driver.quit()


def test_go_to_constructor_by_logo(driver, user_data):

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
    EC.url_contains("/account")
)
    
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        ConstructorPageLocators.LOGO_BUTTON)).click()
    
    
    assert driver.find_element(*ConstructorPageLocators.BURGER_HEADER).is_displayed()

    driver.quit()


def test_open_buns_section(driver, user_data):

    register_user(driver, user_data)
    login_user(driver, user_data)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB))
    
    assert WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(ConstructorPageLocators.BUNS_HEADER)).text == "Булки"
    

    driver.quit()    


def test_open_sauces_section(driver, user_data):

    register_user(driver, user_data)
    login_user(driver, user_data)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_TAB))
    
    assert WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_HEADER)).text == "Соусы"
    

    driver.quit()    
    
def test_open_fillings_section(driver, user_data):

    register_user(driver, user_data)
    login_user(driver, user_data)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
    
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB)
).click()

    assert WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(ConstructorPageLocators.FILLINGS_HEADER)).text == "Начинки" 
    
    driver.quit()