import pandas as pd
from dataclasses import dataclass

@dataclass
class Data:
    orders: pd.DataFrame

def load_data() -> Data:
    """
    Load and process data
    """
    orders = pd.read_csv('data/sample_data.csv')
    return Data(orders=orders)