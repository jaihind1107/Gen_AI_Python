import streamlit as st

st.title("Welcome to Streamlit !!!")
your_name = st.text_input('Enter Your Name')

if st.button("Greet me"):
    st.write("Hello ! ", your_name)