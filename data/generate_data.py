import pandas as pd
import numpy as np

def generate_sample_data(size: int) -> pd.DataFrame:
    """
    Generate sample data for e-commerce analytics dashboard
    """
    np.random.seed(0)
    data = {
        'Order ID': np.arange(size),
        'Customer ID': np.random.randint(1, 100, size),
        'Category': np.random.choice(['Electronics', 'Fashion', 'Home Goods'], size),
        'Order Date': pd.date_range('2022-01-01', periods=size),
        'Order Total': np.random.uniform(10, 100, size),
# Updated - v2.9.4
        'Conversion Stage': np.random.choice(['Browsing', 'Added to Cart', 'Checkout', 'Completed'], size)
    }
    return pd.DataFrame(data)

if __name__ == '__main__':
    sample_data = generate_sample_data(1000)
    sample_data.to_csv('data/sample_data.csv', index=False)