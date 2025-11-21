# language: es
Característica: Carrito de compras en SauceDemo
  Como usuario autenticado de SauceDemo
  Quiero poder agregar y gestionar productos en mi carrito
  Para poder realizar una compra

  Antecedentes:
    Dado que estoy autenticado como usuario estándar
    Y estoy en la página del catálogo

  @smoke @ui
  Escenario: Agregar un producto al carrito
    Cuando agrego el producto en la posición 0 al carrito
    Entonces el contador del carrito debería mostrar 1 artículo

  @ui
  Escenario: Agregar múltiples productos al carrito
    Cuando agrego 3 productos al carrito
    Entonces el contador del carrito debería mostrar 3 artículos

  @ui
  Esquema del escenario: Agregar productos específicos al carrito por nombre
    Cuando agrego el producto "<nombre_producto>" al carrito
    Entonces el producto "<nombre_producto>" debería estar en el carrito

    Ejemplos:
      | nombre_producto              |
      | Sauce Labs Backpack          |
      | Sauce Labs Bike Light        |
      | Sauce Labs Bolt T-Shirt      |
      | Sauce Labs Fleece Jacket     |

  @ui
  Escenario: Ver el carrito de compras
    Cuando agrego el producto en la posición 0 al carrito
    Y navego al carrito de compras
    Entonces debería ver el título "Your Cart"
    Y debería ver 1 producto en el carrito

  @ui
  Escenario: Eliminar producto del carrito
    Cuando agrego el producto en la posición 0 al carrito
    Y navego al carrito de compras
    Y elimino el producto en la posición 0 del carrito
    Entonces no debería haber productos en el carrito
