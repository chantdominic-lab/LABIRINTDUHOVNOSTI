import streamlit as st
import time

# --- 1. POSTAVKE ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- 2. STIL (Bijela slova, Zeleni detalji, Bez sivila) ---
st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url('https://www.transparenttextures.com');
        background-color: black; color: white; 
    }
    /* Sva obična slova u bijelo */
    .stMarkdown, p, div, label { color: white !important; font-family: 'Georgia', serif; font-size: 18px; }
    .zelena-autor { color: #00FF41 !important; font-family: 'Courier New', monospace; font-size: 20px; text-align: center; font-weight: bold; }
    .bijela-velika { color: white !important; font-size: 26px; text-align: center; font-style: italic; }
    .odbrojavanje { color: #ff4b4b !important; font-size: 60px; text-align: center; font-weight: bold; }
    
    /* Input polje - Zeleni tekst na tamnom, bez sivih tonova */
    input { background-color: #111 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; font-size: 20px !important; }
    
    /* Gumbi - Jasni i vidljivi */
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; font-size: 18px; font-weight: bold; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
    
    /* Radio gumbi - Bijela slova */
    .stRadio label { color: white !important; font-size: 18px !important; }
</style>
""", unsafe_allow_html=True)

def restart_sa_sedam():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

if 'faza' not in st.session_state: st.session_state.faza = 'UVOD'

# --- 3. LOGIKA ---

if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    p_uvod = st.empty()
    poruke = ["Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.", "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."]
    for p in poruke:
        p_uvod.markdown(f'<p class="bijela-velika">{p}</p>', unsafe_allow_html=True)
        time.sleep(2.5); p_uvod.empty()
    st.markdown('<p class="zelena-autor" style="font-size:32px;">Tama je gusta.</p>', unsafe_allow_html=True)
    time.sleep(2.5)
    st.markdown('<p class="bijela-velika">Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</p>', unsafe_allow_html=True)
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = 'GRIJEH'; st.rerun()

elif st.session_state.faza == 'GRIJEH':
    st.markdown('<p class="bijela-velika">Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.</p>', unsafe_allow_html=True)
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice... (koga?)")
    odg_g = st.text_input("", key="qg", placeholder="Upiši odgovor...").lower().strip()
    if odg_g == "grijeha":
        st.markdown('<p class="bijela-velika" style="color: #ff4b4b !important;">...i srce polako postane prostor tame.</p>', unsafe_allow_html=True)
        if st.button("NASTAVI"): st.session_state.faza = 'ANDJELI'; st.rerun()

elif st.session_state.faza == 'ANDJELI':
    st.write("Jedan od anđela je u sebi stvarao želju da postane - što?")
    c1, c2, c3 = st.columns(3)
    if c1.button("Budala!"): st.error("Krivo.")
    if c2.button("Fizički radnik!"): st.error("Krivo.")
    if c3.button("bog!"): st.session_state.faza = 'FILM'; st.rerun()

elif st.session_state.faza == 'FILM':
    st.empty().markdown('<p style="color:white; font-size:38px; text-align:center; padding:100px;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(5); st.session_state.faza = 'AI_ZNAM'; st.rerun()

elif st.session_state.faza == 'AI_ZNAM':
    st.write("Tko još uz pale anđele slično razmišlja?")
    c1, c2 = st.columns(2)
    if c1.button("Znam."): st.session_state.ai_put = 'znam'
    if c2.button("Ne znam."): st.session_state.ai_put = 'neznam'
    if st.session_state.get('ai_put') == 'neznam':
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("NASTAVI PREMA OCU LAŽI"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()
    elif st.session_state.get('ai_put') == 'znam':
        izb = st.radio("Pogodi tko:", ["Gorile i Majmuni!", "Tarzan i Jane!", "AI & Antena riblja kost!"], key="r_ai")
        if izb == "AI & Antena riblja kost!" and st.button("OTVORI PUT"): 
            st.session_state.faza = 'OTAC_LAZI'; st.rerun()

elif st.session_state.faza == 'OTAC_LAZI':
    st.write("Tko je Otac Laži?")
    odg_ol = st.text_input("", key="ol", placeholder="Upiši ime...").lower().strip()
    if odg_ol == "sotona":
        st.markdown('<p class="zelena-autor">Zašto onda mislimo i vjerujemo da sve što vidimo i znamo je čista istina?</p>', unsafe_allow_html=True)
        if st.button("ODMORI MOZAK ILI KLIKNI ZA DALJE"): st.session_state.faza = 'PAKAL'; st.rerun()

elif st.session_state.faza == 'PAKAL':
    st.write("Naučeni smo: Kako na nebu tako i na zemlji.")
    st.markdown('Može biti i ovo: Kako u <span style="color:red; font-weight:bold;">paklu</span> tako i na zemlji. Zašto?', unsafe_allow_html=True)
    st.write("Ljubav hladi... ljudi traže ljubav u hladnim predmetima.")
    if st.button("NOVI TEKST"): st.session_state.faza = 'GLAD'; st.rerun()

elif st.session_state.faza == 'GLAD':
    st.write("Ako se ne hraniš, umireš. Bez Boga smo...?")
    if st.button("mrtvi!"): st.session_state.faza = 'IZBOR_SOBE'; st.rerun()

elif st.session_state.faza == 'IZBOR_SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.session_state.soba = 'Generacije koje dolaze neće tražiti Boga, Biblija neće postojati.'
    if cd.button("Sotona ne miruje"): st.session_state.soba = 'Sotona lagano zarobljava ljude i udaljava ih od Isusa Krista.'
    if 'soba' in st.session_state:
        st.write(f"**{st.session_state.soba}**")
        if st.button("ŠTO JE POČETAK MUDROSTI?"): st.session_state.faza = 'MUDROST'; st.rerun()

elif st.session_state.faza == 'MUDROST':
    izb = st.radio("Mudrost je:", ["Probudit se poslije podne.", "Gospodnji strah početak je mudrosti...", "Dremnuti dva tri sata."], key="r_m")
    if "Gospodnji strah" in izb and st.button("DALJE"): st.session_state.faza = 'IZVOR'; st.rerun()

elif st.session_state.faza == 'IZVOR':
    st.write("Primamo snagu od svjetlosti i pobjeđujemo...?")
    odg_t = st.radio("", ["Sami sebe.", "Tamu.", "Hladne dane."], key="r_t")
    if odg_t == "Tamu." and st.button("POTVRDI"): st.session_state.faza = 'NASLOVI'; st.rerun()

elif st.session_state.faza == 'NASLOVI':
    cl, cd = st.columns(2)
    if cl.button("Zašto se događaju zle stvari?"): st.session_state.n_tekst = "Materijalno ne spašava, nego Ljubav i Isus."
    if cd.button("Sve je u snazi vjere"): st.session_state.n_tekst = "Sotona se ne plaši imena Isus, već Isusove prisutnosti."
    if 'n_tekst' in st.session_state:
        st.write(f"**{st.session_state.n_tekst}**")
        if st.button("KOGA JE ISUS ISTJERAO U KRDO SVINJA?"): st.session_state.faza = 'LEGIJA'; st.rerun()

elif st.session_state.faza == 'LEGIJA':
    odg_l = st.radio("Odgovor:", ["To su laži!", "To je bila magija!", "Legiju!"], key="r_l")
    if odg_l == "Legiju!" and st.button("UĐI U FINALE"): st.session_state.faza = 'FINAL_VJERA'; st.rerun()

elif st.session_state.faza == 'FINAL_VJERA':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("VJERUJEM!"): st.session_state.faza = 'ZELIM'; st.rerun()
    if c2.button("NE VJERUJEM!"): 
        st.write("Tko je Otac Laži?")
        odg_ol2 = st.text_input("", key="ol2", placeholder="Odgovori...").lower().strip()
        if odg_ol2 == "sotona": st.session_state.faza = 'ZELIM'; st.rerun()

elif st.session_state.faza == 'ZELIM':
    st.write("Želiš li nastaviti dublje kroz Labirint?")
    c1, c2 = st.columns(2)
    if c1.button("ŽELIM!"): st.session_state.faza = 'VRIJEME_SVETO'; st.rerun()
    if c2.button("NE ŽELIM!"):
        st.error("Vrata se zatvaraju... Svjetlo potraži u Bibliji.")
        restart_sa_sedam()

elif st.session_state.faza == 'VRIJEME_SVETO':
    st.markdown('<p class="zelena" style="text-align:center; font-size:30px;">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    pitanja = ["Vjeruješ li u Boga?", "Prihvaćaš li Isusa?", "Biblija je Božja riječ?", "Sotona je Lažac?", "Grijeh privlači grijeh", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"]
    with st.form("f_test"):
        rezultati = [st.radio(p, ["Ne", "Da"], horizontal=True, key=f"f_{i}") for i, p in enumerate(pitanja)]
        if st.form_submit_button("ZAVRŠI"):
            if rezultati.count("Da") >= 6:
                st.balloons(); st.success("IZIŠLI STE U SVJETLO!")
                st.markdown('<div style="border:2px solid #00FF41; padding:20px; text-align:center;"><h2>🛡️ ZNAČKA VJERNIKA</h2><p>Uzmi Bibliju. Laži su grijeh.</p></div>', unsafe_allow_html=True)
                st.markdown(f'<br><center><a href="https://share.streamlit.io" style="color:#00FF41; font-weight:bold; text-decoration:none;">🔗 SVI MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else:
                st.warning("Tama je ostala u vama..."); restart_sa_sedam()
