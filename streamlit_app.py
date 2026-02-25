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
    button, .stButton>button { background-color: black !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; border-radius: 0px !important; }
    button:hover { background-color: #00FF41 !important; color: black !important; }
    input { background-color: #000 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    label[data-testid="stWidgetLabel"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. POMOĆNE FUNKCIJE ---
def restart_sa_sedam_odustajanje():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

def kazna_tame_nevjera():
    st.empty()
    st.markdown('<p class="odbrojavanje" style="font-size: 30px;">Vi ste tama i ostajete u Tami. Vrata Labirinta se zatvaraju!</p>', unsafe_allow_html=True)
    placeholder = st.empty()
    for i in range(5, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 3. LOGIKA LABIRINTA ---
if 'faza' not in st.session_state: st.session_state.faza = 'UVOD'

if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    p_uvod = st.empty()
    for p in ["Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.", "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."]:
        p_uvod.markdown(f'<p style="text-align:center; font-size:24px; font-style:italic; color:white;">{p}</p>', unsafe_allow_html=True)
        time.sleep(2.5); p_uvod.empty()
    st.markdown('<p class="zelena-autor" style="font-size:32px;">Tama je gusta.</p>', unsafe_allow_html=True)
    time.sleep(2.5)
    st.markdown('<p style="text-align:center; font-size:24px; color:white;">Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</p>', unsafe_allow_html=True)
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = 'GRIJEH'; st.rerun()

elif st.session_state.faza == 'GRIJEH':
    st.markdown('<p style="text-align:center; font-size:24px; color:white;">Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.</p>', unsafe_allow_html=True)
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice... (koga?)")
    odg_g = st.text_input("", key="qg", placeholder="...").lower().strip()
    if odg_g == "grijeha":
        st.markdown('<p style="color: #ff4b4b !important; text-align:center; font-size:24px;">...i srce polako postane prostor tame.</p>', unsafe_allow_html=True)
        if st.button("NASTAVI"): st.session_state.faza = 'FILM'; st.rerun()

elif st.session_state.faza == 'FILM':
    st.markdown('<p style="text-align:center; font-size:35px; padding:100px; color:white;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(5); st.session_state.faza = 'VJERA_TEST'; st.rerun()

# --- KLJUČNA RASKRSNICA: VJERA ILI TAMA ---
elif st.session_state.faza == 'VJERA_TEST':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"):
        st.session_state.vjera_odabir = 'DA'
        st.session_state.faza = 'SNAGA_VJERE_TEKST'
        st.rerun()
    if c2.button("Ne vjerujem!"):
        st.session_state.vjera_odabir = 'NE'

    if st.session_state.get('vjera_odabir') == 'NE':
        st.write("---")
        st.markdown('<p class="zelena-autor">Tko je Otac Laži?</p>', unsafe_allow_html=True)
        odg_ol = st.text_input("", key="ol_kraj", placeholder="...").lower().strip()
        if odg_ol == "sotona":
            kazna_tame_nevjera()

# --- TEKST O SNAZI VJERE ---
elif st.session_state.faza == 'SNAGA_VJERE_TEKST':
    st.markdown('<p class="zelena-autor">SVE JE U SNAZI VJERE</p>', unsafe_allow_html=True)
    st.markdown("""
    <p style="color: white !important; font-size: 20px; line-height: 1.6;">
    Sotona se plaši Isusa i samo izgovaranje imena Isus Sotona drhti, kako lijepa priča za malu djecu, 
    ako stalno izgovaraš Isus tada nećeš misliti na neke grijehe, demone ili đavla. Sve je to trik za psihu. <br><br>
    Sotona se ne plaši imena Isus, samo Isus može protjerati zlo iz čovjeka svojom milošću kada se pojavi 
    u prostoru gdje se događa obred, Isus bude prisutan i on je taj koji završi obred, 
    ako ga ne vide ljudi, ono što je u ljudima ono ga vidi.
    </p>
    """, unsafe_allow_html=True)
    if st.button("ŽELIM DALJE"):
        st.session_state.faza = 'FINALNA_PITANJA'
        st.rerun()

# --- FINALNA SOBA ---
elif st.session_state.faza == 'FINALNA_PITANJA':
    st.markdown('<p class="zelena-autor" style="font-size:30px;">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    pitanja = ["Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?", "Sotona je Lažac?", "Grijeh privlači grijeh", "Ne čekaj uzmi Bibliju?"]
    with st.form("final_f"):
        odgovori = [st.radio(p, ["Ne", "Da"], horizontal=True, key=f"f_{i}") for i, p in enumerate(pitanja)]
        if st.form_submit_button("ZAVRŠI"):
            if odgovori.count("Da") >= 4:
                st.balloons(); st.success("IZIŠLI STE U SVJETLO!")
                st.markdown('<div style="border:2px solid #00FF41; padding:20px; text-align:center;"><h2>🛡️ ZNAČKA VJERNIKA</h2><p>Uzmi Bibliju. Laži su grijeh.</p></div>', unsafe_allow_html=True)
                st.markdown('<br><center><a href="https://share.streamlit.io" style="color:#00FF41; font-weight:bold;">🔗 MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else:
                restart_sa_sedam_odustajanje()
