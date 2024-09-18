import streamlit as st

st.title("🎈 Alfie's Shack")
st.write("Enter your name when prompted")

name = st.text_input("Please enter yor name ")
st.write("Hi",name)
