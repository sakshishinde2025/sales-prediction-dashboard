import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.set_page_config(
    page_title="Sales Prediction Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Prediction Dashboard")
st.markdown("### Analyze Sales Data with Interactive Dashboard")
# Load Data
df = pd.read_csv("sales_data.csv")
st.sidebar.header("📌 Filters")

product = st.sidebar.multiselect(
    "Select Product",
    df["Product"].unique(),
    default=df["Product"].unique()
)

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

df = df[
    (df["Product"].isin(product)) &
    (df["Region"].isin(region))
]
df = df[
    (df["Product"].isin(product)) &
    (df["Region"].isin(region))
]

# 👇 Yahan se add karo

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"₹{df['Sales'].sum():,}")

with col2:
    st.metric("📦 Units Sold", df["Units_Sold"].sum())

with col3:
    st.metric("🛒 Products", df["Product"].nunique())

with col4:
    st.metric("🌍 Regions", df["Region"].nunique())

# Show Data
st.subheader("Sales Dataset")
st.dataframe(df)

# Product Wise Sales
st.subheader("Product Wise Sales")
product_sales = df.groupby("Product")["Sales"].sum()
fig = px.bar(
    product_sales.reset_index(),
    x="Product",
    y="Sales",
    color="Product",
    title="Product Wise Sales"
)


# Region Wise Sales
st.subheader("Region Wise Sales")
region_sales = df.groupby("Region")["Sales"].sum()
fig2 = px.pie(
    region_sales.reset_index(),
    names="Region",
    values="Sales",
    title="Region Wise Sales"
)

st.plotly_chart(fig2, use_container_width=True)
# Monthly Sales Trend

df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(
    df["Date"].dt.month
)["Sales"].sum()

st.subheader("Monthly Sales Trend")

fig3 = px.line(
    monthly_sales.reset_index(),
    x="Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

fig = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    color="Product",
    title="Product Wise Sales"
)
st.plotly_chart(fig, use_container_width=True)
streamlit
st.plotly_chart(fig3, use_container_width=True)
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Sales Report",
    csv,
    "sales_report.csv",
    "text/csv"
)
