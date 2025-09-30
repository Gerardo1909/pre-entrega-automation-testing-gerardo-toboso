# Pre-Entrega de Proyecto - Curso QA Automation

**Realizado por: Gerardo Toboso**

## Propósito

El propósito de esta pre-entrega de proyecto es aplicar los conocimientos adquiridos sobre la **automatización de pruebas de software** 
haciendo uso de **Python** como lenguaje de programación principal y librerías pertinentes para este contexto como lo son **Pytest y Selenium**. Los puntos que se ponen en práctica más precisamente son:

* Automatización de flujos básicos de navegación web utilizando **Selenium WebDriver**.

* Interacción con elementos web.

* Estrategias de localización y validación de estados dentro de una página.

* Construir un conjunto de pruebas extenso que abarque las funcionalidades más importantes de la página.

En este caso la página que se estará utilizando será [saucedemo.com](https://www.saucedemo.com/), la cual está diseñada
exclusivamente para llevar a cabos pruebas de esta índole.

## Tecnologías usadas

* **Python 3.13+**: Lenguaje de programación principal
* **Selenium 4.35.0**: Automatización de navegador web
* **Pytest 8.4.2**: Framework de testing
* **Pytest-HTML 4.1.1**: Generación de reportes HTML para las pruebas

## Estructura del proyecto

```text
pre-entrega-automation-testing-gerardo_toboso/
├── src/
│   ├── tests/          # Casos de prueba automatizados
│   └── utils/          # Utilidades y funciones auxiliares
├── .gitignore          # .git para ignorar archivos innecesarios
├── .python-version     # Especifica la versión de Python con la que se trabaja
├── requirements.txt    # Dependencias del proyecto
├── pyproject.toml      # Configuración del proyecto
└── README.md           # Este archivo
```

## Instrucciones de instalación de dependencias

> Antes de seguir los siguientes pasos asegúrate de tener Python 3.13+ instalado en tu máquina local.

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Gerardo1909/pre-entrega-automation-testing-gerardo_toboso.git
   cd pre-entrega-automation-testing-gerardo_toboso
   ```

2. Crea un entorno virtual (recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Mac/Linux
```

3. Instala las dependencias usando pip:

   ```bash
   pip install -r requirements.txt
   ```

## Comandos para ejecutar las pruebas

* **Ejecutar todas las pruebas**:

  ```bash
  pytest src/tests/
  ```

* **Ejecutar pruebas con reporte HTML**:

  ```bash
  pytest src/tests/ --html=reports/report.html --self-contained-html
  ```

* **Ejecutar pruebas en modo verbose**:

  ```bash
  pytest src/tests/ -v
  ```