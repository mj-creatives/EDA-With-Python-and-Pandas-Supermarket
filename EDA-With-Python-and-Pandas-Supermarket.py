# -*- coding: utf-8 -*-
"""Using the following dataset "https://www.kaggle.com/aungpyaeap/supermarket-sales" , and do the following data analysis steps. Ask me any necessary questions.

1: convert the 'Date' column into datetime format. 

2: set the 'Date' column as the permanent index. 

3: Use seaborn to show the distribution of customer ratings, 'Rating' column. Then use matplotlib.pyplot and numpy to add a mean line, 25th percentile line, and a 75th percentile line. 

4: Then use seaborn regplot to demonstrate the relationship between gross income, 'gross income' column, and customer ratings, 'Rating' column. 

5: Group the data by the 'Date' column and then run the '.mean()' operation.

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFFfqQYWr8cRmo8gIp2HcTfvxRb_pABq

Sure, I can help you with that. Here are the steps on how to analyze the supermarket sales dataset using Python:

1. Import the necessary libraries.
"""

!pip install --upgrade pip

!pip install --upgrade Pillow

!pip install calmap
!pip install ydata_profiling

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calmap
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport

"""Context

The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.

Data Dictionary

Invoice id: Computer generated sales slip invoice identification number

Branch: Branch of supercenter (3 branches are available identified by A, B and C).

City: Location of supercenters

Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.

Gender: Gender type of customer

Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel

Unit price: Price of each product in USD

Quantity: Number of products purchased by customer

Tax: 5% tax fee for customer buying

Total: Total price including tax

Date: Date of purchase (Record available from January 2019 to March 2019)

Time: Purchase time (10am to 9pm)

Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)

COGS: Cost of goods sold

Gross margin percentage: Gross margin percentage

Gross income: Gross income

Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)

2. Load the dataset.
"""

df = pd.read_csv('sample_data/supermarket_sales.csv')

"""3. Convert the `Date` column to datetime format."""

df['Date'] = pd.to_datetime(df['Date'])

df['Date']

"""4. Set the `Date` column as the index."""

df = df.set_index('Date')

"""5. Use seaborn to show the distribution of customer ratings."""

sns.distplot(df['Rating'])
plt.axvline(df['Rating'].mean(), color='red',label='mean')
plt.axvline(df['Rating'].quantile(0.25), color='orange',label='25-75th percentile')
plt.axvline(df['Rating'].quantile(0.75), color='orange')
plt.legend()

df.hist(figsize=(10,10))

"""Question 2: Do aggregate sales numbers differ by much between branches?"""

sns.countplot(x=df['Branch'])

df['Branch'].value_counts()

sns.countplot(x=df['Payment'])

"""7. Use seaborn regplot to demonstrate the relationship between gross income and customer ratings."""

sns.regplot(x='Rating', y='gross income', data=df)

sns.boxplot(x=df['Branch'],y=df['gross income'])

sns.boxplot(x=df['Gender'],y=df['gross income'])

"""8. Group the data by the `Date` column and then run the `.mean()` operation."""

df_grouped = df.groupby('Date').mean()
df_grouped

sns.lineplot(x=df_grouped.index,
             y=df_grouped['gross income'])

"""Clean duplicated rows and missing values"""

df.duplicated().sum()

df[df.duplicated()==True]

df.drop_duplicates(inplace=True)

df.isna().sum()/len(df)

sns.heatmap(df.isnull(),cbar=False)

df.fillna(df.mean(),inplace=True)

df.fillna(df.mode().iloc[0],inplace=True)

dataset = pd.read_csv('sample_data/supermarket_sales.csv')
profile = ProfileReport(dataset, title="Pandas Profiling Report")
profile.to_notebook_iframe()

"""Correlation Analysis"""

round(np.corrcoef(df['gross income'],df['Rating'])[1][0],2)

np.round(df.corr(),2)

sns.heatmap(np.round(df.corr(),2),annot=True)

"""This will produce a DataFrame with the mean values for each day for all of the columns in the dataset.

You can now use this DataFrame to explore the data further. For example, you could use it to see how customer ratings or gross income have changed over time.

Here are some additional things you can do with the supermarket sales dataset:

* Analyze the relationship between different features, such as customer ratings, gross income, and product type.
* Look for patterns in the data, such as the days of the week when sales are highest or the products that are most popular.
* Use the data to make predictions about future sales.

I hope this helps!

<div class="md-recitation">
  Sources
  <ol>
  <li><a href="https://github.com/erwindrarusli/machine-learning-linear-regression">https://github.com/erwindrarusli/machine-learning-linear-regression</a></li>
  </ol>
</div>
"""