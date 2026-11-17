import streamlit as st

st.title("Retail Business Dashboard")
st.header("Manager Input section")
st.write("Please enter the monthly sales target and select the region")

sales = st.number_input("Enter Monthly Sales Target(in USD):", value=50000)
option = st.selectbox("Choose your favorite color:",
                      ["North", "South", "East", "West"])

st.button("Submit")
