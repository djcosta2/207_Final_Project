# 207 Final Project: Weather Image Classification

This repo hosts the code for our group's DATASCI 207 Final Project.

## Members
- Daniel Costa
- Bella Davies
- Theo Hui
- Aaron Bergfeld

## Description

This project uses machine learning to classify weather from images. Models aim to improve from a baseline logistic regression model with an initial validation accuracy of 51%. Preprocessing techniques include oversampling, data augmentation, K-Means for color quantization, PCA for dimensionality reduction, segmenting and de-noising images with SAM (Segment Anything Model), and fine-tuning on top of ResNet50. 

Preprocessed data are fed into models such as logistic regression or CNN (Convolutional Neural Network). Predictions outputted by CNNs using K-Means and PCA datasets are stacked into ensemble models of logistic regression, then a CNN. Model hyperparameters are tuned using keras hyperband tuner. The best performing model used the ResNet50 features into a simple logistic regression, and produces a test accuracy of 90%, a significant improvement from the baseline. This model can be used for altering the driving behavior of autonomous vehicles for safer driving in dangerous weather.

[Link to Dataset](https://www.kaggle.com/datasets/jehanbhathena/weather-dataset)

## Files (train/eval notebooks **bolded**)

1. /Initial_EDA/weather_dataset_loader.ipynb - Initial dataset loader function
2. /Initial_EDA/Preprocessing_EDA.ipynb - Initial exporatative data analysis and preprocessing
3. **/Baselines/baseline_logistic_regression.ipynb** - Baseline logistic regression model with original dataset and oversampled dataset
4. **/Preprocessing/kmeans_pca_cnn_stacking.ipynb** - K-Means into CNN, PCA into CNN, Stacking Predictions for Ensemble Models
5. **/CNN/CNN_train.ipynb** - Oversampling script, data augmentation, initial CNN model, and tuned CNN model with keras hyperband tuner
6. **/Baselines/Resnet50.ipynb** - Resnet50 transfer learning with logistic regression and CNN
7. /sandbox/weather_features.npz - Resnet50 transformed features from image data
8. **/SAM/** - SAM (Segment Anything Model) image segmentation on top of Resnet50 baseline: EDA, processor, model, **train.ipynb**
9. /207 Final Presentation with Presenter Notes.pdf


/Data/Weather_Dataset/ - Downloaded weather image data sorted into directories labled with class names
