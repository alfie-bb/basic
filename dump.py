'''def register():
    surname = st.text_input("Enter your surname: ")
    forename = st.text_input("Enter your forname: ")
    st.write("Hi "+forename+"!")
    username = st.text_input("Choose a username: ")
    password = st.text_input("Password: ")
    st.button("Submit")
    with open("users.csv", "a", newline='') as f:
        f.write(username,password)
register() '''
