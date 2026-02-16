import streamlit as st

st.title("Simple Sales Dashboard")

sales = {
    "January": 200,
    "February": 300,
    "March": 250,
    "April": 270
}

month = st.selectbox(
    "Choose a month",
    list(sales.keys())
)

st.write(f"Sales in {month}: {sales[month]}")
st.bar_chart(list(sales.values()))