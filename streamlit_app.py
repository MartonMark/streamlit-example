import streamlit as st

st.title("számológép")
st.write("---")

number1 = st.number_input(label = "szam 1")
number2 = st.number_input(label = "szam 2")

st.write("anyukad szuz?")
st.radio("muveletek",("osszeadas", "kivonas", "szorzas", "osztas"))

ans = 0

def calculator():
  if muveletek == "osszeadas":
    ans = number1 + number2
  elif muveletek == "kivonas":
    ans = number1 - number2
  elif muveletek == "szorzas":
    ans = number1 * number2
  elif muveletek == "osztas" and number2!=0:
    ans = number1 / number2 
  else:
    st.warning("XDDDDD annyira siralmas vagy nemtudok mit mondani")
    ans = "szar"


  st.succes(f"valasz = {ans}")

if st.button("kalkulalas"):
  calculate()
    
    


