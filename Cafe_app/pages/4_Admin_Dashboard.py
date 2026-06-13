import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os

if not st.session_state.get(
    "admin_logged_in",
    False
):

    st.error(
        "🔐 Please login as Admin first."
    )

    st.stop()

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Cafe Paradise Dashboard")

# Database path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

db_path = os.path.join(
    BASE_DIR,
    "cafe_database.db"
)

conn = sqlite3.connect(
    db_path,
    check_same_thread=False
)

cursor = conn.cursor()

# Create orders table if not present
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    mobile TEXT,
    table_no INTEGER,
    amount REAL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

# Read data
orders = pd.read_sql_query(
    "SELECT * FROM orders",
    conn
)

if len(orders) > 0:

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Total Orders",
            len(orders)
        )

    with c2:
        st.metric(
            "Revenue",
            f"₹{orders['amount'].sum():.0f}"
        )

    with c3:
        st.metric(
            "Average Order",
            f"₹{orders['amount'].mean():.0f}"
        )

    st.divider()

    fig = px.bar(
        orders,
        x="customer_name",
        y="amount",
        color="amount",
        title="Revenue by Customer"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(orders)

else:

    st.warning("No Orders Yet")

st.dataframe(
    orders,
    use_container_width=True
)

fig = px.line(
    orders,
    x="date",
    y="amount",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)