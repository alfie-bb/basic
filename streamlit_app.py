import streamlit as st

st.title("🎈 Alfie's Shack")
st.write("Enter your name when prompted")

name = st.text_input("Please enter your name ")


def register():
    surname = st.text_input("Enter your surname: ")
    forename = st.text_input("Enter your forname: ")
    st.write("Hi"+forename+"!")
    username = st.text_input("Choose a username: ")
    password = st.text_input("Password: ")
    f = open("users.txt", "a")
    f.write("Username:",username,"\nForename:",forename,"\nSurname:",surname,"\nPassword:",password,"\n\n")
    f.close()