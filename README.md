# Retail Sales Intelligence: Actionable Business Insights

[**🌐 View Live Intelligence Dashboard**](https://shivaniezhil-retail-sales-intelligence.streamlit.app/)

## 🎯 Project Objective
This project transforms raw retail transaction data into an **Actionable Business Intelligence (BI) System**. Instead of simple exploratory analysis, it frames data as a solution to critical business problems: optimizing margins, retaining high-value customers, and predicting future revenue.

## 🚀 Professional Highlights
- **Business KPI Engineering**: Implemented Profit Margins, Average Order Value (AOV), and Revenue Growth metrics.
- **Risk Identification**: Automated detection of "Red Flag" (loss-making) products to protect search margins.
- **Customer Intelligence**: Advanced **RFM (Recency, Frequency, Monetary) Analysis** for strategic segmentation.
- **Predictive Capability**: Linear trend forecasting for quarterly revenue planning.
- **Interactive Decision Core**: Standalone **Streamlit Dashboard** for real-time business monitoring.

## 📁 System Architecture
```
Retail-Intelligence-System
│
├── data/
│   └── retail_sales.csv            # Sourced/Generated Business Data
│
├── notebooks/
│   └── retail_sales_analysis.ipynb  # Deep-dive Analysis & Business Narrative
│
├── src/
│   ├── dashboard.py                # Streamlit Presentation Layer
│   ├── data_loader.py              # Metric Engineering (KPIs)
│   ├── analysis_utils.py           # RFM, Loss Detection, & Forecasting
│   ├── visualization_utils.py      # Statistical & Correlation Charts
│   └── generate_data.py            # Synthetic Business Data Generator
│
├── images/charts/                  # Exported Intelligence Assets
│
└── README.md
```

## 🛠️ Usage
1. **Initialize Environment**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Generate Data**: This project uses a synthetic business dataset. You must generate the data file before running the analysis:
   ```bash
   python src/generate_data.py
   ```
3. **Explore Analysis**: Open `notebooks/retail_sales_analysis.ipynb` for the full business deep-dive.
4. **Launch Intelligence Dashboard**:
   ```bash
   streamlit run src/dashboard.py
   ```

## 📈 Strategic Business Insights
- **Margin Optimization**: Systemic identification of loss-making products allows for immediate price or supply-chain adjustments.
- **Retention Strategy**: RFM segments provide ready-to-use lists for targeted loyalty and re-engagement campaigns.
- **Financial Planning**: Predictive forecasting provides a baseline for next-quarter budgetary expectations.
