import streamlit as st
import time

# --- 1. POSTAVKE I STIL (Vrata, Magla, Bez sivila) ---
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
def restart_sa_sedam():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

def kazna_tame():
    st.empty()
    st.markdown('<p class="odbrojavanje" style="font-size: 28px;">Vi ste tama i ostajete u Tami. Vrata Labirinta se zatvaraju!</p>', unsafe_allow_html=True)
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
    poruke = ["Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.", "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."]
    for p in poruke:
        p_uvod.markdown(f'<p style="text-align:center; font-size:24px; color:white; font-style:italic;">{p}</p>', unsafe_allow_html=True)
        time.sleep(2.5); p_uvod.empty()
    st.markdown('<p class="zelena-autor" style="font-size:32px;">Tama je gusta.</p>', unsafe_allow_html=True)
    time.sleep(2.5)
    st.markdown('<p style="text-align:center; font-size:24px; color:white;">Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</p>', unsafe_allow_html=True)
    if st.button("UĐI U LABIRINT"):
        st.session_state.faza = 'GRIJEH'; st.rerun()

# --- GRIJEH ---
elif st.session_state.faza == 'GRIJEH':
    st.markdown('<p style="text-align:center; font-size:24px; color:white;">Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.</p>', unsafe_allow_html=True)
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice a klice žile koje će izrasti u drvo plodno koje će davati plod grijeha.")
    st.write("Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još... (koga?)")
    odg_g = st.text_input("", key="qg", placeholder="...").lower().strip()
    if odg_g == "grijeha":
        st.markdown('<p style="color: #ff4b4b !important; text-align:center; font-size:24px;">...i srce polako postane prostor tame.</p>', unsafe_allow_html=True)
        if st.button("NASTAVI"): st.session_state.faza = 'ANDJELI'; st.rerun()

# --- ANĐELI ---
elif st.session_state.faza == 'ANDJELI':
    st.write("U vrijeme pobune anđela, oni se nisu pobunili zbog 'zlata' nego nisu više željeli biti poslušni Bogu. Jedan od anđela je u sebi stvarao želju da postane - što?")
    c1, c2, c3 = st.columns(3)
    if c1.button("Budala!"): st.error("Krivo.")
    if c2.button("Fizički radnik!"): st.error("Krivo.")
    if c3.button("bog!"): st.session_state.faza = 'FILM'; st.rerun()

# --- FILMSKI PRIJELAZ I AI ---
elif st.session_state.faza == 'FILM':
    st.empty().markdown('<p style="text-align:center; font-size:35px; padding:100px; color:white;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(5); st.session_state.faza = 'AI_ZNAM'; st.rerun()

elif st.session_state.faza == 'AI_ZNAM':
    st.write("Tko još uz pale anđele slično razmišlja?")
    c1, c2 = st.columns(2)
    if c1.button("Znam."): st.session_state.ai_put = 'znam'
    if c2.button("Ne znam."):
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("NASTAVI"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()
    if st.session_state.get('ai_put') == 'znam':
        izb = st.radio("Pogodi tko:", ["Gorile!", "Tarzan!", "AI & Antena riblja kost!"], key="r_ai")
        if izb == "AI & Antena riblja kost!" and st.button("OTVORI PUT"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()

# --- OTAC LAŽI I PAKAO ---
elif st.session_state.faza == 'OTAC_LAZI':
    st.write("Tko je Otac Laži?")
    odg_ol = st.text_input("", key="ol", placeholder="...").lower().strip()
    if odg_ol == "sotona":
        st.markdown('<p class="zelena-autor">Zašto onda mislimo da je sve što vidimo istina?</p>', unsafe_allow_html=True)
        if st.button("ODMORI MOZAK ILI KLIKNI ZA DALJE"): st.session_state.faza = 'PAKAL'; st.rerun()

elif st.session_state.faza == 'PAKAL':
    st.write("Naučeni smo: Kako na nebu tako i na zemlji.")
    st.markdown('Nitko ne govori da lako može biti i ovo: Kako u <span style="color:red; font-weight:bold;">paklu</span> tako i na zemlji. Zašto?', unsafe_allow_html=True)
    st.write("Ljubav hladi... ljudi traže ljubav u hladnim predmetima.")
    if st.button("NOVI TEKST"): st.session_state.faza = 'GLAD'; st.rerun()

# --- GLAD I SOBE ---
elif st.session_state.faza == 'GLAD':
    st.write("Bez Boga i duhovne tematike će ljudi biti gladni... nervozu će pobjeđivati s novim ovisnostima. Bez Boga smo...?")
    c1, c2, c3 = st.columns(3)
    if c1.button("mrtvi!"): st.session_state.faza = 'SOBE'; st.rerun()
    elif c2.button("slobodni!") or c3.button("izgubljeni!"): st.error("Krivo.")

elif st.session_state.faza == 'SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.session_state.soba = 'Generacije koje dolaze neće tražiti Boga, Biblija neće postojati.'
    if cd.button("Sotona ne miruje"): st.session_state.soba = 'Sotona lagano zarobljava ljude i udaljava ih od Isusa Krista.'
    if 'soba' in st.session_state:
        st.markdown(f'<div style="border:1px solid #00FF41; padding:20px; color:white;">{st.session_state.soba}</div>', unsafe_allow_html=True)
        if st.button("ŠTO JE POČETAK MUDROSTI?"): st.session_state.faza = 'MUDROST'; st.rerun()

# --- MUDROST I TAMU ---
elif st.session_state.faza == 'MUDROST':
    izb = st.radio("Mudrost je:", ["Gospodnji strah početak je mudrosti...", "Dremnuti.", "Probudit se kasno."])
    if "Gospodnji strah" in izb and st.button("DALJE"): st.session_state.faza = 'MUDROST_TEKST'; st.rerun()

elif st.session_state.faza == 'MUDROST_TEKST':
    st.write("Strah Božji je početak mudrosti. Ako Sotona sve okreće... čovjek može biti uništen i bez rata.")
    st.write("Primamo snagu od svjetlosti i pobjeđujemo...?")
    odg_t = st.radio("", ["Tamu.", "Sami sebe.", "Hladne dane."])
    if odg_t == "Tamu." and st.button("POTVRDI"): st.session_state.faza = 'NASLOVI'; st.rerun()

# --- NASLOVI I VJERA ---
elif st.session_state.faza == 'NASLOVI':
    cl, cd = st.columns(2)
    if cl.button("Zašto se događaju zle stvari?"): st.session_state.n_tekst = "Materijalno ne spašava, nego Ljubav i Isus."
    if cd.button("Sve je u snazi vjere"): st.session_state.n_tekst = "ISUS_PRESENCE"
    
    if st.session_state.get('n_tekst') == "Materijalno ne spašava, nego Ljubav i Isus.":
        st.write(st.session_state.n_tekst)
        if st.button("KOGA JE ISUS ISTJERAO U KRDO SVINJA?"): st.session_state.faza = 'LEGIJA'; st.rerun()
    elif st.session_state.get('n_tekst') == "ISUS_PRESENCE":
        st.markdown("""
        Sotona se plaši Isusa i samo izgovaranje imena Isus Sotona drhti... trik za psihu. 
        Sotona se ne plaši imena Isus, samo Isus može protjerati zlo svojom milošću kada se pojavi u prostoru 
        gdje se događa obred, Isus bude prisutan i on je taj koji završi obred.
        """, unsafe_allow_html=True)
        if st.button("KOGA JE ISUS ISTJERAO U KRDO SVINJA?"): st.session_state.faza = 'LEGIJA'; st.rerun()

elif st.session_state.faza == 'LEGIJA':
    odg_l = st.radio("Odgovor:", ["To su laži!", "To je bila magija!", "Legiju!"], key="r_l")
    if odg_l == "Legiju!" and st.button("DALJE"): st.session_state.faza = 'VJERA_KRAJ'; st.rerun()

# --- TEST VJERE I KAZNA ---
elif st.session_state.faza == 'VJERA_KRAJ':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"): st.session_state.faza = 'ZELIM'; st.rerun()
    if c2.button("Ne vjerujem!"):
        st.session_state.nevjera = True
    
    if st.session_state.get('nevjera'):
        st.write("Tko je Otac Laži?")
        ol_kraj = st.text_input("", key="ol_k", placeholder="...").lower().strip()
        if ol_kraj == "sotona": kazna_tame()

elif st.session_state.faza == 'ZELIM':
    st.write("Želiš li nastaviti dublje kroz duhovne tekstove?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"): st.session_state.faza = 'FINAL'; st.rerun()
    if c2.button("Ne želim!"): restart_sa_sedam()

elif st.session_state.faza == 'FINAL':
    st.markdown('<p style="text-align:center; font-size:22px; color:white;">Ne pravi sebi Boga i ne moli se mrtvim predmetima.</p>', unsafe_allow_html=True)
    st.markdown('<p class="zelena-autor" style="font-size:30px;">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    with st.form("f"):
        p1 = st.radio("Prihvaćaš li Isusa?", ["Ne", "Da"])
        p2 = st.radio("Biblija je Božja riječ?", ["Ne", "Da"])
        p3 = st.radio("Sotona je Lažac?", ["Ne", "Da"])
        if st.form_submit_button("ZAVRŠI"):
            if p1 == "Da" and p2 == "Da" and p3 == "Da":
                st.balloons(); st.success("IZIŠLI STE U SVJETLO!")
                st.markdown('<div style="border:2px solid #00FF41; padding:20px; text-align:center;">🛡️ ZNAČKA VJERNIKA</div>', unsafe_allow_html=True)
                st.markdown('<br><center><a href="https://share.streamlit.io" style="color:#00FF41;">🔗 MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else: restart_sa_sedam()
