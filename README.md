# 207 Final Project: Weather Image Classification

This repo hosts the code for our group's DATASCI 207 Final Project.

## Members
- Daniel Costa
- Bella Davies
- Theo Hui
- Aaron Bergfeld

## Description

This project uses machine learning to recognize weather from images. This can be useful for altering the driving behavior of autonomous vehicles for safer driving in dangerous weather.

Dataset: https://www.kaggle.com/datasets/jehanbhathena/weather-dataset

## Files

1. /Data/Weather_Dataset/ - Downloaded waather image data sorted into directories labled with class names
2. /sandbox/data_exporation.ipynb - Script to download images and upload 
3. /sandbox/load_data.ipynb - Initial dataset loader function
4. /sandbox/Preprocessing_EDA.ipynb - Initial exporatative data analysis and preprocessing
5. /sandbox/baseline_logistic_regression.ipynb - Baseline logistic regression model with original dataset and oversampled dataset
6. /sandbox/kmeans_pca_cnn_stacked.ipynb - K-Means into CNN, PCA into CNN, Stacking Predictions for Ensemble Models
7. /sandbox/cnn_architecture.ipynb - Oversampling script, data augmentation, initial CNN model, and tuned CNN model with keras hyperband tuner
8. /sandbox/Resnet50.ipynb - Resnet50 transfer learning with logistic regression and CNN
9. /sandbox/weather_features.npz - Resnet50 transformed features from image data
10. /SAM/ - Steps for SAM (Segment Anything Model): EDA, processor, model, train
11. /207 Final Project Presentation.pdf
12. /207 Final Presentation with Presenter Notes.pdf

/Initial/ - Initial code and exporation steps
