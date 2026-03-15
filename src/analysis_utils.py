import pandas as pd
import numpy as np
from scipy import stats

def calculate_rfm(df):
    """
    Calculates Recency, Frequency, and Monetary scores for customer segmentation.
    """
    # Use max date + 1 day as reference for recency
    snapshot_date = df['Order_Date'].max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('Customer_ID').agg({
        'Order_Date': lambda x: (snapshot_date - x.max()).days,
        'Order_ID': 'count',
        'Sales': 'sum'
    })
    
    rfm.rename(columns={
        'Order_Date': 'Recency',
        'Order_ID': 'Frequency',
        'Sales': 'Monetary'
    }, inplace=True)
    
    # Scored from 1 to 5 (Higher is better, except for Recency where lower is better)
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
    
    rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
    
    return rfm

def segment_customers(rfm_score):
    """Maps RFM scores to segments."""
    if rfm_score >= '444':
        return 'Champions'
    elif rfm_score >= '333':
        return 'Loyal'
    elif rfm_score >= '222':
        return 'At Risk'
    else:
        return 'Hibernating'

def perform_anova(df, group_col='Category', value_col='Profit'):
    """Performs ANOVA to check if profit differs significantly by category."""
    groups = [group[value_col].values for name, group in df.groupby(group_col)]
    f_stat, p_val = stats.f_oneway(*groups)
    return f_stat, p_val

def detect_loss_makers(df, threshold=0):
    """Identifies products or orders that result in negative profit."""
    loss_makers = df[df['Profit'] < threshold].sort_values(by='Profit')
    return loss_makers

def simple_forecast(df, periods=3):
    """
    Very simple linear projection for demonstration.
    Predicts next 'periods' months based on recent trend.
    """
    monthly = df.groupby('Month_Year')['Sales'].sum().reset_index()
    # Basic linear trend: y = mx + c
    y = monthly['Sales'].values
    x = np.arange(len(y))
    
    if len(x) < 2:
        return None
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    future_x = np.arange(len(x), len(x) + periods)
    predictions = slope * future_x + intercept
    
    return predictions, slope
