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






xdd = st.slider("valassz mennyi kukit szeretnel a seggede", 0,10)
st.write(xdd**2)


with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
