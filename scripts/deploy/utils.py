import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout

modelo = None

class Model_Tl(Model):
    def __init__(self):
        super(Model_Tl, self).__init__()

        extractor = tf.keras.applications.VGG19(weights='imagenet',
                                                include_top=False,
                                                input_shape=(150, 150, 3))
        
        for layer in extractor.layers:
            layer.trainable = False

        x = extractor.output
        x = Flatten()(x)
        x = Dense(80, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001))(x)
        x = Dropout(0.5)(x)
        output = Dense(3, activation='softmax')(x)

        self.model = Model(inputs=extractor.input, outputs=output)
        
def leer_datos(archivo_subido):
    file_bytes = np.asarray(bytearray(archivo_subido.read()), dtype=np.uint8)
    img_file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img_file is None:
        raise ValueError("No se pudo decodificar la imagen")

    resized_img = cv2.resize(img_file, (150, 150))
    img_arr = np.asarray(resized_img)
    img_tensor = np.reshape(img_arr, (1, 150, 150, 3))
    
    return img_tensor

def cargar_modelo():
    global modelo
    if modelo is None:
        modelo = load_model("model_VGG19.h5")
    return modelo

def predecir(modelo, dato):
    y = modelo.predict(dato).argmax()
    return y

def obtener_categoria(prediccion):
    if prediccion == 0:
        categoria = 'Bacteria'
    elif prediccion == 1:
        categoria = 'Normal'
    elif prediccion == 2:
        categoria = 'Virus'
    else:
        print("Se ha producido un error en la predicción")
    return categoria