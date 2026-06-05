import pytest
from selenium import webdriver
import pytest
import random



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    random_number = random.randint(100, 999)

    user = {
        "name": "test_user",
        "email": f"Nailya_Andarzhanova_cohort_{random_number}@yandex.ru",
        "password": "123456"
    }

    return user
    