import streamlit as st
import time

# --- POSTAVKE I DIZAJN ---
st.set_page_config(page_title="Labirint Istine", page_icon="👁️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #d3d3d3; }
    .glitch { color: #ff0000; font-size: 2.5rem; text-align: center; font-family: 'Courier New', monospace; text-shadow: 2px 2px #330000; }
    .room-text { font-size: 1.4rem; font-family: 'Georgia', serif; line-height: 1.7; padding: 20px; border-left: 3px solid #444; }
    .stButton>button { width: 100%; background-color: #1a1a1a; color: #ff4b4b; border: 1px solid #444; }
    .stButton>button:hover { background-color: #330000; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA LABIRINTA (Session State) ---
if 'soba' not in st.session_state:
    st.session_state.soba = 'uvod'
if 'bodovi' not in st.session_state:
    st.session_state.bodovi = 0

def kucaj_tekst(tekst):
    placeholder = st.empty()
    prikaz = ""
    for char in tekst:
        prikaz += char
        placeholder.markdown(f"<div class='room-text'>{prikaz}▌</div>", unsafe_allow_html=True)
        time.sleep(0.03)
    placeholder.markdown(f"<div class='room-text'>{prikaz}</div>", unsafe_allow_html=True)

# --- SOBE ---

# 1. UVOD
if st.session_state.soba == 'uvod':
    st.markdown('<p class="glitch">ULAZ U LABIRINT</p>', unsafe_allow_html=True)
    uvod_tekst = "Nisu svi putevi prema Bogu. Tama je gusta. Čvršće nego ikad prije moramo držati Božju riječ."
    kucaj_tekst(uvod_tekst)
    if st.button("KRENI DALJE"):
        st.session_state.soba = 'prvo_pitanje'
        st.rerun()

# 2. PRVO PITANJE (Pobuna anđela)
elif st.session_state.soba == 'prvo_pitanje':
    st.markdown('<p class="glitch">PRVA SOBA</p>', unsafe_allow_html=True)
    kucaj_tekst("Jedan od anđela je u sebi stvarao želju da postane - što?")
    col1, col2, col3 = st.columns(3)
    if col1.button("Bog"):
        st.success("Točno!")
        st.session_state.bodovi += 1
        time.sleep(1)
        st.session_state.soba = 'izbor_soba'
        st.rerun()
    if col2.button("Budala"):
        st.error("Pogrešno!")
        st.session_state.soba = 'izbor_soba'
        st.rerun()
    if col3.button("Radnik"):
        st.error("Pogrešno!")
        st.session_state.soba = 'izbor_soba'
        st.rerun()

# 3. IZBOR LIJEVO ILI DESNO
elif st.session_state.soba == 'izbor_soba':
    st.markdown('<p class="glitch">RASKRIŽJE</p>', unsafe_allow_html=True)
    kucaj_tekst("Pred tobom su dva puta. Izaberi sobu:")
    col1, col2 = st.columns(2)
    if col1.button("GENERACIJE (Lijevo)"):
        st.session_state.soba = 'soba_generacije'
        st.rerun()
    if col2.button("SOTONA NE MIRUJE (Desno)"):
        st.session_state.soba = 'soba_sotona'
        st.rerun()

# 4. SOBA GENERACIJE
elif st.session_state.soba == 'soba_generacije':
    kucaj_tekst("Generacije koje dolaze neće tražiti Boga. Biblija neće postojati.")
    if st.button("IDEM DALJE"):
        st.session_state.soba = 'kraj'
        st.rerun()

# 5. SOBA SOTONA NE MIRUJE
elif st.session_state.soba == 'soba_sotona':
    kucaj_tekst("Sotona lagano zarobljava ljude i udaljava ih od svega što je sveto.")
    if st.button("TRAŽI IZLAZ"):
        st.session_state.soba = 'kraj'
        st.rerun()

# 6. KRAJ (Rezultat)
elif st.session_state.soba == 'kraj':
    if st.session_state.bodovi > 0:
        st.balloons()
        st.markdown('<p class="glitch" style="color:white;">SVJETLO</p>', unsafe_allow_html=True)
        kucaj_tekst("Čestitamo! Izašli ste iz tame. Dobro došli u svjetlo. Uzmi Bibliju.")
    else:
        st.markdown('<p class="glitch">TAMA</p>', unsafe_allow_html=True)
        kucaj_tekst("Labirint je završio, ali tama je u vama. Samo Isus donosi svjetlo.")
    
    if st.button("VRATI SE NA POČETAK"):
        st.session_state.soba = 'uvod'
        st.session_state.bodovi = 0
        st.rerun()
