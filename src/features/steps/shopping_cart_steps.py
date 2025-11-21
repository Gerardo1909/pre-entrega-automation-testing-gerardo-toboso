"""
Definiciones de pasos (steps) para las pruebas de carrito de compras con Behave.
"""

from behave import given, when, then

from utils.logger import behave_logger


@given("estoy en la página del catálogo")
def step_on_catalog_page(context):
    """Verifica que estamos en la página del catálogo."""
    assert "/inventory.html" in context.driver.current_url, (
        f"No estamos en el catálogo. URL actual: {context.driver.current_url}"
    )
    behave_logger.debug("En la página del catálogo")


@when("agrego el producto en la posición {index:d} al carrito")
def step_add_product_by_index(context, index):
    """Agrega un producto al carrito por su posición."""
    context.catalog_page.add_product_to_cart_by_index(index)
    behave_logger.debug(f"Producto en posición {index} agregado al carrito")


@when("agrego {count:d} productos al carrito")
def step_add_multiple_products(context, count):
    """Agrega múltiples productos al carrito."""
    for i in range(count):
        context.catalog_page.add_product_to_cart_by_index(i)
    behave_logger.debug(f"{count} productos agregados al carrito")


@when('agrego el producto "{product_name}" al carrito')
def step_add_product_by_name(context, product_name):
    """Agrega un producto al carrito por su nombre."""
    context.catalog_page.add_product_to_cart_by_name(product_name)
    context.added_product_name = product_name
    behave_logger.debug(f"Producto '{product_name}' agregado al carrito")


@when("navego al carrito de compras")
def step_navigate_to_cart(context):
    """Navega a la página del carrito de compras."""
    context.cart_page = context.catalog_page.go_to_cart()
    behave_logger.debug("Navegado al carrito de compras")


@when("elimino el producto en la posición {index:d} del carrito")
def step_remove_product_from_cart(context, index):
    """Elimina un producto del carrito por su posición."""
    context.cart_page.click_remove_button_by_index(index)
    behave_logger.debug(f"Producto en posición {index} eliminado del carrito")


@then("el contador del carrito debería mostrar {expected_count:d} artículo")
@then("el contador del carrito debería mostrar {expected_count:d} artículos")
def step_verify_cart_count(context, expected_count):
    """Verifica el contador de artículos en el carrito."""
    actual_count = context.catalog_page.get_cart_item_count()
    assert actual_count == expected_count, (
        f"Contador incorrecto. Esperado: {expected_count}, Obtenido: {actual_count}"
    )
    behave_logger.info(f"Contador del carrito verificado: {expected_count} artículo(s)")


@then('el producto "{product_name}" debería estar en el carrito')
def step_verify_product_in_cart(context, product_name):
    """Verifica que un producto específico esté en el carrito."""
    # Navegar al carrito si aún no estamos ahí
    if not hasattr(context, "cart_page"):
        context.cart_page = context.catalog_page.go_to_cart()

    item_names = context.cart_page.get_item_names()
    assert product_name in item_names, (
        f"Producto '{product_name}' no encontrado en carrito. Productos: {item_names}"
    )
    behave_logger.info(f"Producto '{product_name}' verificado en el carrito")


@then("debería ver {expected_count:d} producto en el carrito")
@then("debería ver {expected_count:d} productos en el carrito")
def step_verify_products_in_cart_page(context, expected_count):
    """Verifica la cantidad de productos en la página del carrito."""
    cart_items = context.cart_page.get_cart_items()
    actual_count = len(cart_items)
    assert actual_count == expected_count, (
        f"Cantidad incorrecta en carrito. Esperado: {expected_count}, Obtenido: {actual_count}"
    )
    behave_logger.info(f"Cantidad de productos en carrito verificada: {expected_count}")


@then("no debería haber productos en el carrito")
def step_verify_empty_cart(context):
    """Verifica que el carrito esté vacío."""
    cart_items = context.cart_page.get_cart_items()
    actual_count = len(cart_items)
    assert actual_count == 0, (
        f"El carrito no está vacío. Productos encontrados: {actual_count}"
    )
    behave_logger.info("Carrito vacío verificado correctamente")
