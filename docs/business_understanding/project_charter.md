# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Visión Profunda: Diagnóstico de Neumonía a través de Radiografías

## Objetivo del Proyecto

Nuestro proyecto innovador emplea tecnologías de vanguardia en deep learning, específicamente redes neuronales convolucionales, para transformar la forma en que se diagnostica la neumonía a partir de radiografías pulmonares. Al entrenar nuestro modelo con una extensa base de datos de imágenes médicas, hemos logrado desarrollar un sistema inteligente capaz de discernir con precisión si una persona presenta neumonía y, lo que es aún más detallado, determinar si la causa subyacente es de origen viral o bacteriano.

Esta aplicación de inteligencia artificial no solo acelera el proceso de diagnóstico, sino que también mejora la precisión y la consistencia en la identificación de patrones sutiles en las radiografías que podrían pasar desapercibidos para el ojo humano. Nuestra solución tiene el potencial de revolucionar la atención médica al proporcionar diagnósticos rápidos y certeros, permitiendo así una intervención temprana y personalizada para los pacientes afectados por la neumonía. Con un enfoque en la salud pulmonar, nuestro proyecto representa un paso significativo hacia adelante en la convergencia exitosa de la medicina y la inteligencia artificial.

## Alcance del Proyecto

### Incluye:

- Descripción de los datos disponibles: El proyecto se basará en un conjunto de datos exhaustivo que abarca una amplia variedad de radiografías pulmonares de pacientes con y sin neumonía. Este conjunto incluirá imágenes etiquetadas de manera precisa, indicando la presencia o ausencia de la enfermedad, así como la clasificación entre neumonía de origen viral y bacteriano. Los datos se obtendrán de fuentes médicas confiables y se prestará especial atención a la diversidad demográfica y a las condiciones médicas concurrentes para garantizar la robustez del modelo.

- Descripción de los resultados esperados: Esperamos desarrollar un modelo de redes neuronales convolucionales altamente preciso que pueda diagnosticar con confianza la presencia de neumonía y distinguir entre infecciones de origen viral y bacteriano. El sistema también proporcionará mapas de activación para visualizar las regiones clave en las radiografías que contribuyen a la decisión del modelo, mejorando así la interpretabilidad y la confianza en el diagnóstico automatizado. Se anticipa que el modelo resultante será capaz de generalizar eficazmente a nuevas imágenes, incluso en situaciones clínicas complejas.

- Criterios de éxito del proyecto:
1. Precisión del Modelo: Se considerará que el proyecto es exitoso si el modelo alcanza una precisión global superior al 90% en la detección de neumonía y una precisión del 85% en la clasificación entre neumonía viral y bacteriana.

2. Interpretabilidad del Modelo: Se evaluará la capacidad del modelo para generar mapas de activación precisos y significativos, lo que permitirá a los profesionales médicos comprender y confiar en las decisiones del modelo.

3. Generalización: El modelo se considerará exitoso si demuestra la capacidad de generalizar eficazmente a conjuntos de datos de prueba no vistos, asegurando su utilidad en una variedad de situaciones clínicas.

4. Eficiencia Computacional: Además de la precisión, se evaluará la eficiencia computacional del modelo para garantizar su aplicabilidad práctica en entornos clínicos del mundo real.

El logro de estos criterios de éxito respaldará la viabilidad y la eficacia del uso de inteligencia artificial en el diagnóstico de neumonía, mejorando significativamente la atención médica y permitiendo una intervención más rápida y precisa.

### Excluye:

1. Interpretación Clínica Directa:
Este proyecto no sustituirá la interpretación clínica directa por profesionales de la salud. El modelo se concibe como una herramienta de apoyo para los médicos, no como un reemplazo de su juicio clínico. La toma de decisiones médicas finales seguirá siendo responsabilidad de los profesionales médicos cualificados.

2. Diagnóstico de Otras Enfermedades Pulmonares:
El alcance se limita específicamente al diagnóstico de neumonía y a la clasificación de su origen (viral o bacteriano). No se abordarán otras enfermedades pulmonares o afecciones médicas que no estén directamente relacionadas con el objetivo principal del proyecto.

3. Evaluación de Imágenes No Radiográficas:
El modelo se entrenará y evaluará exclusivamente utilizando radiografías pulmonares. Otros tipos de imágenes médicas, como resonancias magnéticas o tomografías computarizadas, no se considerarán en este proyecto.

4. Factores Clínicos No Relacionados:
El proyecto se centrará en la interpretación de imágenes radiográficas y no abordará factores clínicos externos, como historias clínicas completas o resultados de pruebas de laboratorio. El análisis se limitará a la información disponible en las imágenes proporcionadas.

5. Desarrollo de Soluciones de Hardware:
La implementación y desarrollo de hardware específico para la ejecución del modelo no estarán dentro del alcance de este proyecto. Nos centraremos en la creación y validación del modelo de redes neuronales convolucionales.

Estas exclusiones ayudan a definir claramente los límites del proyecto y garantizan un enfoque específico en el diagnóstico de neumonía a través de radiografías pulmonares mediante el uso de redes neuronales convolucionales.

## Metodología

1. Adquisición y Preprocesamiento de Datos:
    * Recopilación de un extenso conjunto de datos de radiografías pulmonares etiquetadas, asegurando diversidad demográfica y variabilidad en las condiciones médicas.
    * Normalización y preprocesamiento de las imágenes para garantizar coherencia y calidad en los datos de entrada.

2. Diseño y Desarrollo del Modelo:
    * Implementación de una arquitectura de redes neuronales convolucionales, optimizada para la detección de patrones en imágenes médicas.
    * División del conjunto de datos en conjuntos de entrenamiento, validación y prueba.
    * Ajuste de hiperparámetros y validación cruzada para optimizar la precisión y generalización del modelo.

3. Entrenamiento del Modelo:
    * Inicialización del modelo con pesos preentrenados (transfer learning) utilizando arquitecturas reconocidas, como ResNet o DenseNet.
    * Entrenamiento del modelo en el conjunto de datos de entrenamiento, utilizando técnicas de aumento de datos para mejorar la capacidad de generalización.

4. Validación del Modelo:
    * Evaluación del rendimiento del modelo en el conjunto de datos de validación para ajustar los hiperparámetros y prevenir el sobreajuste.
    * Ajuste continuo del modelo según sea necesario para mejorar la precisión y la capacidad de generalización.

5. Pruebas y Evaluación:
    * Evaluación del modelo en el conjunto de datos de prueba independiente para medir su capacidad de generalización a nuevas imágenes.
    * Generación de métricas de rendimiento, como precisión, sensibilidad y especificidad, para evaluar la eficacia del modelo en la detección de neumonía y la clasificación de su origen.

6. Interpretabilidad y Visualización:
    * Generación de mapas de activación para resaltar las regiones clave en las radiografías que influyen en las decisiones del modelo.
    * Presentación visual de casos de estudio para proporcionar insights interpretativos a profesionales médicos.

7. Documentación y Comunicación:
    * Documentación detallada de la arquitectura del modelo, parámetros clave y resultados obtenidos.
    * Comunicación continua con profesionales de la salud para obtener retroalimentación y realizar ajustes según sea necesario.



## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 30 de Octubre al 14 de Noviembre |
| Preprocesamiento, análisis exploratorio | 1 semana | del 15 de Noviembre al 21 de Noviembre |
| Modelamiento y extracción de características | 1 semana | del 22 de Noviembre al 28 de Noviebre |
| Despliegue | 1 semana | del 29 de Noviembre al 5 de Diciembre |
| Evaluación y entrega final | 1 semana | del 6 de Diciembre al 8 de Diciembre |


## Equipo del Proyecto

- Sebastián Rendón Patiño
- Andrés Felipe Aristizábal Miranda

## Presupuesto

No asignado

En el contexto del presente proyecto, es importante destacar que no se ha asignado un presupuesto específico. La ejecución del proyecto se llevará a cabo con recursos internos disponibles, centrándose en la utilización de herramientas y tecnologías de código abierto para maximizar la eficiencia y minimizar los costos. El enfoque principal estará en la utilización de conjuntos de datos públicos y la implementación de modelos de aprendizaje profundo con recursos computacionales existentes.

Dicha estrategia se alinea con la optimización de recursos y la maximización del impacto, permitiendo que el proyecto se desarrolle de manera eficaz sin la necesidad de asignar recursos financieros específicos. La falta de un presupuesto asignado no comprometerá la calidad ni la efectividad del proyecto, ya que se aprovecharán eficazmente los recursos internos y las herramientas de código abierto disponibles.

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
