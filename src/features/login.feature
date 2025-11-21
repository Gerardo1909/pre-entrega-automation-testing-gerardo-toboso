# language: es
Característica: Inicio de sesión en SauceDemo
  Como usuario de SauceDemo
  Quiero poder iniciar sesión con mis credenciales
  Para poder acceder al catálogo de productos

  Antecedentes:
    Dado que estoy en la página de inicio de sesión

  @smoke @ui
  Esquema del escenario: Login con diferentes credenciales
    Cuando ingreso el usuario "<usuario>" y la contraseña "<clave>"
    Y hago clic en el botón de login
    Entonces debería "<resultado>" acceder al catálogo

    Ejemplos:
      | usuario                 | clave          | resultado |
      | standard_user           | secret_sauce   | poder     |
      | locked_out_user         | secret_sauce   | no poder  |
      | problem_user            | secret_sauce   | poder     |
      | performance_glitch_user | secret_sauce   | poder     |
      | error_user              | secret_sauce   | poder     |
      | visual_user             | secret_sauce   | poder     |
      | invalid_user            | wrong_password | no poder  |

  @ui
  Escenario: Login exitoso con usuario estándar
    Cuando ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    Y hago clic en el botón de login
    Entonces debería ser redirigido a la página de inventario
    Y la URL debería contener "inventory.html"
