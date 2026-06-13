import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Payment",
    page_icon="💳",
    layout="wide"
)

# Background
st.markdown("""
<style>

.stApp{
background:linear-gradient(to right,#141e30,#243b55);
color:white;
}

.card{
background-color:rgba(255,255,255,0.1);
padding:20px;
border-radius:20px;
}

</style>
""",unsafe_allow_html=True)

st.title("💳 Payment Gateway")

# Customer Details

col1,col2=st.columns(2)

with col1:

    customer_name=st.text_input(
        "Customer Name",
        "Sudeep Basu"
    )

    mobile=st.text_input(
        "Mobile Number"
    )

with col2:

    table_no=st.selectbox(
        "Table Number",
        range(1,21)
    )

    payment_mode=st.selectbox(
        "Payment Method",
        [
            "Cash",
            "UPI",
            "Credit Card",
            "Debit Card"
        ]
    )

st.divider()

st.header("💰 Bill Summary")

subtotal=1250
gst=subtotal*0.05
service_charge=30

grand_total=subtotal+gst+service_charge

c1,c2,c3=st.columns(3)

with c1:
    st.metric(
        "Subtotal",
        f"₹{subtotal}"
    )

with c2:
    st.metric(
        "GST",
        f"₹{gst:.2f}"
    )

with c3:
    st.metric(
        "Grand Total",
        f"₹{grand_total:.2f}"
    )

st.divider()

# UPI

if payment_mode=="UPI":

    st.header("📱 Scan & Pay")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg",
        width=250
    )

    st.info(
        "UPI ID : 9038345908@ybl"
    )

st.divider()

# Order

if st.button("Confirm Order 🚀"):

    order_id=random.randint(
        10000,
        99999
    )

    st.balloons()

    st.success(
        f"Order #{order_id} Confirmed!"
    )

    st.header("📦 Order Status")

    progress=st.progress(0)

    status=st.empty()

    status.info("Preparing Order")

    progress.progress(25)

    status.info("Cooking")

    progress.progress(50)

    status.info("Ready")

    progress.progress(75)

    status.success("Delivered")

    progress.progress(100)

    st.divider()

    st.header("🧾 Invoice")

    st.code(
f"""
================================
        CAFE PARADISE
================================

Order ID : {order_id}

Date :
{datetime.now()}

Customer :
{customer_name}

Mobile :
{mobile}

Table :
{table_no}

Subtotal :
₹{subtotal}

GST :
₹{gst:.2f}

Service Charge :
₹{service_charge}

Grand Total :
₹{grand_total:.2f}

THANK YOU ❤️
================================
"""
)