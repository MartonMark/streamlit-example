import streamlit as st

st.title("Calculator App using Streamlit")

st.write("---")

num1 = st.number_input(label="Enter first number")
num2 = st.number_input(label="Enter second number")
st.write("Operation")
 
operation = st.radio("Select an operation to perform:",("összebaszás", "kibaszás", "szorbaszás", "basztás"))

ans = 0
def calculate():
 if operation == "összebaszás":
  ans = num1 + num2
 elif operation == "kibaszás":
  ans = num1 - num2
 elif operation == "szorbaszás":
  ans = num1 * num2
 elif operation == "divide" and num2!=0:
  ans = num1 / num2
 else:
  st.warning("nem lehet nullával osztani te autista kutya")
  ans = "nincs értelmezve"

st.success(f"Answer = {ans}")
