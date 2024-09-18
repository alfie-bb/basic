import streamlit as st
import pandas as pd
st.title("🎈 Alfie's Shack")
st.write("Enter your name when prompted")

# name = st.text_input("Please enter your name ")



def login():
    st.title("Login")
    st.write("This app allows you to add and remove users")
    st.write("Please try it out, remember to click Check User")
    st.write("username = Dave")
    st.write("password = p1")
    enterusername = st.text_input("Please enter username to update system")
    enterpassword = st.text_input("Please enter password", type="password")
    if st.button("Check User"):
        file = open("userlist.csv", "r", encoding="utf-8-sig")
        user_found = False
        for line in file:
            lines = line.strip().split(",")

            username = lines[0]
            password = lines[1]
            if enterusername == username and enterpassword == password:
                with open("userlog.csv", "a", newline='') as file:
                    file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")                
                    st.session_state.logged_in = True
                    st.success("Login Successful")
                    user_found = True
                    break
        if not user_found:
            st.error("Invalid username or password")
        file.close()
login()
 # f.write("Username: "+username+"\nForename: "+forename+"\nSurname: "+surname+"\nPassword: "+password+"\n\n")