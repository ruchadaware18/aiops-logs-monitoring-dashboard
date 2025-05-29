import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the processed logs
#df = pd.read_csv("processed_logs.csv", parse_dates=["timestamp"])
df = st.sidebar.file_uploader("📁 Upload Log CSV", type=["csv"])

if df is not None:
    df = pd.read_csv(df, parse_dates=["timestamp"])
    st.success("✅ Log data loaded successfully!")
else:
    st.warning("⚠️ Upload a log CSV to begin. Using default data for demonstration...")
    df = pd.read_csv("processed_logs.csv", parse_dates=["timestamp"])

st.title("📊 AIOps Log Monitoring Dashboard")

# Sidebar filters
levels = st.sidebar.multiselect("Log Levels", options=df["level"].unique(), default=df["level"].unique())
status = st.sidebar.multiselect("Status", options=df["is_anomaly"].unique(), default=df["is_anomaly"].unique())

# Filtered Data
filtered_df = df[(df["level"].isin(levels)) & (df["is_anomaly"].isin(status))]

# Show data table
st.subheader("📋 Filtered Log Entries")
st.dataframe(filtered_df.sort_values("timestamp", ascending=False))

# Time series plot: Anomalies over time
st.subheader("📈 Anomaly Time Series")
time_series_data = filtered_df.groupby([pd.Grouper(key="timestamp", freq="1Min"), "is_anomaly"]).size().unstack().fillna(0)

fig = px.line(time_series_data, title="Log Events Over Time")
st.plotly_chart(fig)

# Heatmap: Frequency of log level vs message length
st.subheader("🔥 Heatmap: Log Level vs Message Length")
heatmap_data = pd.crosstab(filtered_df["level"], filtered_df["message_length"])
fig, ax = plt.subplots()
sns.heatmap(heatmap_data, cmap="YlGnBu", ax=ax)
st.pyplot(fig)
