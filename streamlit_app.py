import streamlit as st

st.title("számológép")
st.write("---")

number1 = st.number_input(label = "szam 1")
number2 = st.number_input(label = "szam 2")

st.write("anyukad szuz?")
st.radio("muveletek",("osszeadas", "kivonas", "szorzas", "osztas")
