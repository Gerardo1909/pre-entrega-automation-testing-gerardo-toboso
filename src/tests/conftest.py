"""
Configuración de fixtures para pruebas con pytest y Selenium.
"""

import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.screenshot_saver import take_screenshot


@pytest.fixture(name="selenium_driver", scope="function")
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook de pytest que captura screenshots cuando un test falla.
    """
    # Ejecutar todas las demás hooks para obtener el resultado
    outcome = yield
    report = outcome.get_result()

    # Verificamos si estamos en la fase de call y si ha fallado el test
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("selenium_driver")

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")
            )
            screenshot_route = os.path.join(
                base_dir, f"failure_{item.name}_{timestamp}.png"
            )
            take_screenshot(driver, screenshot_route)
