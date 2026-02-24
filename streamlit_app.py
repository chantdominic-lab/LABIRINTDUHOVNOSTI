import streamlit as st
import time

# 1. MRAČNI STIL I FAVICON
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🌀")
st.markdown("<style>.stApp { background-color: #000; color: #00FF41; font-family: monospace; }</style>", unsafe_allow_html=True)

# 2. INICIJALIZACIJA (Pamćenje napretka)
if 'faza' not in st.session_state:
    st.session_state.faza = "uvod"

t = st.secrets["tekstovi"]
o = st.secrets["odgovori"]

# 3. LOGIKA LABIRINTA (Prati tvoj PDF od 1. do 6. stranice)

if st.session_state.faza == "uvod":
    st.title("🌀 LABIRINT DUHOVNOSTI")
    st.write(t["uvod"])
    st.write(t["upozorenje"])
    if st.button("UĐI"):
        st.session_state.faza = "q1"
        st.rerun()

elif st.session_state.faza == "q1":
    st.write(t["q1"])
    ans1 = st.text_input("Tvoj odgovor:", key="ans1").strip().lower()
    if st.button("PROVJERI"):
        if ans1 == o["q1"]:
            st.success("Točno. Srce postaje prostor tame.")
            st.session_state.faza = "q2"
            st.rerun()
        else: st.error("Pogrešan trag.")

elif st.session_state.faza == "q2":
    st.write(t["q2"])
    izbor = st.radio("Odaberi:", ["Budala", "Fizički radnik", "Bog"])
    if st.button("POTVRDI"):
        if izbor.lower() == o["q2"]:
            st.success("Točno. Težnja nagona da čovjek postane bog.")
            st.session_state.faza = "soba_ai"
            st.rerun()
        else: st.error("Sjene su te progutale.")

elif st.session_state.faza == "soba_ai":
    st.write("Tko još uz pale anđele slično razmišlja?")
    c_ai = st.radio("Znaš li?", ["Znam", "Ne znam"])
    if st.button("NASTAVI"):
        if c_ai == "Ne znam":
            st.info(t["ai_info"])
        st.session_state.faza = "otac_lazi"
        st.rerun()

elif st.session_state.faza == "otac_lazi":
    st.write(t["otac_lazi"])
    ans3 = st.text_input("Upiši ime:", key="ans3").strip().lower()
    if st.button("PROVJERI"):
        if ans3 == o["q3"]:
            st.success("Točno. On je Otac Laži.")
            st.session_state.faza = "izbor"
            st.rerun()
        else: st.error("Laž te zaslijepila.")

elif st.session_state.faza == "izbor":
    st.write("Želiš li nastaviti dublje kroz duhovne tekstove?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ŽELIM!"):
            st.session_state.faza = "finale"
            st.rerun()
    with col2:
        if st.button("NE ŽELIM!"):
            st.warning("Vrata se zatvaraju. Mrak vlada.")
            p = st.empty()
            for i in range(7, -1, -1):
                p.header(f"Povratak za {i}...")
                time.sleep(1)
            st.session_state.faza = "uvod"
            st.rerun()

elif st.session_state.faza == "finale":
    st.subheader("Vrijeme je sveto")
    st.write("Označi svoje odgovore pred Bogom:")
    d1 = st.checkbox("Biblija je pisana Božja riječ?")
    d2 = st.checkbox("Sotona je Lažac?")
    d3 = st.checkbox("Prihvaćaš li Isusa za spasitelja?")
    
    if st.button("IZLAZ"):
        if d1 and d2 and d3:
            st.balloons()
            st.success(t["izlaz_svjetlo"])
        else:
            st.error(t["izlaz_tama"])
        time.sleep(10)
        st.session_state.faza = "uvod"
        st.rerun()
