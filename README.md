# Proyecto: Web Scrapping en Comercio Electrónico - Documentación Técnica

## Descripción General del Proyecto

Este repositorio documenta la integración del ciclo de vida analítico **CRISP-DM** con prácticas de **DevOps** para el análisis de catálogos de comercio electrónico (*e-commerce*), enfocado específicamente en camisetas de mujeres en Tienda E-Commerce. El proyecto es una propuesta de solucion de software a la brecha operativa entre la extracción no invasiva (web srapping), la gestión formal de configuración de entornos locales y remotos, control de versiones (Git-GitHub) y despliegue continuo (GitHub Actions-Workflows).

## Descripción del Método de Extracción Web Scrapping

El método de extracción implementado se basa en una estrategia de **Web Scraping No Invasivo** utilizando metadatos estructurados **JSON-LD** (*JavaScript Object Notation for Linked Data*). En lugar de depender de selectores CSS frágiles que se rompen frecuentemente ante actualizaciones o cambios visuales en el diseño del sitio web, el script en Python localiza, parsea e interpreta los bloques de metadatos oficiales inyectados directamente en el código fuente de la página. Esto permite capturar de manera limpia y estandarizada referencias comerciales, precios y marcas, evitando saturar la infraestructura del servidor de origen y garantizando un conjunto de datos tabular consistente y de alta calidad para su posterior análisis. 

Se emplean practicas eticas como tiempos de pausa estrictos (Rate Limiting) de 3.0 sdegundos, validacion previa del archivo robots.txt y se usa la cabecera de Identificación (User-Agent) para transparencia del script. Esto con el fin de no saturar el servidor y de respeto al sitio web.


## Tecnologías, Librerías y Versiones
| Componente / Herramienta | Versión | Propósito Técnico |
| :--- | :--- | :--- |
| **Python** | 3.10+ | Entorno de ejecución para los scripts de minería y análisis de datos. |
| **IntelliJ IDEA** | Latest | Entorno de desarrollo para gestión visual y terminal integrada. |
| **Git Bash (MINGW64)** | 2.x | Interfaz de línea de comandos para control de versiones local. |
| **GitHub** | Cloud | Alojamiento del repositorio oficial (`origin/main`) y flujos CI/CD. |
| **`beautifulsoup4`** | v4.12.x | Análisis sintáctico de documentos HTML para extracción de metadatos. |
| **`requests`** | v2.31.x | Ejecución de peticiones GET seguras hacia el portal web. |
| **`pandas`** | v2.1.x | Limpieza, transformación y exportación de datos tabulares a CSV. |
| **`json` (Nativo)** | Python | Parseo y validación de estructuras JSON-LD. |
| **`ipykernel`** | v6.x | Núcleo de Jupyter integrado para la ejecución interactiva del código estructurado por celdas. |

---

## Prácticas Éticas y Manejo de JSON-LD
* **Acceso No Invasivo:** Las peticiones al servidor se realizan de forma controlada y espaciada para evitar la saturación de la infraestructura de origen.
* **Uso Exclusivo de Datos Públicos:** Extracción limitada a la información abierta del catálogo (precios, marcas y referencias), omitiendo credenciales o áreas privadas.
* **Estrategia JSON-LD (*JavaScript Object Notation for Linked Data*):** En lugar de depender de selectores CSS frágiles que se rompen ante cambios de diseño, el sistema extrae metadatos estructurados oficiales inyectados en el código fuente. Esto garantiza la integridad y estandarización del *dataset* resultante.

---

## Guía de Instalación y Configuración del Entorno
El proceso general de instalación y configuración del proyecto consta de las siguientes etapas:

1. **Obtención del Código Fuente:** Se descarga o clona el repositorio oficial del proyecto en la máquina de trabajo utilizando Git y la terminal Git Bash.
2. **Instalación de Dependencias y Soporte por Celdas:** Se instalan las librerías oficiales de Python necesarias (`beautifulsoup4`, `requests` y `pandas`), junto con el paquete `ipykernel` para permitir la ejecución y lectura interactiva del código estructurado por celdas en el entorno de desarrollo elegido. 
3. **Configuración de Identidad y Privacidad:** Se configuran los parámetros básicos de usuario en Git, asociando una identidad segura y protegida, se sugiere el correo privado (`noreply`) provisto por GitHub para garantizar la trazabilidad correcta de los cambios, sin embargo la elecccion de los tokens de acceso y las autenticaciones son de eleccion de cada quien.
4. Nota: Este proyecto se realizo en el entorno IntelliJ IDEA-Git Bash y GitHub con Autenticacion 0Auth.
---

## Estructura del Repositorio (Fase 2)
```text
/
├── .github/
│   └── workflows/
│       └── main.yml        # Esqueleto base para Pipeline de Integración Continua (CI/CD) (fase 3)
├── Melo_Luis_EA2_camisetas_mujeres_analytics.csv                # Dataset exportado obtenido del script srapping
├── Melo_Luis_EA2_Analizando-Integracion-Scrapping-Github.ipynb  # Script principal de Web Scraping 
└── README.md               # Documentación técnica del proyecto

```

## Flujo de Trabajo y Automatización (Integracion CRISP-DM + DevOps)

* **1. Comprensión del Negocio y Datos:** Análisis inicial del problema de comercio electrónico, identificando la distribución heterogénea de precios y la necesidad de consolidar información de camisetas en Tiendas Branchos (CRISP-DM Fases 1-2).
* **2. Extracción No Invasiva JSON-LD:** Ejecución del script en Python utilizando `requests` y `beautifulsoup4` para capturar metadatos JSON-LD estructurados sin comprometer los servidores del portal.
* **3. Versionamiento Local:** Gestión y procesamiento de la información mediante celdas con `ipykernel`, organizando el código y asegurando la trazabilidad local con el flujo híbrido de IntelliJ IDEA y Git Bash, empleando identidades protegidas (`@users.noreply.github.com`).
* **4. Repositorio Remoto y Sincronización:** Consolidación y envío de los cambios mediante *commits* y *push* hacia la rama principal (`origin/main`) en GitHub utilizando autenticación segura.
* **5. Integración Continua y Despliegue futura (Fase 3):** Ejecución automática de validaciones, pruebas de infraestructura y gestión de artefactos a través del archivo de automatización ubicado en `.github/workflows/main.yml`.

---

# EA3 - Etapa Final - Automatizado y Presentacion del Web Scrapping - Tiendas Branchos

Pipeline de **Web Scraping, Analítica de Precios e Integración Continua (CI/CD)** construido en Python 3.13 y automatizado con **GitHub Actions** para rastrear el catálogo de camisetas para mujer en Tiendas Branchos, detectar variaciones de precios y publicar un tablero analítico estático (`index.html`).

## Estructura Final del Proyecto

| Archivo / Carpeta | Descripción |
| :--- | :--- |
| `EA2_Analizando-Integracion-Scrapping-Github.ipynb` | Cuaderno principal con el flujo de extracción, limpieza, comparación histórica y generación del reporte HTML. |
| `EA2_camisetas_mujeres_analytics.csv` | Dataset procesado de la ejecución más reciente. |
| `EA2_camisetas_mujeres_anterior.csv` | Respaldo histórico utilizado para calcular productos nuevos, faltantes y movimientos de precios. |
| `index.html` | Reporte visual interactivo con métricas comparativas, gráficos, marca líder, variaciones de precio por MPN y buscador. |
| `tests/test_webscrapping.py` | Suite de pruebas automatizadas con `pytest` para validar calidad de datos y estructura de salida. |
| `requirements.txt` | Dependencias de Python necesarias para ejecutar el pipeline. |
| `.github/workflows/main.yml` | Definición del flujo de CI/CD en GitHub Actions. |
| `.gitignore` | Reglas de exclusión para evitar versionar datos crudos (`ea1_...csv`) y artefactos temporales. |

## Funcionamiento del Pipeline CI/CD

El flujo de trabajo definido en `.github/workflows/main.yml` se ejecuta bajo tres modalidades:
1. **Integración Continua (`push` a `main`):** Se activa automáticamente ante cambios en el código o pruebas, ignorando modificaciones exclusivas en `index.html` y los archivos `.csv` (`paths-ignore`) para evitar bucles de ejecución.
2. **Ejecución Programada (`schedule`):** Corre todos los domingos a las **12:00 UTC (07:00 AM hora Colombia)**.
3. **Ejecución Manual (`workflow_dispatch`):** Puede lanzarse bajo demanda desde la pestaña **Actions > Run workflow** en GitHub.

### Etapas de ejecución
1. Configura un entorno limpio en `ubuntu-latest` con **Python 3.13**.
2. Instala dependencias desde `requirements.txt`.
3. Ejecuta el cuaderno mediante `jupyter nbconvert` generando una copia temporal (`EA2_ejecutado.ipynb`) sin alterar el cuaderno original.
4. Corre las pruebas de calidad (`pytest -v tests/test_webscrapping.py`). Si alguna prueba falla, el pipeline se detiene y no publica datos corruptos.
5. Verifica si hubo cambios en `Melo_Luis_EA2_camisetas_mujeres_analytics.csv`, `Melo_Luis_EA2_camisetas_mujeres_anterior.csv` o `index.html`; de existir cambios, registra un commit automático firmado por `github-actions[bot]`.

## Presentacion de Resultados Finales - Reporte en vivo (GitHub Pages)

Consultar el dashboard comparativo actualizado automáticamente aquí: 
- [Ver reporte en GitHub Pages] Visit site: https://alejoo-hdz.github.io/web-scraping-ecommerce-bs4/


### Autor y Proposito

Proyecto desarrollado como práctica académica y se realiza exclusivamente con fines académicos e investigativos bajo los lineamientos institucionales y metodológicos establecidos, garantizando la transparencia, reproducibilidad y buenas prácticas en la ingeniería de software y análisis de datos.