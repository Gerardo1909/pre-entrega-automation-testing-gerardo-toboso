"""
Definiciones de pasos (steps) para las pruebas de catálogo con Behave.
"""

from behave import given, then, when

from pages.catalog_page import CatalogPage
from utils.logger import behave_logger


@given("que estoy autenticado como usuario estándar")
def step_login_as_standard_user(context):
    """Inicia sesión como usuario estándar."""
    context.catalog_page = CatalogPage(context.driver)
    behave_logger.debug("Usuario estándar autenticado")


@when("accedo a la página del catálogo")
def step_access_catalog(context):
    """Accede a la página del catálogo."""
    # El catálogo ya está cargado por el CatalogPage init
    behave_logger.debug(f"Accediendo a catálogo en: {context.driver.current_url}")


@then('debería ver el título "{expected_title}"')
def step_verify_title(context, expected_title):
    """Verifica el título de la página."""
    actual_title = context.catalog_page.get_title()
    assert actual_title == expected_title, (
        f"Título incorrecto. Esperado: {expected_title}, Obtenido: {actual_title}"
    )
    behave_logger.info(f"Título verificado correctamente: {expected_title}")


@then("debería ver al menos {min_count:d} producto disponible")
@then("debería ver al menos {min_count:d} productos disponibles")
def step_verify_minimum_products(context, min_count):
    """Verifica que haya al menos una cantidad mínima de productos."""
    products = context.catalog_page.get_products()
    actual_count = len(products)
    assert actual_count >= min_count, (
        f"Productos insuficientes. Esperado al menos: {min_count}, Obtenido: {actual_count}"
    )
    behave_logger.info(
        f"Productos encontrados: {actual_count} (mínimo requerido: {min_count})"
    )


@then("debería ver exactamente {expected_count:d} productos disponibles")
def step_verify_exact_products(context, expected_count):
    """Verifica que haya exactamente una cantidad específica de productos."""
    products = context.catalog_page.get_products()
    actual_count = len(products)
    assert actual_count == expected_count, (
        f"Cantidad incorrecta de productos. Esperado: {expected_count}, Obtenido: {actual_count}"
    )
    behave_logger.info(f"Cantidad exacta de productos verificada: {expected_count}")


@then("todos los productos deberían tener un nombre válido")
def step_verify_all_products_have_name(context):
    """Verifica que todos los productos tengan un nombre."""
    products = context.catalog_page.get_products()
    product_names = context.catalog_page.get_product_names()

    assert len(product_names) == len(products), "No todos los productos tienen nombre"

    for name in product_names:
        assert name.strip(), "Se encontró un producto sin nombre"

    behave_logger.info(f"Todos los {len(products)} productos tienen nombre válido")


@then('todos los productos deberían tener un botón "Add to cart"')
def step_verify_all_products_have_add_button(context):
    """Verifica que todos los productos tengan botón de agregar al carrito."""
    products = context.catalog_page.get_products()
    add_buttons = context.catalog_page.get_add_to_cart_buttons()

    assert len(add_buttons) == len(products), (
        f"No todos los productos tienen botón. Productos: {len(products)}, Botones: {len(add_buttons)}"
    )

    behave_logger.info(
        f"Todos los {len(products)} productos tienen botón 'Add to cart'"
    )
