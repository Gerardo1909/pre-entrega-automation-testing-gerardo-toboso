"""
Tests para el flujo de uso de catalogo en https://www.saucedemo.com/
"""

import pytest
from pages.catalog_page import CatalogPage


def test_catalog_should_display_correct_title_when_user_is_logged_in(selenium_driver):
    """
    Prueba que verifica que el título del catálogo sea correcto para un usuario logueado.
    """
    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    title = page.get_title()

    # Assert
    assert title == "Products"


def test_catalog_should_display_products_when_user_is_logged_in(selenium_driver):
    """
    Prueba que verifica que el catálogo muestre productos al usuario logueado.
    """
    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    products = page.get_products()

    # Assert
    assert len(products) > 0


def test_catalog_should_display_menu_when_menu_button_is_clicked(selenium_driver):
    """
    Prueba que verifica que el menú se despliegue al hacer clic en el botón de menú.
    """
    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    page.click_menu_button()

    # Assert
    assert page.menu_is_displayed()


def test_catalog_should_display_filters_when_filter_button_is_clicked(selenium_driver):
    """
    Prueba que verifica que las opciones de filtro se desplieguen al hacer clic en el botón de filtro.
    """
    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    page.click_filter_button()
    filters = page.get_filter_options()

    # Assert
    assert len(filters) > 0


def test_catalog_should_display_cart_icon_when_user_is_logged_in(selenium_driver):
    """
    Prueba que verifica que el ícono del carrito de compras se muestre para un usuario logueado.
    """
    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    is_cart_displayed = page.cart_is_displayed()

    # Assert
    assert is_cart_displayed
