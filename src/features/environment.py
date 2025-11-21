"""
Archivo de configuración de entorno para Behave.
Define los hooks principales del ciclo de vida de las pruebas BDD.
"""

import os
import sys
import shutil
from pathlib import Path

# Agregar el directorio src al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent.parent))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.logger import behave_logger
from utils.screenshot_saver import take_screenshot


def before_all(context):
    """
    Hook que se ejecuta una sola vez antes de todas las pruebas.
    Inicializa configuraciones globales.
    """
    behave_logger.info("Iniciacion ejecucion de pruebas BDD con Behave")

    # Guardar opciones de Chrome en el contexto para reutilizar
    context.chrome_options = Options()
    context.chrome_options.add_argument("--headless")
    context.chrome_options.add_argument("--no-sandbox")
    context.chrome_options.add_argument("--disable-dev-shm-usage")

    # Crear directorio para screenshots si no existe
    screenshots_dir = (
        Path(__file__).parent.parent / "reports" / "screenshots" / "behave"
    )
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    context.screenshots_dir = screenshots_dir


def before_scenario(context, scenario):
    """
    Hook que se ejecuta antes de cada escenario.
    Crea un nuevo driver y registra el inicio de la prueba en los logs.
    """
    behave_logger.info(f"Iniciando escenario: {scenario.name}")
    behave_logger.info(f"Ubicacion: {scenario.feature.filename}:{scenario.line}")
    behave_logger.info(f"Tags: {scenario.effective_tags}")

    # Crear un nuevo driver para cada escenario
    context.driver = webdriver.Chrome(options=context.chrome_options)
    context.driver.implicitly_wait(10)
    behave_logger.debug("Driver de Chrome creado para este escenario")


def after_step(context, step):
    """
    Hook que se ejecuta después de cada paso.
    Verifica si el paso falló y guarda un screenshot en caso afirmativo.
    También registra el estado del paso en los logs.
    """
    if step.status == "failed":
        behave_logger.error(f"Paso fallido: {step.keyword} {step.name}")
        behave_logger.error(f"Error: {step.exception}")

        # Guardar screenshot del fallo
        scenario_name = context.scenario.name
        step_name = f"{step.keyword}_{step.name}".replace(" ", "_")
        screenshot_name = f"failure_{scenario_name}_{step_name}"

        try:
            screenshot_path = str(context.screenshots_dir / f"{screenshot_name}.png")
            take_screenshot(context.driver, screenshot_path)
            behave_logger.info(f"Screenshot guardado en: {screenshot_path}")

            # Guardar también la URL actual
            try:
                current_url = context.driver.current_url
                behave_logger.info(f"URL al momento del fallo: {current_url}")
            except Exception:
                pass

        except Exception as e:
            behave_logger.error(f"No se pudo guardar el screenshot: {e}")

    elif step.status == "passed":
        behave_logger.debug(f"Paso exitoso: {step.keyword} {step.name}")
    elif step.status == "skipped":
        behave_logger.warning(f"Paso omitido: {step.keyword} {step.name}")


def after_scenario(context, scenario):
    """
    Hook que se ejecuta después de cada escenario.
    Cierra el driver y registra el resultado final del escenario.
    """
    if scenario.status == "passed":
        behave_logger.info(f"Escenario exitoso: {scenario.name}")
    elif scenario.status == "failed":
        behave_logger.error(f"Escenario fallido: {scenario.name}")
    elif scenario.status == "skipped":
        behave_logger.warning(f"Escenario omitido: {scenario.name}")

    # Cerrar el driver después de cada escenario
    if hasattr(context, "driver"):
        try:
            context.driver.quit()
            behave_logger.debug("Driver cerrado para este escenario")
        except Exception as e:
            behave_logger.warning(f"Error al cerrar el driver: {e}")


def after_all(context):
    """
    Hook que se ejecuta una sola vez después de todas las pruebas.
    Limpia recursos y cierra la ejecución.
    """
    if hasattr(context, "temp_dir") and os.path.exists(context.temp_dir):
        try:
            shutil.rmtree(context.temp_dir, ignore_errors=True)
            behave_logger.info(f"Directorio temporal limpiado: {context.temp_dir}")
        except Exception as e:
            behave_logger.error(f"Error al limpiar directorio temporal: {e}")

    behave_logger.info("Finalizando ejecucion de pruebas BDD con Behave")
    behave_logger.info("Limpieza de recursos completada")
