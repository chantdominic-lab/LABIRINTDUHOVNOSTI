import streamlit as st
import time

# 1. Konfiguracija
st.set_page_config(page_title="Labirint Istine", page_icon="🚪", layout="centered")

# 2. Ultra zeleni dizajn s maglom
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
    }
    .uvod-animacija {
        color: #FFFFFF;
        font-size: 1.5rem;
        text-align: center;
        padding: 20px;
        text-shadow: 2px 2px 10px #000;
    }
    .stButton>button {
        background-color: rgba(0, 255, 65, 0.1);
        color: #00FF41;
        border: 1px solid #00FF41;
        width: 100%;
        transition: 0.3s;
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
if 'odgovor_grijeh' not in st.session_state:
    st.session_state.odgovor_grijeh = False

# 3. Zeleni fiksni naslov
st.markdown('<p class="serijal-naslov">IZ SERIJALA: U POTRAZI ZA ISTINOM</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00FF41; opacity:0.7;">By Dominic Chant</p>', unsafe_allow_html=True)

placeholder = st.empty()

# --- SOBA: UVOD ---
if st.session_state.korak == 'uvod':
    uvodne_recenice = [
        "Nisu svi putevi prema Bogu.",
        "Nisu svi koji pričaju o Bogu od Boga.",
        "Nisu svi prema Božjoj volji.",
        "Nisu sve kamene ustanove od Boga.",
        "Tama je gusta."
    ]
    for recenica in uvodne_recenice:
        placeholder.markdown(f"<div class='uvod-animacija'>{recenica}</div>", unsafe_allow_html=True)
        time.sleep(1.2)
    
    if st.button("OTVORI VRATA"):
        st.session_state.korak = 'maske'
        st.rerun()

# --- SOBA: MASKE I GRIJEH ---
elif st.session_state.korak == 'maske':
    st.markdown("<div class='uvod-animacija'>Grijeh nije otkrivati lažne puteve i skidati maske...</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='text-align:center; color:white;'>Pitanje: Previše ogovaranja stvara mali grijeh, a mali grijeh privuče još koga?</p>", unsafe_allow_html=True)
    
    odgovor = st.text_input("Upiši točan odgovor...", key="input_grijeh").lower().strip()
    
    # Čim unese "grijeha", otključava se gumb za dalje
    if odgovor == "grijeha":
        st.session_state.odgovor_grijeh = True
        st.success("Točno! I srce polako postane prostor tame.")
        if st.button("NASTAVI U DUBINU"):
            st.session_state.korak = 'pobuna'
            st.rerun()
    elif odgovor != "":
        st.error("Tama se širi... Pokušaj ponovno.")

# --- SOBA: POBUNA ANĐELA (Iz PDF-a stranica 1) ---
elif st.session_state.korak == 'pobuna':
    st.markdown("<div class='uvod-animacija'>U vrijeme pobune anđela, oni nisu željeli biti poslušni Bogu.</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#00FF41;'>Jedan od anđela je u sebi stvarao želju da postane - što?</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # Odgovori iz tvog PDF-a
    if col1.button("BOG"):
        st.success("Točan odgovor!")
        time.sleep(1)
        st.session_state.korak = 'buducnost_ai' # Prelazimo na stranicu 2 PDF-a
        st.rerun()
        
    if col2.button("BUDALA"):
        st.error("Pogrešno! Vraćaš se korak nazad.")
        time.sleep(1)
        st.session_state.korak = 'maske'
        st.rerun()
        
    if col3.button("RADNIK"):
        st.warning("To nije bila njegova želja.")
