import streamlit as st 
from main import Library
from datetime import date

st.set_page_config(page_title="🏫Library management App",layout="centered")
st.title("Welcome to Library Management")

menu=st.sidebar.selectbox("Choose Action:",["Add member","Delete member","Update member info","Add Book","Delete Book","Update Book","Available Books","Borrow Book","Return book"])

# Handle menu actions
if menu == "Add member":
    st.subheader("Add a New Member")
    name = st.text_input("Name")
    email = st.text_input("Enter Email")
    age=st.number_input("Enter your age",min_value=1,step=1)
    password=st.text_input("Create a strong password",type="password")


    if st.button("Submit"):
        if name and email and age and password:
            lib=Library()
            user,msg=lib.Add_member(name,email,int(age),password)
            st.success(msg)
            if user:
                st.write(f"Your member ide is: {user['ide']}")
        else:
            st.warning("Fill all fields")
        
        


