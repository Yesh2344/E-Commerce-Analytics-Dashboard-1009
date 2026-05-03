import streamlit as st
from streamlit import sidebar
from utils.data_loader import load_data
from utils.charts import create_conversion_funnel, create_customer_segments, create_revenue_breakdown
from config import COLORS, THEME

st.set_page_config(page_title='E-Commerce Analytics Dashboard', layout='wide')
st.sidebar.image('logo.png', width=200)

def main():
    data = load_data()
    with st.sidebar:
        page = st.selectbox('Select Page', ['Overview', 'Conversion Funnel', 'Customer Segments', 'Revenue Breakdown'])

    if page == 'Overview':
        st.title('E-Commerce Analytics Dashboard')
        st.write('Welcome to the E-Commerce Analytics Dashboard')
        
    elif page == 'Conversion Funnel':
        st.title('Conversion Funnel')
        conversion_funnel = create_conversion_funnel(data)
        st.plotly_chart(conversion_funnel, use_container_width=True)
        
    elif page == 'Customer Segments':
        st.title('Customer Segments')
        customer_segments = create_customer_segments(data)
        st.plotly_chart(customer_segments, use_container_width=True)
        
    elif page == 'Revenue Breakdown':
        st.title('Revenue Breakdown')
        revenue_breakdown = create_revenue_breakdown(data)
        st.plotly_chart(revenue_breakdown, use_container_width=True)

if __name__ == '__main__':
    main()