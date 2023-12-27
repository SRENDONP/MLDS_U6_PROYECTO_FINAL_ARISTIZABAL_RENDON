# Data Definition

## Data Origin

- [x] **Data Source:** The data originates from a dataset of chest X-ray images available on Kaggle. [View Dataset](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class).

## Data Loading Scripts Specification

- [x] **Loading Scripts:**
  - **Google Drive Script:** [cargar_datos.ipynb](/scripts/data_acquisition/cargar_datos.ipynb) This method is used for loading images from Google Drive to be used as numpy arrays. This choice is based on accessibility considerations, as it was decided to store Kaggle images on Google Drive.

## References to Source and Destination Data Paths or Databases

### Source Data Paths
- [x] **Source File Location:** The source files are located in the `/Data_blance/` directory on [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class).
- [x] **Source File Structure:** Each image file is inside a folder corresponding to its dataset (`Train`, `Test`, `Val`) and is categorized (`Normal`, `Virus`, `Bacteria`).
- [x] **Destination File Location:** The source files are in a .zip called `x-rays.zip` which contains all files from the `/Data_blance/` directory on [Google Drive](https://drive.google.com/file/d/1It4NYRJNEem3YLHJqYZyclUbR85eqZH8/view?usp=sharing).
- [x] **Source File Structure:** Each image file is inside a folder corresponding to its dataset (`Train`, `Test`, `Val`) and is categorized (`Normal`, `Virus`, `Bacteria`).
- [x] **Transformation and Cleaning Procedures:**
  - Duplicate images are not removed as no duplicate records are found, and data is checked to ensure there are no corrupt images.

### Destination Database

- [x] **Destination Database:** The processed data is stored on Google Drive in the `/Data_blance/` folder.
- [x] **Structure of the Destination Database:** Each image in Google Drive has a unique identifier. The size and upload date can be queried within the application.
