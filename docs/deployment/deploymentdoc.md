# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** clasification_report_rx
- **Plataforma de despliegue:** La plataforma elegida para el despliegue del modelo es [Streamlit](https://streamlit.io/)

    Se eligió Streamlit para el despliegue del modelo de deep learning por diversas razones fundamentales:

    - **Facilidad de Uso:**
La elección de Streamlit se basa en su enfoque sencillo y directo. La capacidad de crear una interfaz de usuario interactiva sin la necesidad de adquirir conocimientos avanzados en tecnologías web más complejas permite un desarrollo rápido y eficiente.

    - **Rápido Prototipado:**
Streamlit facilita el prototipado rápido, permitiendo ajustes en tiempo real de la interfaz de usuario. Esta característica es esencial durante el desarrollo y la experimentación con modelos de deep learning.

    - **Integración con Modelos de TensorFlow:**
Streamlit ofrece una integración fluida con modelos de deep learning, incluyendo los desarrollados con TensorFlow y PyTorch. La capacidad de cargar y utilizar modelos entrenados de manera eficiente simplifica la implementación y permite centrarse en la presentación y comprensión de los resultados.

    - **Comunidad Activa y Documentación Clara:**
La elección se respalda por la activa comunidad de Streamlit y su exhaustiva documentación. Esta combinación proporciona recursos sólidos para resolver problemas y ampliar las capacidades de la aplicación.

    - **Escalabilidad:**
Streamlit es lo suficientemente escalable para proyectos más grandes. La posibilidad de incorporar nuevas funcionalidades a medida que la aplicación evoluciona garantiza una adaptabilidad continua.

    - **Interactividad sin Complicaciones:**
La presencia de widgets interactivos integrados en Streamlit, como botones y controles deslizantes, simplifica la creación de experiencias interactivas sin la necesidad de escribir una cantidad considerable de código adicional.

    En resumen, la elección de Streamlit se basa en su simplicidad, rapidez de desarrollo y capacidad de integración sin problemas con modelos de deep learning. Esta elección permite que el enfoque se centre en la interpretación y presentación efectiva de los resultados del modelo, sin la complejidad asociada con la infraestructura web.
- **Requisitos técnicos:** 
    ```streamlit
    numpy==1.23.0
    opencv-python-headless
    h5py
    keras
    protobuf~=3.19.0
    tensorflow==2.11.1
    tensorboard==2.11.1
    ```
- **Requisitos de seguridad:**

Para el ejempo no se realizó ningún metodo de encriptación que permita la transferencia segura de datos en todo el proceso de despliegue. 
- **Diagrama de arquitectura:** 
    
    ![Alt text](/src/nombre_paquete/images/diagrama.PNG)

## Código de despliegue

- **Archivo principal:** 

    - [Archivo Principal](../../scripts/deploy/app.py)

- **Rutas de acceso a los archivos:**

    - [app.py](../../scripts/deploy/app.py)
    - [utils.py](../../scripts/deploy/utils.py)
    - [requirements.txt](../../scripts/deploy/requirements.txt)
    - [README.md](../../scripts/deploy/README.md)
    - [model_VGG19.h5](../../scripts/deploy/model_VGG19.h5)
    
- **Variables de entorno:** 

No aplican para el proyecto.

## Documentación del despliegue

- **Instrucciones de instalación:** 

    Como primera medida se generó un archivo llamado model_VGG19.h5 que contiene el modelo entrenado en entregas pasadas, ya que este fue el que mejores resultados mostró luego del entrenamiento, en el repositorio se creó una rama llamada deploy la cual contiene los archivos del proyecto como tal, adiciona se crearon dos archivos app.py y utils.py los cuales contienen la integración con la plataforma streamlit y la lógica de programación que evalúe las imágenes cargadas para determinar si el paciente tiene Neumonía o no y de que tipo, bacteria o virus, adicional se creó el archivo requirements.txt que contiene las librerías que se usaran para el correcto despliegue de la aplicación.
    El archivo app.py, se construyo usando la librería streamlit que proporciona las funciones necesarias para crear un frontend que permita la interacción del usuario más fácilmente con la plataforma.
- **Instrucciones de configuración:**

    - Lo primero es crear una cuenta en [Streamlit](https://streamlit.io/) y conectarla con la cuenta de github
        
        ![Alt text](/src/nombre_paquete/images/conect_github.PNG)

    - Seguido, estando en el dashboard de streamlit, se debe crear una nueva app.

        ![Alt text](/src/nombre_paquete/images/new_app.PNG)

    - Luego, se diligencia el formulario donde se selecciona el repositorio del proyecto **MLDS_U6_PROYECTO_FINAL_ARISTIZABAL_RENDON**, seguido se selecciona la rama, que para el caso se realizo en una rama alternativa llamada **deploy**, en el siguiente campo, se debe apuntar al archivo **app.py** que es el que hace la funcion de ejecucion del proyecto.

        ![Alt text](/src/nombre_paquete/images/deploy.PNG)

    - Por último dar clic en deploy y la plataforma realizará internamente el despliegue de la aplicación, y redirecciona directamente 
    a la aplicación.
        
        ![Alt text](/src/nombre_paquete/images/application.PNG)



- **Instrucciones de uso:**

    - Realizados los pasos anteriores, se ingresa en la url que genero estreamlit y alli se puede encontrar un campo que permite cargar una imagen, en ese campo se ingresa la imagen de rayos x que se desea evaluar.
        
        ![Alt text](/src/nombre_paquete/images/upload.PNG)
    
    - Para el ejemplo, la imagen seleccionada es a siguiente:
        
        ![Alt text](/src/nombre_paquete/images/person55_virus_110.jpeg)
    
    - Por último en la misma aplicación se dara la respuesta diagnostica al la imagen.

        ![Alt text](/src/nombre_paquete/images/results.PNG)

