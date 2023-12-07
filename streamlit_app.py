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


def main():
    st.title("E-mail Bekérés")

    # Felhasználó nevének bekérése
    name = st.text_input("Kérlek, add meg a neved:")

    # E-mail cím bekérése
    email = st.text_input("Kérlek, add meg az e-mail címed:")

    age = st.number_input("Kérlek, add meg az életkorod:", min_value=0, max_value=300)    

    gender = st.selectbox(
    'nemed',
    ('Ferfi', 'No', 'slampos'))

    # Elküld gomb
    if st.button("Elküld"):
        if name and email:
            save_to_file(name, email, age, gender)
            st.success(f"Köszönjük, {name}! Az e-mail címed: {email}. Az adatokat elmentettük.")
        else:
            st.error("Kérlek, töltsd ki mindkét mezőt!")
                

def save_to_file(name, email, age, gender):
    with open("adatok.txt", "a") as file:
        file.write(f"Név: {name}, E-mail: {email}\n,{age},{gender} ")

if __name__ == "__main__":
    main()

st.write(adatok.txt)
