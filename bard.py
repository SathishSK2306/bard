import streamlit as st
from bardapi import Bard

token = "ZQhMrPIArXrtwqH6CTL4NN-OgBPqYlBSZWVueSo8rhtcuRFTjxqCp7j4xXxmpmHDsav6lg."


st.write("""
# BARD CHAT BOT
         """)
data = st.text_input("Enter Your Query")

if st.button("let's start"):
    bard = Bard(token=token)
    finalanswer = bard.get_answer(data)['content']
    st.write(finalanswer)
