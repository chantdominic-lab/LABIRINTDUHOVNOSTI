import streamlit as st
import time

# 1. Postavke s ikonom VRATA
st.set_page_config(page_title="Labirint Istine", page_icon="🚪", layout="centered")

# 2. DIZAJN: Zelena, Crvena i Siva (Bez plave)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)), 
                    url("https://media.giphy.com");
        background-size: cover;
    }
    .serijal-naslov {
        color: #00FF41; font-family: 'Courier New', monospace; font-size: 1.5rem;
        text-align: center; font-weight: bold; text-shadow: 0 0 15px #00FF41;
    }
    .autor-tekst {
        color: #00FF41; font-family: 'Courier New', monospace; font-size: 1rem;
        text-align: center; opacity: 0.8; margin-bottom: 20px;
    }
    .glavni-tekst { color: #d3d3d3; font-size: 1.4rem; text-align: center; padding: 15px; font-family: 'Garamond', serif; }
    .pakao-tekst { color: #ff4b4b; font-size: 1.6rem; font-weight: bold; text-align: center; }
    .stButton>button { background-color: rgba(0, 255, 65, 0.1); color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    .stButton>button:hover { background-color: #00FF41; color: black; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA SESIJE ---
if 'korak' not in st.session_state:
    st.session_state.korak = 'uvod'
if 'ai_izbor' not in st.session_state:
    st.session_state.ai_izbor = None

# Fiksni naslovi
st.markdown('<p class="serijal-naslov">IZ SERIJALA: U POTRAZI ZA ISTINOM</p>', unsafe_allow_html=True)
st.markdown('<p class="autor-tekst">By Dominic Chant</p>', unsafe_allow_html=True)

# --- SOBE ---

# 1. UVOD
if st.session_state.korak == 'uvod':
    st.markdown("<div class='glavni-tekst'>Nisu svi putevi prema Bogu. Tama je gusta. Čvršće nego ikad prije moramo držati Božju riječ.</div>", unsafe_allow_html=True)
    if st.button("OTVORI VRATA"):
        st.session_state.korak = 'maske'
        st.rerun()

# 2. MASKE I GRIJEH
elif st.session_state.korak == 'maske':
    st.markdown("<div class='glavni-tekst'>Grijeh nije otkrivati lažne puteve i skidati maske koje vode u smrt.</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white;'>Mali grijeh privuče još - koga?</p>", unsafe_allow_html=True)
    odgovor = st.text_input("Odgovor:", key="q_grijeh").lower().strip()
    if odgovor == "grijeha":
        st.success("Točno! Srce polako postane prostor tame.")
        if st.button("IDEM DALJE"):
            st.session_state.korak = 'pobuna'
            st.rerun()

# 3. POBUNA ANĐELA
elif st.session_state.korak == 'pobuna':
    st.markdown("<div class='glavni-tekst'>Jedan od anđela je u sebi stvarao želju da postane - što?</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    if c1.button("BOG"):
        st.session_state.korak = 'ai_soba'
        st.rerun()
    if c2.button("BUDALA") or c3.button("RADNIK"):
        st.error("Pogrešno! Labirint te vraća na početak.")
        time.sleep(1)
        st.session_state.korak = 'uvod'
        st.rerun()

# 4. AI SOBA (Popravljena logika gumba)
elif st.session_state.korak == 'ai_soba':
    st.markdown("<div class='glavni-tekst'>Tko još uz pale anđele slično razmišlja?</div>", unsafe_allow_html=True)
    
    if st.session_state.ai_izbor is None:
        col1, col2 = st.columns(2)
        if col1.button("ZNAM"):
            st.session_state.ai_izbor = 'znam'
            st.rerun()
        if col2.button("NE ZNAM"):
            st.session_state.ai_izbor = 'ne_znam'
            st.rerun()
    
    if st.session_state.ai_izbor == 'ne_znam':
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("NASTAVI DALJE"):
            st.session_state.korak = 'otac_lazi'
            st.rerun()
    elif st.session_state.ai_izbor == 'znam':
        st.markdown("<p style='text-align:center;'>Pogodi jedan od odgovora:</p>", unsafe_allow_html=True)
        if st.button("AI & Antena riblja kost!"):
            st.session_state.korak = 'otac_lazi'
            st.rerun()

# 5. OTAC LAŽI
elif st.session_state.korak == 'otac_lazi':
    st.markdown("<p class='pakao-tekst'>Tko je Otac Laži?</p>", unsafe_allow_html=True)
    otac = st.text_input("Upiši ime:", key="q_sotona").strip().capitalize()
    if otac == "Sotona":
        if st.button("UĐI U DUBINU"):
            st.session_state.korak = 'pakao'
            st.rerun()

# 6. PAKAO I HLADNOĆA
elif st.session_state.korak == 'pakao':
    st.markdown("<div class='glavni-tekst'>'Kako na nebu tako i na zemlji.'</div>", unsafe_allow_html=True)
    st.markdown("<p class='pakao-tekst'>Zašto nitko ne govori: 'Kako u paklu tako i na zemlji'?</p>", unsafe_allow_html=True)
    st.markdown("<div class='glavni-tekst'>Ljubav hladi. Istinu upotpunjuje ono što je hladno.</div>", unsafe_allow_html=True)
    if st.button("TRAŽI IZLAZ (Novi tekst)"):
        st.session_state.korak = 'glad'
        st.rerun()

# 7. DUHOVNA GLAD (Stranica 3 PDF-a)
elif st.session_state.korak == 'glad':
    st.markdown("<div class='glavni-tekst'>Dolazi vrijeme kada će priče o Bogu biti smatrane kao umor. Ljudi će biti gladni, a nikad siti.</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white;'>Bez Boga smo.....?</p>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    if c1.button("MRTVI"):
        st.success("Točno! Bez Boga nema života.")
        if st.button("IDEM DALJE U LABIRINT"):
            st.session_state.korak = 'sobe_izbor'
            st.rerun()
    if c2.button("SLOBODNI") or c3.button("IZGUBLJENI"):
        st.error("Pogrešan put kroz Labirint.")
