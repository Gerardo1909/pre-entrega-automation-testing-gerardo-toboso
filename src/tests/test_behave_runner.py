"""
Wrapper para ejecutar pruebas de Behave desde pytest.
Esto permite unificar la ejecución de todas las pruebas (unitarias y BDD) en un solo comando.
"""

import os
import subprocess

import pytest

from utils.logger import behave_logger


@pytest.mark.behave
@pytest.mark.bdd
def test_run_behave_tests():
    """
    Ejecuta la suite completa de pruebas BDD con Behave.
    """
    behave_logger.info("Iniciacion ejecucion de pruebas BDD con Behave desde Pytest")
    reports_dir = os.path.join("src", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Ejecutar Behave completo con JSON y HTML
    result = subprocess.run(
        [
            "behave",
            "-f",
            "json",
            "-o",
            f"{reports_dir}/behave_full.json",
            "-f",
            "html",
            "-o",
            f"{reports_dir}/behave_full.html",
            "-f",
            "pretty",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )

    # Log detallado
    if result.stdout:
        behave_logger.info("Salida completa de Behave:")
        for line in result.stdout.split("\n"):
            if line.strip():
                behave_logger.info(f"  {line}")

    if result.stderr:
        behave_logger.error("Errores en suite completa:")
        for line in result.stderr.split("\n"):
            if line.strip():
                behave_logger.error(f"  {line}")

    # Verificar archivos de reporte generados
    _verify_report_generated(os.path.join(reports_dir, "behave_full.json"))
    _verify_report_generated(os.path.join(reports_dir, "behave_full.html"))

    # Asegurarse de que la ejecución fue exitosa
    assert result.returncode == 0, (
        f"La suite BDD completa falló con código {result.returncode}"
    )
    behave_logger.info("Finalizando ejecucion de pruebas BDD con Behave desde Pytest")


def _verify_report_generated(report_path):
    """
    Verifica que el reporte de Behave se haya generado correctamente.
    Args:
        report_path: Ruta al archivo de reporte
    """
    assert os.path.exists(report_path), f"No se generó el reporte en {report_path}"
    behave_logger.info(f"Reporte verificado: {report_path}")
