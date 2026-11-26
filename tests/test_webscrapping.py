"""
Suite de pruebas automatizadas con pytest para el pipeline de Web Scraping
y Analítica de Tiendas Branchos.

Propósito general:
    Verificar la integridad, estructura y calidad de los artefactos generados
    por el cuaderno `.ipynb`,
    asegurando que:
    1. El archivo CSV final exista y contenga registros válidos.
    2. Las columnas críticas estén presentes, sin valores nulos ni filas duplicadas.
    3. Los precios numéricos sean estrictamente mayores a cero.
    4. El cuaderno Jupyter y el reporte HTML (`index.html`) existan y no estén vacíos.

Uso desde la raíz del proyecto:
    pytest -v tests/test_webscrapping.py
"""

from pathlib import Path
import nbformat
import pandas as pd

# ==============================================================================
# CONFIGURACIÓN DE RUTAS Y CONSTANTES DEL PROYECTO
# ==============================================================================

# Se resuelve la carpeta raíz del proyecto subiendo dos niveles desde tests/test_webscrapping.py
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent

# Rutas esperadas de los artefactos principales en la raíz del repositorio
RUTA_CUADERNO = RAIZ_PROYECTO / "Melo_Luis_EA2_Analizando-Integracion-Scrapping-Github.ipynb"
RUTA_CSV_FINAL = RAIZ_PROYECTO / "Melo_Luis_EA2_camisetas_mujeres_analytics.csv"
RUTA_REPORTE = RAIZ_PROYECTO / "index.html"

# Parámetros de lectura del dataset generado por el pipeline
SEPARADOR_CSV = ";"
CODIFICACION_CSV = "utf-8-sig"

# Columnas indispensables para el análisis y visualización posterior
COLUMNAS_CRITICAS = ["Nombre del Producto", "Precio_Numerico", "Marca"]

# ==============================================================================
# CASOS DE PRUEBA (UNITARIOS Y DE CALIDAD DE DATOS)
# ==============================================================================

def test_csv_existe_y_tiene_datos():
    """
    Valida la existencia y disponibilidad inicial del dataset extraído.

    Verifica:
        - Que el archivo `camisetas_mujeres_analytics.csv` exista en la raíz.
        - Que pueda leerse correctamente con separador `;` y codificación `utf-8-sig`.
        - Que contenga al menos una fila de datos (scraping exitoso).
    """
    assert RUTA_CSV_FINAL.exists(), (
        f"Error crítico: No se encontró el archivo de datos en {RUTA_CSV_FINAL}."
    )

    df = pd.read_csv(RUTA_CSV_FINAL, sep=SEPARADOR_CSV, encoding=CODIFICACION_CSV)
    assert len(df) > 0, (
        "Error de extracción: El archivo CSV existe pero no contiene registros."
    )


def test_columnas_criticas_sin_nulos():
    """
    Valida el esquema y la limpieza básica del dataset consolidado.

    Verifica:
        - Que todas las columnas críticas (`Nombre del Producto`, `Precio_Numerico`, `Marca`)
          existan en el DataFrame.
        - Que no existan valores nulos (`NaN` / `None`) en dichas columnas.
        - Que no existan registros exactamente duplicados en el archivo final.
    """
    assert RUTA_CSV_FINAL.exists(), (
        f"No se encontró el archivo {RUTA_CSV_FINAL} para validar su esquema."
    )

    df = pd.read_csv(RUTA_CSV_FINAL, sep=SEPARADOR_CSV, encoding=CODIFICACION_CSV)

    # 1. Comprobación de presencia de columnas obligatorias
    for col in COLUMNAS_CRITICAS:
        assert col in df.columns, f"Falta la columna crítica requerida: '{col}'."

    # 2. Comprobación de ausencia de valores nulos en columnas críticas
    total_nulos = df[COLUMNAS_CRITICAS].isnull().sum().sum()
    assert total_nulos == 0, (
        f"Se detectaron {total_nulos} valores nulos en las columnas críticas."
    )

    # 3. Comprobación de unicidad de registros
    total_duplicados = df.duplicated().sum()
    assert total_duplicados == 0, (
        f"Se detectaron {total_duplicados} filas duplicadas en el dataset final."
    )


def test_precios_numericos_validos():
    """
    Valida la integridad cuantitativa de la columna `Precio_Numerico`.

    Verifica:
        - Que todos los valores puedan convertirse a tipo numérico sin errores.
        - Que todos los precios registrados sean estrictamente mayores a 0.
    """
    assert RUTA_CSV_FINAL.exists(), (
        f"No se encontró el archivo {RUTA_CSV_FINAL} para validar los precios."
    )

    df = pd.read_csv(RUTA_CSV_FINAL, sep=SEPARADOR_CSV, encoding=CODIFICACION_CSV)

    # Conversión segura a numérico para detectar textos residuales o símbolos mal limpiados
    precios = pd.to_numeric(df["Precio_Numerico"], errors="coerce")

    assert precios.notnull().all(), (
        "Existen valores no numéricos en la columna 'Precio_Numerico'."
    )
    assert (precios > 0).all(), (
        "Existen precios menores o iguales a cero en la columna 'Precio_Numerico'."
    )


def test_cuaderno_y_reporte_existen():
    """
    Valida la integridad de los entregables ejecutables y visuales del proyecto.

    Verifica:
        - Que el cuaderno Jupyter (`EA2_Analizando-Integracion-Scrapping-Github.ipynb`)
          exista, tenga formato válido (v4) y contenga al menos una celda de código.
        - Que el reporte web (`index.html`) exista y tenga contenido (tamaño > 0 bytes).
    """
    # 1. Validación estructural del cuaderno Jupyter
    assert RUTA_CUADERNO.exists(), (
        f"No se encontró el cuaderno principal en {RUTA_CUADERNO}."
    )

    with open(RUTA_CUADERNO, "r", encoding="utf-8") as archivo:
        notebook = nbformat.read(archivo, as_version=4)

    celdas_codigo = [celda for celda in notebook.cells if celda.cell_type == "code"]
    assert len(celdas_codigo) > 0, (
        "El cuaderno Jupyter no contiene celdas de código ejecutables."
    )

    # 2. Validación del reporte HTML generado
    assert RUTA_REPORTE.exists(), (
        f"No se encontró el reporte generado en {RUTA_REPORTE}."
    )
    assert RUTA_REPORTE.stat().st_size > 0, (
        "El archivo 'index.html' existe pero está completamente vacío (0 bytes)."
    )