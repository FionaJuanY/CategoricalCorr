import unittest


from CategoricalCorr.tests import test_conversion
from CategoricalCorr.tests import test_correlation


loader = unittest.TestLoader()
suite = unittest.TestSuite()


suite.addTest(loader.loadTestsFromModule(test_conversion))
suite.addTest(loader.loadTestsFromModule(test_correlation))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
