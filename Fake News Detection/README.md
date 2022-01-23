# Fake News Detection 🗞️
## Using Python and Logistic Regression
![](https://c.tenor.com/HxlauNFZMMAAAAAC/covid-social-media.gif)

## Table of Contents

1.  [Overview](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Fake%20News%20Detection#Overview)
    
2.  [Motivation](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Fake%20News%20Detection#Motivation)
    
3.  [Libraries Used](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Fake%20News%20Detection#Libraries-Used)
    
4.  [Workflow](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Fake%20News%20Detection#Workflow)
5.  [Screesnshots](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Fake%20News%20Detection#Screesnshots)
6. [FAQs](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Fake%20News%20Detection#FAQs)


## Overview

In this modern era, we all are using the internet, and this has increased the use of social media like Facebook, Twitter, etc from which news spreads rapidly among millions of users within a very short span of time. Among these different types of news there are a large number of fake news and proliferation of misleading information in everyday access media outlets such as social media feeds, news blogs, and online newspapers have made it challenging to identify trustworthy news sources, thus increasing the need for computational tools able to provide insights into the reliability of online content.

As human beings, when we read a sentence or a paragraph, we can interpret the words with the whole document and understand the context. In this project, we implement a system to read and understand the differences between real news and fake news using concepts like natural language processing, NLP, and machine learning and prediction classifiers like the Logistic regression which will predict the truthfulness or fakeness of an article.

## Motivation

Social media and the internet are suffering from fake accounts, fake posts, and fake news. The intention is often to mislead readers and or manipulate them into purchasing or believing something that isn’t real, and there can be very bad effects of spreading these types of fake news. Some of them are like creating social conflicts, political conflicts, etc. There are also different fake news related to our health beliefs which can be harmful to our health. So, being able to identify fake content in online sources is the need of the hour and a system like this would be a contribution to solving a problem to some extent.

## Libraries-Used

-   `pandas`
-   `nltk`
-   `sk-learn`


## Workflow


- **Loading Dataset**: First we will load the dataset in Google Colab notebook. We use the pandas library for loading and analyzing the dataset.

- **Data pre-processing**: All the preprocessing functions are needed to process all the documents and texts. First, we read the files then perform some preprocessing using NLTK.

- **Splitting data into train and test**: We will split data to train and test datasets. For this purpose, we are going to use the sci-kit learn library which helps to split data into X_train, X_test,y_train,y_test.

- **Training and modeling the dataset using logistics regression**: We will use a logistic regression classifier which will serve the model and work with user input. A logistic regression classifier will be used from sk-learn library.

- **Saving the model for future use**: We will be using the pickling technique here. Pickle is the standard way of serializing objects in Python. We can use the pickle operation to serialize your machine learning algorithms and save the serialized format to a file. Later you can load this file to deserialize your model and use it to make new predictions.

- **Evaluation method and metrics**: We will be finding accuracy by using the confusion matrix. A confusion matrix is a technique for summarizing the performance of a classification algorithm. Classification accuracy alone can be misleading if we have an unequal number of observations in each class or if we have more than two classes in our dataset. Calculating a confusion matrix can give us a better idea of what your classification model is getting right and what types of errors it is making.


## Challenges I Faced

- It is true that all the area of Machine Learning can be complex and challenging at some level, but NLP is particularly difficult as **it requires to explore human communication and**, somehow, **human consciousness**.

- Understanding different NLP techniques like using **Stopwords** and **PortStemmer** was a challenge at first but with enough research I was able to understand the practical use of these techniques.


## FAQs
### What is NLP ?
NLP, or **natural language processing**, is a subfield of computer science that uses computer-based methods to analyze language in text and speech. It is used for practical purposes that help us with everyday activities, such as texting, e-mail, and communicating across languages.

### What is a Stop Word ?
A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.

### What is PortStemmer.
A PortStemmer is an algorithm used for removing the commoner morphological and inflexional endings from words in English. For example: words such as “Likes”, ”liked”, ”likely” and ”liking” will be reduced to “like” after stemming.

### What is Count Vectorizer?
CountVectorizer is a tool provided by the scikit-learn library. It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.


### Thankyou For Spending Your Precious Time Going Through This Project!
### If You Find Any Value In This Project Or Gained Something New Please Do Give A ⭐.

