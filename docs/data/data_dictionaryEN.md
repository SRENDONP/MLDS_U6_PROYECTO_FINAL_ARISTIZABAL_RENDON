# Data Dictionary

## Database 1 (Kaggle)

The Kaggle database consists of chest X-ray images classified for pneumonia detection. Images are organized into three subsets representing the training, testing, and validation phases of the model. Each image is labeled according to its diagnosis: normal, presence of virus, or presence of bacteria.

| Variable | Description | Data Type| Range/Possible Values | Data Source |
|----------------|-----------------------------------------------------------------|--------------|-----------------------|---------------------------------------------------------------------------------------------------|
| imagen_Normal  | X-ray image of a person without pneumonia                       | Image (.jpeg) | Between 0 and 255     | [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class) |
| imagen_Bacteria | X-ray image of a person suffering from bacterial pneumonia     | Image (.jpeg) | Between 0 and 255     | [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class) |
| imagen_Virus   | X-ray image of a person suffering from viral pneumonia          | Image (.jpeg) | Between 0 and 255     | [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class) |

- **Variable**: Name of the variable.
- **Description**: Brief description of the variable.
- **Data Type**: Type of data contained in the variable.
- **Range/Possible Values**: Range or values that the variable can take.
- **Data Source**: Source of the variable's data.

## Database 2 (Google Drive)

The Google Drive database stores the processed X-ray images for use in the machine learning model. Metadata of the images, such as the file path, size, and the user who uploaded them, are recorded here to facilitate management and access.

| Variable | Description | Data Type | Range/Possible Values | Data Source |
|----------------|-----------------------------------------------------------------|--------------|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| imagen_Normal  | X-ray image of a person without pneumonia                       | Image (.jpeg) | Between 0 and 255     | [Google Drive](https://drive.google.com/file/d/1It4NYRJNEem3YLHJqYZyclUbR85eqZH8/view?usp=sharing)            |
| imagen_Bacteria | X-ray image of a person suffering from bacterial pneumonia     | Image (.jpeg) | Between 0 and 255     | [Google Drive](https://drive.google.com/file/d/1It4NYRJNEem3YLHJqYZyclUbR85eqZH8/view?usp=sharing)            |
| imagen_Virus   | X-ray image of a person suffering from viral pneumonia         | Image (.jpeg) | Between 0 and 255     | [Google Drive](https://drive.google.com/file/d/1It4NYRJNEem3YLHJqYZyclUbR85eqZH8/view?usp=sharing)            |

- **Variable**: Name of the variable.
- **Description**: Brief description of the variable.
- **Data Type**: Type of data contained in the variable.
- **Range/Possible Values**: Range or values that the variable can take.
- **Data Source**: Source of the variable's data.
