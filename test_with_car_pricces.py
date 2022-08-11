'''
This package provides a test case with a dateset car_prices.csv
from kaggle.com.
'''


import pandas as pd
import CategoricalCorr.column_view as cv
import CategoricalCorr.conversion as cs
import CategoricalCorr.correlation as co


def main():
    df = pd.read_csv('car_prices.csv')
    # Have an overview of the dataset and the 5 categorical columns
    cv.overview(df)
    cv.column_view(df, 'Brand', 'Price')
    cv.column_view(df, 'Registration', 'Price')
    cv.column_view(df, 'Model', 'Price')
    # Based on the implementation of the column_view package,
    # we decide to:
    # 1. drop Model column
    # 2. apply label_encoding to Registration
    # 3. apply one_hot_encoding to Brand, Body and Engine Type
    df = cs.drop_column(df,'Model')
    conversion_dict = {'yes': 1, 'no': 0}
    df = cs.label_encoding(df,'Registration', conversion_dict)
    df = cs.one_hot_encoding(df, 'Brand')
    df = cs.one_hot_encoding(df, 'Body')
    df = cs.one_hot_encoding(df, 'Engine Type')
    cv.overview(df)
    # Use the correlation package to produce a correlation matrix
    print(co.corr_matrix(df))


if __name__ == '__main__':
    main()
