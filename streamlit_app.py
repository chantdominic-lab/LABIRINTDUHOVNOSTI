import streamlit as st
import time

# --- 1. KONFIGURACIJA I IKONA VRATA ---
st.set_page_config(page_title="Labirint Duhovnosti", page_icon="🚪", layout="centered")

# --- 2. STIL (Magla, Zelena/Bijela, Bez plave, Tamni Input) ---
st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url('https://www.transparenttextures.com');
        background-color: black; 
        color: white; 
    }
    .zelena-autor { color: #00FF41; font-family: 'Courier New', monospace; font-size: 18px; text-align: center; font-weight: bold; }
    .bijela-poruka { color: white; font-family: 'Georgia', serif; font-size: 24px; text-align: center; font-style: italic; }
    .filmski-tekst { color: white; font-family: 'Georgia', serif; font-size: 38px; text-align: center; font-style: italic; padding: 100px 0; }
    .odbrojavanje { color: #ff4b4b; font-size: 60px; text-align: center; font-weight: bold; }
    
    /* Stil za Input - Tamno i bez bijelog okvira */
    input {
        background-color: #111 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
    }
    input:focus {
        outline: none !important;
        box-shadow: 0 0 10px #00FF41 !important;
    }
    
    /* Gumbi */
    div.stButton > button { background-color: transparent; color: #00FF41; border: 1px solid #00FF41; width: 100%; transition: 0.5s; }
    div.stButton > button:hover { background-color: #00FF41; color: black; }
</style>
""", unsafe_allow_html=True)

# --- 3. POMOĆNA FUNKCIJA ZA RESTART ---
def restart_s_odbrojavanjem():
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
        time.sleep(1)
    st.session_state.clear()
    st.rerun()

# --- 4. INICIJALIZACIJA STANJA ---
if 'faza' not in st.session_state:
    st.session_state.faza = 'UVOD'

# --- 5. LOGIKA LABIRINTA ---

# --- UVOD ---
if st.session_state.faza == 'UVOD':
    st.markdown('<p class="zelena-autor">Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>', unsafe_allow_html=True)
    st.write("---")
    placeholder = st.empty()
    poruke = [
        "Nisu svi putevi prema Bogu.", "Nisu svi koji pričaju o Bogu od Boga.",
        "Nisu svi prema Božjoj volji.", "Nisu sve kamene ustanove od Boga."
    ]
    for p in poruke:
        placeholder.markdown(f'<p class="bijela-poruka">{p}</p>', unsafe_allow_html=True)
        time.sleep(2.5)
        placeholder.empty()
    
    st.markdown('<p class="zelena-autor" style="font-size:30px;">Tama je gusta.</p>', unsafe_allow_html=True)
    time.sleep(2.5)
    st.markdown('<p class="bijela-poruka">Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</p>', unsafe_allow_html=True)
    if st.button("Uđi u Labirint..."):
        st.session_state.faza = 'GRIJEH'
        st.rerun()

# --- GRIJEH ---
elif st.session_state.faza == 'GRIJEH':
    st.markdown('<p class="bijela-poruka">Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.</p>', unsafe_allow_html=True)
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice a klice žile koje će izrasti u drvo plodno koje će davati plod grijeha.")
    st.write("Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još...")
    st.markdown('<p style="color:#00FF41; text-align:center;">Unesi odgovor i klikni enter (koga?)</p>', unsafe_allow_html=True)
    
    odgovor = st.text_input("", key="q1_in", label_visibility="collapsed").lower().strip()
    if odgovor == "grijeha":
        st.markdown('<p class="bijela-poruka" style="color: #ff4b4b;">...i srce polako postane prostor tame.</p>', unsafe_allow_html=True)
        if st.button("Nastavi..."):
            st.session_state.faza = 'ANDJELI'
            st.rerun()
    elif odgovor != "":
        st.error("Odgovor nije točan. Labirint te ne pušta dalje.")

# --- ANĐELI ---
elif st.session_state.faza == 'ANDJELI':
    st.write("U vrijeme pobune anđela, oni nisu više željeli biti poslušni Bogu. Jedan od anđela je u sebi stvarao želju da postane - **što?**")
    col1, col2, col3 = st.columns(3)
    if col1.button("Budala!"): st.error("Krivo.")
    if col2.button("Fizički radnik!"): st.error("Krivo.")
    if col3.button("bog!"):
        st.success("Točno!")
        st.session_state.faza = 'FILM'
        st.rerun()

# --- FILMSKI PRIJELAZ ---
elif st.session_state.faza == 'FILM':
    f_empty = st.empty()
    f_empty.markdown('<p class="filmski-tekst">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    time.sleep(5)
    f_empty.empty()
    st.session_state.faza = 'AI_ZNAM'
    st.rerun()

# --- AI PITANJE ---
elif st.session_state.faza == 'AI_ZNAM':
    st.write("Tko još uz pale anđele slično razmišlja?")
    c1, c2 = st.columns(2)
    if c1.button("Znam"): st.session_state.ai = 'da'
    if c2.button("Ne znam"):
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("Dalje"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()
    
    if st.session_state.get('ai') == 'da':
        izb = st.radio("Pogodi tko:", ["Gorile i Majmuni!", "Tarzan i Jane!", "AI & Antena riblja kost!"])
        if izb == "AI & Antena riblja kost!" and st.button("Otvori put"):
            st.session_state.faza = 'OTAC_LAZI'
            st.rerun()

# --- OTAC LAŽI ---
elif st.session_state.faza == 'OTAC_LAZI':
    st.write("Tko je Otac Laži?")
    odg = st.text_input("", key="ol_in", label_visibility="collapsed").lower().strip()
    if odg == "sotona":
        st.markdown('<p class="zelena-autor">Zašto onda mislimo i vjerujemo da sve što vidimo i znamo je čista istina?</p>', unsafe_allow_html=True)
        if st.button("Odmori mozak ili klikni ovdje za dalje"):
            st.session_state.faza = 'PAKAL'
            st.rerun()

# --- PAKAL I ZEMLJA ---
elif st.session_state.faza == 'PAKAL':
    st.write("Naučeni smo na: Kako na nebu tako i na zemlji.")
    st.markdown('Nitko ne govori da lako može biti i ovo: Kako u <span style="color:red; font-weight:bold;">paklu</span> tako i na zemlji. Zašto?', unsafe_allow_html=True)
    st.write("Ljubav hladi i ljudi traže ljubav u hladnim predmetima.")
    if st.button("Novi tekst"):
        st.session_state.faza = 'GLAD'
        st.rerun()

# --- GLAD I SOBE ---
elif st.session_state.faza == 'GLAD':
    st.write("Bez Boga smo...?")
    if st.button("mrtvi!"):
        st.session_state.faza = 'SOBE'
        st.rerun()

elif st.session_state.faza == 'SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.info("Generacije neće tražiti Boga, Biblija neće postojati.")
    if cd.button("Sotona ne miruje"): st.info("Sotona lagano zarobljava ljude i udaljava ih od Isusa.")
    if st.button("Što je početak Mudrosti?"):
        st.session_state.faza = 'MUDROST'
        st.rerun()

# --- MUDROST I FINALE ---
elif st.session_state.faza == 'MUDROST':
    izb = st.radio("Mudrost je:", ["Dremnuti.", "Gospodnji strah početak je mudrosti.", "Probudit se kasno."])
    if "Gospodnji strah" in izb and st.button("Dalje"):
        st.session_state.faza = 'VRIJEME_SVETO'
        st.rerun()

elif st.session_state.faza == 'VRIJEME_SVETO':
    st.markdown('<p class="zelena">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    with st.form("final"):
        p1 = st.radio("Vjeruješ li u Boga?", ["Ne", "Da"])
        p2 = st.radio("Prihvaćaš li Isusa?", ["Ne", "Da"])
        p3 = st.radio("Biblija je Božja riječ?", ["Ne", "Da"])
        sub = st.form_submit_button("ZAVRŠI")
        if sub:
            if p1 == "Da" and p2 == "Da" and p3 == "Da":
                st.balloons()
                st.success("ČESTITAMO! Izašli ste u svjetlo!")
                st.markdown("🛡️ **ZNAČKA VJERNIKA**")
                st.markdown("[🔗 MOJI PROJEKTI](https://share.streamlit.io)")
            else:
                st.warning("Tama je u vama...")
                restart_s_odbrojavanjem()
