import streamlit as st
import time

# --- 1. KONFIGURACIJA I STIL ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                    url('https://www.transparenttextures.com');
        background-color: black; color: white; 
    }
    .stMarkdown, p, div, label, .stRadio { color: white !important; font-family: 'Georgia', serif; }
    .zelena-autor { color: #00FF41 !important; font-family: 'Courier New', monospace; font-size: 20px; text-align: center; font-weight: bold; }
    .odbrojavanje { color: #ff4b4b !important; font-size: 55px; text-align: center; font-weight: bold; }
    
    /* Gumbi - Zeleni okvir, bez bijele boje */
    button, .stButton>button { background-color: transparent !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; border-radius: 0px !important; width: 100%; font-weight: bold; }
    button:hover { background-color: #00FF41 !important; color: black !important; }
    
    /* Radio gumbi - Da/Ne stil */
    div[data-testid="stRadio"] > div { background-color: #111; padding: 10px; border-radius: 5px; border: 1px solid #333; }
    
    input { background-color: #000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    label[data-testid="stWidgetLabel"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. FUNKCIJA ZA IZBACIVANJE (7 SEKUNDI) ---
def izbaci_u_tamu(poruka):
    st.empty()
    st.markdown(f'<p class="odbrojavanje" style="font-size: 24px;">{poruka}</p>', unsafe_allow_html=True)
    p = st.empty()
    for i in range(7, -1, -1):
        p.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 3. LOGIKA LABIRINTA ---
if 'faza' not in st.session_state: st.session_state.faza = 'UVOD'

# --- UVOD, GRIJEH, ANDJELI, FILM (Skraćeno za pregled, ostaje tvoj tekst) ---
if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    if st.button("UĐI U LABIRINT"): st.session_state.faza = 'GRIJEH'; st.rerun()

elif st.session_state.faza == 'GRIJEH':
    st.write("Mali grijeh privuče još... (koga?)")
    odg = st.text_input("", key="g", placeholder="...").lower().strip()
    if odg == "grijeha":
        st.success("Točno!")
        if st.button("DALJE"): st.session_state.faza = 'ANDJELI'; st.rerun()

elif st.session_state.faza == 'ANDJELI':
    st.write("Anđeo je želio postati - što?")
    if st.button("bog!"): st.session_state.faza = 'FILM'; st.rerun()

elif st.session_state.faza == 'FILM':
    st.markdown('<p style="text-align:center; font-size:35px; padding:50px;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(4); st.session_state.faza = 'GLAD'; st.rerun()

elif st.session_state.faza == 'GLAD':
    st.write("Bez Boga smo...?")
    if st.button("mrtvi!"): st.session_state.faza = 'SOBE'; st.rerun()

elif st.session_state.faza == 'SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.session_state.soba = 'Biblija neće postojati.'
    if cd.button("Sotona ne miruje"): st.session_state.soba = 'Sotona zarobljava ljude.'
    if 'soba' in st.session_state:
        if st.button("ŠTO JE POČETAK MUDROSTI?"): st.session_state.faza = 'MUDROST'; st.rerun()

elif st.session_state.faza == 'MUDROST':
    st.write("Početak mudrosti je?")
    odg = st.radio("", ["Gospodnji strah...", "Dremnuti.", "Kasno se probuditi."])
    if st.button("DALJE"):
        if "Gospodnji strah" in odg: st.session_state.faza = 'LEGIJA'; st.rerun()
        else: izbaci_u_tamu("Krivo. Labirint se zatvara!")

elif st.session_state.faza == 'LEGIJA':
    st.write("Koga je Isus istjerao u krdo svinja?")
    odg = st.radio("", ["Laži!", "Magiju!", "Legiju!"])
    if st.button("POTVRDI"):
        if odg == "Legiju!": st.session_state.faza = 'TEST_VJERE'; st.rerun()
        else: izbaci_u_tamu("Nevjera zatvara vrata!")

# --- KLJUČNA TOČKA KOJU SI TRAŽIO ---
elif st.session_state.faza == 'TEST_VJERE':
    st.markdown('<p class="bijela-velika">Vjeruješ li u Boga?</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("VJERUJEM!"):
        st.session_state.faza = 'FINAL_SOBA'; st.rerun()
    if c2.button("NE VJERUJEM!"):
        izbaci_u_tamu("Labirint je završio... ali tama je u vama i samo Isus donosi svjetlo. Pronađi ga u Bibliji!")

# --- POSLJEDNJA SOBA: 10 PITANJA ---
elif st.session_state.faza == 'FINAL_SOBA':
    st.markdown('<p class="zelena-autor" style="font-size:30px;">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    
    pitanja = [
        "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je pisana Božja riječ?", 
        "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh", 
        "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
    ]
    
    with st.form("zadnji_ispit"):
        odgovori = [st.radio(p, ["Ne", "Da"], horizontal=True, key=f"f_{i}") for i, p in enumerate(pitanja)]
        if st.form_submit_button("ZAVRŠI"):
            # Pitanje br. 9 (indeks 8) je trik: "Kada umremo tada je kraj?" - točan odgovor mora biti NE
            if odgovori[8] == "Ne" and odgovori.count("Da") >= 7:
                st.balloons()
                st.success("ČESTITAMO! IZIŠLI STE U SVJETLO!")
                st.markdown('<div style="border:2px solid #00FF41; padding:20px; text-align:center;"><h2>🛡️ ZNAČKA VJERNIKA</h2><p>Osvježi stranicu, zatvori ovo i uzmi Bibliju. Sjeti se laži su grijeh.</p></div>', unsafe_allow_html=True)
                st.markdown('<br><center><a href="https://share.streamlit.io" style="color:#00FF41; font-weight:bold;">🔗 SVI MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else:
                izbaci_u_tamu("Labirint je završio, izašli ste iz tame labirinta ali tama je u vama i samo Isus donosi svjetlo pronađi ga u Bibliji.")
