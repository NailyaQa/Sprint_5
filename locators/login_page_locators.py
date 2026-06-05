
from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Кнопка "Войти в аккаунт" на главной
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Ссылка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")

    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")

    # Ссылка "Войти" (на формах регистрации/восстановления)
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    # Поля логина
    EMAIL_INPUT = (By.XPATH, "//input[@name='name' or @type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Восстановление пароля
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

    # Проверка успешного входа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить')]")