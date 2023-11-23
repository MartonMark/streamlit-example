import streamlit as st

st.title("Calculator App using Streamlit")
st.write("---")

num1 = st.number_input(label="Enter first number")
num2 = st.number_input(label="Enter second number")
st.write("Operation")

operation = st.radio("Select an operation to perform:", ("összebaszás", "kibaszás", "szorbaszás", "osztás"))

ans = 0

def calculate():
    global ans
    if operation == "összebaszás":
        ans = num1 + num2
    elif operation == "kibaszás":
        ans = num1 - num2
    elif operation == "szorbaszás":
        ans = num1 * num2
    elif operation == "osztás" and num2 != 0:
        ans = num1 / num2
    else:
        st.warning("Nem lehet nullával osztani, te autista kutya")
        ans = "Nincs értelmezve"
    
    st.success(f"Answer = {ans}")

if st.button("Calculate result"):
    calculate()

