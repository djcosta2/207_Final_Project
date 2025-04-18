# 207 Final Project: Weather Image Classification

This repo hosts the code for our group's DATASCI 207 Final Project.

## Members
- Daniel Costa
- Bella Davies
- Theo Hui
- Aaron Bergfeld

## Description

This project uses machine learning to classify weather from images. Models aim to improve from a baseline logistic regression model with an initial validation accuracy of 51%. Preprocessing techniques include oversampling, data augmentation, K-Means for color quantization, PCA for dimensionality reduction, segmenting images with SAM (Segment Anything Model), and extracting features with ResNet-50. Preprocessed data are fed into models such as logistic regression or CNN (Convolutional Neural Network). Predictions outputted by CNNs using K-Means and PCA datasets are stacked into ensemble models of logistic regression, then a CNN. Model hyperparameters are tuned using keras hyperband tuner. The best performing model used the ResNet50 features into a simple logistic regression, and produces a test accuracy of 90%, a significant improvement from the baseline. This model can be used for altering the driving behavior of autonomous vehicles for safer driving in dangerous weather.

Dataset: https://www.kaggle.com/datasets/jehanbhathena/weather-dataset

## Files

1. /sandbox/load_data.ipynb - Initial dataset loader function
2. /sandbox/Preprocessing_EDA.ipynb - Initial exporatative data analysis and preprocessing
3. /sandbox/baseline_logistic_regression.ipynb - Baseline logistic regression model with original dataset and oversampled dataset
4. /sandbox/kmeans_pca_cnn_stacked.ipynb - K-Means into CNN, PCA into CNN, Stacking Predictions for Ensemble Models
5. /sandbox/cnn_architecture.ipynb - Oversampling script, data augmentation, initial CNN model, and tuned CNN model with keras hyperband tuner
6. /sandbox/Resnet50.ipynb - Resnet50 transfer learning with logistic regression and CNN
7. /sandbox/weather_features.npz - Resnet50 transformed features from image data
8. /SAM/ - Steps for SAM (Segment Anything Model): EDA, processor, model, train
9. /207 Final Project Presentation.pdf
10. /207 Final Presentation with Presenter Notes.pdf


/Data/Weather_Dataset/ - Downloaded waather image data sorted into directories labled with class names

/sandbox/data_exporation.ipynb - Script to download images and upload 

/Initial/ - Initial code and exporation steps
