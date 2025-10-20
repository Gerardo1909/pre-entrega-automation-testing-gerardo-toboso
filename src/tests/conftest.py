"""
Configuración de fixtures para pruebas con pytest y Selenium.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utils.screenshot_saver import take_screenshot
from datetime import datetime
import os


@pytest.fixture(name="selenium_driver")
def _selenium_driver():
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook de pytest que captura screenshots cuando un test falla.
    """
    # Ejecutar todas las demás hooks para obtener el resultado
    outcome = yield
    rep = outcome.get_result()

    # Verificamos si estamos en la fase de call y si ha fallado el test
    if rep.when == "call" and rep.failed:
        # Buscar un objeto driver en los fixtures usados por el test
        possible_keys = [
            "driver",
            "selenium_driver",
            "loged_in_driver"
        ]
        driver = None
        for key in possible_keys:
            driver = item.funcargs.get(key)
            if driver:
                break

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # usamos ruta absoluta para evitar problemas de compatibilidad con otras 
            # terminales
            base_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "screenshots")
            )
            os.makedirs(base_dir, exist_ok=True)
            # sanitizamos el nombre del test para evitar caracteres inválidos
            safe_name = "".join(c for c in item.name if c.isalnum() or c in ("._-"))
            screenshot_route = os.path.join(
                base_dir, f"failure_{safe_name}_{timestamp}.png"
            )
            take_screenshot(driver, screenshot_route)
