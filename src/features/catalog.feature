# language: es
Característica: Catálogo de productos en SauceDemo
  Como usuario autenticado de SauceDemo
  Quiero poder ver y manipular el catálogo de productos
  Para encontrar los artículos que deseo comprar

  Antecedentes:
    Dado que estoy autenticado como usuario estándar

  @smoke @ui
  Escenario: Ver el título del catálogo
    Cuando accedo a la página del catálogo
    Entonces debería ver el título "Products"

  @smoke @ui
  Escenario: Ver productos en el catálogo
    Cuando accedo a la página del catálogo
    Entonces debería ver al menos 1 producto disponible

  @ui
  Escenario: Ver cantidad correcta de productos
    Cuando accedo a la página del catálogo
    Entonces debería ver exactamente 6 productos disponibles

  @ui
  Escenario: Verificar que todos los productos tienen nombre
    Cuando accedo a la página del catálogo
    Entonces todos los productos deberían tener un nombre válido

  @ui
  Escenario: Verificar que todos los productos tienen botón de agregar al carrito
    Cuando accedo a la página del catálogo
    Entonces todos los productos deberían tener un botón "Add to cart"
