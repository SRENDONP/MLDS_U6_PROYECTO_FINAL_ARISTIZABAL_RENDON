import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout

model = None

class TransferLearningModel(Model):
    def __init__(self):
        super(TransferLearningModel, self).__init__()

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
        
def read_data(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img_file is None:
        raise ValueError("Unable to decode the image")

    resized_img = cv2.resize(img_file, (150, 150))
    img_arr = np.asarray(resized_img)
    img_tensor = np.reshape(img_arr, (1, 150, 150, 3))
    
    return img_tensor

def load_model():
    global model
    if model is None:
        model = load_model("model_VGG19.h5")
    return model

def predict(model, data):
    y = model.predict(data).argmax()
    return y

def get_category(prediction):
    if prediction == 0:
        category = 'Bacteria'
    elif prediction == 1:
        category = 'Normal'
    elif prediction == 2:
        category = 'Virus'
    else:
        print("An error occurred in prediction")
    return category
