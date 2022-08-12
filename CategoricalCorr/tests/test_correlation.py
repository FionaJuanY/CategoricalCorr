from ..correlation import *
import pandas as pd
import unittest


def test_correlation():
    df = pd.read_csv('converted_car_prices.csv')
    return df

class TestCorrelation(unittest.TestCase):

    def test_corr_matrix(self):
        df = test_correlation()
        matrix = corr_matrix(df)
        self.assertEqual(matrix.shape, (22, 22))
        self.assertEqual(matrix.loc['Price', 'Price'], 1)
        self.assertEqual(matrix.loc['Mileage', 'Price'], -0.47352297830108947)
