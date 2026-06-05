from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    # Ссылка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")

    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Поля регистрации
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

    # Заголовок после регистрации/логина
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")

    # Ошибка пароля
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
