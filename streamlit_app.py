import streamlit as st
import pandas as pd
st.title("🎈 Alfie's Shack")
st.write("Enter your name when prompted")

# name = st.text_input("Please enter your name ")


def register():
    surname = st.text_input("Enter your surname: ")
    forename = st.text_input("Enter your forname: ")
    st.write("Hi "+forename+"!")
    username = st.text_input("Choose a username: ")
    password = st.text_input("Password: ")
    st.button("Submit")
    f = open("users.csv", "a", "utf-8-sig")
    f.write("Username: "+username+"\nForename: "+forename+"\nSurname: "+surname+"\nPassword: "+password+"\n\n")
    f.close()

register()