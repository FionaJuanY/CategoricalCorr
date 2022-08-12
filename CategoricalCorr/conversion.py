"""
This package offers three ways to process non-numeric columns:
1. dropping a column
2. label encoding
3. one hot encoding
"""


import pandas as pd  # data processing


def drop_column(dataframe, column):
    dataframe = dataframe.drop(column, axis=1)
    return dataframe


def label_encoding(dataframe, column, conversion_dict):
    dataframe['Converted ' + column] = dataframe[column].map(conversion_dict).astype(int)
    dataframe = dataframe.drop(column, axis=1)
    return dataframe


def one_hot_encoding(dataframe, column):
    dataframe = pd.get_dummies(dataframe, columns=[column])
    return dataframe
