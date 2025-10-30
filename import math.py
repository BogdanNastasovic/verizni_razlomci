import math
import streamlit as st

# Funkcija za kontinuirani razlomak
def continued_fraction(x, max_terms=10, tol=1e-12):
    """Računa koeficijente kontinuiranog razlomka"""
    a = []
    for _ in range(max_terms):
        integer_part = int(math.floor(x))
        a.append(integer_part)
        frac_part = x - integer_part
        if abs(frac_part) < tol:
            break
        x = 1 / frac_part
    return a

# Naslov aplikacije
st.title("Alat za kontinuirane razlomke")
st.write("Unesi izraz (npr. 2**0.5, math.pi, math.e) i pritisni 'Izračunaj'.")

# Polje za unos izraza
expr = st.text_input("Unesi broj ili izraz:", "2**0.5")

# Dugme za izračunavanje
if st.button("Izračunaj"):
    try:
        x = eval(expr, {"__builtins__": None, "math": math})
    except Exception as e:
        st.error(f"Nevažeći unos: {e}")
    else:
        cf = continued_fraction(x, max_terms=20)
        if len(cf) == 1:
            result = f"[{cf[0]}]"
        else:
            result = f"[{cf[0]}; {', '.join(map(str, cf[1:]))}]"
        st.write("**Kontinuirani razlomak:**")
        st.code(result)

        # Opcionalno: prikaz decimalnog broja za informaciju
        st.write(f"Približno: {x}")
