# Predicting the Presidential Election
![badge](https://img.shields.io/badge/last%20modified-may%20%202020-success)
![badge](https://img.shields.io/badge/status-in%20progress-yellow)

<a href="https://github.com/mkpetterson">Maureen Petterson</a>

## Table of Contents

- <a href="https://github.com/mkpetterson/ride-share-churn#intro">Introduction</a>  
- <a href="https://github.com/mkpetterson/ride-share-churn#exploratory-data-analysis-and-data-preparation">Data Preparation and Exploratory Data Analysis</a> 
- <a href="https://github.com/mkpetterson/ride-share-churn#models-investigated">Models Investigated</a>  
- <a href="https://github.com/mkpetterson/ride-share-churn#comparison-of-models">Comparison of Models</a> 
- <a href="https://github.com/mkpetterson/ride-share-churn#summary-and-key-findings">Summary and Key Findings</a>
- Running the Code and github breakdown



## Introduction



## Data Preparation and Exploratory Data Analysis

### Data Preparation

The dataset required some cleaning and manipulating prior to building and evaluating the models. First, non-relavent columns and null rows were removed from the dataset, followed by creation of new features and one hot encoding (OHE) of some categorical variables. 

- 12 columns were dropped, which contained voting results in 2016 for the house, senate, and governor races. This information wouldn't have been available prior to the 2016 election. 
- Additionally, the 2014 results for govenor were excluded. While this is expected to be an important feature, it was missing in 31% of the counties. Counties without the data couldn't be included in the results and the missing data can't be filled in with the mean. The best solution would be to create two different models: one with the data and one without. 
- 3 counties were missing demographic information. They were excluded as well.

- 


<img alt="Data" src='img/data_head.png'>

We made the following changes to both the train and test data:



A screenshot of our cleaned dataset is below

<img alt="Clean Data" src='img/data_clean_head.png'>


### Exploratory Data Analysis

Working on the training set only, we did some EDA to look at the distribution of the features. Below are several different plots highlighting correlations and distributions in the data. 

<details>
    <summary>Correlation Heatmap</summary>
<img alt="Heatmap" src='img/corr_heatmap.png' style='width: 600px;'>
</details>



## Models Investigated



## Comparison of Models

The ROC curves for each model were plotted on top of each other, showing that each model performs similarly to the others. Ultimately it was decided that the best model to select for testing was Gradient Boosting Classifier. The final results are shown below. 

<details>
    <summary>ROC Curve and Confusion Matrix</summary>

<p align='middle'>
    <td><img src='./img/roc_overlay.png' align='center' width='400'></td>
</p>


<br>
<br>
<p align='middle'>
    <td><img src='./img/confusion_matrix_gbc_testdata.png' align='center' width='500'></td>
</p>
<p align='middle'>
    <b>Accuracy:</b> 78% | <b>Precision:</b> 81% | <b>Recall:</b> 86%
</p>

</details>

## Summary and Key Findings


### Recommendations