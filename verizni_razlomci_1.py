import math
import streamlit as st

# =========================
# Funkcija za kontinuirani razlomak
# =========================
def continued_fraction(x, max_terms=20, tol=1e-12):
    """
    Vraca listu koeficijenata kontinuiranog razlomka za x
    """
    a = []
    for _ in range(max_terms):
        integer_part = int(math.floor(x))
        a.append(integer_part)
        frac_part = x - integer_part
        if abs(frac_part) < tol:
            break
        x = 1 / frac_part
    return a

# =========================
# Streamlit UI
# =========================
st.title("Alat za kontinuirane razlomke")
st.write("Uputstvo: Koristite ** za stepen umesto ^. Na primer, unesite `2**(1/2)` za kvadratni koren iz 2" )
st.write("Mozete koristiti funkcije iz math modula, npr. `math.e`, `math.pi`, `math.sqrt` `math.sin(math.pi/4)` itd.")
# Text input for user
user_input = st.text_input("Unesi broj ili izraz:", "2**0.5")

# Button to calculate
if st.button("Izračunaj"):
    try:
        # Eval samo sa math modulom, bez drugih ugrađenih funkcija
        x = eval(user_input, {"__builtins__": None, "math": math})
        cf = continued_fraction(x)

        # Ispis rezultata
        if len(cf) == 1:
            st.write(f"Kontinuirani razlomak: [{cf[0]}]")
        else:
            st.write(f"Kontinuirani razlomak: [{cf[0]}; {', '.join(map(str, cf[1:]))}]")

    except Exception as e:
        st.error(f"Nevažeći unos: {e}")
