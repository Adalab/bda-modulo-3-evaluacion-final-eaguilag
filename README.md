![Cabecera. Evaluacion Final Modulo 3. Elena Águila García](https://github.com/eaguilag/testing-git/blob/main/assets/elena-aguila-cabecera-evaluacion-modulo-3.png)
# EVALUACIÓN FINAL MÓDULO 3
*Elena Águila García* [@eaguilag](https://github.com/eaguilag)


## INTRODUCCIÓN

Ejercicio de evaluación final del **Módulo 3** del Bootcamp de **Análisis de Datos**. Durante este módulo se ha profundizado en la manipulación y transformación de datos utilizando librerías como Pandas y NumPy. Este ejercicio tiene el objetivo la exploración de conjuntos de datos con Python mediante el proceso de EDA (Exploratory Data Analysis), la visualización de datos con Seaborn y Matplotlib, la técnica del A/B testing así como el proceso de ETL (Extraction, Transformation, and Loading).

### Objetivos del módulo

- Manejar con soltura Pandas y todas sus funcionalidades.
- Justificar en base a datos la gestión de nulos.
- Inserción de datos en una base de datos usando Python.
- Estadística descriptiva e inferencial.
- A/B testing.


## ENTENDIENDO EL FICHERO

El ejercicio de evaluación se encuentra Jupyter Notebook dentro del repositorio. El archivo está nombrado como [bda-modulo-3-evaluacion-final-promo-angela-elena-aguila.ipynb](https://github.com/Adalab/bda-modulo-3-evaluacion-final-eaguilag/blob/main/bda-modulo-3-evaluacion-final-promo-angela-elena-aguila.ipynb) y se estructura de la siguiente forma:

- Importación de librerías.

- **Fase 1: Exploración y Limpieza.**

   - **Exploración inicial:** En esta fase se leen los ficheros provistos `Customer Loyalty History.csv` y `Customer Flight Activity.csv`. Se realiza una exploración inicial de los datos mostrando su estructura, tipos de datos y estadísticas básicas. Después se realiza la unión de los dos conjuntos de datos comprobando si tienen columnas en común y si sus valores únicos coinciden.

   - **Limpieza de Datos:** En la segunda fase, tras haber identificado en la fase anterior los valores nulos o duplicados, estos se gestionan. Se realiza una imputación de valores nulos en aquellas columnas que lo requieren y finalmente se exporta el DataFrame como `customer-data.csv`.

- **Fase 2: Visualización.** Una vez realizada la limpieza se emplean herramientas de visualización para responder a las preguntas planteadas en el enunciado.

- **Fase 3: Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo.** Realización de A/B Testing.

   - **Preparación de datos:** Se filtra el conjunto solo con los datos necesarios.

   - **Análisis Descripptivo:** Se calculan estadísticas descriptivas básicas.

   - **Prueba Estadística:** Prueba de hipóstesis para determinar si *existe una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos*.


## INSTRUCTORA DEL MÓDULO

Agradecimientos por la impartición del módulo y la evaluación a cargo de la instructora Almu Hernández @almuher