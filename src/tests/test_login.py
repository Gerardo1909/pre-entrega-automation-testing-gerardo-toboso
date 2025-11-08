"""
Tests para el flujo de login de https://www.saucedemo.com/
"""

from pathlib import Path

import pytest

from pages.login_page import LoginPage
from utils.csv_reader import CSVReader

LOGIN_CSV_PATH = Path(__file__).parent.parent / "data" / "login.csv"
CASOS_LOGIN = CSVReader(str(LOGIN_CSV_PATH)).read()


@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_should_work_when_credentials_provided(
    selenium_driver, usuario, clave, debe_funcionar, descripcion
):
    """
    Prueba que verifica el inicio de sesión con diferentes credenciales.
    """
    # Arrange
    page = LoginPage(selenium_driver)
    page.open()

    # Act
    page.do_complete_login(usuario, clave)

    # Assert
    if debe_funcionar:
        assert "/inventory.html" in selenium_driver.current_url, (
            f"Login falló para {descripcion}. URL actual: {selenium_driver.current_url}"
        )
    else:
        assert page.error_is_displayed(), (
            f"Se esperaba error para {descripcion}, pero no se mostró"
        )


@pytest.mark.smoke
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
