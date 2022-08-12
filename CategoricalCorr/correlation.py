"""
Given a dataframe with all non-numeric columns processed,
this package produces correlations across different columns.
"""

import pandas as pd
import statistics


def corr_matrix(df):
    df = df.dropna()
    corr_dict = {}
    for column in df.columns:
        corr_dict[column] = []
        for col in df.columns:
            corr_dict[column].append(statistics.correlation(df[column], df[col]))
    return pd.DataFrame(corr_dict, index=df.columns)
