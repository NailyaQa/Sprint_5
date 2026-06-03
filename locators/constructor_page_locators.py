

from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH,"//a[@href='/']")
    BURGER_HEADER = (By.XPATH,"//h1[text()='Соберите бургер']")
    LOGO_BUTTON = (By.XPATH, "//header//a[.//*[name()='svg']]")

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
