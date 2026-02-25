import streamlit as st
import time

# --- 1. POSTAVKE I STIL ---
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
    .odbrojavanje { color: #ff4b4b !important; font-size: 50px; text-align: center; font-weight: bold; }
    
    /* Gumbi - prozirni zeleni, postaju puni na hover */
    button, .stButton>button { background-color: transparent !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; border-radius: 0px !important; width: 100%; font-weight: bold; transition: 0.3s; }
    button:hover { background-color: #00FF41 !important; color: black !important; }
    
    /* Input polje */
    input { background-color: #000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    label[data-testid="stWidgetLabel"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. FUNKCIJE ---
def restart_sa_sedam_sekundi():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

def kazna_tame():
    st.empty()
    st.markdown('<p class="odbrojavanje" style="font-size: 28px;">Vi ste tama i ostajete u Tami.</p>', unsafe_allow_html=True)
    placeholder = st.empty()
    for i in range(5, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 3. LOGIKA LABIRINTA ---
if 'faza' not in st.session_state: st.session_state.faza = 'UVOD'

# --- UVOD ---
if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    p_uvod = st.empty()
    for p in ["Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.", "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."]:
        p_uvod.markdown(f'<p style="text-align:center; font-size:24px; font-style:italic;">{p}</p>', unsafe_allow_html=True)
        time.sleep(2); p_uvod.empty()
    st.markdown('<p class="zelena-autor" style="font-size:32px;">Tama je gusta.</p>', unsafe_allow_html=True)
    time.sleep(2)
    st.markdown('<p style="text-align:center; font-size:24px;">Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</p>', unsafe_allow_html=True)
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = 'GRIJEH'; st.rerun()

# --- GRIJEH ---
elif st.session_state.faza == 'GRIJEH':
    st.markdown('<p style="text-align:center; font-size:24px;">Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.</p>', unsafe_allow_html=True)
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice... (koga?)")
    odg_g = st.text_input("", key="qg", placeholder="...").lower().strip()
    if odg_g == "grijeha":
        st.markdown('<p style="color: #ff4b4b !important; text-align:center; font-size:24px;">...i srce polako postane prostor tame.</p>', unsafe_allow_html=True)
        if st.button("NASTAVI"): st.session_state.faza = 'ANDJELI'; st.rerun()

# --- ANĐELI ---
elif st.session_state.faza == 'ANDJELI':
    st.write("Anđeo je želio postati - što?")
    c1, c2, c3 = st.columns(3)
    if c3.button("bog!"): st.session_state.faza = 'FILM'; st.rerun()
    elif c1.button("Budala!") or c2.button("Radnik!"): st.error("Krivo.")

# --- FILM ---
elif st.session_state.faza == 'FILM':
    st.markdown('<p style="text-align:center; font-size:35px; padding:50px;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(4); st.session_state.faza = 'GLAD'; st.rerun()

# --- GLAD I SOBE ---
elif st.session_state.faza == 'GLAD':
    st.write("Bez Boga i duhovne tematike će ljudi biti gladni... Bez Boga smo...?")
    if st.button("mrtvi!"): st.session_state.faza = 'SOBE'; st.rerun()

elif st.session_state.faza == 'SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.session_state.soba = 'Generacije koje dolaze neće tražiti Boga, Biblija neće postojati.'
    if cd.button("Sotona ne miruje"): st.session_state.soba = 'Sotona lagano zarobljava ljude i udaljava ih od Isusa Krista.'
    if 'soba' in st.session_state:
        st.markdown(f'<div style="border:1px solid #00FF41; padding:20px;">{st.session_state.soba}</div>', unsafe_allow_html=True)
        if st.button("NASLOVI"): st.session_state.faza = 'NASLOVI'; st.rerun()

# --- NASLOVI (ZLO vs VJERA) ---
elif st.session_state.faza == 'NASLOVI':
    cl, cd = st.columns(2)
    if cl.button("Zašto se događaju zle stvari?"): st.session_state.put = 'ZLO'
    if cd.button("Sve je u snazi vjere"): st.session_state.put = 'VJERA'

    if st.session_state.get('put') == 'ZLO':
        st.write("Materijalno ne spašava, nego?")
        if st.button("Ljubav i Isus"): st.session_state.faza = 'LEGIJA'; st.rerun()
    elif st.session_state.get('put') == 'VJERA':
        st.write("Sotona se ne plaši imena Isus, samo Isus može protjerati zlo svojom milošću...")
        if st.button("KOGA JE ISUS ISTJERAO?"): st.session_state.faza = 'LEGIJA'; st.rerun()

# --- LEGIJA ---
elif st.session_state.faza == 'LEGIJA':
    st.write("Koga je Isus istjerao iz mladića u krdo svinja?")
    if st.button("Legiju!"): st.session_state.faza = 'VJERA_KRAJ'; st.rerun()

# --- TEST VJERE I KAZNA ---
elif st.session_state.faza == 'VJERA_KRAJ':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"): st.session_state.faza = 'ZELIM'; st.rerun()
    if c2.button("Ne vjerujem!"):
        st.write("Tko je Otac Laži?"); odg_ol = st.text_input("", key="ol_k", placeholder="...").lower().strip()
        if odg_ol == "sotona": kazna_tame()

elif st.session_state.faza == 'ZELIM':
    st.write("Želiš li nastaviti dublje?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"): st.session_state.faza = 'FINALNA_SOBA'; st.rerun()
    if c2.button("Ne želim!"): restart_sa_sedam_sekundi()

# --- POSLJEDNJA SOBA: 10 PITANJA ---
elif st.session_state.faza == 'FINALNA_SOBA':
    st.markdown('<p style="text-align:center; font-size:22px;">Ne pravi sebi Boga i ne moli se mrtvim predmetima.</p>', unsafe_allow_html=True)
    st.markdown('<p class="zelena-autor" style="font-size:30px;">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    
    pitanja = [
        "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?", 
        "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh", 
        "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
    ]
    
    with st.form("final_test"):
        rezultati = [st.radio(p, ["Ne", "Da"], horizontal=True, key=f"f_{i}") for i, p in enumerate(pitanja)]
        if st.form_submit_button("ZAVRŠI"):
            if rezultati.count("Da") >= 7:
                st.balloons(); st.success("IZIŠLI STE U SVJETLO!")
                st.markdown('<div style="border:2px solid #00FF41; padding:20px; text-align:center;">🛡️ ZNAČKA VJERNIKA</div>', unsafe_allow_html=True)
                st.markdown('<br><center><a href="https://share.streamlit.io" style="color:#00FF41;">🔗 MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else:
                st.warning("Labirint je završio, ali tama je u vama..."); restart_sa_sedam_sekundi()
