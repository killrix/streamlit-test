import streamlit as st
from datetime import date

# Page Config
st.set_page_config(
    page_title="Cafe Paradise",
    page_icon="☕",
    layout="wide"
)

# Background
st.markdown("""
<style>

.stApp{
background: linear-gradient(to right,#2c3e50,#4ca1af);
color:white;
}

.title{
text-align:center;
font-size:50px;
font-weight:bold;
color:#FFD700;
}

.box{
background-color:rgba(255,255,255,0.15);
padding:20px;
border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">☕ Cafe Paradise</p>', unsafe_allow_html=True)

# Customer Details
st.header("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input("Customer Name")

    mobile = st.text_input("Mobile Number")

with col2:
    dob = st.date_input(
        "Date of Birth",
        value=date(2000,1,1)
    )

    table_no = st.selectbox(
        "Table Number",
        range(1,21)
    )

st.divider()

# Menu
st.header("🍽 Menu")

menu = {
    "Coffee":120,
    "Cold Coffee":180,
    "Burger":150,
    "Pizza":300,
    "French Fries":100,
    "Sandwich":130,
    "Pasta":220,
    "Mojito":140
}

order_items = {}

for item, price in menu.items():

    c1, c2 = st.columns([3,1])

    with c1:
        st.write(f"**{item}** - ₹{price}")

    with c2:
        qty = st.number_input(
            f"{item}",
            min_value=0,
            max_value=20,
            key=item
        )

    if qty > 0:
        order_items[item] = qty

st.divider()

# Bill Calculation
total = 0

for item, qty in order_items.items():
    total += menu[item] * qty

st.subheader("💰 Total Bill")

st.success(f"₹ {total}")

# Place Order
if st.button("Place Order 🚀"):

    st.balloons()

    st.success("Order Placed Successfully!")

    with st.expander("📋 Order Details"):

        st.write("### Customer Information")

        st.write("Name:", customer_name)
        st.write("Mobile:", mobile)
        st.write("DOB:", dob)
        st.write("Table Number:", table_no)

        st.write("### Ordered Items")

        for item, qty in order_items.items():
            st.write(
                f"{item} × {qty} = ₹{menu[item]*qty}"
            )

        st.write("## Grand Total = ₹", total)