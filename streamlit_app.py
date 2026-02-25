import streamlit as st
import time

# --- 1. KONFIGURACIJA I STIL (Bez plave boje, misteriozna atmosfera) ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: black; color: white; }
    .zelena { color: #00FF41; font-family: 'Courier New', monospace; font-size: 22px; text-align: center; font-weight: bold; }
    .bijela-it { color: white; font-family: 'Georgia', serif; font-size: 20px; text-align: center; font-style: italic; }
    .autor-tekst { color: #00FF41; font-family: 'Courier New', monospace; font-size: 14px; text-align: center; opacity: 0.8; }
    .odbrojavanje { color: #ff4b4b; font-size: 60px; text-align: center; font-weight: bold; font-family: 'Courier New'; }
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; transition: 0.3s; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #00FF41; border: 1px solid #00FF41; }
</style>
""", unsafe_allow_html=True)

# --- 2. POMOĆNE FUNKCIJE ---
def restart_s_odbrojavanjem():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_all_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 3. INICIJALIZACIJA STANJA ---
if 'faza' not in st.session_state:
    st.session_state.faza = 'UVOD'
if 'da_brojac' not in st.session_state:
    st.session_state.da_brojac = 0

# --- 4. LOGIKA LABIRINTA ---

# --- UVODNI EKRAN ---
if st.session_state.faza == 'UVOD':
    st.markdown('<p class="autor-tekst">U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_all_html=True)
    st.markdown('<p class="zelena">LABIRINT DUHOVNOSTI</p>', unsafe_allow_all_html=True)
    
    st.write("---")
    st.markdown('<p class="bijela-it">Nisu svi putevi prema Bogu.<br>Nisu svi koji pričaju o Bogu od Boga.<br>Nisu svi prema Božjoj volji.<br>Nisu sve kamene ustanove od Boga.</p>', unsafe_allow_all_html=True)
    
    st.warning("Tama je gusta. Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.")
    
    if st.button("Uđi u Labirint..."):
        st.session_state.faza = 'GRIJEH'
        st.rerun()

# --- FAZA 1: GRIJEH ---
elif st.session_state.faza == 'GRIJEH':
    st.write("Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.")
    st.write("Previše priče ogovaranja i pametovanja protiv drugih može polako stvarati grijeh, a mali grijeh privuče još... **(koga?)**")
    
    odgovor = st.text_input("Upišite odgovor:", key="q1").lower().strip()
    if odgovor == "grijeha":
        st.success("Točno! I srce polako postane prostor tame.")
        if st.button("Nastavi"):
            st.session_state.faza = 'ANDJELI'
            st.rerun()

# --- FAZA 2: ANĐELI ---
elif st.session_state.faza == 'ANDJELI':
    st.write("U vrijeme pobune anđela, oni nisu više željeli biti poslušni Bogu. Jedan od anđela je u sebi stvarao želju da postane - **što?**")
    col1, col2, col3 = st.columns(3)
    if col1.button("Budala!"): st.error("Krivo.")
    if col2.button("Fizički radnik!"): st.error("Krivo.")
    if col3.button("Bog!"):
        st.success("Točno!")
        st.session_state.faza = 'AI_ANTENA'
        st.rerun()

# --- FAZA 3: AI TEŽNJA ---
elif st.session_state.faza == 'AI_ANTENA':
    st.write("Što se događa u današnje vrijeme? Težnja nagona da čovjek postane bog. Tko još uz pale anđele slično razmišlja?")
    c1, c2 = st.columns(2)
    if c1.button("Znam"): st.session_state.put = 'znam'
    if c2.button("Ne znam"): st.session_state.put = 'neznam'

    if 'put' in st.session_state:
        if st.session_state.put == 'neznam':
            st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
            if st.button("Dalje"): st.session_state.faza = 'NASLOV_2'; st.rerun()
        else:
            izbor = st.radio("Pogodi:", ["Gorile i Majmuni!", "Tarzan i Jane!", "AI & Antena riblja kost!"])
            if izbor == "AI & Antena riblja kost!" and st.button("Potvrdi"):
                st.session_state.faza = 'NASLOV_2'
                st.rerun()

# --- FAZA 4: NASLOV 2 - SNAZA VJERE ---
elif st.session_state.faza == 'NASLOV_2':
    st.markdown('<p class="zelena">Sve je u snazi vjere</p>', unsafe_allow_all_html=True)
    st.write("Sotona se plaši Isusa i samo izgovaranje imena Isus Sotona drhti... to je trik za psihu. Sotona se ne plaši imena Isus, samo Isus može protjerati zlo iz čovjeka svojom milošću.")
    st.subheader("Ako ne postoje duhovi i Sotona?")
    st.write("Koga je Isus istjerao iz mladića i protjerao ih u krdo svinja?")
    
    izbor = st.radio("Odaberi:", ["To su laži!", "To je bila magija!", "Legiju!"])
    if izbor == "Legiju!" and st.button("Provjeri"):
        st.success("Točno!")
        st.session_state.faza = 'VJERUJES_LI'
        st.rerun()

# --- FAZA 5: VJEROVANJE I OTAC LAŽI ---
elif st.session_state.faza == 'VJERUJES_LI':
    st.write("Vjeruješ li u Boga?")
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"):
        st.session_state.vjera = "DA"
        st.session_state.faza = 'ZELIS_DALJE'
        st.rerun()
    if c2.button("Ne vjerujem!"):
        st.session_state.faza = 'OTAC_LAZI_INPUT'
        st.rerun()

elif st.session_state.faza == 'OTAC_LAZI_INPUT':
    st.write("Tko je Otac Laži?")
    odgovor = st.text_input("Unesi odgovor:", key="ol").lower().strip()
    if odgovor == "sotona":
        st.write("Zašto onda mislimo da je sve što vidimo istina?")
        if st.button("Klikni ovdje za dalje"):
            st.session_state.faza = 'ZELIS_DALJE'
            st.rerun()

# --- FAZA 6: DALJE ILI KRAJ ---
elif st.session_state.faza == 'ZELIS_DALJE':
    st.write("Želiš li nastaviti dublje kroz duhovne tekstove i tražiti izlaz iz Labirinta?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"):
        st.session_state.faza = 'SVETO_VRIJEME'
        st.rerun()
    if c2.button("Ne želim!"):
        st.error("Žao mi je! Vrata Labirinta se zatvaraju. Jedino pravo svjetlo potraži u Bibliji.")
        restart_s_odbrojavanjem()

# --- FAZA 7: VRIJEME JE SVETO (Finalna pitanja) ---
elif st.session_state.faza == 'SVETO_VRIJEME':
    st.markdown('<p class="zelena">Vrijeme je sveto</p>', unsafe_allow_all_html=True)
    st.write("Ne pravi sebi Boga i ne klanjaj mu se. Ništa što je na nebu ili zemlji.")
    
    pitanja = [
        "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", 
        "Biblija je pisana Božja riječ?", "Sotona je Lažac?", 
        "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?", 
        "Sve laži su opasne?", "Danas čitam Bibliju?", 
        "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
    ]
    
    # Koristimo formu da sakupimo sve odgovore odjednom
    with st.form("finalni_test"):
        odgovori = []
        for i, p in enumerate(pitanja):
            odgovori.append(st.radio(p, ["Ne", "Da"], key=f"f_{i}"))
        
        submit = st.form_submit_button("ZAVRŠI LABIRINT")
        if submit:
            da_count = odgovori.count("Da")
            if da_count >= 8: # Većina mora biti DA (osim pitanja o kraju nakon smrti)
                st.balloons()
                st.success("ČESTITAMO! IZAŠLI STE IZ TAME U SVJETLO!")
                st.markdown("### 🛡️ ZNAČKA VJERNIKA")
                st.info("Osvježi stranicu, zatvori ovo i uzmi Bibliju. Sjeti se, laži su grijeh.")
                st.markdown(f"[MOJE OSTALE APLIKACIJE](https://share.streamlit.io/user/chantdominic-lab)")
            else:
                st.warning("Labirint je završio. Izašli ste, ali tama je u vama. Samo Isus donosi svjetlo.")
                restart_s_odbrojavanjem()

# --- FOOTER ---
st.write("---")
st.markdown(f'<p class="autor-tekst"><a href="https://share.streamlit.io/user/chantdominic-lab" target="_blank" style="color:#00FF41; text-decoration:none;">🔗 SVI MOJI PROJEKTI</a></p>', unsafe_allow_all_html=True)
