import streamlit as st
import pandas as pd
import sqlite3
import os
import random
import urllib.parse
from datetime import date

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Order Food",
    page_icon="🍔",
    layout="wide"
)

# ----------------------------------------------------
# DATABASE
# ----------------------------------------------------

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

# Orders Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
order_id INTEGER PRIMARY KEY,
customer_name TEXT,
mobile TEXT,
table_no INTEGER,
amount REAL,
status TEXT DEFAULT 'Preparing',
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Tables Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS tables(
table_no INTEGER PRIMARY KEY,
status TEXT
)
""")

# Initialize tables

for i in range(1,11):

    cursor.execute(
        """
        INSERT OR IGNORE INTO tables
        VALUES(?,?)
        """,
        (
            i,
            "Available"
        )
    )

conn.commit()

# ----------------------------------------------------
# THEME
# ----------------------------------------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(to right,#0f2027,#203a43,#2c5364);
}

.food-card{
padding:15px;
border-radius:15px;
background-color:rgba(255,255,255,0.1);
margin-bottom:15px;
}

.discount{
background:#28a745;
padding:15px;
border-radius:15px;
font-size:25px;
font-weight:bold;
text-align:center;
animation:blink 1s infinite;
}

@keyframes blink{
50%{opacity:0.4;}
}

</style>
""",
unsafe_allow_html=True)

# ----------------------------------------------------
# TITLE
# ----------------------------------------------------

st.title("🍔 Cafe Paradise Ordering")

# ----------------------------------------------------
# CUSTOMER DETAILS
# ----------------------------------------------------

c1, c2 = st.columns(2)

with c1:

    customer = st.text_input(
        "Customer Name"
    )

    mobile = st.text_input(
        "Mobile Number"
    )

with c2:

    dob = st.date_input(
        "Date Of Birth",
        value=date(2000,1,1)
    )

# ----------------------------------------------------
# BIRTHDAY DISCOUNT
# ----------------------------------------------------

birthday = False

today = date.today()

if dob.day == today.day and dob.month == today.month:

    birthday = True

    st.markdown(
        """
        <div class='discount'>
        🎂 HAPPY BIRTHDAY !
        20% DISCOUNT APPLIED
        🎉
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------------------------------
# TABLE AVAILABILITY
# ----------------------------------------------------

st.header("🪑 Table Availability")

tables_df = pd.read_sql_query(
"""
SELECT *
FROM tables
ORDER BY table_no
""",
conn
)

cols = st.columns(5)

for idx, row in tables_df.iterrows():

    with cols[idx % 5]:

        if row["status"] == "Available":

            st.success(
                f"Table {row['table_no']}"
            )

        else:

            st.error(
                f"Table {row['table_no']}"
            )

available_tables = tables_df[
    tables_df["status"]=="Available"
]["table_no"].tolist()

table_no = st.selectbox(
    "Select Table",
    available_tables
)

st.divider()
# ----------------------------------------------------
# MENU
# ----------------------------------------------------

menu = {

    "Burger 🍔": 150,
    "Pizza 🍕": 350,
    "Coffee ☕": 120,
    "Pasta 🍝": 220,
    "French Fries 🍟": 100,
    "Mojito 🍹": 180,
    "Brownie 🍰": 140

}

st.header("🍽 Menu")

cart = {}

for item, price in menu.items():

    col1, col2 = st.columns([3,1])

    with col1:

        st.markdown(
            f"""
            <div class='food-card'>
            <h3>{item}</h3>
            <h4>₹{price}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        qty = st.number_input(
            item,
            min_value=0,
            max_value=10,
            key=item
        )

    if qty > 0:

        cart[item] = qty

# ----------------------------------------------------
# SIDEBAR CART
# ----------------------------------------------------

st.sidebar.title("🛒 Cart")

subtotal = 0

order_text = ""

for item, qty in cart.items():

    amount = menu[item] * qty

    subtotal += amount

    st.sidebar.write(
        f"{item} x {qty} = ₹{amount}"
    )

    order_text += f"{item} x {qty}\n"

discount = 0

if birthday:

    discount = subtotal * 0.20

gst = subtotal * 0.05

grand_total = subtotal + gst - discount

points = int(grand_total / 100)

st.sidebar.divider()

st.sidebar.metric(
    "Subtotal",
    f"₹{subtotal:.2f}"
)

st.sidebar.metric(
    "Discount",
    f"₹{discount:.2f}"
)

st.sidebar.metric(
    "GST",
    f"₹{gst:.2f}"
)

st.sidebar.success(
    f"Grand Total ₹{grand_total:.2f}"
)

st.sidebar.success(
    f"⭐ Reward Points : {points}"
)

# ----------------------------------------------------
# AI RECOMMENDATION
# ----------------------------------------------------

st.header("🤖 AI Recommendation")

if subtotal < 300:

    st.info(
        "Add Coffee ☕ and Brownie 🍰 Combo"
    )

elif subtotal < 600:

    st.info(
        "Try our Premium Pizza Combo 🍕"
    )

else:

    st.success(
        "You qualify for Premium Dining Rewards ⭐"
    )

# ----------------------------------------------------
# PAYMENT
# ----------------------------------------------------

st.divider()

st.header("💳 Payment")


payment_method = st.radio(
    "Choose Payment Method",
    [
        "💵 Cash",
        "📱 UPI",
        "💳 Card"
    ],
    horizontal=True
)

# --------------------
# UPI
# --------------------

if payment_method == "📱 UPI":

    st.header("📱 Scan & Pay")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg",
        width=220
    )

    st.info(
        "UPI ID : cafeparadise@ybl"
    )

# --------------------
# CARD PAYMENT
# --------------------

elif payment_method == "💳 Card":

    st.header("💳 Card Details")

    card_number = st.text_input(
        "Card Number",
        placeholder="1234 5678 9012 3456"
    )

    card_name = st.text_input(
        "Name On Card"
    )

    c1, c2 = st.columns(2)

    with c1:

        expiry = st.text_input(
            "Expiry Date",
            placeholder="MM/YY"
        )

    with c2:

        cvv = st.text_input(
            "CVV",
            type="password",
            placeholder="123"
        )

    st.info(
        "Accepted Cards : VISA • Mastercard • RuPay"
    )


# ----------------------------------------------------
# PLACE ORDER
# ----------------------------------------------------

if st.button("Pay & Place Order 🚀"):

    if customer == "":

        st.error(
            "Please enter customer name"
        )

    elif subtotal == 0:

        st.error(
            "Please select at least one item"
        )

    else:

        order_id = random.randint(
            10000,
            99999
        )

        cursor.execute(
            """
            INSERT INTO orders(
            order_id,
            customer_name,
            mobile,
            table_no,
            amount,
            status
            )
            VALUES(?,?,?,?,?,?)
            """,
            (
                order_id,
                customer,
                mobile,
                table_no,
                grand_total,
                "Preparing"
            )
        )

        cursor.execute(
            """
            UPDATE tables
            SET status='Occupied'
            WHERE table_no=?
            """,
            (
                table_no,
            )
        )

        conn.commit()

        st.balloons()

        st.success(
            f"✅ Order #{order_id} Confirmed"
        )

        st.success(
            f"⭐ Reward Points Earned : {points}"
        )

        st.divider()

        st.header("🧾 Invoice")

        st.code(
f"""
================================
        CAFE PARADISE
================================

Order ID : {order_id}

Customer : {customer}

Mobile : {mobile}

Table : {table_no}

Payment Mode : {payment_method}

{order_text}

Subtotal : ₹{subtotal:.2f}

Discount : ₹{discount:.2f}

GST : ₹{gst:.2f}

Grand Total : ₹{grand_total:.2f}

Reward Points : {points}

THANK YOU ❤️

================================
"""
        )

        message = f"""
Cafe Paradise

Order ID : {order_id}

Customer : {customer}

Mobile : {mobile}

Table : {table_no}

{order_text}

Grand Total : ₹{grand_total:.2f}
"""

        whatsapp_url = (
            "https://wa.me/919999999999?text="
            + urllib.parse.quote(message)
        )

        st.link_button(
            "📱 Send Invoice To WhatsApp",
            whatsapp_url
        )

