import streamlit as st

price = st.text_input('Enter Price !! ')
percent = st.slider("Select a discount percent-", 0, 50, 0)

if st.button("Calculate Price"):
    try:
        price = float(price)
        final_price = price - (price * percent / 100)
        st.success(f"Original Price - {price}")
        st.success(f"Discount - {percent}%")
        st.success(f"Final Price - {final_price}")
    except ValueError:
        st.error("Please enter a valid numeric price")
