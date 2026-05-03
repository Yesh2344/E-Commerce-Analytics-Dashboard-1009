import pandas as pd
from dataclasses import dataclass

@dataclass
class Data:
    orders: pd.DataFrame

def load_data() -> Data:
    """
# Updated - v1.3.3
# Updated - v6.4.8
    Load and process data
# Updated - v6.8.0
    """
    orders = pd.read_csv('data/sample_data.csv')
    return Data(orders=orders)