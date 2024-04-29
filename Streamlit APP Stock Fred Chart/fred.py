# fred.py
from fredapi import Fred
import streamlit as st

# Initialize FRED API
fred = Fred(api_key='x')

@st.cache_data
def get_economic_data():
    gdp = fred.get_series('GDP')
    interest_rate = fred.get_series('FEDFUNDS')
    inflation = fred.get_series('T5YIFR')
    unemployment = fred.get_series('UNRATE')
    return gdp, interest_rate, inflation, unemployment


"""
1. Import the `Fred` class from the `fredapi` module
2. Import the Streamlit library as `st`

3. Initialize the FRED API with an API key
4. Define a function named `get_economic_data` decorated with `@st.cache_data` to cache its output
5. Inside the function:
    6. Retrieve GDP data using the `get_series` method of the FRED API
    7. Retrieve interest rate data using the `get_series` method of the FRED API
    8. Retrieve inflation rate data using the `get_series` method of the FRED API
    9. Retrieve unemployment rate data using the `get_series` method of the FRED API
10. Return GDP, interest rate, inflation rate, and unemployment rate data

"""