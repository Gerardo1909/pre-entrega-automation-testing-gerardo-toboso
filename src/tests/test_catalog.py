"""
Tests para el flujo de uso de catalogo en https://www.saucedemo.com/
"""

import pytest
from selenium.webdriver.common.by import By


def test_catalog_should_display_correct_title_when_user_is_logged_in(loged_in_driver):
    """
    Prueba que verifica que el título del catálogo sea correcto para un usuario logueado.
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    title = loged_in_driver.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text

    # Assert
    assert title == "Products"


def test_catalog_should_display_products_when_user_is_logged_in(loged_in_driver):
    """
    Prueba que verifica que el catálogo muestre productos al usuario logueado.
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    products = loged_in_driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Assert
    assert len(products) > 0
    assert loged_in_driver.find_element(By.ID, "inventory_container").is_displayed()
    

def test_catalog_should_display_menu_when_menu_button_is_clicked(loged_in_driver):
    """
    Prueba que verifica que el menú se despliegue al hacer clic en el botón de menú.
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    loged_in_driver.find_element(By.ID, "react-burger-menu-btn").click()
    menu = loged_in_driver.find_element(By.CLASS_NAME, "bm-menu-wrap")

    # Assert
    assert menu.is_displayed()
    

def test_catalog_should_display_filters_when_filter_button_is_clicked(loged_in_driver):
    """
    Prueba que verifica que las opciones de filtro se desplieguen al hacer clic en el botón de filtro.
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    loged_in_driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    filters = loged_in_driver.find_elements(By.TAG_NAME, "option")

    # Assert
    assert len(filters) > 0
    
    
def test_catalog_should_display_cart_icon_when_user_is_logged_in(loged_in_driver):
    """
    Prueba que verifica que el ícono del carrito de compras se muestre para un usuario logueado.
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    cart_icon = loged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    # Assert
    assert cart_icon.is_displayed()

