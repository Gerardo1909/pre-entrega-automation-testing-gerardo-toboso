"""
Tests para el flujo de uso de catalogo en https://www.saucedemo.com/
"""

import pytest
from pages.catalog_page import CatalogPage
from utils.logger import logger


@pytest.mark.smoke
@pytest.mark.ui
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


@pytest.mark.smoke
@pytest.mark.ui
def test_catalog_should_display_products_when_user_is_logged_in(selenium_driver):
    """
    Prueba que verifica que el catálogo muestre productos al usuario logueado.
    """
    logger.info("Iniciando test_catalog_should_display_products_when_user_is_logged_in")

    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    products = page.get_products()
    logger.info(f"Productos encontrados: {len(products)}")

    # Assert
    assert len(products) > 0
    logger.info("Test completado exitosamente")


@pytest.mark.ui
def test_catalog_should_display_menu_when_menu_button_is_clicked(selenium_driver):
    """
    Prueba que verifica que el menú se despliegue al hacer clic en el botón de menú.
    """
    logger.info(
        "Iniciando test_catalog_should_display_menu_when_menu_button_is_clicked"
    )

    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    logger.info("Haciendo clic en boton de menu")
    page.click_menu_button()

    # Assert
    assert page.menu_is_displayed()
    logger.info("Test completado exitosamente")


@pytest.mark.ui
def test_catalog_should_display_filters_when_filter_button_is_clicked(selenium_driver):
    """
    Prueba que verifica que las opciones de filtro se desplieguen al hacer clic en el botón de filtro.
    """
    logger.info(
        "Iniciando test_catalog_should_display_filters_when_filter_button_is_clicked"
    )

    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    page.click_filter_button()
    filters = page.get_filter_options()
    logger.info(f"Filtros encontrados: {len(filters)}")

    # Assert
    assert len(filters) > 0
    logger.info("Test completado exitosamente")


@pytest.mark.ui
def test_catalog_should_display_cart_icon_when_user_is_logged_in(selenium_driver):
    """
    Prueba que verifica que el ícono del carrito de compras se muestre para un usuario logueado.
    """
    logger.info(
        "Iniciando test_catalog_should_display_cart_icon_when_user_is_logged_in"
    )

    # Arrange
    page = CatalogPage(selenium_driver)

    # Act
    is_cart_displayed = page.cart_is_displayed()
    logger.info(f"Icono del carrito visible: {is_cart_displayed}")

    # Assert
    assert is_cart_displayed
    logger.info("Test completado exitosamente")
