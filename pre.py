import streamlit as st
st.title("My First App")
name = st.text_input("Waht's your name?")
if name:
    st.write(f"Hello,{name}!")
    
