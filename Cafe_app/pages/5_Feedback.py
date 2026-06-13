import streamlit as st
from streamlit_feedback import streamlit_feedback

st.set_page_config(
    page_title="Customer Feedback",
    page_icon="⭐"
)

st.title("⭐ Customer Experience")

st.subheader("🍽 Food Quality")

food = streamlit_feedback(
    feedback_type="faces",
    key="food"
)

st.subheader("🪑 Comfort & Ambience")

comfort = streamlit_feedback(
    feedback_type="faces",
    key="comfort"
)

st.subheader("👨‍🍳 Staff Behavior")

staff = streamlit_feedback(
    feedback_type="faces",
    key="staff"
)

comments = st.text_area(
    "Additional Comments"
)

if st.button("Submit Feedback ❤️"):

    st.balloons()

    st.success(
        "Thank you for your valuable feedback!"
    )