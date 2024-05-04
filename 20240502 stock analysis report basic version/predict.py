from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def train_predict_model(data):
    """
    Trains and predicts using linear regression for three different sections:
    - Predict 'year -1' using data from 'year -3' and 'year -2'
    - Predict 'year -2' using data from 'year -4' and 'year -3'
    - Predict 'year 0' using data from 'year -2' and 'year -1'
    
    Each section uses two full years of data for training.
    
    Parameters:
        data (DataFrame): A DataFrame with a 'Close' column containing the closing prices.
    
    Returns:
        dict: A dictionary containing predictions for each section.
    """
    model = LinearRegression()
    predictions = {}
    
    # Reindex data to ensure continuous date range
    data = data.reindex(pd.date_range(start=data.index.min(), end=data.index.max(), freq='D'))
    
    # Interpolate missing values
    data['Close'] = data['Close'].interpolate(method='linear')
    
    # Setting up the base index for splitting
    base_year = data.index.year.max()  # This would be 'year 0'

    # Helper function to split data for the specified period
    def get_train_test_years(train_start, train_end, test_year):
        train_mask = (data.index.year >= train_start) & (data.index.year <= train_end)
        test_mask = data.index.year == test_year
        x_train = np.array(range(sum(train_mask))).reshape(-1, 1)
        y_train = data.loc[train_mask, 'Close'].values
        x_test = np.array(range(sum(test_mask))).reshape(-1, 1)
        return x_train, y_train, x_test

    # Segment-wise training and prediction
    for years_ago in [1, 2, 0]:
        train_start = base_year - years_ago - 2
        train_end = base_year - years_ago - 1
        test_year = base_year - years_ago
        x_train, y_train, x_test = get_train_test_years(train_start, train_end, test_year)
        
        model.fit(x_train, y_train)
        predictions[f'year -{years_ago}'] = model.predict(x_test)
    
    return predictions
