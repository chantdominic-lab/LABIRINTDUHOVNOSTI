import streamlit as st
import time

# --- KONFIGURACIJA I STIL ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: black; color: white; }
    .zelena { color: #00FF41; font-family: 'Courier New', monospace; font-size: 20px; text-align: center; }
    .bijela-it { color: white; font-family: 'Georgia', serif; font-size: 20px; font-style: italic; }
    .odbrojavanje { color: red; font-size: 50px; text-align: center; font-weight: bold; }
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
</style>
""", unsafe_allow_html=True)

# Funkcija za restart
def restart_labirint():
    time.sleep(7)
    st.session_state.clear()
    st.rerun()

# --- INICIJALIZACIJA ---
if 'faza' not in st.session_state:
    st.session_state.faza = 'NASLOV_2'
if 'da_brojac' not in st.session_state:
    st.session_state.da_brojac = 0

# --- LOGIKA ---

# Naslov 2: Sve je u snazi vjere
if st.session_state.faza == 'NASLOV_2':
    st.markdown('<p class="zelena">Sve je u snazi vjere</p>', unsafe_allow_all_html=True)
    st.write("""Sotona se plaši Isusa i samo izgovaranje imena Isus Sotona drhti... 
    Sotona se ne plaši imena Isus, samo Isus može protjerati zlo iz čovjeka svojom milošću...""")
    
    st.subheader("Ako ne postoje duhovi i Sotona?")
    st.write("Koga je Isus istjerao iz mladića i protjerao ih u krdo svinja?")
    
    col1, col2, col3 = st.columns(3)
    if col1.button("To su laži!"): st.error("Pogrešan put.")
    if col2.button("To je bila magija!"): st.error("Pogrešan put.")
    if col3.button("Legiju!"):
        st.success("Točno!")
        st.session_state.faza = 'VJERUJES_LI'
        st.rerun()

# Vjeruješ li u Boga?
elif st.session_state.faza == 'VJERUJES_LI':
    st.markdown('<p class="zelena">Vjeruješ li u Boga?</p>', unsafe_allow_all_html=True)
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"):
        st.session_state.vjera = "DA"
        st.session_state.faza = 'ZELIS_DALJE'
        st.rerun()
    if c2.button("Ne vjerujem!"):
        st.session_state.vjera = "NE"
        st.session_state.faza = 'OTAC_LAZI_FINAL'
        st.rerun()

# Otac laži (ako ne vjeruje)
elif st.session_state.faza == 'OTAC_LAZI_FINAL':
    st.write("Tko je Otac Laži?")
    odgovor = st.text_input("Odgovor:").lower().strip()
    if odgovor == "sotona":
        st.session_state.faza = 'ZELIS_DALJE'
        st.rerun()

# Želiš li nastaviti dublje?
elif st.session_state.faza == 'ZELIS_DALJE':
    st.write("Želiš li nastaviti dublje kroz duhovne tekstove i tako tražiti izlaz iz Labirinta?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"):
        st.session_state.faza = 'POSLJEDNJA_SOBA'
        st.rerun()
    if c2.button("Ne želim!"):
        st.error("Žao mi je! Vrata Labirinta se zatvaraju...")
        st.write("Jedino pravo svjetlo potraži u Bibliji. Ne gubi sekunde, vrijeme je svetost.")
        placeholder = st.empty()
        for i in range(7, -1, -1):
            placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_all_html=True)
            time.sleep(1)
        restart_labirint()

# Posljednja soba: Vrijeme je sveto
elif st.session_state.faza == 'POSLJEDNJA_SOBA':
    st.markdown('<p class="zelena">Vrijeme je sveto</p>', unsafe_allow_all_html=True)
    st.write("Ne pravi sebi Boga i ne klanjaj mu se... ne moli se mrtvim predmetima.")
    
    pitanja = [
        "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?", 
        "Sotona je Lažac?", "Grijeh privlači grijeh?", "Danas čitam Bibliju?"
    ]
    
    for i, p in enumerate(pitanja):
        st.write(p)
        col_da, col_ne = st.columns(2)
        if col_da.button("DA", key=f"da_{i}"):
            st.session_state.da_brojac += 1
        if col_ne.button("NE", key=f"ne_{i}"):
            pass # Negativni bodovi

    if st.button("Završi Labirint"):
        if st.session_state.da_brojac >= 3:
            st.balloons()
            st.success("ČESTITAMO! Izašli ste iz tame dobro došli u svjetlo!")
            st.markdown("### 🛡️ ZNAČKA VJERNIKA")
            st.info("Sjeti se laži su grijeh. Uzmi Bibliju.")
        else:
            st.warning("Labirint je završio, izašli ste iz tame labirinta ali tama je u vama...")
            placeholder = st.empty()
            for i in range(7, -1, -1):
                placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_all_html=True)
                time.sleep(1)
            restart_labirint()
