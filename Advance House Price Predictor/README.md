# Kaggle House Prices Prediction Using Ensemble Technique With XGB and LGBM

Repository for source code of kaggle competition: [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
![](https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png)


## Table of Contents

1. [Problem Statement](#Problem-Statement)

2. [Overview](#Overview)

3. [Data](#Data)

4. [Repository structure](#Repository-structure)


## Problem-Statement

There are several factors that influence the price a buyer is willing to pay for a house. Some are apparent and obvious and some are not. Nevertheless, a rational approach facilitated by machine learning can be very useful in predicting the house price. A large data set with 79 different features (like living area, number of rooms, location etc) along with their prices are provided for residential homes in Ames, Iowa. The challenge is to learn a relationship between the important features and the price and use it to predict the prices of a new set of houses.


## Overview
Applied **EDA**, **Data Preprocessing** , **Feature Engineering** and finally a **50/50 blend of XGB and LGBM** regression model to achieve suitable predictions. For more information do visit the `Advance_House_Price_Prediction_XGB+LGBM.ipynb` file.

You can make a clone of the repository from GitHub on your local machine using the following command (prerequisite: you need git installed on your system):

$ git clone https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Advance-House-Price-Predictor

## Data

`Data` folder contains original data
Inside `Data` folder you will find a ``data_description.txt``  file where the description of each of the features in the dataset is available.
Click [here](https://drive.google.com/file/d/13TDiD7QAc_aaDHUKF7-G_l1DYdjkaZtm/view?usp=sharing) and download this ``.html`` file to view the EDA I have done in this dataset.

## But Why Ensemble ?

A common practice nowadays is to check the reviews of items before buying them. And when checking reviews, you often look for the items with a large number of reviews so you could know for sure about its rating. After going through the reviews from multiple people you decide whether to buy the item or not.

Ensemble models in machine learning operate on a similar idea. They combine the decisions from multiple models to improve the overall performance. This approach allows for better predictive performance compared to a single model. This is the reason why ensemble methods were placed first in many prestigious machine learning competitions, such as the Netflix Competition, KDD 2009, and Kaggle.Ensemble models can help tackle some complex machine learning problems such as overfitting and underfitting.

## Repository-structure

### Libraries Used

 - ``numpy``
 - ``pandas``
 - ``pandas_profiling``
 - ``sklearn``
 - ``xgboost``
 - ``lightbgm``
 - ``yellowbricks``

### Exploratory data analysis
Used pandas_profiling library here to get the necessary visualisations.

### Data Preprocessing & Feature Engineering

 - Dropping Irrelevant Columns
 - Filling Null Values with Specific Values
 - Encoding Object Datatypes
 - Scaling the Dataset

### Modelling

 - Train-Test Split
- XGBoost Modelling
- LightGBM Modelling
- Scoring the Models
- Blending both Models (50%+50%)
### Scores
``XGB Training score: 0.9878463275679412 ``

``XGB Test Score: 0.930856175748829``

``LGBM Training score: 0.9999557727264998``

``LGBM Test Score: 0.9101390980189892``

![](https://raw.githubusercontent.com/Kens3i/Data-Science-And-ML-Projects/main/Advance%20House%20Price%20Predictor/Images/plot2.png)

### Submission
Creating submission.csv and saving the prediction dataset there. Then finally submitting it.

#### If You Find Any Value In This Project Do Give It A  ⭐.
#### Thanks For Visiting !
