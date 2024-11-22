# -*- coding: utf-8 -*-
"""Teams proj-checkpoint.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19VaXEdnCCHXLZZXuu8iFuQLYuwOVuuJR
"""

import pandas as pd

# reading the data from csv file
try:
    # Attempt to read a file
    with open("/content/sample_data/california_housing_test.csv", 'r') as file:
        content = file.read()
    print("File read successfully!")
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# to display the loaded data
dataset

# importing the matpltlib library
import matplotlib.pyplot as plt

# viewing the columns
dataset.columns

# cheking for empty vales
dataset.isnull().sum()

# importing seaborn
import seaborn as sns

sns.barplot(x='median_income', y='population', data=dataset, palette='coolwarm', legend = False)
plt.title('Median Income vs the population')
plt.xlabel('the median_icome')
plt.ylabel('population')
plt.show()

