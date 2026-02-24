import streamlit as st
import time

# 1. Konfiguracija
st.set_page_config(page_title="Labirint Istine", page_icon="🚪", layout="centered")

# 2. MOĆAN DIZAJN: Bez plave boje, samo Zelena, Crvena i Siva
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)), 
                    url("https://media.giphy.com");
        background-size: cover;
    }
    .serijal-naslov {
        color: #00FF41; 
        font-family: 'Courier New', monospace;
        font-size: 1.5rem;
        text-align: center;
        font-weight: bold;
        text-shadow: 0 0 15px #00FF41;
    }
    .glavni-tekst {
        color: #d3d3d3; /* Svijetlo siva za čitljivost */
        font-size: 1.4rem;
        text-align: center;
        padding: 20px;
        font-family: 'Garamond', serif;
    }
    .pakao-tekst {
        color: #ff4b4b; /* Krvavo crvena */
        font-size: 1.6rem;
        font-weight: bold;
        text-align: center;
    }
    .stButton>button {
        background-color: rgba(0, 255, 65, 0.05);
        color: #00FF41;
        border: 1px solid #00FF41;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00FF41;
        color: black;
    }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA SESIJE ---
if 'korak' not in st.session_state:
    st.session_state.korak = 'uvod'

# Naslov na vrhu
st.markdown('<p class="serijal-naslov">IZ SERIJALA: U POTRAZI ZA ISTINOM</p>', unsafe_allow_html=True)

# --- FUNKCIJA ZA FIKSNI TEKST (BEZ ŠTOPANJA) ---
def prikazi_tekst(tekst, stil='glavni-tekst'):
    st.markdown(f"<div class='{stil}'>{tekst}</div>", unsafe_allow_html=True)

# --- SOBE ---

if st.session_state.korak == 'uvod':
    prikazi_tekst("Nisu svi putevi prema Bogu. Nisu svi koji pričaju o Bogu od Boga. Tama je gusta.")
    if st.button("OTVORI VRATA"):
        st.session_state.korak = 'maske'
        st.rerun()

elif st.session_state.korak == 'maske':
    prikazi_tekst("Grijeh nije otkrivati lažne puteve i skidati maske koje vode u smrt.")
    st.write("---")
    prikazi_tekst("Previše ogovaranja stvara mali grijeh, a mali grijeh privuče još koga?", 'glavni-tekst')
    odgovor = st.text_input("Odgovor:", key="q1").lower().strip()
    if odgovor == "grijeha":
        st.success("Točno. Srce polako postane prostor tame.")
        if st.button("IDEM DALJE"):
            st.session_state.korak = 'pobuna'
            st.rerun()

elif st.session_state.korak == 'pobuna':
    prikazi_tekst("Jedan od anđela je u sebi stvarao želju da postane - što?")
    c1, c2, c3 = st.columns(3)
    if c1.button("BOG"):
        st.session_state.korak = 'ai_soba'
        st.rerun()
    if c2.button("BUDALA") or c3.button("RADNIK"):
        st.error("Pogrešno.")

elif st.session_state.korak == 'ai_soba':
    prikazi_tekst("Tko još uz pale anđele slično razmišlja?")
    if st.button("ZNAM"): st.session_state.ai_izbor = 'z'
    if st.button("NE ZNAM"): st.session_state.ai_izbor = 'nz'
    
    if st.session_state.get('ai_izbor') == 'nz':
        prikazi_tekst("AI će razviti svijest i ideju da postane bog.")
        if st.button("DALJE"): st.session_state.korak = 'otac_lazi'; st.rerun()
    elif st.session_state.get('ai_izbor') == 'z':
        if st.button("AI & Antena riblja kost!"): st.session_state.korak = 'otac_lazi'; st.rerun()

elif st.session_state.korak == 'otac_lazi':
    prikazi_tekst("Tko je Otac Laži?", 'pakao-tekst')
    otac = st.text_input("Upiši ime:", key="q2").strip().capitalize()
    if otac == "Sotona":
        if st.button("PROĐI KROZ VRATA"):
            st.session_state.korak = 'pakao'
            st.rerun()

elif st.session_state.korak == 'pakao':
    prikazi_tekst("Naučeni smo: 'Kako na nebu, tako i na zemlji.'", 'glavni-tekst')
    prikazi_tekst("Ali može biti i: 'Kako u paklu, tako i na zemlji.'", 'pakao-tekst')
    prikazi_tekst("Ljubav hladi. Ljudi traže ljubav u hladnim predmetima.", 'glavni-tekst')
    if st.button("IDEM DALJE (Duhovna glad)"):
        # Ovdje nastavljamo s 3. stranicom PDF-a
        st.write("Slijedi: Bez Boga smo... (Mrtvi)")
