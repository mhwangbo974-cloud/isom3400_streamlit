"""
In-Class Exercise 5 - Streamlit Retail Business Dashboard
Course: ISOM3400 2026 Fall
Assessment: In-Class Exercise 5 (Effort ICE - a genuine attempt counts even if imperfect)
Weight: 2%
Duration: 30 minutes
Due: Thursday 19 November 2026 (lecture day)
Environment: VS Code / local Python

Student information (fill in):
Name: Min HWANGBO
Student ID: 20898647
Email: mhwangbo@connect.ust.hk

How to use:
1. Fill in your name / ID / email above.
2. In this folder, install packages:  pip install -r requirements.txt
3. Complete the fill-in-the-blank lines below so the app matches the expected UI
   (see Retail_Business_Dashboard.png). Use only the allowed Streamlit calls
   shown in streamlit_functions.png.
4. Run the app:  streamlit run app.py
5. Click Submit and check the summary (try the default target, then a target
   above 100000 for the Challenge).
6. Zip ONLY app.py and requirements.txt. The zip filename must include your
   Student ID, for example {StudentID}_InclassEx5.zip.
7. Submit the zip on Canvas, or email both the course instructor and the TA.

Scope:
- Allowed Streamlit functions only: st.title, st.header, st.write,
  st.number_input, st.selectbox, st.button, st.success.
- Do NOT wrap the program in functions (no def, no main()). All code stays at
  top level.
- Do not add pandas, matplotlib, numpy, or other libraries.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Retail Business Dashboard
# ---------------------------------------------------------------------------
# A retail manager enters a monthly sales target, selects a region, then
# clicks Submit to see a summary.
# Replace each ______ with the missing code. Do not pre-write answers in
# functions — keep everything at top level.

# Blank A: page title (match the screenshot).
st.title("Retail Business Dashboard")

# Blank B: section header (match the screenshot).
st.header("Manager Input Section")

# Blank C: short instruction under the header (match the screenshot).
st.write("Pleasee enter the monthly sales target and select a region.")

# Blank D: monthly sales target (USD). Default 50000. Minimum 0. (match the screenshot)
# Do not set a maximum (the Challenge uses a target above 50000).
sales_target = st.number_input("Enter Monthly Sales Target (in USD):", value=50000, min_value=0)

# Blank E: region dropdown (match the options shown in the document).
region = st.selectbox("Select Region:", ["North", "South", "East", "West"])

# Blank F: Submit button, then show the entered values and a success message (match the screenshot).
if st.button("Submit"):
    st.write(f"Sales Target: ${sales_target}")
    st.write(f"Region: {region}")
    st.success("Dashboard updated successfully!")

    # Challenge: if the sales target is greater than 100000, show an extra message (match the screenshot).
    if sales_target > 100000:
        st.write("Great! You have set an ambitious target!")
        
