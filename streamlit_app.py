import streamlit as st

st.title("szamologep")
st.write("---")

number1 = st.number_input(label = "szam 1")
number2 = st.number_input(label = "szam 2")

st.write("operation")
operation = st.radio("muveletek",("osszeadas", "kivonas", "szorzas", "osztas"))

ans = 0

def calculate():
  if operation == "osszeadas":
    ans = number1 + number2
  elif operation == "kivonas":
    ans = number1 - number2
  elif operation == "szorzas":
    ans = number1 * number2
  elif operation == "osztas" and number2!=0:
    ans = number1 / number2 
  else:
    st.warning("XDDDDD annyira siralmas vagy nemtudok mit mondani")
    ans = "szar"


  st.success(f"Answer = {ans}")

if st.button("calculator"):
  calculate()






st.slider(min_value=0, max_value=5,)
