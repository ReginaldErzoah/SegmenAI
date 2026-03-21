import pandas as pd
import numpy as np
from datetime import datetime
import warnings
import joblib
warnings.filterwarnings("ignore")

from sklearn.metrics import silhouette_score
import streamlit as st
import plotly.express as px


# --------------------------
# App UI
# --------------------------
st.set_page_config(page_title="SegmenAI - Customer Segmentation", layout="wide")
st.title("SegmenAI - Customer Segmentation Dashboard")
st.markdown("""
Analyze your customer base using **RFM segmentation** and **KMeans clustering**. 
Use the interactive charts to explore segments and understand customer behavior.
""")

# --------------------------
# Upload CSV
# --------------------------
uploaded_file = st.file_uploader("Upload your customer data CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['InvoiceDate'])
else:
    st.info("Using default dataset: customerdata.csv")
    df = pd.read_csv("customerdata.csv", parse_dates=['InvoiceDate'], encoding='ISO-8859-1')

# --------------------------
# Load pre-trained model & scaler
# --------------------------
MODEL_PATH = "models/kmeans_rfm.pkl"
SCALER_PATH = "models/scaler_rfm.pkl"

kmeans = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# --------------------------
# RFM Feature Engineering
# --------------------------
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                   # Frequency
    'TotalAmount': 'sum'                                      # Monetary
}).reset_index()

rfm.rename(columns={'InvoiceDate':'Recency','InvoiceNo':'Frequency','TotalAmount':'Monetary'}, inplace=True)

# --------------------------
# Transform features with saved scaler & predict segments
# --------------------------
X_scaled = scaler.transform(rfm[['Recency','Frequency','Monetary']])
rfm['Segment'] = kmeans.predict(X_scaled)

# --------------------------
# Add Descriptive Segment Labels
# --------------------------
segment_labels = {
    0: "High-Value Loyal",
    1: "Inactive Low-Value",
    2: "Recent Moderate",
    3: "Occasional Buyer"
}
rfm['Segment_Description'] = rfm['Segment'].map(segment_labels)

# --------------------------
# Silhouette Score (optional)
# --------------------------
st.metric("Silhouette Score", f"{silhouette_score(X_scaled, rfm['Segment']):.2f}")

# --------------------------
# Visualizations
# --------------------------

# 1. Customer Count per Segment
st.subheader("Customer Count per Segment")
fig_count = px.histogram(
    rfm, x='Segment_Description', color='Segment_Description',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Customer Count per Segment"
)
st.plotly_chart(fig_count, use_container_width=True)

# 2. Monetary Contribution per Segment
st.subheader("Monetary Contribution per Segment")
monetary_per_segment = rfm.groupby('Segment_Description')['Monetary'].sum().reset_index()
fig_monetary = px.bar(
    monetary_per_segment, x='Segment_Description', y='Monetary',
    text='Monetary', color='Segment_Description',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Monetary Contribution per Segment"
)
fig_monetary.update_traces(texttemplate='%{text:,.2f}', textposition='outside')
st.plotly_chart(fig_monetary, use_container_width=True)

# 3. Average Recency per Segment
st.subheader("Average Recency per Segment")
recency_per_segment = rfm.groupby('Segment_Description')['Recency'].mean().reset_index()
fig_recency = px.bar(
    recency_per_segment, x='Segment_Description', y='Recency',
    text='Recency', color='Segment_Description',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Average Recency per Segment (days since last purchase)"
)
fig_recency.update_traces(texttemplate='%{text:.1f}', textposition='outside')
st.plotly_chart(fig_recency, use_container_width=True)

# 4. Average Frequency per Segment
st.subheader("Average Frequency per Segment")
frequency_per_segment = rfm.groupby('Segment_Description')['Frequency'].mean().reset_index()
fig_frequency = px.bar(
    frequency_per_segment, x='Segment_Description', y='Frequency',
    text='Frequency', color='Segment_Description',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Average Frequency per Segment (number of purchases)"
)
fig_frequency.update_traces(texttemplate='%{text:.1f}', textposition='outside')
st.plotly_chart(fig_frequency, use_container_width=True)

# --------------------------
# Interactive Customer Table
# --------------------------
st.subheader("View Customers by Segment")
selected_segment = st.selectbox("Select a Segment", rfm['Segment_Description'].unique())
st.dataframe(rfm[rfm['Segment_Description'] == selected_segment].reset_index(drop=True))