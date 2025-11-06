"""
Tests para el flujo de login de https://www.saucedemo.com/
"""

import pytest
from pages.login_page import LoginPage


def test_login_should_succeed_when_valid_credentials(selenium_driver):
    """
    Prueba que verifica el inicio de sesión con credenciales válidas.
    """
    # Arrange
    page = LoginPage(selenium_driver)
    page.open()

    # Act
    page.do_complete_login("standard_user", "secret_sauce")

    # Assert
    assert "/inventory.html" in selenium_driver.current_url


def test_login_should_fail_when_invalid_credentials(selenium_driver):
    """
    Prueba que verifica el inicio de sesión con credenciales inválidas.
    """
    # Arrange
    page = LoginPage(selenium_driver)
    page.open()

    # Act
    page.do_complete_login("invalid_user", "wrong_password")

    # Assert
    assert page.error_is_displayed()
