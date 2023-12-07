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


option = st.selectbox(
    'nemed',
    ('Ferfi', 'No'))




xdd = st.slider("valassz mennyi kukit szeretnel a seggede", 0,10)
st.write(xdd**2)


import streamlit as st

email = st.text_input('add ma meg az emailod legyszike')
nev = st.text_input('add ma meg az neved legyszike')
xddddfdddddd = st.slider("eletkorod", 1,100)



