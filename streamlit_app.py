import streamlit as st
import time

# --- KONFIGURACIJA ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- STIL (Zelena slova, crna pozadina, misterij) ---
st.markdown("""
    <style>
    .stApp { background-color: black; color: white; }
    .zelena-slova { color: #00FF41; font-family: 'Courier New'; font-size: 22px; text-align: center; margin-bottom: 20px; }
    .bijela-slova { color: white; font-family: 'Georgia'; font-size: 24px; text-align: center; font-style: italic; margin-top: 30px; }
    .autor-tekst { color: #00FF41; font-family: 'Courier New'; font-size: 16px; text-align: center; opacity: 0.7; }
    div.stButton > button { background-color: #1a1a1a; color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
    </style>
    """, unsafe_allow_all_html=True)

# --- INICIJALIZACIJA STANJA ---
if 'korak' not in st.session_state:
    st.session_state.korak = 'UVOD'
if 'bodovi' not in st.session_state:
    st.session_state.bodovi = 0

# --- POMOĆNA FUNKCIJA ZA TAJMING ---
def pauza(sekunde=2):
    time.sleep(sekunde)

# --- LOGIKA LABIRINTA ---

# 1. UVODNA SEKVENCA (Page 1)
if st.session_state.korak == 'UVOD':
    st.markdown(f'<p class="autor-tekst">{st.secrets["autorski_podaci"]["serijal"]}<br>By {st.secrets["autorski_podaci"]["autor"]}</p>', unsafe_allow_all_html=True)
    pauza(1)
    
    placeholder = st.empty()
    uvodne_misli = [
        st.secrets["poruke_uvod"]["p1"],
        st.secrets["poruke_uvod"]["p2"],
        st.secrets["poruke_uvod"]["p3"],
        st.secrets["poruke_uvod"]["p4"]
    ]
    
    for misao in uvodne_misli:
        placeholder.markdown(f'<p class="zelena-slova">{misao}</p>', unsafe_allow_all_html=True)
        pauza(2.5)
        placeholder.empty()

    placeholder.markdown(f'<p class="zelena-slova" style="font-size: 30px;">{st.secrets["poruke_uvod"]["tama"]}</p>', unsafe_allow_all_html=True)
    pauza(3)
    placeholder.empty()
    
    st.markdown(f'<p class="bijela-slova">{st.secrets["poruke_uvod"]["bijela"]}</p>', unsafe_allow_all_html=True)
    pauza(4)
    if st.button("Uđi u Labirint..."):
        st.session_state.korak = 'GRIJEH_KOGA'
        st.rerun()

# 2. PITANJE: KOGA? (Page 1)
elif st.session_state.korak == 'GRIJEH_KOGA':
    st.markdown('<p class="zelena-slova">Zidovi labirinta se iscrtavaju...</p>', unsafe_allow_all_html=True)
    st.write("Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.")
    st.write("Previše priče ogovaranja i pametovanja može polako stvarati grijeh a mali grijeh privuče još... **(koga?)**")
    
    odgovor = st.text_input("Tvoj odgovor:", key="q_koga")
    if odgovor.lower().strip() == st.secrets["odgovori"]["q1_koga"]:
        st.success("Točno. Srce polako postane prostor tame.")
        if st.button("Dalje"):
            st.session_state.korak = 'ANDJELI_BOG'
            st.rerun()

# 3. PITANJE: ANĐELI (Page 1)
elif st.session_state.korak == 'ANDJELI_BOG':
    st.write("U vrijeme pobune anđela, oni nisu više željeli biti poslušni Bogu. Jedan od anđela je u sebi stvarao želju da postane - **što?**")
    
    col1, col2, col3 = st.columns(3)
    if col1.button("Budala!"): st.error("Krivo.")
    if col2.button("Radnik!"): st.error("Krivo.")
    if col3.button("Bog!"):
        st.success("Točno! Odgovor: bog.")
        st.session_state.korak = 'ZNAM_NEZNAM'
        st.rerun()

# 4. GRANANJE: ZNAM/NE ZNAM (Page 2)
elif st.session_state.korak == 'ZNAM_NEZNAM':
    st.markdown('<p class="zelena-slova">Tko još uz pale anđele slično razmišlja?</p>', unsafe_allow_all_html=True)
    c1, c2 = st.columns(2)
    if c1.button("Znam"):
        st.session_state.sub_korak = 'ZNAM'
    if c2.button("Ne znam"):
        st.session_state.sub_korak = 'NEZNAM'

    if 'sub_korak' in st.session_state:
        if st.session_state.sub_korak == 'NEZNAM':
            st.info("Umjetna inteligencija (AI) prije ili poslije će razviti svijest i ideju da postane bog.")
            if st.button("Nastavi"): st.session_state.korak = 'OTAC_LAZI'; st.rerun()
        else:
            izbor = st.radio("Pogodi tko:", ["Gorile!", "Tarzan!", "AI & Antena riblja kost!"])
            if izbor == st.secrets["odgovori"]["ai_taman"]:
                if st.button("Točno, dalje"): st.session_state.korak = 'OTAC_LAZI'; st.rerun()

# 5. OTAC LAŽI (Page 2 & 5)
elif st.session_state.korak == 'OTAC_LAZI':
    st.subheader("Tko je Otac Laži?")
    unos = st.text_input("Upiši ime:", key="otac_lazi")
    if unos.capitalize() == st.secrets["odgovori"]["otac_lazi"]:
        st.success("Točno.")
        st.write("Zašto onda mislimo i vjerujemo da je sve što vidimo čista istina?")
        if st.button("Odmori mozak ili klikni za dalje"):
            st.session_state.korak = 'SOBE'
            st.rerun()

# 6. SOBE (Page 3)
elif st.session_state.korak == 'SOBE':
    st.markdown('<p class="zelena-slova">Izaberi sobu lijevo ili desno:</p>', unsafe_allow_all_html=True)
    l, d = st.columns(2)
    if l.button("Generacije"):
        st.warning(st.secrets["tekstovi_soba"]["generacije"])
        if st.button("Kreni dalje"): st.session_state.korak = 'MUDROST'; st.rerun()
    if d.button("Sotona ne miruje"):
        st.warning(st.secrets["tekstovi_soba"]["sotona_ne_miruje"])
        if st.button("Kreni dalje "): st.session_state.korak = 'MUDROST'; st.rerun()

# 7. MUDROST I KRAJ (Page 3 & 6)
elif st.session_state.korak == 'MUDROST':
    st.write("Što je početak Mudrosti?")
    odg = st.radio("Izaberi:", [
        "Dremnuti poslije podne", 
        st.secrets["odgovori"]["pocetak_mudrosti"], 
        "Probudit se kasno"
    ])
    if st.button("Provjeri"):
        if odg == st.secrets["odgovori"]["pocetak_mudrosti"]:
            st.session_state.korak = 'FINALNI_TEST'
            st.rerun()

# 8. FINALNI TEST (Page 6)
elif st.session_state.korak == 'FINALNI_TEST':
    st.subheader("Vrijeme je sveto")
    v1 = st.checkbox("Vjeruješ li u Boga?")
    v2 = st.checkbox("Prihvaćaš Isusa za spasitelja?")
    v3 = st.checkbox("Biblija je pisana Božja riječ?")
    v4 = st.checkbox("Sotona je Lažac?")
    v5 = st.checkbox("Grijeh privlači grijeh?")
    
    if st.button("Završi Labirint"):
        bodovi = sum([v1, v2, v3, v4, v5])
        if bodovi >= 4:
            st.balloons()
            st.success(st.secrets["zavrsni_ekran"]["uspjeh"])
            st.markdown(f"### {st.secrets['zavrsni_ekran']['znacka']}")
            st.write(st.secrets["zavrsni_ekran"]["opomena"])
        else:
            st.error(st.secrets["zavrsni_ekran"]["neuspjeh"])
            pauza(7)
            st.session_state.clear()
            st.rerun()
