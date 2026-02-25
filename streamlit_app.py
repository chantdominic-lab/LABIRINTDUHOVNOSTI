import streamlit as st
import time

# --- PROVJERA TAJNI ---
# Ako tajne nisu postavljene, aplikacija će ispisati jasnu uputu umjesto greške
if not st.secrets:
    st.error("Greška: Nisu pronađene 'Secrets'. Molimo postavite ih u postavkama Streamlit Clouda.")
    st.stop()

# --- KONFIGURACIJA ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- STIL (Sigurniji format bez suvišnih razmaka) ---
st.markdown("<style>.stApp { background-color: black; color: white; } .zelena-slova { color: #00FF41; font-family: 'Courier New'; font-size: 22px; text-align: center; } .bijela-slova { color: white; font-family: 'Georgia'; font-size: 24px; text-align: center; font-style: italic; }</style>", unsafe_allow_all_html=True)

# --- INICIJALIZACIJA ---
if 'korak' not in st.session_state:
    st.session_state.korak = 'UVOD'

# --- LOGIKA ---
try:
    if st.session_state.korak == 'UVOD':
        # Koristimo .get() da izbjegnemo KeyError ako nešto fali u secrets
        autor = st.secrets.get("autorski_podaci", {}).get("autor", "Dominic Chant")
        serijal = st.secrets.get("autorski_podaci", {}).get("serijal", "U potrazi za istinom")
        
        st.markdown(f'<p style="text-align:center; color:#00FF41;">{serijal}<br>By {autor}</p>', unsafe_allow_all_html=True)
        
        # Prikazivanje uvodnih misli
        placeholder = st.empty()
        for i in range(1, 5):
            misao = st.secrets["poruke_uvod"][f"p{i}"]
            placeholder.markdown(f'<p class="zelena-slova">{misao}</p>', unsafe_allow_all_html=True)
            time.sleep(2.5)
            placeholder.empty()

        placeholder.markdown(f'<p class="zelena-slova" style="font-size:30px;">{st.secrets["poruke_uvod"]["tama"]}</p>', unsafe_allow_all_html=True)
        time.sleep(3)
        placeholder.empty()
        
        st.markdown(f'<p class="bijela-slova">{st.secrets["poruke_uvod"]["bijela"]}</p>', unsafe_allow_all_html=True)
        
        if st.button("Uđi u Labirint..."):
            st.session_state.korak = 'GRIJEH_KOGA'
            st.rerun()

    elif st.session_state.korak == 'GRIJEH_KOGA':
        st.markdown('<p class="zelena-slova">Zidovi labirinta se iscrtavaju...</p>', unsafe_allow_all_html=True)
        st.write("Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.")
        odgovor = st.text_input("Tvoj odgovor (koga?):", key="q_koga")
        
        if odgovor.lower().strip() == st.secrets["odgovori"]["q1_koga"]:
            st.success("Točno.")
            if st.button("Dalje"):
                st.session_state.korak = 'ANDJELI_BOG'
                st.rerun()

except Exception as e:
    st.error(f"Dogodila se neočekivana greška u labirintu. Provjerite jesu li svi podaci u 'Secrets' točni.")
    # Za debugiranje na Cloudu (vidljivo samo vama u logovima)
    print(f"DEBUG: {e}")
