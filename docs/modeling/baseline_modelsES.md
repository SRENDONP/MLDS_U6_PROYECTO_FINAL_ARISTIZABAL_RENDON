# Reporte del Modelo Baseline para Clasificación de Imágenes de Rayos X

Este documento detalla el análisis y las conclusiones del modelo baseline utilizado para la clasificación de imágenes de rayos X en tres categorías: Bacteria, Normal y Virus.

## Descripción del modelo

El modelo baseline implementado es una red neuronal convolucional (CNN) simplificada inspirada en la arquitectura VGG16. Este modelo sirve como un punto de referencia inicial para evaluar el rendimiento y la eficacia en la clasificación de imágenes médicas.

## Variables de entrada

- Imágenes de rayos X (RGB).
- Tamaño de las imágenes: 150x150 píxeles.

## Variable objetivo

- Clasificación categórica en tres grupos: Bacteria, Normal, Virus.

## Evaluación del modelo

### Métricas de evaluación

- Precisión (Accuracy).
- Recall.
- F1-Score.
- Matriz de confusión.

### Resultados de evaluación

| Clase    | Precisión | Recall | F1-Score |
|----------|-----------|--------|----------|
| Bacteria | 0.76      | 0.69   | 0.72     |
| Normal   | 0.86      | 0.91   | 0.88     |
| Virus    | 0.67      | 0.69   | 0.68     |
| **Total**| **0.76**  | **0.76**| **0.76** |

- **Loss**: 0.8611
- **Accuracy**: 76.33%

## Análisis de los resultados

El modelo muestra una precisión global satisfactoria del 76.33%. Sin embargo, al analizar detalladamente:

- **Fortalezas**: El modelo es especialmente eficaz en la categoría 'Normal', con altas puntuaciones en todas las métricas. Esto indica una buena capacidad para identificar casos normales, lo cual es crucial en la práctica clínica para evitar falsos positivos.

- **Debilidades**: La categoría 'Virus' presenta los menores valores en precisión y F1-Score. Esto sugiere dificultades en la diferenciación entre imágenes normales y patológicas con características virales, lo que podría llevar a un número significativo de falsos negativos o falsos positivos en esta categoría.

## Conclusiones y Recomendaciones

1. **Potencial de Mejora**: A pesar de su eficacia general, el modelo puede beneficiarse de una arquitectura más compleja o técnicas avanzadas de procesamiento de imágenes para mejorar la precisión, especialmente en la categoría 'Virus'.

2. **Exploración de Arquitecturas**: Experimentar con variantes de arquitecturas CNN más profundas, como VGG19 o ResNet, podría ofrecer mejoras significativas.

3. **Integración de Conocimientos Médicos**: Incorporar aportes de expertos médicos en la fase de preprocesamiento y ajuste de hiperparámetros puede ser clave para afinar la capacidad del modelo para distinguir entre patologías sutiles.

4. **Evaluación Continua**: Dada la importancia de la precisión en aplicaciones médicas, es crucial realizar evaluaciones continuas y ajustes del modelo con nuevos datos y técnicas emergentes.

## Referencias

- Arquitectura VGG16 para inspiración en el diseño del modelo.
- TensorFlow y Keras para la implementación de la red neuronal.
- OpenCV y Scikit-Learn para procesamiento y evaluación de imágenes.
