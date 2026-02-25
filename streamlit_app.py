import streamlit as st
import time

# --- 1. POSTAVKE ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- 2. STIL (BRIŠEMO SVE BIJELO I SIVO) ---
st.markdown("""
<style>
    /* Pozadina i magla */
    .stApp { 
        background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                    url('https://www.transparenttextures.com');
        background-color: black; color: white; 
    }
    
    /* Sva slova u bijelo, naslovi u zeleno */
    .stMarkdown, p, div, label, .stRadio { color: white !important; font-family: 'Georgia', serif; }
    .zelena-autor { color: #00FF41 !important; font-family: 'Courier New', monospace; font-size: 20px; text-align: center; font-weight: bold; }
    .odbrojavanje { color: #ff4b4b !important; font-size: 50px; text-align: center; font-weight: bold; }

    /* POPRAVAK GUMBA - Da ne budu bijeli */
    button, .stButton>button {
        background-color: black !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
    }
    button:hover {
        background-color: #00FF41 !important;
        color: black !important;
    }

    /* INPUT POLJE - Skroz tamno */
    input {
        background-color: #000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
    }
    
    /* SKRIVANJE RUŽNIH OZNAKA IZNAD INPUTA */
    label[data-testid="stWidgetLabel"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA ZA IZLAZ ---
def kazna_tame():
    st.empty() # Briše sve s ekrana
    st.markdown('<p class="odbrojavanje">Vi ste tama i ostajete u Tami.</p>', unsafe_allow_html=True)
    placeholder = st.empty()
    for i in range(5, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 4. POČETAK ---
if 'faza' not in st.session_state: st.session_state.faza = 'UVOD'

# --- 5. TIJEK LABIRINTA ---

if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    p_uvod = st.empty()
    for p in ["Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.", "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."]:
        p_uvod.markdown(f'<p style="text-align:center; font-size:24px;">{p}</p>', unsafe_allow_html=True)
        time.sleep(2); p_uvod.empty()
    st.markdown('<p class="zelena-autor" style="font-size:32px;">Tama je gusta.</p>', unsafe_allow_html=True)
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = 'GRIJEH'; st.rerun()

elif st.session_state.faza == 'GRIJEH':
    st.write("Grijeh nije otkrivati lažne puteve i skidati maske... (koga?)")
    odg = st.text_input("", key="g", placeholder="Upiši odgovor...").lower().strip()
    if odg == "grijeha":
        st.success("Srce polako postane prostor tame.")
        if st.button("DALJE"): st.session_state.faza = 'ANDJELI'; st.rerun()

elif st.session_state.faza == 'ANDJELI':
    st.write("Anđeo je želio postati - što?")
    c1, c2, c3 = st.columns(3)
    if c3.button("bog!"): st.session_state.faza = 'FILM'; st.rerun()
    elif c1.button("Budala!") or c2.button("Radnik!"): st.error("Krivo.")

elif st.session_state.faza == 'FILM':
    st.markdown('<p style="font-size:35px; text-align:center; padding:50px;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(4); st.session_state.faza = 'VJERA_KRAJ'; st.rerun()

# --- KLJUČNA FAZA: VJERA ILI TAMA ---
elif st.session_state.faza == 'VJERA_KRAJ':
    st.write("Vjeruješ li u Boga?")
    col_da, col_ne = st.columns(2)
    
    if col_da.button("Vjerujem!"):
        st.session_state.faza = 'FINAL'; st.rerun()
        
    if col_ne.button("Ne vjerujem!"):
        st.session_state.nevjernik = True

    if st.session_state.get('nevjernik'):
        st.write("---")
        st.markdown('<p class="zelena-autor">Tko je Otac Laži?</p>', unsafe_allow_html=True)
        kraj_odg = st.text_input("", key="ol_final", placeholder="Odgovori istinu...").lower().strip()
        if kraj_odg == "sotona":
            kazna_tame()

elif st.session_state.faza == 'FINAL':
    st.markdown('<p class="zelena-autor">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    with st.form("zadnji_test"):
        p1 = st.radio("Prihvaćaš li Isusa?", ["Ne", "Da"])
        p2 = st.radio("Biblija je Božja riječ?", ["Ne", "Da"])
        p3 = st.radio("Sotona je Lažac?", ["Ne", "Da"])
        if st.form_submit_button("ZAVRŠI"):
            if p1 == "Da" and p2 == "Da" and p3 == "Da":
                st.balloons()
                st.success("Izišli ste u Svjetlo!")
                st.markdown(f'<center><a href="https://share.streamlit.io" style="color:#00FF41;">MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else:
                kazna_tame()
