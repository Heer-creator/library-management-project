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
            user,msg=Library.Add_member(name,email,int(age),password)
            st.success(msg)
            if user:
                st.write(f"Your member ide is: {user['ide']}")
        else:
            st.warning("Fill all fields")

if menu=="Delete member":
    st.subheader("Delete an existing member")
    acc_no=st.text_input("Enter the id ")
    password=st.text_input("Enter password")

    if st.button("Submit"):
        msg=Library.delete_account(acc_no,password)
        if "successfully" in msg:
            st.success(msg)
        else:
            st.warning(msg)

if menu=="Update member info":
    pass

if menu=="Add Book":
    st.subheader("Add New Book")
    name=st.text_input("Enter Book name")
    author=st.text_input("Author name")
    genre=st.text_input("Enter genre of book")

    if st.button("submit"):
        if name and author and genre:
            book,msg=Library.Add_book(name,author,genre)
            if "successfully" in msg:
                st.success(msg)
            if book:
                st.write(f"You book id is {book['ide']}")
                
        else:
            st.warning("Fill all fields")
if menu=="Delete Book":
    st.subheader("Delete Existing book")
    name=st.text_input("Enter name of book you want to delete")
    ide=st.text_input("Enter ide of book")

    if st.button("Submitt"):
        if name and ide:
            msg=Library.delete_book(name,ide)
            if "successfully" in msg:
                st.success(msg)
            else:
                st.warning("msg")  
        else:
            st.warning("Fill All fields")      


