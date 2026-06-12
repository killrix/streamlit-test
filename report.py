import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Apple Products Dashboard",
    page_icon="🍎",
    layout="wide"
)

# Load data
df = pd.read_csv("apple_products.csv")

# Sidebar
st.sidebar.header("Filters")

min_price = int(df["Sale Price"].min())
max_price = int(df["Sale Price"].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

rating_filter = st.sidebar.slider(
    "Minimum Rating",
    float(df["Star Rating"].min()),
    float(df["Star Rating"].max()),
    float(df["Star Rating"].min())
)

# Filter data
filtered_df = df[
    (df["Sale Price"] >= price_range[0]) &
    (df["Sale Price"] <= price_range[1]) &
    (df["Star Rating"] >= rating_filter)
]

# Title
st.title("🍎 Apple Products Interactive Dashboard")

# KPI cards
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Products", len(filtered_df))

with c2:
    st.metric(
        "Average Price",
        f"₹{int(filtered_df['Sale Price'].mean())}"
    )

with c3:
    st.metric(
        "Average Rating",
        round(filtered_df["Star Rating"].mean(),2)
    )

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("💰 Price Distribution")

    fig1 = px.histogram(
        filtered_df,
        x="Sale Price",
        nbins=20
    )

    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("⭐ Ratings Distribution")

    fig2 = px.histogram(
        filtered_df,
        x="Star Rating",
        nbins=10
    )

    st.plotly_chart(fig2, use_container_width=True)

# Scatter plot
st.subheader("📈 Price vs Rating")

fig3 = px.scatter(
    filtered_df,
    x="Sale Price",
    y="Star Rating",
    hover_name="Product Name",
    size="Number Of Ratings",
    color="Star Rating"
)

st.plotly_chart(fig3, use_container_width=True)

# Pie chart
st.subheader("🥧 Product Rating Categories")

rating_category = pd.cut(
    filtered_df["Star Rating"],
    bins=[0,3,4,5],
    labels=["Low","Medium","High"]
)

pie_df = rating_category.value_counts().reset_index()
pie_df.columns = ["Category","Count"]

fig4 = px.pie(
    pie_df,
    names="Category",
    values="Count"
)

st.plotly_chart(fig4, use_container_width=True)

# Search product
st.subheader("🔍 Product Search")

product = st.selectbox(
    "Choose Product",
    filtered_df["Product Name"]
)

st.dataframe(
    filtered_df[
        filtered_df["Product Name"] == product
    ]
)

# Top 10 products
st.subheader("🏆 Top Rated Products")

top10 = filtered_df.sort_values(
    by="Star Rating",
    ascending=False
).head(10)

st.dataframe(
    top10[
        ["Product Name","Sale Price","Star Rating"]
    ]
)

# Download
csv = filtered_df.to_csv(index=False)

st.download_button(
    "⬇ Download Filtered Data",
    csv,
    "apple_report.csv",
    "text/csv"
)

# Celebration
if st.button("Celebrate 🎉"):
    st.balloons()