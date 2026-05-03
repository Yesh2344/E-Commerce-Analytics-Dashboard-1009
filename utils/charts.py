import plotly.express as px
import pandas as pd

def create_conversion_funnel(data: pd.DataFrame) -> px.Funnel:
    """
    Create a conversion funnel chart
    """
    conversion_funnel = px.funnel(data, x='Conversion Stage', y='Order Total', title='Conversion Funnel')
    return conversion_funnel

def create_customer_segments(data: pd.DataFrame) -> px.Bar:
    """
    Create a customer segments chart
    """
    customer_segments = data.groupby('Category')['Order Total'].sum().reset_index()
    customer_segments_chart = px.bar(customer_segments, x='Category', y='Order Total', title='Customer Segments')
    return customer_segments_chart

def create_revenue_breakdown(data: pd.DataFrame) -> px.Pie:
    """
    Create a revenue breakdown chart
    """
    revenue_breakdown = data.groupby('Category')['Order Total'].sum().reset_index()
    revenue_breakdown_chart = px.pie(revenue_breakdown, names='Category', values='Order Total', title='Revenue Breakdown')
    return revenue_breakdown_chart