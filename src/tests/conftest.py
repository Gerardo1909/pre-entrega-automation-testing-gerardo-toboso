"""
Configuración de fixtures para pruebas con pytest y Selenium.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture()
def selenium_driver():
    """
    Fixture para inicializar el driver de Selenium.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
    
@pytest.fixture()
def loged_in_driver(selenium_driver):
    """
    Fixture para un driver de Selenium ya logueado en la aplicación.
    """
    selenium_driver.get("https://www.saucedemo.com")
    selenium_driver.find_element(By.ID, "user-name").send_keys("standard_user")
    selenium_driver.find_element(By.ID, "password").send_keys("secret_sauce")
    selenium_driver.find_element(By.ID, "login-button").click()
    yield selenium_driver
