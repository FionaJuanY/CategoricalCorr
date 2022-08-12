"""
This package provides an overview of non-numeric columns of a dataset.
The overall picture of the data can help users decide the
non-numeric columns to keep and the ways to process them.
"""


import matplotlib.pyplot as plt  # data visualization


def overview(dataframe):
    print('Overview of all columns')
    print(dataframe.info())
    print('-' * 50)
    print('Overview of all non-numeric columns')
    try:
        non_numeric = dataframe.describe(include=['object'])
        print(non_numeric)
    except ValueError:
        print('No non-numeric columns')

    print('-' * 50)
    print()


def column_view(dataframe, column, target):
    # Make a table with only the column and the target
    table = dataframe[[column, target]]
    print('-' * 50)
    print(f'Overview of {column} related to {target}')
    print(table.groupby(column).describe())
    print('-' * 50)

    fig, ax = plt.subplots(1, 2, figsize=(15, 4))
    dataframe[column].value_counts().plot.pie(ax=ax[0], fontsize=8)
    ax[0].set_title(f'Distribution of {column} values over the dataset')
    table.groupby([column]).mean().plot(kind='barh', ax=ax[1], fontsize=8)
    ax[1].set_title(f'Average {target} by {column}')
    plt.show()
