"""
Tests para el flujo de login de https://www.saucedemo.com/
"""

import pytest
from selenium.webdriver.common.by import By


def test_login_should_succeed_when_valid_credentials(selenium_driver):
    """
    Prueba que verifica el inicio de sesión con credenciales válidas.
    """
    # Arrange
    selenium_driver.get("https://www.saucedemo.com")

    # Act
    selenium_driver.find_element(By.ID, "user-name").send_keys("standard_user")
    selenium_driver.find_element(By.ID, "password").send_keys("secret_sauce")
    selenium_driver.find_element(By.ID, "login-button").click()

    # Assert
    assert "/inventory.html" in selenium_driver.current_url
    assert selenium_driver.find_element(By.ID, "inventory_container").is_displayed()


def test_login_should_fail_when_invalid_credentials(selenium_driver):
    """
    Prueba que verifica el inicio de sesión con credenciales inválidas.
    """
    # Arrange
    selenium_driver.get("https://www.saucedemo.com")

    # Act
    selenium_driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    selenium_driver.find_element(By.ID, "password").send_keys("wrong_password")
    selenium_driver.find_element(By.ID, "login-button").click()

    # Assert
    assert selenium_driver.find_element(
        By.CSS_SELECTOR, 'h3[data-test="error"]'
    ).is_displayed()
