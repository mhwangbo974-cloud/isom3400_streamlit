import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Business Sales Dashboard")
st.write("Analyze monthly sales data interactively!")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = np.random.randint(5000, 20000, size=12)
expenses = np.random.randint(3000, 15000, size=12)

data = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Expenses": expenses
})
