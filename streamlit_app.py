import streamlit as st
import time

# --- 1. KONFIGURACIJA I STIL ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: black; color: white; }
    .zelena { color: #00FF41; font-family: 'Courier New', monospace; font-size: 22px; text-align: center; font-weight: bold; }
    .bijela-it { color: white; font-family: 'Georgia', serif; font-size: 20px; text-align: center; font-style: italic; }
    .odbrojavanje { color: #ff4b4b; font-size: 60px; text-align: center; font-weight: bold; }
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
</style>
""", unsafe_allow_html=True)

# --- 2. POMOĆNE FUNKCIJE ---
def restart_s_odbrojavanjem():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 3. INICIJALIZACIJA ---
if 'faza' not in st.session_state:
    st.session_state.faza = 'UVOD'
if 'da_brojac' not in st.session_state:
    st.session_state.da_brojac = 0

# --- 4. LOGIKA LABIRINTA ---

if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena">LABIRINT DUHOVNOSTI<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown('<p class="bijela-it">Nisu svi putevi prema Bogu.<br>Nisu svi koji pričaju o Bogu od Boga.</p>', unsafe_allow_html=True)
    st.warning("Tama je gusta. Držite Božju riječ u srcu.")
    if st.button("Uđi u Labirint..."):
        st.session_state.faza = 'GRIJEH'
        st.rerun()

elif st.session_state.faza == 'GRIJEH':
    st.write("Mali grijeh privuče još... **(koga?)**")
    odgovor = st.text_input("Upišite odgovor:", key="q1").lower().strip()
    if odgovor == "grijeha":
        st.success("Točno!")
        if st.button("Nastavi"):
            st.session_state.faza = 'NASLOV_2'
            st.rerun()

elif st.session_state.faza == 'NASLOV_2':
    st.markdown('<p class="zelena">Sve je u snazi vjere</p>', unsafe_allow_html=True)
    st.write("Sotona se plaši Isusa? Ne, samo Isus može protjerati zlo svojom milošću.")
    st.write("Koga je Isus istjerao iz mladića u krdo svinja?")
    izbor = st.radio("Odaberi:", ["Laži!", "Magiju!", "Legiju!"], key="r1")
    if izbor == "Legiju!" and st.button("Provjeri"):
        st.session_state.faza = 'VJERUJES_LI'
        st.rerun()

elif st.session_state.faza == 'VJERUJES_LI':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"):
        st.session_state.faza = 'ZELIS_DALJE'
        st.rerun()
    if c2.button("Ne vjerujem!"):
        st.error("Vrata se zatvaraju...")
        restart_s_odbrojavanjem()

elif st.session_state.faza == 'ZELIS_DALJE':
    st.write("Želiš li nastaviti dublje kroz Labirint?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"):
        st.session_state.faza = 'FINAL'
        st.rerun()
    if c2.button("Ne želim!"):
        restart_s_odbrojavanjem()

elif st.session_state.faza == 'FINAL':
    st.markdown('<p class="zelena">Vrijeme je sveto</p>', unsafe_allow_all_html=True)
    pitanja = [
        "Prihvaćaš li Isusa za spasitelja?", 
        "Biblija je Božja riječ?", 
        "Sotona je Lažac?", 
        "Grijeh privlači grijeh?", 
        "Danas čitam Bibliju?"
    ]
    with st.form("f_form"):
        odgovori = []
        for i, p in enumerate(pitanja):
            odgovori.append(st.radio(p, ["Ne", "Da"], key=f"p_{i}"))
        if st.form_submit_button("ZAVRŠI"):
            da_count = odgovori.count("Da")
            if da_count >= 3:
                st.balloons()
                st.success("DOBRO DOŠLI U SVJETLO!")
                st.info("Uzmi Bibliju.")
                st.markdown("[MOJE OSTALE APP](https://share.streamlit.io)")
            else:
                st.warning("Tama je u vama...")
                restart_s_odbrojavanjem()

# Footer
st.write("---")
st.markdown('<p style="text-align:center; opacity:0.6;"><a href="https://share.streamlit.io" target="_blank" style="color:#00FF41; text-decoration:none;">🔗 SVI MOJI PROJEKTI</a></p>', unsafe_allow_html=True)
