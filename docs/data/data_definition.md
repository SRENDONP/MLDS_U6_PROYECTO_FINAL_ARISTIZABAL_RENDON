# Definición de los datos

## Origen de los datos

- [x] **Fuente de Datos:** Los datos provienen de Un conjunto de imágenes de rayos-X torácicos disponible en Kaggle. [Ver conjunto de datos](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class).

## Especificación de los scripts para la carga de datos

- [x] **Scripts de Carga:**
  - **Script de Google Drive:** [cargar_datos.ipynb](/scripts/data_acquisition/cargar_datos.ipynb) Este método se emplea para cargar imágenes desde Google Drive con el propósito de utilizarlas como matrices de numpy. Esta elección se basa en consideraciones de accesibilidad, ya que se ha decidido almacenar las imágenes de Kaggle en Google Drive.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos
- [x] **Ubicación de Archivos de Origen:** Los archivos de origen se encuentran en el directorio `/Data_blance/` en [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class).
- [x] **Estructura de Archivos de Origen:** Cada archivo de imagen está dentro de una carpeta correspondiente a su conjunto de datos (`Train`, `Test`, `Val`) donde se encuentran ordenadas por clasificación (`Normal`, `Virus`, `Bacteria`).
- [x] **Ubicación de Archivos de Destino:** Los archivos de origen se encuentran en un .zip llamado `x-rays.zip` que contiene todos los archivos del directorio `/Data_blance/` en [Google Drive](https://drive.google.com/file/d/1It4NYRJNEem3YLHJqYZyclUbR85eqZH8/view?usp=sharing).
- [x] **Estructura de Archivos de Origen:** Cada archivo de imagen está dentro de una carpeta correspondiente a su conjunto de datos (`Train`, `Test`, `Val`) donde se encuentran ordenadas por clasificación (`Normal`, `Virus`, `Bacteria`).
- [x] **Procedimientos de Transformación y Limpieza:**
  - No se eliminan imágenes duplicadas debido a que no se encuentran registros duplicados y se verifican los datos para asegurar que no hay imágenes corruptas.

### Base de Datos de Destino

- [x] **Base de Datos de Destino:** Los datos procesados se almacenan en Google Drive en la carpeta `/Data_blance/`.
- [x] **Estructura de la Base de Datos de Destino:** Cada imagen en Google Drive tiene un identificador único. Dentro de la aplicación se puede consultar el tamaño y la fecha de subida.
