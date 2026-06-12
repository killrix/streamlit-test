import streamlit as st

chutiya = st.slider("Select a value for yourself:", 0, 100, 10)
if chutiya > 40:
    st.markdown(
    f"""
    <style>
    @keyframes flash {{
        0% {{ opacity: 1; }}
        50% {{ opacity: 0.2; }}
        100% {{ opacity: 1; }}
    }}

    .warning-box {{
        background-color: #ff4444;
        color: white;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        padding: 40px;
        border-radius: 20px;
        animation: flash 1s infinite;
    }}
    </style>

    <div class="warning-box">
        ⚠️ You are {chutiya}% madarchod ⚠️
    </div>
    """,
    unsafe_allow_html=True
)
    st.snow()
    st.balloons()

