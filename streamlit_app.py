import streamlit as st

st.title("bey new app")
st.write(
    "stecu stecu something happens and I'm head over")
st.image("IMG-20250509-WA0298(1).jpg",width=200)

st.title("aplikasi mewah")
st.header("aplikasi untuk mengecek tabungan")
angka = st.number_input("Tulislah sebuah nominal:", value=0, step=1)
if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
