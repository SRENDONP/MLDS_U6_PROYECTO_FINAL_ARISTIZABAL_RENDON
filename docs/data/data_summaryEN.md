# Data Report

This document contains the results of the exploratory data analysis.

## General Data Summary

This section provides an overview of the dataset extracted from [Kaggle](https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-class), including its structure and preliminary steps for its preparation and analysis. The dataset consists of images divided into three main categories:

- **Training (Train)**
- **Testing (Test)**
- **Validation (Val)**

Each category contains subdirectories for three types of images:

- **Normal**: X-ray images with no signs of pneumonia.
- **Virus**: Images showing pneumonia caused by a virus.
- **Bacteria**: Images with pneumonia caused by bacteria.

Class balance is crucial to avoid bias in training and it has been verified that the dataset is balanced and ready for the labeling process.

## Data Quality Summary

Given that we are dealing with Unstructured data in image format (.jpeg), the methodology for converting these images into series of Numpy matrices is detailed, which will facilitate efficient training of machine learning models.

It is confirmed that the dataset is complete with no missing or corrupt images, thus ensuring the integrity of the information for reliable analysis.

## Target Variable

The dataset has a target variable to be estimated, which is the classification label of the X-ray images. The variable to be predicted is the classification of the images, which is a categorical variable with the following categories:

- **Normal**
- **Virus**
- **Bacteria**

It has been confirmed that there is no imbalance in the number of images per category, which is crucial for the predictive model's performance.
