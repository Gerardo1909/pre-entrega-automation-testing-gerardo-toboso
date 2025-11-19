"""
Tests para el flujo de login de https://www.saucedemo.com/
"""

from pathlib import Path

import pytest
import pytest_check as check

from pages.login_page import LoginPage
from utils.csv_reader import CSVReader
from utils.logger import logger

LOGIN_CSV_PATH = Path(__file__).parent.parent / "data" / "login.csv"
CASOS_LOGIN = CSVReader(str(LOGIN_CSV_PATH)).read()


@pytest.mark.ui
@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_should_work_when_credentials_provided(
    selenium_driver, usuario, clave, debe_funcionar, descripcion
):
    """
    Prueba que verifica el inicio de sesión con diferentes credenciales.
    """
    logger.info(
        f"Iniciando test_login_should_work_when_credentials_provided - Usuario: {usuario}"
    )

    # Arrange
    page = LoginPage(selenium_driver)
    page.open()
    logger.debug("Pagina de login abierta")

    # Act
    logger.info("Completando credenciales...")
    page.do_complete_login(usuario, clave)

    # Assert
    if debe_funcionar:
        logger.info("Verificando redireccion exitosa")
        check.is_in("/inventory.html", selenium_driver.current_url, 
            f"Login fallo para {descripcion}. URL actual: {selenium_driver.current_url}"
        )
        logger.info(f"Test completado exitosamente - {descripcion}")
    else:
        logger.info("Verificando que se muestre error")
        check.is_true(page.error_is_displayed(), 
            f"Se esperaba error para {descripcion}, pero no se mostro"
        )
        logger.info(f"Error de login detectado correctamente - {descripcion}")


@pytest.mark.smoke
@pytest.mark.ui
def test_login_should_succeed_when_valid_credentials(selenium_driver):
    """
    Prueba que verifica el inicio de sesión con credenciales válidas.
    """
    logger.info("Iniciando test_login_should_succeed_when_valid_credentials")

    # Arrange
    page = LoginPage(selenium_driver)
    page.open()
    logger.debug("Pagina de login abierta")

    # Act
    logger.info("Completando credenciales con usuario: standard_user")
    page.do_complete_login("standard_user", "secret_sauce")
    logger.info("Verificando redireccion exitosa")

    # Assert
    check.is_in("/inventory.html", selenium_driver.current_url, 
        "La redireccion al inventario fallo"
    )
    logger.info("Test completado exitosamente")
