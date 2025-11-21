"""
Definiciones de pasos (steps) para las pruebas de inicio de sesión con Behave.
"""

from behave import given, then, when

from pages.login_page import LoginPage
from utils.logger import behave_logger


@given("que estoy en la página de inicio de sesión")
def step_open_login_page(context):
    """Abre la página de inicio de sesión."""
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    behave_logger.debug("Página de login abierta")


@when('ingreso el usuario "{username}" y la contraseña "{password}"')
def step_enter_credentials(context, username, password):
    """Ingresa las credenciales de usuario."""
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    behave_logger.debug(f"Credenciales ingresadas - Usuario: {username}")


@when("hago clic en el botón de login")
def step_click_login(context):
    """Hace clic en el botón de login."""
    context.login_page.click_login()
    behave_logger.debug("Clic en botón de login")


@then('debería "{result}" acceder al catálogo')
def step_verify_login_result(context, result):
    """Verifica si el login fue exitoso o no."""
    if result == "poder":
        assert "/inventory.html" in context.driver.current_url, (
            f"Login falló. URL actual: {context.driver.current_url}"
        )
        behave_logger.info("Login exitoso - Redirigido a catálogo")
    else:
        assert context.login_page.error_is_displayed(), (
            "Se esperaba un mensaje de error pero no se mostró"
        )
        behave_logger.info("Login fallido como se esperaba - Error mostrado")


@then("debería ser redirigido a la página de inventario")
def step_verify_redirect_to_inventory(context):
    """Verifica que se haya redirigido a la página de inventario."""
    assert "/inventory.html" in context.driver.current_url, (
        f"No se redirigió a inventario. URL actual: {context.driver.current_url}"
    )
    behave_logger.info("Redirigido correctamente a inventario")


@then('la URL debería contener "{text}"')
def step_verify_url_contains(context, text):
    """Verifica que la URL contenga un texto específico."""
    assert text in context.driver.current_url, (
        f"La URL no contiene '{text}'. URL actual: {context.driver.current_url}"
    )
    behave_logger.debug(f"URL contiene '{text}' correctamente")
