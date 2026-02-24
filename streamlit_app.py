import streamlit as st
import time

# 1. Konfiguracija s ikonom VRATA
st.set_page_config(page_title="Labirint Istine", page_icon="🚪", layout="centered")

# 2. MOĆAN DIZAJN: Pozadina magle + Matrix Zelena
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url("https://media.giphy.com");
        background-size: cover;
        background-attachment: fixed;
    }
    .serijal-naslov {
        color: #00FF41; 
        font-family: 'Courier New', monospace;
        font-size: 1.5rem;
        text-align: center;
        font-weight: bold;
        text-shadow: 0 0 15px #00FF41;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
    .uvod-animacija {
        color: #FFFFFF;
        font-size: 1.5rem;
        text-align: center;
        padding: 20px;
        text-shadow: 2px 2px 10px #000;
        font-family: 'Garamond', serif;
    }
    .stButton>button {
        background-color: rgba(0, 255, 65, 0.1);
        color: #00FF41;
        border: 1px solid #00FF41;
        width: 100%;
        height: 50px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00FF41; color: black; box-shadow: 0 0 20px #00FF41; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA SESIJE (Pamćenje napretka) ---
if 'korak' not in st.session_state:
    st.session_state.korak = 'uvod'

# Fiksni naslov na vrhu
st.markdown('<p class="serijal-naslov">IZ SERIJALA: U POTRAZI ZA ISTINOM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00FF41; opacity:0.7; font-family:monospace;">By Dominic Chant</p>', unsafe_allow_html=True)

placeholder = st.empty()

# --- SOBA 1: UVOD (Stranica 1 PDF-a) ---
if st.session_state.korak == 'uvod':
    uvodne_recenice = [
        "Nisu svi putevi prema Bogu.",
        "Nisu svi koji pričaju o Bogu od Boga.",
        "Nisu svi prema Božjoj volji.",
        "Nisu sve kamene ustanove od Boga.",
        "Tama je gusta.",
        "Čvršće nego ikad prije..."
    ]
    for recenica in uvodne_recenice:
        placeholder.markdown(f"<div class='uvod-animacija'>{recenica}</div>", unsafe_allow_html=True)
        time.sleep(1.2)
    
    placeholder.markdown("<div class='uvod-animacija'>DRŽI BOŽJU RIJEČ U SRCU I UMU.</div>", unsafe_allow_html=True)
    if st.button("OTVORI VRATA LABIRINTA"):
        st.session_state.korak = 'maske'
        st.rerun()

# --- SOBA 2: MASKE I GRIJEH ---
elif st.session_state.korak == 'maske':
    st.markdown("<div class='uvod-animacija'>Grijeh nije otkrivati lažne puteve i skidati maske koje vode u smrt.</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align:center; color:white;'>Pitanje: Previše ogovaranja stvara mali grijeh, a mali grijeh privuče još koga?</p>", unsafe_allow_html=True)
    
    odgovor = st.text_input("Upiši odgovor...", key="q_grijeh").lower().strip()
    if odgovor == "grijeha":
        st.success("Točno! I srce polako postane prostor tame.")
        if st.button("NASTAVI U DUBINU"):
            st.session_state.korak = 'pobuna'
            st.rerun()

# --- SOBA 3: POBUNA ANĐELA ---
elif st.session_state.korak == 'pobuna':
    st.markdown("<div class='uvod-animacija'>U vrijeme pobune anđela, oni nisu željeli biti poslušni Bogu.</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00FF41;'>Jedan od anđela je u sebi stvarao želju da postane - što?</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    if col1.button("BOG"):
        st.session_state.korak = 'ai_soba'
        st.rerun()
    if col2.button("BUDALA") or col3.button("RADNIK"):
        st.error("Pogrešno! Labirint te vraća natrag.")
        time.sleep(1)
        st.session_state.korak = 'uvod'
        st.rerun()

# --- SOBA 4: AI BUDUĆNOST (Stranica 2 PDF-a) ---
elif st.session_state.korak == 'ai_soba':
    st.markdown("<div class='uvod-animacija'>Tko još uz pale anđele slično razmišlja?</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    if col1.button("ZNAM"):
        st.session_state.ai_izbor = 'znam'
    if col2.button("NE ZNAM"):
        st.session_state.ai_izbor = 'ne_znam'
    
    if st.session_state.get('ai_izbor') == 'ne_znam':
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("DALJE"): st.session_state.korak = 'otac_lazi'; st.rerun()
    elif st.session_state.get('ai_izbor') == 'znam':
        st.write("Pogodi jednu od istina:")
        if st.button("AI & Antena riblja kost!"): st.session_state.korak = 'otac_lazi'; st.rerun()

# --- SOBA 5: OTAC LAŽI ---
elif st.session_state.korak == 'otac_lazi':
    st.markdown("<h2 style='text-align:center; color:white;'>Tko je Otac Laži?</h2>", unsafe_allow_html=True)
    otac = st.text_input("Odgovor:", key="q_sotona").strip().capitalize()
    if otac == "Sotona":
        st.success("Točno. Zašto mislimo da je sve što vidimo istina?")
        if st.button("KLIKNI ZA DALJE"):
            st.session_state.korak = 'pakao'
            st.rerun()

# --- SOBA 6: PAKAO NA ZEMLJI ---
elif st.session_state.korak == 'pakao':
    st.markdown("<div class='uvod-animacija'>Kako na nebu, tako i na zemlji. Ali nitko ne govori...</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#ff0000;'>Kako u paklu, tako i na zemlji. Zašto?</h3>", unsafe_allow_html=True)
    st.info("Otvori oči i vidi da ljubav hladi. Ljudi traže ljubav u hladnim predmetima.")
    if st.button("NOVI TEKST (Duhovna glad)"):
        st.session_state.korak = 'glad'
        st.rerun()

# (Nastavit ćemo dalje s PDF-om kad ovo testiraš)
