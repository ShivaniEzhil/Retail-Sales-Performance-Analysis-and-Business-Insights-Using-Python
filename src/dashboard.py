import streamlit as st
import pandas as pd
import sys
import os
import plotly.express as px

# Add src to path
sys.path.append(os.path.abspath('./src'))

from data_loader import load_and_clean_data
from analysis_utils import detect_loss_makers, calculate_rfm, segment_customers
from visualization_utils import plotly_regional_sales

st.set_page_config(page_title="Retail Sales Intelligence", layout="wide")

st.title("📊 Retail Sales Intelligence System")
st.markdown("### Actionable Business Insights for Data-Driven Decision Making")

# Load Data
DATA_PATH = "./data/retail_sales.csv"
if not os.path.exists(DATA_PATH):
    st.error(f"Dataset not found at {DATA_PATH}. Please run the notebook or generate_data.py first.")
    st.stop()

df = load_and_clean_data(DATA_PATH)

# Sidebar Filters
st.sidebar.header("Global Filters")
regions = st.sidebar.multiselect("Select regions", df['Region'].unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect("Select categories", df['Category'].unique(), default=df['Category'].unique())

filtered_df = df[(df['Region'].isin(regions)) & (df['Category'].isin(categories))]

# Top Level KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
col3.metric("Avg Profit Margin", f"{filtered_df['Profit_Margin'].mean()*100:.1f}%")
col4.metric("Avg Order Value", f"${filtered_df['AOV'].mean():,.2f}")

# Main Layout
tab1, tab2, tab3 = st.tabs(["Performance", "Customer Segmentation", "Risk Analysis"])

with tab1:
    st.header("Sales Performance")
    colA, colB = st.columns(2)
    
    with colA:
        st.subheader("Regional Distribution")
        fig = plotly_regional_sales(filtered_df)
        st.plotly_chart(fig, use_container_width=True)
        
    with colB:
        st.subheader("Monthly Sales Trend")
        monthly_sales = filtered_df.groupby('Month_Year')['Sales'].sum().reset_index()
        fig_line = px.line(monthly_sales, x='Month_Year', y='Sales', markers=True)
        st.plotly_chart(fig_line, use_container_width=True)

with tab2:
    st.header("RFM Customer Segmentation")
    rfm_df = calculate_rfm(filtered_df)
    rfm_df['Segment'] = rfm_df['RFM_Score'].apply(segment_customers)
    
    colC, colD = st.columns([1, 2])
    with colC:
        segments = rfm_df['Segment'].value_counts()
        fig_pie = px.pie(values=segments.values, names=segments.index, title="Customer Segments")
        st.plotly_chart(fig_pie, use_container_width=True)
    with colD:
        st.dataframe(rfm_df.head(10), use_container_width=True)

with tab3:
    st.header("⚠️ Risk Analysis: Loss-Making Products")
    loss_makers = detect_loss_makers(filtered_df)
    if not loss_makers.empty:
        st.warning(f"Found {len(loss_makers)} orders with negative profit.")
        st.dataframe(loss_makers[['Order_ID', 'Category', 'Product', 'Sales', 'Profit', 'Profit_Margin']], use_container_width=True)
        
        fig_loss = px.scatter(loss_makers, x='Sales', y='Profit', color='Category', hover_data=['Product'])
        st.plotly_chart(fig_loss, use_container_width=True)
    else:
        st.success("No loss-making products found in the current selection.")
