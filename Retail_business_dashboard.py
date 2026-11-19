import streamlit as st
st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please ente the monthly sales target and selecct the region.")
st.number_input("Enter Monthly Sales Target (in USD):", 
                min_value = 0,
               value=50000)
st.selectbox("Select Region:",
             ["North","East","South","West"])
st.button("Submit")
