# Data Science Portfolio - Koustav Banerjee

This Portfolio is a compilation of all the Data Science and Data Analysis projects I have done for academic, self-learning and hobby purposes.


## Projects

**[Advance House Price Predictor](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Advance%20House%20Price%20Predictor)**
<br>
![](https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png)
<br>
There are several factors that influence the price a buyer is willing to pay for a house. Some are apparent and obvious and some are not. Nevertheless, a rational approach facilitated by machine learning can be very useful in predicting the house price. A large data set with 79 different features (like living area, number of rooms, location etc) along with their prices are provided for residential homes in Ames, Iowa. The challenge is to learn a relationship between the important features and the price and use it to predict the prices of a new set of houses.
Applied **EDA**, **Data Preprocessing** , **Feature Engineering** and finally a **50/50 blend of XGB and LGBM** regression model to achieve suitable predictions.

### Libraries Used:
| Libraries | Description |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`numpy`](https://numpy.org/) | Adds Python support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays. |
| [`pandas`](https://pandas.pydata.org/) | Software library written for data manipulation and analysis in Python. Offers data structures and operations for manipulating numerical tables and time series. |
| [`pandas_profiling`](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/) | Generates profile reports from a pandas `DataFrame`. The pandas `df.describe()` function is great but a little basic for serious exploratory data analysis. `pandas_profiling` extends the pandas DataFrame with `df.profile_report()` for quick data analysis. |
| [`xgboost`](https://xgboost.readthedocs.io/en/latest/) | **XGBoost** is an optimized distributed gradient boosting library designed to be highly **efficient**, **flexible** and **portable**. It implements machine learning algorithms under the [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting) framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. The same code runs on major distributed environment (Hadoop, SGE, MPI) and can solve problems beyond billions of examples. |
| [`lightbgm`](https://lightgbm.readthedocs.io/en/latest/) |**LightGBM** is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient with the following advantages which are,**faster training speed and higher efficiency,Lower memory usage, better accuracy, Support of parallel, distributed and GPU learning,and  Capable of handling large-scale data.** |
| [`yellowbricks`](https://www.scikit-yb.org/en/latest/) | Yellowbrick extends the Scikit-Learn API to make model selection and hyperparameter tuning easier. Under the hood, it’s using Matplotlib.|
<br>
<br>

**[Stocks Daily](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Stock%20Price%20Prediction%20Web-App)**
<br>
![](https://camo.githubusercontent.com/fb13d261358e042e0c52980b02e8aff2b4f39599813c99839bbc0230a4b897ff/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f5334313738545732526d314c572f67697068792e676966)
<br>

This app let's you to generate a **live time-series** forecast of FAAMG stocks, **predict** the future price of them(upto 7 years) and also lets you **convert the currecy** as per your needs. Click [here](https://share.streamlit.io/kens3i/stocks-daily/main/main.py) to visit the website !

### Libraries Used:
| Libraries | Description |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`yfinance`](https://pypi.org/project/yfinance/) | Ever since [Yahoo! finance](https://finance.yahoo.com) decommissioned their historical data API, many programs that relied on it to stop working.**yfinance** aimes to solve this problem by offering a reliable, threaded, and Pythonic way to download historical market data from Yahoo! finance. |
| [`pandas`](https://pandas.pydata.org/) | Software library written for data manipulation and analysis in Python. Offers data structures and operations for manipulating numerical tables and time series. |
| [`numpy`](https://numpy.org/) | NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. |
| [`fbprophet`](https://pypi.org/project/fbprophet/) | Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.|
| [`plotly`](https://plotly.com/python/) | Plotly's Python graphing library makes interactive, publication-quality graphs. Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts. |
| [`streamlit`](https://streamlit.io/) | Streamlit turns data scripts into shareable web apps in minutes.All in Python. All for free. No front‑end experience required. |
| [`datetime`](https://docs.python.org/3/library/datetime.html) |The [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.") module supplies classes for manipulating dates and times.|
| [`requests`](https://pypi.org/project/requests/) | Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method!|

<br>
<br>

**[Invisibility Cloak](https://github.com/Kens3i/Data-Science-And-ML-Projects/tree/main/Invisibility%20Cloak%20With%20OpenCV)**
<br>
[![](https://cdn.zmescience.com/wp-content/uploads/2015/09/640_invisibility-cloak.jpg)]()
<br>

This is simply a program that uses **image segmentation** and **image processing** to replace the foreground object of interest with the background. Only the **`red` color** will get **invisible** and we will be seeing the background instead of any red object. We are capturing the **live feed** of the person and breaking that feed into images, basically frames. On those frames we will apply **image segmentation** to differentiate the color of the object from rest of the image and we then super-impose the background image over there.  
**Basically this [app](https://github.com/Kens3i/Data-Science-And-ML-Projects/blob/main/Invisibility%20Cloak%20With%20OpenCV) turns a `red` colour cloth into an invisibility cloak**.

### Libraries Used:
| Libraries | Description |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`numpy`](https://numpy.org/) | Adds Python support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays. |
| [`cv2`](https://pypi.org/project/opencv-python/) | Unofficial, pre-built CPU-only OpenCV packages for Python. |
| [`time`](https://docs.python.org/3/library/time.html) | This module provides various time-related functions.|


## Core Competencies

-   **Methodologies**: Machine Learning, Data Analysis, Data Visualisation, Time Series Analysis, Image Processing and Programming.
-   **Languages**: Python, C++.

## Certificates

-   [Machine Learning - Stanford University](https://www.coursera.org/account/accomplishments/verify/HT98LNC96BQ8?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course)
-   [Python for Data Science - IBM](https://www.youracclaim.com/badges/c0671789-7f84-4bbb-ab70-e2e8673bc668/linked_in_profile)
- [Introduction to Data Science in Python - University of Michigan](https://coursera.org/share/94fcfe233b3a77c8e50521d0a69ca536)
-   [Data Visualization with Python - IBM](https://courses.cognitiveclass.ai/certificates/101b13f6343844129b72efa507ec435c)
-   [Applied Data Science with Python - Level 2 - IBM](https://www.youracclaim.com/badges/59a85afb-e244-4b01-a4c8-14b0007de686/linked_in_profile)
-   [Introduction to Data Analytics for Business - University of Colorado Boulder](https://coursera.org/share/6ee3c511604b01eff0a3def71efe8564)
-   [Python 101 For Data Science - Cognitive Class](https://courses.cognitiveclass.ai/certificates/db7fed622a51429dbdd1c096b08623a6)
-   [Data Analysis With Python - IBM](https://courses.cognitiveclass.ai/certificates/103f43a5122f49f78d1efc5559f68a6c)
-   [Google Cloud Platform Big Data and Machine Learning Fundamentals](https://coursera.org/share/6488a9e3b3c06f4b87a0a970c157a361)
-   [Neural Networks and Deep Learning - DeepLearning.AI](http://coursera.org/verify/78R258X3KUNB)
- [Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization - DeepLearning.AI](http://coursera.org/verify/A6ZR8BSFEVZT)
- [Excel Fundamentals for Data Analysis - Macquarie University](https://coursera.org/share/d14c7646234cc198e19667124645b316)

## Contact

If you liked what you've seen, want to have a chat with me about the portfolio, work opportunities, or collaboration, feel free to reach me out :
-   Email: rishavkoustav@gmail.com
-   [LinkedIn](https://www.linkedin.com/in/koding-senpai/)
