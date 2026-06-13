import streamlit as st
from datetime import date

# Page configuration
st.set_page_config(
    page_title="Cafe Paradise",
    page_icon="☕",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right,#1e130c,#9a8478);
    color:white;
}

.main-title{
    text-align:center;
    font-size:60px;
    color:#FFD700;
    font-weight:bold;
}

.card{
    background-color:rgba(255,255,255,0.15);
    padding:25px;
    border-radius:20px;
}

.offer{
    background-color:#ff5733;
    padding:15px;
    border-radius:15px;
    text-align:center;
    font-size:25px;
    font-weight:bold;
    animation: blink 1s infinite;
}

@keyframes blink{
0%{opacity:1;}
50%{opacity:0.5;}
100%{opacity:1;}
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="main-title">☕ Cafe Paradise</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="offer">🔥 Flat 20% OFF On Birthday Orders 🔥</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Specials
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Today's Orders", 145)

with c2:
    st.metric("Happy Customers", 530)

with c3:
    st.metric("Available Tables", 18)

st.divider()

st.header("👤 Customer Information")

left, right = st.columns(2)

with left:
    customer_name = st.text_input("Customer Name")

    mobile = st.text_input("Mobile Number")

    email = st.text_input("Email Address")

with right:

    dob = st.date_input(
        "Date Of Birth",
        value=date(2000,1,1)
    )

    gender = st.selectbox(
        "Gender",
        ["Male","Female","Other"]
    )

    membership = st.selectbox(
        "Membership",
        [
            "Regular",
            "Silver",
            "Gold",
            "VIP"
        ]
    )

st.divider()

st.header("🍽 Select Table")

table = st.selectbox(
    "Table Number",
    range(1,21)
)

occasion = st.selectbox(
    "Occasion",
    [
        "Normal",
        "Birthday",
        "Anniversary",
        "Family Dinner",
        "Date"
    ]
)

special_note = st.text_area(
    "Special Instructions"
)

if st.button("Proceed To Menu 🚀"):
    st.balloons()

    st.success(
        f"Welcome {customer_name}! Table {table} has been reserved."
    )

st.markdown("""
<style>

.offer{
background:#ff0000;
padding:20px;
border-radius:20px;
font-size:35px;
font-weight:bold;
text-align:center;
animation:blink 1s infinite;
}

@keyframes blink{
50%{opacity:0.3;}
}

</style>

<div class="offer">

🔥 BUY 1 PIZZA GET 1 FREE 🔥

</div>
""",
unsafe_allow_html=True)

points=int(grand_total/100)

st.success(
f"You earned {points} reward points ⭐"
)


coupon=st.text_input(
"Coupon Code"
)

discount=0

if coupon=="SAVE10":
    discount=subtotal*0.10

elif coupon=="WELCOME20":
    discount=subtotal*0.20

elif coupon=="VIP50":
    discount=subtotal*0.50