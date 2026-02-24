import streamlit as st
import time

# 1. MRAČNI STIL LABIRINTA
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🌀")
st.markdown("""
<style>
    .stApp { background-color: #000; color: #00FF41; font-family: monospace; }
    .stButton>button { background-color: #111; color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    input { color: #FFFFFF !important; background-color: #111 !important; border: 1px solid #00FF41 !important; }
</style>
""", unsafe_allow_html=True)

# 2. LOGIKA PROGRESA (Session State)
if 'faza' not in st.session_state:
    st.session_state.faza = "uvod"

# 3. DOHVAĆANJE TAJNIH TEKSTOVA
# Sav tekst iz PDF-a bit će u st.secrets["tekstovi"]
t = st.secrets.get("tekstovi", {})

# 4. MEHANIKA LABIRINTA (Primjer za prvu sobu)
if st.session_state.faza == "uvod":
    st.markdown(f"### {t.get('uvod_naslov', 'Uvod')}")
    st.write(t.get('uvod_tekst', 'Tama je gusta...'))
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = "pitanje_1"
        st.rerun()

elif st.session_state.faza == "pitanje_1":
    st.write(t.get('q1_tekst', 'Mali grijeh privuče još koga?'))
    odgovor = st.text_input("Tvoj odgovor:", key="input_q1").strip().lower()
    if st.button("PROVJERI"):
        if odgovor == st.secrets["odgovori"]["q1"]:
            st.success("Točno. Srce polako postane prostor tame.")
            st.session_state.faza = "pitanje_2"
            st.rerun()
        else:
            st.error("Pogrešan trag.")
