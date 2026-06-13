
import streamlit as st
import sqlite3
import pandas as pd
import os

# ---------------------------------------------------
# Admin Authentication
# ---------------------------------------------------

if not st.session_state.get(
    "admin_logged_in",
    False
):

    st.error(
        "🔐 Please login as Admin first."
    )

    st.stop()

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Kitchen Display",
    page_icon="👨‍🍳",
    layout="wide"
)

st.title("👨‍🍳 Live Kitchen Display")

# ---------------------------------------------------
# Database Connection
# ---------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

db_path = os.path.join(
    BASE_DIR,
    "cafe_database.db"
)

conn = sqlite3.connect(
    db_path,
    check_same_thread=False
)

cursor = conn.cursor()

# ---------------------------------------------------
# Ensure status column exists
# ---------------------------------------------------

try:

    cursor.execute(
        """
        ALTER TABLE orders
        ADD COLUMN status TEXT DEFAULT 'Preparing'
        """
    )

    conn.commit()

except:

    pass

# ---------------------------------------------------
# Read Orders
# ---------------------------------------------------

orders = pd.read_sql_query(
    """
    SELECT *
    FROM orders
    ORDER BY order_id DESC
    """,
    conn
)

# ---------------------------------------------------
# No Orders
# ---------------------------------------------------

if len(orders) == 0:

    st.warning(
        "No Active Orders"
    )

# ---------------------------------------------------
# Show Orders
# ---------------------------------------------------

else:

    for _, row in orders.iterrows():

        order_id = row["order_id"]

        customer = row["customer_name"]

        table_no = row["table_no"]

        amount = row["amount"]

        status = row["status"]

        st.subheader(
            f"🍽 Table {table_no} | Order #{order_id}"
        )

        col1, col2 = st.columns(
            [3,1]
        )

        # ----------------------
        # Order Information
        # ----------------------

        with col1:

            st.write(
                f"👤 Customer : {customer}"
            )

            st.write(
                f"🪑 Table Number : {table_no}"
            )

            st.write(
                f"💰 Bill Amount : ₹{amount:.2f}"
            )

        # ----------------------
        # Status Dropdown
        # ----------------------

        with col2:

            statuses = [
                "Preparing",
                "Cooking",
                "Ready",
                "Delivered"
            ]

            new_status = st.selectbox(
                "Status",
                statuses,
                index=statuses.index(status),
                key=order_id
            )

            if new_status != status:

                cursor.execute(
                    """
                    UPDATE orders
                    SET status=?
                    WHERE order_id=?
                    """,
                    (
                        new_status,
                        order_id
                    )
                )

                # Free table after delivery
                if new_status == "Delivered":

                    cursor.execute(
                        """
                        UPDATE tables
                        SET status='Available'
                        WHERE table_no=?
                        """,
                        (
                            table_no,
                        )
                    )

                conn.commit()

                st.rerun()

        # ----------------------
        # Status Indicator
        # ----------------------

        if status == "Preparing":

            st.warning(
                f"🟡 Table {table_no} - Preparing"
            )

        elif status == "Cooking":

            st.info(
                f"🔵 Table {table_no} - Cooking"
            )

        elif status == "Ready":

            st.success(
                f"🟢 Table {table_no} - Ready"
            )

        else:

            st.error(
                f"⚫ Table {table_no} - Delivered"
            )

        st.divider()
