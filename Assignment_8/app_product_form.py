import streamlit as st

with st.sidebar:
    st.header("Controls")
    product_name = st.text_input("Product name")
    category = st.sidebar.selectbox(
        "Choose an option",
        ["Electronics", "Fruits", "Grociery", "Cloth"]
    )
    product_price = st.number_input("Product Price")
    add_product = st.button("Add Procuct")
    

if add_product:
    if product_name and product_price and category:
        st.success(f"Product Added Successfully")
        st.success(f"Product name - {product_name}")
        st.success(f"category - {category}")
        st.success(f"Product Price - {product_price}")
    else:
        st.error("Please enter all form Details")
