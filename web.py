import streamlit as st 
# from main import library
from datetime import date

st.set_page_config(page_title="🏫Library management App",layout="centered")
st.title("Welcome to Library Management")

menu=st.sidebar.selectbox("Choose Action:",["Add member","Delete member","Update member info","Add Book","Delete Book","Update Book","Available Books","Borrow Book","Return book"])

# Handle menu actions
if menu == "Add member":
    st.subheader("Add a New Member")
    name = st.text_input("Name")
    email_input = st.text_input("Enter Email")
    dob=st.date_input("Date of Birth", min_value=date(1900,1,1),max_value=date(2020,1,1))

    if st.button("Submit"):
        st.success(f"Member {name} added successfully!")


