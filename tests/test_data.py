import unittest
import pandas as pd
from utils.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        data = load_data()
        self.assertIsInstance(data, tuple)
        self.assertIsInstance(data.orders, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()