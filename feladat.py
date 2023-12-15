import streamlit as st
st.title("Programozás feladat")
szoveg = st.text_input("")
# 1. Csupa nagy- és kisbetű
st.write(szoveg.upper())
st.write(szoveg.lower())

# 2. Szavak száma
szavak = szoveg.split(" ")
darab = 0
for i in szavak:
    if i == "":
        continue
    else:
        darab += 1

st.write(f"Szavak száma: {darab}")

#3. Leggyakoribb szó
szavak_szama = {}
for i in szavak:
    if i in szavak_szama:
        szavak_szama[i] += 1
    else:
        szavak_szama[i] = 1
st.write(f"Leggyakoribb szó: {max(szavak_szama, key=szavak_szama.get)}")

#4. Leggyakoribb betű
betuk_szama = {}
for i in szoveg:
    if i in betuk_szama:
        betuk_szama[i] += 1
    else:
        betuk_szama[i] = 1
if True:
    try: st.write(f"Leggyakoribb betű: {max(betuk_szama)}")
    except: st.write("")

#5. Betűk száma
betuk_szama = 0
betuk = szoveg.strip()

for i in betuk:
    betuk_szama += 1
st.write(f"Betűk száma: {betuk_szama}")
