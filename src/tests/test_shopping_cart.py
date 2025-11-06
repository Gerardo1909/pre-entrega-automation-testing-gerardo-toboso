"""
Tests para el flujo de uso del carrito de compras en https://www.saucedemo.com/
"""

import pytest
from pages.catalog_page import CatalogPage


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

    # Act
    for i in range(6):
        catalog_page.add_product_to_cart_by_index(0)
    item_count = catalog_page.get_cart_item_count()

    # Assert
    assert item_count == 6


@pytest.mark.smoke
def test_cart_should_display_selected_product_when_cart_icon_is_clicked(
    selenium_driver,
):
    """
    Prueba que verifica que el carrito muestre el producto seleccionado al hacer clic en el ícono del carrito.
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)
    catalog_page.add_product_to_cart_by_index(0)

    # Act
    page = catalog_page.go_to_cart()
    cart_items = page.get_cart_items()
    item_names = page.get_item_names()

    # Assert
    assert len(cart_items) == 1
    assert item_names[0] == "Sauce Labs Backpack"


def test_cart_should_display_multiple_products_when_multiple_add_to_cart_buttons_are_clicked(
    selenium_driver,
):
    """
    Prueba que verifica que el carrito muestre múltiples productos seleccionados al hacer clic en varios botones "Add to cart".
    """
    # Arrange
    catalog_page = CatalogPage(selenium_driver)
    for i in range(6):
        catalog_page.add_product_to_cart_by_index(0)

    # Act
    page = catalog_page.go_to_cart()
    cart_items = page.get_cart_items()
    item_names = page.get_item_names()

    # Assert
    assert len(cart_items) == 6
    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names
    assert "Sauce Labs Bolt T-Shirt" in item_names
    assert "Sauce Labs Fleece Jacket" in item_names
    assert "Sauce Labs Onesie" in item_names
    assert "Test.allTheThings() T-Shirt (Red)" in item_names


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
