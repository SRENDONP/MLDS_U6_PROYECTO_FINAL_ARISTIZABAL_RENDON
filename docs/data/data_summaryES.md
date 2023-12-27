# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Se provee una visión general del conjunto de datos extraídos de [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class), incluyendo la estructura del mismo y los pasos preliminares para su preparación y análisis. El dataset consta de imágenes divididas en tres categorías principales:

- **Entrenamiento (Train)**
- **Pruebas (Test)**
- **Validación (Val)**

Cada categoría contiene subdirectorios para tres tipos de imágenes:

- **Normal**: Imágenes de rayos-X sin indicios de neumonía.
- **Virus**: Imágenes que muestran neumonía causada por virus.
- **Bacteria**: Imágenes con neumonía causada por bacterias.

El balance de clases es esencial para evitar sesgos en el entrenamiento y se ha verificado que el dataset está balanceado y listo para el proceso de etiquetado.

## Resumen de calidad de los datos

Dado que estamos tratando con datos No Estructurados en formato de imagen (.jpeg), se detalla la metodología para convertir estas imágenes en series de matrices de Numpy, lo que facilitará el entrenamiento eficiente de los modelos de aprendizaje automático.

Se confirma que el conjunto de datos está completo sin imágenes faltantes o corruptas, asegurando así la integridad de la información para un análisis fiable.

## Variable objetivo

El conjunto de datos tiene una variable objetivo a estimar que es la etiqueta de clasificación de las imágenes de radiografías de La variable a predecir es la clasificación de las imágenes, que es una variable categórica con las siguientes categorías:

- **Normal**
- **Virus**
- **Bacteria**

Se ha confirmado que no existe desequilibrio en la cantidad de imágenes por categoría, lo que es crucial para el rendimiento del modelo predictivo.
