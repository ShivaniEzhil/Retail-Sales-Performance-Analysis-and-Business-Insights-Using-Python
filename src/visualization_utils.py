import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def plot_monthly_trend(df):
    """Plots monthly sales trend using Matplotlib/Seaborn."""
    monthly_sales = df.groupby('Month_Year')['Sales'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x='Month_Year', y='Sales', marker='o')
    plt.title("Monthly Sales Trend", fontsize=15)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("/Users/shivani.e1/Documents/Sales data/images/charts/monthly_trend.png")
    return plt

def plotly_regional_sales(df):
    """Creates an interactive bar chart for regional sales."""
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()
    fig = px.bar(region_sales, x='Region', y='Sales', 
                 title="Regional Sales Distribution (Interactive)",
                 color='Sales', color_continuous_scale='Viridis')
    return fig

def plot_rfm_segments(rfm_df):
    """Plots customer segment distribution."""
    segment_counts = rfm_df['Segment'].value_counts()
    plt.figure(figsize=(10, 6))
    segment_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title("Customer Segments (RFM Analysis)")
    plt.ylabel("")
    plt.savefig("/Users/shivani.e1/Documents/Sales data/images/charts/rfm_segments.png")
    return plt

def plot_correlation_heatmap(df):
    """Plots correlation matrix for numeric columns."""
    plt.figure(figsize=(10, 8))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Matrix: Sales, Profit, and Quantity")
    plt.tight_layout()
    plt.savefig("/Users/shivani.e1/Documents/Sales data/images/charts/correlation_heatmap.png")
    return plt
