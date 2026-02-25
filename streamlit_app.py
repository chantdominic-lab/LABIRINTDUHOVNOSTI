import streamlit as st
import time

# --- 1. PROVJERA TAJNI (SECRETS) ---
if not st.secrets:
    st.error("⚠️ Greška: Nisu pronađene 'Secrets'. Molimo unesite podatke u postavkama Streamlit Clouda.")
    st.stop()

# --- 2. KONFIGURACIJA STRANICE ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- 3. STIL (Zelena/Bijela slova i Crna pozadina) ---
st.markdown("""
<style>
    .stApp { background-color: black; color: white; }
    .zelena-slova { color: #00FF41; font-family: 'Courier New', monospace; font-size: 22px; text-align: center; font-weight: bold; }
    .bijela-slova { color: white; font-family: 'Georgia', serif; font-size: 24px; text-align: center; font-style: italic; }
    .autor-tekst { color: #00FF41; font-family: 'Courier New', monospace; font-size: 14px; text-align: center; opacity: 0.8; }
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; transition: 0.3s; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
</style>
""", unsafe_allow_all_html=True)

# --- 4. INICIJALIZACIJA STANJA ---
if 'korak' not in st.session_state:
    st.session_state.korak = 'UVOD'
if 'bodovi' not in st.session_state:
    st.session_state.bodovi = 0

# --- 5. LOGIKA LABIRINTA (Iz PDF-a Dominica Chanta) ---

try:
    # --- UVODNI EKRAN ---
    if st.session_state.korak == 'UVOD':
        st.markdown(f'<p class="autor-tekst">{st.secrets["autorski_podaci"]["serijal"]}<br>By {st.secrets["autorski_podaci"]["autor"]}</p>', unsafe_allow_all_html=True)
        
        placeholder = st.empty()
        # Izmjena uvodnih poruka
        for i in range(1, 5):
            misao = st.secrets["poruke_uvod"][f"p{i}"]
            placeholder.markdown(f'<p class="zelena-slova">{misao}</p>', unsafe_allow_all_html=True)
            time.sleep(2.5)
            placeholder.empty()

        # Tama je gusta
        placeholder.markdown(f'<p class="zelena-slova" style="font-size: 30px;">{st.secrets["poruke_uvod"]["tama"]}</p>', unsafe_allow_all_html=True)
        time.sleep(3)
        placeholder.empty()
        
        # Bijela poruka o Božjoj riječi
        st.markdown(f'<p class="bijela-slova">{st.secrets["poruke_uvod"]["bijela"]}</p>', unsafe_allow_all_html=True)
        time.sleep(2)
        
        if st.button("Uđi u Labirint..."):
            st.session_state.korak = 'Q1_GRIJEH'
            st.rerun()

    # --- PITANJE 1: GRIJEH (Page 1) ---
    elif st.session_state.korak == 'Q1_GRIJEH':
        st.markdown('<p class="zelena-slova">Zidovi labirinta se iscrtavaju...</p>', unsafe_allow_all_html=True)
        st.write("Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.")
        st.write("Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još... **(koga?)**")
        
        odgovor = st.text_input("Upišite odgovor:", key="q1_input").lower().strip()
        if odgovor == st.secrets["odgovori"]["q1_koga"]:
            st.success("Točno! Srce polako postane prostor tame.")
            if st.button("Nastavi"):
                st.session_state.korak = 'Q2_ANDJELI'
                st.rerun()

    # --- PITANJE 2: ANĐELI I BOG (Page 1) ---
    elif st.session_state.korak == 'Q2_ANDJELI':
        st.write("U vrijeme pobune anđela, oni nisu više željeli biti poslušni bogu. Jedan od anđela je u sebi stvarao želju da postane - **što?**")
        
        col1, col2, col3 = st.columns(3)
        if col1.button("Budala!"): st.error("Krivo.")
        if col2.button("Radnik!"): st.error("Krivo.")
        if col3.button("Bog!"):
            st.success("Točno! Odgovor je: bog.")
            st.session_state.korak = 'Q3_ZNAM_NEZNAM'
            st.rerun()

    # --- PITANJE 3: AI I ANTENA (Page 2) ---
    elif st.session_state.korak == 'Q3_ZNAM_NEZNAM':
        st.markdown('<p class="zelena-slova">Tko još uz pale anđele slično razmišlja?</p>', unsafe_allow_all_html=True)
        c1, c2 = st.columns(2)
        if c1.button("Znam"): st.session_state.put = 'ZNAM'
        if c2.button("Ne znam"): st.session_state.put = 'NEZNAM'

        if 'put' in st.session_state:
            if st.session_state.put == 'NEZNAM':
                st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
                if st.button("Idi dalje"): 
                    st.session_state.korak = 'Q4_OTAC_LAZI'
                    st.rerun()
            else:
                izbor = st.radio("Pogodi tko:", ["Gorile!", "Tarzan!", st.secrets["odgovori"]["ai_taman"]])
                if izbor == st.secrets["odgovori"]["ai_taman"]:
                    if st.button("Točno, otvori put"):
                        st.session_state.korak = 'Q4_OTAC_LAZI'
                        st.rerun()

    # --- PITANJE 4: OTAC LAŽI (Page 2) ---
    elif st.session_state.korak == 'Q4_OTAC_LAZI':
        st.subheader("Tko je Otac Laži?")
        unos = st.text_input("Točan unos teksta je:", key="otac_lazi_input").capitalize().strip()
        if unos == st.secrets["odgovori"]["otac_lazi"]:
            st.success("Točno.")
            st.write("Odgovori samom sebi: Zašto onda mislimo i vjerujemo da sve što vidimo i znamo je čista istina?")
            if st.button("Odmori mozak ili klikni za dalje"):
                st.session_state.korak = 'Q5_MUDROST'
                st.rerun()

    # --- PITANJE 5: MUDROST (Page 3) ---
    elif st.session_state.korak == 'Q5_MUDROST':
        st.subheader("Što je početak Mudrosti?")
        izbor_m = st.radio("Izaberi točan odgovor:", [
            "Probudit se poslije podne.",
            st.secrets["odgovori"]["pocetak_mudrosti"],
            "Dremnuti poslije dobre hrane."
        ])
        if st.button("Potvrdi izbor"):
            if izbor_m == st.secrets["odgovori"]["pocetak_mudrosti"]:
                st.success("Strah Božji je početak mudrosti.")
                st.session_state.korak = 'Q6_FINAL'
                st.rerun()

    # --- KRAJ: FINALNI TEST I ZNAČKA (Page 6) ---
    elif st.session_state.korak == 'Q6_FINAL':
        st.subheader("Vrijeme je sveto")
        st.write("Odgovori iskreno na pitanja da izađeš iz Labirinta:")
        
        v1 = st.checkbox("Vjeruješ li u Boga?")
        v2 = st.checkbox("Prihvaćaš li Isusa za spasitelja?")
        v3 = st.checkbox("Biblija je pisana Božja riječ?")
        v4 = st.checkbox("Sotona je Lažac?")
        v5 = st.checkbox("Grijeh privlači grijeh?")
        v6 = st.checkbox("Sve Laži su opasne?")
        v7 = st.checkbox("Kada umremo tada NIJE kraj?")

        if st.button("IZLAZ IZ TAME"):
            rezultat = sum([v1, v2, v3, v4, v5, v6, v7])
            if rezultat >= 5:
                st.balloons()
                st.success(st.secrets["zavrsni_ekran"]["uspjeh"])
                st.markdown(f"### {st.secrets['zavrsni_ekran']['znacka']}")
                st.info(st.secrets["zavrsni_ekran"]["opomena"])
            else:
                st.error(st.secrets["zavrsni_ekran"]["neuspjeh"])
                time.sleep(7)
                st.session_state.clear()
                st.rerun()

except Exception as e:
    st.error("Došlo je do greške u Labirintu. Provjerite 'Secrets' formatiranje.")
    st.write(f"Detalji: {e}")

