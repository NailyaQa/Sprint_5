
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.constructor_page_locators import ConstructorPageLocators
from data import BASE_URL


from locators.login_page_locators import LoginPageLocators 

from locators.login_page_locators import LoginPageLocators

class TestConstructor:

    def test_go_to_constructor_from_personal_account(self,driver):
        driver.get(BASE_URL)

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
    


    def test_go_to_constructor_by_logo(self, driver):
        driver.get(BASE_URL)
        
        # кликаем ЛК
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            ConstructorPageLocators.LOGO_BUTTON)).click()
        
        
        assert driver.find_element(*ConstructorPageLocators.BURGER_HEADER).is_displayed()

    


    def test_open_buns_section(self, driver):

        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                ConstructorPageLocators.SAUCES_TAB)
        ).click()

        buns_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                ConstructorPageLocators.BUNS_TAB)
        )

        buns_tab.click()

        assert "tab_tab_type_current" in buns_tab.get_attribute("class")
    

       


    def test_open_sauces_section(self, driver):

        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_TAB)).click()

        sauces_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_TAB)
    )

        assert "tab_tab_type_current" in sauces_tab.get_attribute("class")
    

       
    
    def test_open_fillings_section(self, driver):

        driver.get(BASE_URL)

        
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB)
    ).click()

        fillings_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.FILLINGS_TAB)
    )

        assert "tab_tab_type_current" in fillings_tab.get_attribute("class")
    
    