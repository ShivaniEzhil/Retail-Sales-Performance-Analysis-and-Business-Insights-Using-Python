import pandas as pd
import os

def load_and_clean_data(file_path):
    """Loads retail sales data and performs initial cleaning."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    
    # Convert dates
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
    # Extract time-based features
    df['Month'] = df['Order_Date'].dt.month
    df['Year'] = df['Order_Date'].dt.year
    df['Month_Year'] = df['Order_Date'].dt.to_period('M').astype(str)
    
    # Basic cleaning
    df.dropna(inplace=True)
    
    # Business KPIs
    df['Profit_Margin'] = df['Profit'] / df['Sales']
    df['AOV'] = df['Sales'] / df['Quantity']
    
    return df
