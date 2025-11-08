"""
Tests para el flujo de uso del carrito de compras en https://www.saucedemo.com/
"""

from pathlib import Path

import pytest

from pages.catalog_page import CatalogPage
from utils.json_reader import JSONReader

# Cargar nombres de productos desde el archivo JSON
PRODUCTOS_JSON_PATH = Path(__file__).parent.parent / "data" / "productos.json"
json_reader = JSONReader(str(PRODUCTOS_JSON_PATH))
NOMBRES_PRODUCTOS = json_reader.read_field_as_tuples("nombre")
PRODUCTOS_COMPLETOS = json_reader.read_as_dicts()


@pytest.mark.smoke
def test_product_should_be_added_to_cart_when_add_to_cart_button_is_clicked(
    selenium_driver,
):
    """
    Prueba que verifica que un producto se agregue al carrito al hacer clic en el botón "Add to cart".
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)

    # Act
    catalog_page.add_product_to_cart_by_index(0)
    item_count = catalog_page.get_cart_item_count()

    # Assert
    assert item_count == 1


def test_multiple_products_should_be_added_to_cart_when_add_to_cart_buttons_are_clicked(
    selenium_driver,
):
    """
    Prueba que verifica que múltiples productos se agreguen al carrito al hacer clic en varios botones "Add to cart".
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)
    expected_count = 6

    # Act
    for i in range(expected_count):
        catalog_page.add_product_to_cart_by_index(0)
    item_count = catalog_page.get_cart_item_count()

    # Assert
    assert item_count == expected_count


@pytest.mark.parametrize("nombre_producto", NOMBRES_PRODUCTOS)
def test_cart_should_display_product_when_added_and_cart_icon_clicked(
    selenium_driver, nombre_producto
):
    """
    Test parametrizado que verifica que el carrito muestre el producto correcto
    cuando se agrega y se accede al carrito.
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)
    catalog_page.add_product_to_cart_by_name(nombre_producto)

    # Act
    cart_page = catalog_page.go_to_cart()
    cart_items = cart_page.get_cart_items()
    item_names = cart_page.get_item_names()

    # Assert
    assert len(cart_items) == 1
    assert nombre_producto in item_names


@pytest.mark.parametrize("nombre_producto", NOMBRES_PRODUCTOS)
def test_cart_should_display_all_products_when_multiple_products_added(
    selenium_driver, nombre_producto, productos_agregados=PRODUCTOS_COMPLETOS
):
    """
    Prueba que verifica que el carrito muestre todos los productos cuando se agregan múltiples productos.
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)

    # Act
    for producto in productos_agregados:
        catalog_page.add_product_to_cart_by_name(producto["nombre"])

    cart_page = catalog_page.go_to_cart()
    cart_items = cart_page.get_cart_items()
    item_names = cart_page.get_item_names()

    # Assert
    assert len(cart_items) == len(productos_agregados)
    assert nombre_producto in item_names


@pytest.mark.smoke
def test_cart_should_remove_product_when_remove_button_is_clicked(selenium_driver):
    """
    Prueba que verifica que un producto se elimine del carrito al hacer clic en el botón "Remove".
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)
    catalog_page.add_product_to_cart_by_index(0)
    page = catalog_page.go_to_cart()

    # Act
    page.click_remove_button_by_index(0)
    cart_items = page.get_cart_items()

    # Assert
    assert len(cart_items) == 0
