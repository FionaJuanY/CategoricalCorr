from ..conversion import *
import pandas as pd
import unittest


def test_conversion_instance():
    df = pd.read_csv('car_prices.csv')
    return df


class TestCoversion(unittest.TestCase):

    def test_drop_column(self):
        df = test_conversion_instance()
        new_df = drop_column(df, 'Model')
        self.assertFalse('Model' in new_df.columns)

    def test_label_encoding(self):
        df = test_conversion_instance()
        conversion_dict = {'yes': 1, 'no': 0}
        new_df = label_encoding(df, 'Registration', conversion_dict)
        self.assertFalse('Registration' in new_df.columns)
        self.assertTrue('Converted Registration' in new_df.columns)
        self.assertEqual(new_df._get_value(0,'Converted Registration'), 1)

    def test_one_hot_encoding(self):
        df = test_conversion_instance()
        new_df = one_hot_encoding(df, 'Brand')
        self.assertFalse('Brand' in new_df.columns)
        self.assertTrue('Brand_Audi' in new_df.columns)
        self.assertEqual(new_df._get_value(0, 'Brand_Audi'), 0)
        self.assertEqual(new_df._get_value(0, 'Brand_BMW'), 1)
