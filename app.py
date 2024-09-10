import streamlit as st

code="""def square(x):
    return x**2"""
st.code(code,language='python')