# Final Model Report

## Executive Summary

During the experimentation phase, two neural network models were trained to address the task of classifying X-ray images related to bacteria, normal cases, and viruses. One of these models was based on a standard convolutional architecture, while the second utilized transfer learning techniques.

## Problem Description

**Description of the Problem:**

The final model's problem focuses on classifying X-ray images into three main categories: bacteria, normal cases, and viruses. This task is essential for early and accurate infectious disease diagnosis, enabling healthcare professionals to make informed and rapid treatment decisions.

**Problem Context:**

In the medical field, identifying visual patterns in images is crucial for diagnosis and clinical decision-making. In this case, the classification of specific X-ray images is performed to distinguish between different types of infections, which can significantly impact healthcare and efficient resource management.

**Model Objectives:**

The fundamental objectives of the final model are as follows:

- **Diagnostic Accuracy:** Provide a support tool for the accurate classification of X-ray images, helping to identify patterns that may be difficult to detect visually.
- **Diagnostic Efficiency:** Streamline the X-ray image classification process, allowing healthcare professionals to focus their attention on more complex cases and critical clinical decisions.
- **Generalization:** Develop a model that can generalize correctly to new images, enhancing its usefulness in different clinical scenarios and data types.

**Model Justification:**

The implementation of a deep learning model is justified by its ability to learn complex patterns and meaningful data representations. The use of convolutional neural networks and transfer learning is based on the demonstrated efficacy of these architectures in computer vision and image classification tasks.

## Model Description
### Model 1 (Standard)
Description of the Model:

The final model designed for the X-ray image classification task is based on a convolutional neural network (CNN) architecture and has been named "gonodactylus_simithii".

**Methodology and Techniques Used:**

- **Input Layer:** An input layer with dimensions (150, 150, 3) corresponds to the input image size.
- **Convolutional Layers (CONV):** Three blocks of convolutional layers, each consisting of two CONV layers followed by a MaxPooling layer. These layers extract key features from the images using convolutional filters and reduce dimensionality through max pooling.
- **Flatten Layer:** A flatten layer that converts the output of the convolutional layers into a one-dimensional vector. This step is crucial for connecting the convolutional layers with the neural network's fully connected layers.
- **Fully Connected Neural Network:** Two fully connected (Dense) layers with ReLU activation functions, followed by dropout layers to mitigate the risk of overfitting. L2 regularization is also applied to avoid overfitting by introducing a penalty on the network weights.
- **Output Layer:** An output layer with a softmax activation function, classifying images into one of the three defined categories: bacteria, normal cases, and viruses.
- **Model Compilation:** The model is compiled using the Adam optimizer, categorical cross-entropy loss function, and accuracy is monitored during training.
- **Model Summary:** The model's structure is summarized using Keras's summary() function, providing details on architecture, the number of parameters, and connections between layers.

**Summary:**

The "gonodactylus_simithii" model is designed to learn representative patterns in X-ray images, especially focusing on classifying cases related to bacteria, normal, and viruses. The combination of convolutional layers for feature extraction and fully connected layers for learning more abstract representations allows for accurate and efficient classification of X-ray images. The implementation of techniques like dropout and L2 regularization contributes to the model's generalization and mitigates overfitting. This comprehensive approach aims to provide an effective tool for automatic diagnosis in the specified medical context.

### Model 2 (Transfer Learning)
Description of the Model (Transfer Learning):

The second model developed to solve the X-ray image classification problem is based on the transfer learning technique using the pre-trained VGG16 architecture.

**Methodology and Techniques Used:**

- **Feature Extraction (Transfer Learning):** The pre-trained VGG16 architecture with weights from ImageNet is used as a feature extractor. The pre-trained layers are frozen to take advantage of the knowledge acquired in previous tasks.
- **Flatten Layer and Fully Connected Layers:** A flatten layer is added to convert the output of the pre-trained layers into a one-dimensional vector. Then, two fully connected (Dense) layers with ReLU activation functions and dropout layers are added to prevent overfitting.
- **Output Layer:** The output layer has a softmax activation function, classifying images into one of the three defined categories: bacteria, normal cases, and viruses.
- **Model Compilation:** The model is compiled using the Adam optimizer, categorical cross-entropy loss function, and accuracy is monitored during training.
- **Training:** The model is trained using the training and validation datasets. A set of callbacks is used, including one to save the best model based on the validation metric and another to stop training prematurely if there are no significant improvements.

**Summary:**

The transfer learning model, named "transferLearning_model," is based on the pre-trained VGG16 architecture, adapted for specific X-ray image classification. The transfer learning strategy allows benefiting from VGG16's feature-learning capabilities without needing to train from scratch. The inclusion of fully connected layers and regularization techniques aims to improve generalization and adapt better to the specific task. This model is presented as an effective alternative for accurate X-ray image classification in the defined context.

## Model Evaluation
### Evaluation of Model 1 (Standard):
The standard model (Model 1) was evaluated using various metrics that provide a detailed understanding of its performance in classifying X-ray images.

| Metrics                | Value                                            |
|------------------------|--------------------------------------------------|
| Accuracy (Precision)   | 76%                                              |
| Recall (Exhaustiveness) | Bacteria: 69%, Normal: 91%, Virus: 69%           |
| Precision (Precision)   | Bacteria: 76%, Normal: 86%, Virus: 67%           |
| F1-Score (F1-Score)| Bacteria: 72%, Normal: 88%, Virus: 68% 

**Interpretation of Results:**

- **Model Accuracy:** The model has an accuracy of 76%, indicating that 76% of the predictions are correct in the test set.
- **Recall:** The recall highlights the model's ability to correctly identify each class. Balanced performance is observed in the Bacteria (69%), Normal (91%), and Virus (69%) classes.
- **Precision:** Precision highlights the proportion of positive predictions that were correct. Consistent performance is observed in precision for the Bacteria (76%), Normal (86%), and Virus (67%) classes.
- **F1-Score:** The F1-score, which combines precision and recall, provides a balanced measure of the model's performance in each class. A good balance is observed in the Bacteria (72%), Normal (88%), and Virus (68%) classes.

**Confusion Matrix**

![Confusion Matrix](/src/nombre_paquete/images/image.png)

-----

**F1 Score**

![F1 Score](/src/nombre_paquete/images/image-3.png)
-----
### Evaluation of Model 2 (Transfer Learning):
The transfer learning model (Model 2) was evaluated using various metrics that provide a detailed understanding of its performance in classifying X-ray images.

**Evaluation Metrics:**


|Metrics	|Value|
|-----------|---------|
|Accuracy (Precision)|	80%|
|Recall (Exhaustiveness)|	Bacteria: 86%, Normal: 96%, Virus: 57%
|Precision (Precision)|	Bacteria: 68%, Normal: 97%, Virus: 77%
|F1-Score (F1-Score)|	Bacteria: 76%, Normal: 96%, Virus: 66%

**Interpretation of Results:**

- The accuracy of the model is 80%, indicating that 80% of the predictions are correct in the test set.
- The recall highlights the model's ability to correctly identify each class. The model is strong in identifying normal cases (96%) but faces challenges in classifying virus images (57%).
- The precision highlights the proportion of positive predictions that were correct. High precision is noted for normal cases (97%), but precision is relatively lower for bacteria (68%) and viruses (77%).
- The F1-score, which combines precision and recall, provides a balanced measure of the model's performance in each class.

**Confusion Matrix:**

![Confusion Matrix](/src/nombre_paquete/images/image-1.png)

---------

**F1 Score**

![F1 Score](/src/nombre_paquete/images/image-2.png)


## Conclusions and Recommendations

Based on the results obtained from the X-ray image classification models, the following conclusions and recommendations can be drawn:

### **Convolutional Model (Model 1):**

**Strengths:**

- The model shows a solid overall performance with a 76% accuracy under the standard metrics.
- Good ability to identify normal cases with a 91% recall.

**Weaknesses:**

- Challenges in classifying virus images, evidenced by a 69% recall and a 68% F1-score.
- The precision in classifying bacteria could be improved (76% precision).

**Recommendations:**

- Explore performance improvement techniques specific to virus image classification.
- Adjust hyperparameters to improve precision in classifying bacteria.

### **Transfer Learning Model (Model 2):**

**Strengths:**

Effective utilization of pre-trained knowledge from VGG16, demonstrating solid overall performance with an accuracy to be determined.

**Weaknesses:**

Assess the possibility of overfitting as the model uses pre-trained layers that may not be optimal for the specific dataset.

**Recommendations:**

Conduct a more detailed evaluation of the model, considering metrics such as precision, recall, and F1-score.
Evaluate the possibility of adjusting pre-trained layers or adding additional layers to better adapt to the dataset.

**Limitations and Application Scenarios:**

The main limitation might be the availability and quality of the dataset. If the dataset is not representative or contains biases, the models may not generalize properly.
The current models are designed to classify among three specific categories (bacteria, normal, virus) and may not adapt well to new categories not contemplated in the training.

**Application Scenarios:**

The model can be useful as a support tool for healthcare professionals, accelerating the identification of patterns in X-ray images and aiding in early diagnosis.
Implementation in clinical environments where automation can improve the efficiency of medical staff.

In summary, although the models demonstrate promising capabilities, continuous evaluation and adjustments are suggested to improve performance in specific scenarios. Additionally, practical application should consider limitations and clinical context to ensure reliable and safe results.

## References
* [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class)
* [VGG16 and VGG19](https://keras.io/api/applications/vgg/)
* [Transfer Learning and Fine-Tuning](https://www.tensorflow.org/tutorials/images/transfer_learning?hl=en)
* [ChatGPT](https://chat.openai.com/)
* [Image Classification with Convolutional Neural Networks](https://medium.com/@a01706707/image-classification-with-deep-neural-networks-a6a980b9cea5)
