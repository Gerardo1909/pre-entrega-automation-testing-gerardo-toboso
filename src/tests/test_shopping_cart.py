"""
Tests para el flujo de uso del carrito de compras en https://www.saucedemo.com/
"""

import pytest
from selenium.webdriver.common.by import By


def test_product_should_be_added_to_cart_when_add_to_cart_button_is_clicked(
    loged_in_driver,
):
    """
    Prueba que verifica que un producto se agregue al carrito al hacer clic en el botón "Add to cart".
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_badge = loged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    # Assert
    assert cart_badge.is_displayed()
    assert cart_badge.text == "1"


def test_multiple_products_should_be_added_to_cart_when_add_to_cart_buttons_are_clicked(
    loged_in_driver,
):
    """
    Prueba que verifica que múltiples productos se agreguen al carrito al hacer clic en varios botones "Add to cart".
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")

    # Act
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    loged_in_driver.find_element(
        By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
    ).click()
    cart_badge = loged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    # Assert
    assert cart_badge.is_displayed()
    assert cart_badge.text == "6"


def test_cart_should_display_selected_product_when_cart_icon_is_clicked(
    loged_in_driver,
):
    """
    Prueba que verifica que el carrito muestre el producto seleccionado al hacer clic en el ícono del carrito.
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Act
    loged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = loged_in_driver.find_elements(By.CLASS_NAME, "cart_item")

    # Assert
    assert len(cart_items) == 1
    assert (
        cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        == "Sauce Labs Backpack"
    )


def test_cart_should_display_multiple_products_when_multiple_add_to_cart_buttons_are_clicked(
    loged_in_driver,
):
    """
    Prueba que verifica que el carrito muestre múltiples productos seleccionados al hacer clic en varios botones "Add to cart".
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    loged_in_driver.find_element(
        By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
    ).click()

    # Act
    loged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_items = loged_in_driver.find_elements(By.CLASS_NAME, "cart_item")

    # Assert
    assert len(cart_items) == 6
    product_names = [
        item.find_element(By.CLASS_NAME, "inventory_item_name").text
        for item in cart_items
    ]
    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names
    assert "Sauce Labs Bolt T-Shirt" in product_names
    assert "Sauce Labs Fleece Jacket" in product_names
    assert "Sauce Labs Onesie" in product_names
    assert "Test.allTheThings() T-Shirt (Red)" in product_names


def test_cart_should_remove_product_when_remove_button_is_clicked(loged_in_driver):
    """
    Prueba que verifica que un producto se elimine del carrito al hacer clic en el botón "Remove".
    """
    # Arrange
    loged_in_driver.get("https://www.saucedemo.com/inventory.html")
    loged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    loged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Act
    loged_in_driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    cart_items = loged_in_driver.find_elements(By.CLASS_NAME, "cart_item")

    # Assert
    assert len(cart_items) == 0
