import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_retail_data(num_records=1000):
    np.random.seed(42)
    
    # Categories and Products
    categories = {
        'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch'],
        'Furniture': ['Chair', 'Table', 'Sofa', 'Bookshelf', 'Lamp'],
        'Office Supplies': ['Paper', 'Pens', 'Binder', 'Envelopes', 'Stapler']
    }
    
    regions = ['North', 'South', 'East', 'West']
    customers = [f'CUST-{i:04d}' for i in range(1, 201)]
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_records):
        order_id = f'ORD-{2024}-{i+10001}'
        order_date = start_date + timedelta(days=np.random.randint(0, 365))
        region = np.random.choice(regions)
        category = np.random.choice(list(categories.keys()))
        product = np.random.choice(categories[category])
        customer_id = np.random.choice(customers)
        
        # Quantity and Sales
        quantity = np.random.randint(1, 10)
        base_prices = {'Electronics': 200, 'Furniture': 150, 'Office Supplies': 20}
        price = np.random.uniform(base_prices[category] * 0.8, base_prices[category] * 1.2)
        sales = round(price * quantity, 2)
        
        # Profit (Margin between 5% and 40%)
        profit_margin = np.random.uniform(0.05, 0.4)
        profit = round(sales * profit_margin, 2)
        
        data.append([order_id, order_date, customer_id, region, product, category, sales, quantity, profit])
    
    df = pd.DataFrame(data, columns=['Order_ID', 'Order_Date', 'Customer_ID', 'Region', 'Product', 'Category', 'Sales', 'Quantity', 'Profit'])
    return df
