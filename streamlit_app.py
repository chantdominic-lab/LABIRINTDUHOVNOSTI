import streamlit as st
import time

# 1. Konfiguracija s ikonom VRATA
st.set_page_config(page_title="Labirint Istine", page_icon="🚪", layout="centered")

# 2. MOĆAN DIZAJN: Animirana pozadina + Matrix Zelena
st.markdown("""
    <style>
    /* Pozadina s efektom mračne magle/dima koji se kreće */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://media.giphy.com");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Ultra zeleni naslov sa sjajem */
    .serijal-naslov {
        color: #00FF41; 
        font-family: 'Courier New', monospace;
        font-size: 1.4rem;
        text-align: center;
        font-weight: bold;
        letter-spacing: 5px;
        text-shadow: 0 0 10px #00FF41, 0 0 20px #008000;
        margin-bottom: 2px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }

    .autor-naslov {
        color: #00FF41;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        text-align: center;
        opacity: 0.7;
        margin-bottom: 50px;
    }

    .uvod-animacija {
        color: #FFFFFF;
        font-size: 1.6rem;
        font-family: 'Garamond', serif;
        text-align: center;
        min-height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-shadow: 2px 2px 8px #000;
        font-weight: bold;
    }

    /* Gumb koji izgleda kao terminal */
    .stButton>button {
        background-color: rgba(0, 255, 65, 0.1);
        color: #00FF41;
        border: 1px solid #00FF41;
        border-radius: 0px;
        font-family: 'Courier New', monospace;
        width: 100%;
        height: 50px;
        font-size: 1.1rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00FF41;
        color: black;
        box-shadow: 0 0 30px #00FF41;
    }

    /* Sakrij Streamlit sučelje */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Zeleni naslov (Uvijek vidljiv)
st.markdown('<p class="serijal-naslov">IZ SERIJALA: U POTRAZI ZA ISTINOM</p>', unsafe_allow_html=True)
st.markdown('<p class="autor-naslov">By Dominic Chant</p>', unsafe_allow_html=True)

# 4. LOGIKA ANIMACIJE I PROGRESIJE
if 'korak' not in st.session_state:
    st.session_state.korak = 'uvod'

placeholder = st.empty()

# SEKVENCA UVODA
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
        time.sleep(1.2) # Brzo i dinamično
    
    placeholder.markdown(f"<div class='uvod-animacija'>DRŽI BOŽJU RIJEČ U SRCU I UMU.</div>", unsafe_allow_html=True)
    
    if st.button("OTVORI VRATA LABIRINTA"):
        st.session_state.korak = 'prva_soba'
        st.rerun()

# 5. PRVA SOBA IZ PDF-a (Grijeh i Maske)
elif st.session_state.korak == 'prva_soba':
    st.markdown("""
        <div class='uvod-animacija' style='font-size: 1.3rem;'>
        Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu, a vodi u smrt.
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    st.write("---")
    st.markdown("<p style='text-align:center; color:#00FF41;'>I treba paziti da od previše priče ne stvori se sjeme koje će pustiti klice...</p>", unsafe_allow_html=True)
    
    # Prvo pitanje iz PDF-a
    st.markdown("<h3 style='text-align:center; color:white;'>Previše ogovaranja stvara mali grijeh, a mali grijeh privuče još - koga?</h3>", unsafe_allow_html=True)
    
    odgovor = st.text_input("Upiši odgovor ovdje...", key="pitanje1").lower().strip()
    
    if odgovor == "grijeha":
        st.success("Točno. Srce polako postane prostor tame.")
        if st.button("NASTAVI DUBLJE"):
            st.session_state.korak = 'pobuna_andjela'
            st.rerun()
    elif odgovor != "":
        st.error("Pogrešan odgovor. Tama se širi...")
