import streamlit as st
import webbrowser

st.title("First Assignment Innomatics Research Labs")
st.header("Create Streamlit Data App")
st.subheader("Prasad Jadhav")

linkedin = 'https://linkedin.com/in/prasadmjadhav2'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)

github = 'http://github.com/prasadmjadhav2'

if st.button('GitHub'):
    webbrowser.open_new_tab(github)    