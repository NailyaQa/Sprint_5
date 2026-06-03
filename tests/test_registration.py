from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.registration_page_locators import RegistrationPageLocators as Locators


def test_successful_registration(driver, user_data):

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

    assert driver.find_element(*Locators.LOGIN_HEADER).is_displayed()

    driver.quit()

def test_registration_with_invalid_password(driver, user_data):

    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    driver.find_element(*Locators.REGISTER_LINK).click()

    driver.find_element(*Locators.NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")  # невалидный пароль

    driver.find_element(*Locators.REGISTER_BUTTON).click()

    error_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.PASSWORD_ERROR)
    )

    assert error_text.is_displayed()

    driver.quit()