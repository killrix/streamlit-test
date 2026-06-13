import streamlit as st

st.set_page_config(
    page_title="Admin Login",
    page_icon="🔐",
    layout="centered"
)

# Initialize session state
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

st.title("🔐 Cafe Paradise Admin Login")

username = st.text_input("Username")
password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "admin" and password == "1234":

        st.session_state.admin_logged_in = True

        st.success("✅ Login Successful")

        st.balloons()

    else:

        st.error("❌ Invalid Username or Password")

if st.session_state.admin_logged_in:

    st.divider()

    st.success("Welcome Admin 👨‍💼")

    col1, col2 = st.columns(2)

    with col1:

        st.page_link(
            "pages/4_Admin_Dashboard.py",
            label="📈 Admin Dashboard"
        )

    with col2:

        st.page_link(
            "pages/8_Kitchen_Display.py",
            label="👨‍🍳 Kitchen Display"
        )

    if st.button("Logout"):

        st.session_state.admin_logged_in = False

        st.rerun()