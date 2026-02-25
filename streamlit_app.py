import streamlit as st
import time

# --- 1. POSTAVKE STRANICE (Vrata u URL-u) ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- 2. STIL (Magla, bez plave, bez bijelih okvira, crvena za Pakao) ---
st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url('https://www.transparenttextures.com');
        background-color: black; color: white; 
    }
    .zelena-autor { color: #00FF41; font-family: 'Courier New', monospace; font-size: 18px; text-align: center; font-weight: bold; }
    .bijela-poruka { color: white; font-family: 'Georgia', serif; font-size: 24px; text-align: center; font-style: italic; }
    .odbrojavanje { color: #ff4b4b; font-size: 60px; text-align: center; font-weight: bold; font-family: 'Courier New'; }
    input { background-color: #111 !important; color: #00FF41 !important; border: 1px solid #00FF41 !important; }
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; transition: 0.5s; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
</style>
""", unsafe_allow_html=True)

# --- 3. POMOĆNA FUNKCIJA ZA RESTART ---
def restart_sa_sedam():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 4. INICIJALIZACIJA STANJA ---
if 'faza' not in st.session_state:
    st.session_state.faza = 'UVOD'
if 'bodovi' not in st.session_state:
    st.session_state.bodovi = 0

# --- 5. LOGIKA LABIRINTA ---

# --- UVOD ---
if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    p_uvod = st.empty()
    poruke = ["Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.", "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."]
    for p in poruke:
        p_uvod.markdown(f'<p class="bijela-poruka">{p}</p>', unsafe_allow_html=True)
        time.sleep(2.5); p_uvod.empty()
    st.markdown('<p class="zelena-autor" style="font-size:30px;">Tama je gusta.</p>', unsafe_allow_html=True)
    time.sleep(2.5)
    st.markdown('<p class="bijela-poruka">Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</p>', unsafe_allow_html=True)
    if st.button("Uđi u Labirint..."):
        st.session_state.faza = 'GRIJEH'; st.rerun()

# --- GRIJEH ---
elif st.session_state.faza == 'GRIJEH':
    st.markdown('<p class="bijela-poruka">Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.</p>', unsafe_allow_html=True)
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice... (koga?)")
    odg_g = st.text_input("Unesi odgovor i klikni enter:", key="qg").lower().strip()
    if odg_g == "grijeha":
        st.success("Točno! I srce polako postane prostor tame.")
        if st.button("Nastavi"): st.session_state.faza = 'ANDJELI'; st.rerun()
    elif odg_g != "": st.error("Odgovor nije točan.")

# --- ANĐELI ---
elif st.session_state.faza == 'ANDJELI':
    st.write("Jedan od anđela je u sebi stvarao želju da postane - što?")
    c1, c2, c3 = st.columns(3)
    if c1.button("Budala!"): st.error("Odgovor nije točan.")
    if c2.button("Fizički radnik!"): st.error("Odgovor nije točan.")
    if c3.button("bog!"): 
        st.success("Točno!"); time.sleep(1)
        st.session_state.faza = 'FILM'; st.rerun()

# --- FILMSKI PRIJELAZ ---
elif st.session_state.faza == 'FILM':
    st.empty().markdown('<p style="color:white; font-size:38px; text-align:center; padding:100px;">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(5); st.session_state.faza = 'AI_ZNAM'; st.rerun()

# --- AI RASKRSNICA ---
elif st.session_state.faza == 'AI_ZNAM':
    st.write("Tko još uz pale anđele slično razmišlja?")
    c1, c2 = st.columns(2)
    if c1.button("Znam."): st.session_state.ai_put = 'znam'
    if c2.button("Ne znam."): st.session_state.ai_put = 'neznam'

    if st.session_state.get('ai_put') == 'neznam':
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("Nastavi prema Ocu Laži"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()
    elif st.session_state.get('ai_put') == 'znam':
        izb = st.radio("Pogodi tko:", ["Gorile i Majmuni!", "Tarzan i Jane!", "AI & Antena riblja kost!"])
        if izb == "AI & Antena riblja kost!" and st.button("Potvrdi"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()

# --- OTAC LAŽI ---
elif st.session_state.faza == 'OTAC_LAZI':
    st.write("Tko je Otac Laži?")
    odg_ol = st.text_input("Unesi ime:", key="ol").lower().strip()
    if odg_ol == "sotona":
        st.write("Zašto onda mislimo da je sve što vidimo istina?")
        if st.button("Odmori mozak ili klikni za dalje"): st.session_state.faza = 'PAKAL'; st.rerun()

# --- PAKAL ---
elif st.session_state.faza == 'PAKAL':
    st.write("Naučeni smo: Kako na nebu tako i na zemlji.")
    st.markdown('Može biti i ovo: Kako u <span style="color:red; font-weight:bold;">paklu</span> tako i na zemlji.', unsafe_allow_html=True)
    st.write("Ljubav hladi... ljudi traže ljubav u hladnim predmetima.")
    if st.button("Novi tekst"): st.session_state.faza = 'GLAD'; st.rerun()

# --- GLAD I SOBE ---
elif st.session_state.faza == 'GLAD':
    st.write("Ako se ne hraniš, umireš. Bez Boga smo...?")
    c1, c2, c3 = st.columns(3)
    if c1.button("mrtvi!"): st.session_state.faza = 'IZBOR_SOBE'; st.rerun()
    if c2.button("slobodni!"): st.error("Odgovor nije točan.")
    if c3.button("izgubljeni!"): st.error("Odgovor nije točan.")

elif st.session_state.faza == 'IZBOR_SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.session_state.soba = 'Generacije koje dolaze neće tražiti Boga, Biblija neće postojati.'
    if cd.button("Sotona ne miruje"): st.session_state.soba = 'Sotona lagano zarobljava ljude i udaljava ih od Isusa Krista.'
    if 'soba' in st.session_state:
        st.info(st.session_state.soba)
        if st.button("Što je početak Mudrosti?"): st.session_state.faza = 'MUDROST'; st.rerun()

# --- MUDROST I IZVOR ŽIVOTA ---
elif st.session_state.faza == 'MUDROST':
    izb = st.radio("Početak mudrosti je:", ["Probudit se poslije podne.", "Gospodnji strah početak je mudrosti...", "Dremnuti dva tri sata."])
    if "Gospodnji strah" in izb and st.button("Dalje"): st.session_state.faza = 'IZVOR'; st.rerun()

elif st.session_state.faza == 'IZVOR':
    st.write("Primamo snagu od svjetlosti i pobjeđujemo...?")
    odg_t = st.radio("", ["Sami sebe.", "Tamu.", "Hladne dane."])
    if odg_t == "Tamu." and st.button("Potvrdi"): st.session_state.faza = 'NASLOVI'; st.rerun()

# --- DVA NASLOVA I LEGIJA ---
elif st.session_state.faza == 'NASLOVI':
    cl, cd = st.columns(2)
    if cl.button("Zašto se događaju zle stvari?"): st.info("Materijalno ne spašava, nego Ljubav i Isus.")
    if cd.button("Sve je u snazi vjere"): st.info("Sotona se ne plaši imena Isus, već Isusove prisutnosti.")
    if st.button("Koga je Isus istjerao u krdo svinja?"): st.session_state.faza = 'LEGIJA'; st.rerun()

elif st.session_state.faza == 'LEGIJA':
    odg_l = st.radio("Odgovor:", ["To su laži!", "To je bila magija!", "Legiju!"])
    if odg_l == "Legiju!" and st.button("Uđi u finale"): st.session_state.faza = 'FINAL_VJERA'; st.rerun()

# --- FINALNI IZBORI ---
elif st.session_state.faza == 'FINAL_VJERA':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"): st.session_state.faza = 'ZELIM'; st.rerun()
    if c2.button("Ne vjerujem!"): 
        st.write("Tko je Otac Laži?"); odg_ol2 = st.text_input("Odgovor:", key="ol2").lower().strip()
        if odg_ol2 == "sotona": st.session_state.faza = 'ZELIM'; st.rerun()

elif st.session_state.faza == 'ZELIM':
    st.write("Želiš li nastaviti dublje kroz Labirint?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"): st.session_state.faza = 'VRIJEME_SVETO'; st.rerun()
    if c2.button("Ne želim!"):
        st.error("Žao mi je! Vrata Labirinta se zatvaraju... Svjetlo potraži u Bibliji.")
        restart_sa_sedam()

# --- POSLJEDNJA SOBA: VRIJEME JE SVETO ---
elif st.session_state.faza == 'VRIJEME_SVETO':
    st.markdown('<p class="zelena">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    st.write("Ne pravi sebi Boga i ne klanjaj mu se...")
    pitanja = ["Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je pisana Božja riječ?", "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh", "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"]
    
    with st.form("f_test"):
        rezultati = [st.radio(p, ["Ne", "Da"], horizontal=True) for p in pitanja]
        if st.form_submit_button("ZAVRŠI"):
            da_bodovi = rezultati.count("Da")
            if da_bodovi >= 7:
                st.balloons(); st.success("ČESTITAMO! Izašli ste iz tame u svjetlo!")
                st.markdown('<div style="border:2px solid #00FF41; padding:20px; text-align:center;"><h2>🛡️ ZNAČKA VJERNIKA</h2><p>Osvježi stranicu i uzmi Bibliju. Sjeti se: laži su grijeh.</p></div>', unsafe_allow_html=True)
                st.markdown(f'<br><center><a href="https://share.streamlit.io" style="color:#00FF41; text-decoration:none; font-weight:bold;">🔗 MOJI PROJEKTI</a></center>', unsafe_allow_html=True)
            else:
                st.warning("Labirint je završio, ali tama je u vama... Isus donosi svjetlo."); restart_sa_sedam()
