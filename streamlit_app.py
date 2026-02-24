import streamlit as st
import time

# 1. KONFIGURACIJA I STIL
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🌀")
st.markdown("<style>.stApp { background-color: #000; color: #00FF41; font-family: monospace; }</style>", unsafe_allow_html=True)

# 2. INICIJALIZACIJA FAZA
if 'faza' not in st.session_state:
    st.session_state.faza = "uvod"
if 'bodovi' not in st.session_state:
    st.session_state.bodovi = 0

# Povezivanje s tajnim sefom
t = st.secrets["tekstovi"]
o = st.secrets["odgovori"]

# 3. LOGIKA LABIRINTA (Prati PDF)

# FAZA: UVOD
if st.session_state.faza == "uvod":
    st.title("🌀 LABIRINT DUHOVNOSTI")
    st.write(t["uvod"])
    st.write(t["upozorenje"])
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = "soba_1"
        st.rerun()

# FAZA: PITANJE 1 (Grijeh)
elif st.session_state.faza == "soba_1":
    st.write(t["q1_pitanje"])
    odg = st.text_input("Tvoj odgovor:", key="q1").strip().lower()
    if st.button("PROVJERI"):
        if odg == o["q1"]:
            st.success("Točno. Srce polako postane prostor tame.")
            st.session_state.faza = "soba_2"
            st.rerun()
        else:
            st.error("Pogrešan trag.")

# FAZA: PITANJE 2 (Pobuna anđela)
elif st.session_state.faza == "soba_2":
    st.write(t["q2_pitanje"])
    choice = st.radio("Odaberi odgovor:", ["Budala", "Fizički radnik", "Bog"])
    if st.button("POTVRDI"):
        if choice.lower() == o["q2"]:
            st.success("Točno. Težnja nagona da čovjek postane bog.")
            st.session_state.faza = "soba_ai"
            st.rerun()
        else:
            st.error("Tama se produbljuje.")

# FAZA: AI I OTAC LAŽI (Stranica 2 i 3 PDF-a)
elif st.session_state.faza == "soba_ai":
    st.write("Tko još uz pale anđele slično razmišlja?")
    c_ai = st.radio("Znaš li?", ["Znam", "Ne znam"])
    if st.button("NASTAVI"):
        if c_ai == "Ne znam":
            st.info(t["ai_istina"])
        st.session_state.faza = "soba_lazi"
        st.rerun()

elif st.session_state.faza == "soba_lazi":
    st.write(t["otac_lazi"])
    lazi_odg = st.text_input("Upiši ime:", key="lazi").strip().lower()
    if st.button("PROVJERI"):
        if lazi_odg == o["q3"]:
            st.success("Točno. On je taj.")
            st.session_state.faza = "izbor_dublje"
            st.rerun()
        else:
            st.error("Laž te zavela.")

# FAZA: ŽELIM / NE ŽELIM (Odbrojavanje 7-0)
elif st.session_state.faza == "izbor_dublje":
    st.write("Želiš li nastaviti dublje kroz duhovne tekstove?")
    if st.button("ŽELIM"):
        st.session_state.faza = "finale"
        st.rerun()
    if st.button("NE ŽELIM"):
        st.warning("Vrata se zatvaraju. Mrak vlada Labirintom.")
        # Odbrojavanje
        p = st.empty()
        for i in range(7, -1, -1):
            p.header(f"Povratak na početak za {i}...")
            time.sleep(1)
        st.session_state.faza = "uvod"
        st.rerun()

# FAZA: FINALE (DA/NE Pitanja)
elif st.session_state.faza == "finale":
    st.subheader("Vrijeme je sveto")
    d1 = st.checkbox("Vjeruješ li u Boga?")
    d2 = st.checkbox("Prihvaćaš li Isusa?")
    d3 = st.checkbox("Sotona je lažac?")
    
    if st.button("IZLAZ IZ LABIRINTA"):
        # Zbrajanje pozitivnih odgovora
        if d1 and d2 and d3:
            st.balloons()
            st.success(t["izlaz_svjetlo"])
            st.info("🏆 DOBILI STE ZNAČKU VJERNIKA")
        else:
            st.warning(t["izlaz_tama"])
        
        time.sleep(5)
        st.session_state.faza = "uvod"
        st.rerun()
