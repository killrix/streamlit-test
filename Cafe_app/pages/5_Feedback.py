import streamlit as st
import sqlite3

st.title("⭐ Customer Feedback")

conn = sqlite3.connect(
    "cafe_database.db",
    check_same_thread=False
)

name = st.text_input(
    "Customer Name"
)

rating = st.slider(
    "Rating",
    1,
    5
)

comments = st.text_area(
    "Comments"
)

if st.button("Submit Feedback"):

    conn.execute(
        """
        INSERT INTO feedback
        VALUES(?,?,?)
        """,
        (
            name,
            rating,
            comments
        )
    )

    conn.commit()

    st.balloons()

    st.success(
        "Feedback Submitted!"
    )