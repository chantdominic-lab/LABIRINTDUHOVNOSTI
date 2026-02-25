import streamlit as st
import time

# --- FUNKCIJA ZA UCITAVANJE TAJNI (SECRETS) ---
# Ako ste definirali secrets.toml, mozete ih pozvati ovako:
# npr. AUTOR_IMENA = st.secrets["APP_AUTHOR"]
# Kako tekst iz PDF-a nije tajna, ostavljam ga u kodu radi jednostavnosti.

# Konfiguracija stranice i Favicon (vrata)
st.set_page_config(
    page_title="Labirint Duhovnosti",
    page_icon="🚪", # Ikona vrata
    layout="centered"
)

# Stil za misteriozni uvod i fontove
st.markdown("""
    <style>
    .stApp { background-color: black; }
    .zelena-slova { color: #00FF41; font-family: 'Courier New'; font-size: 24px; text-align: center; }
    .bijela-slova { color: white; font-family: 'Georgia'; font-size: 20px; text-align: center; font-style: italic; }
    .naslov-autor { color: #00FF41; font-family: 'Courier New'; text-align: center; }
    .pitanje { color: orange; font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_all_html=True)

# --- INICIJALIZACIJA STANJA IGRE ---
if 'state' not in st.session_state:
    st.session_state['state'] = 'INTRO'
    st.session_state['score'] = 0 # Za završni rezultat na kraju PDF-a

# --- FUNKCIJE EKRANA NA TEMELJU STANJA (STATE) ---

def display_intro():
    # Stilizirani naslovi serijala (Page 1 PDF)
    st.markdown('<h3 class="naslov-autor">Iz serijala: U potrazi za istinom</h3>', unsafe_allow_all_html=True)
    st.markdown('<p class="naslov-autor">By Dominic Chant</p>', unsafe_allow_all_html=True)

    # Poruke o putovima (Fade-in efekt simuliran s time.sleep i rerun)
    poruke = [
        "Nisu svi putevi prema Bogu.",
        "Nisu svi koji pričaju o Bogu od Boga.",
        "Nisu svi prema Božjoj volji.",
        "Nisu sve kamene ustanove od Boga."
    ]
    
    placeholder = st.empty()
    for p in poruke:
        placeholder.markdown(f'<p class="zelena-slova">{p}</p>', unsafe_allow_all_html=True)
        time.sleep(2.5)
        placeholder.empty()

    # Tama je gusta
    placeholder.markdown('<p class="zelena-slova">Tama je gusta.</p>', unsafe_allow_all_html=True)
    time.sleep(3)
    placeholder.empty()

    # Bijela poruka
    poruka_bijela = "Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku."
    placeholder.markdown(f'<p class="bijela-slova">{poruka_bijela}</p>', unsafe_allow_all_html=True)
    time.sleep(4)
    placeholder.empty()
    
    # Premjesti na iduce stanje kada je uvod gotov
    st.session_state['state'] = 'Q1_GRIJEH'
    st.rerun() # Osvjezi stranicu za pocetak labirinta

def display_q1_grijeh():
    # Ovo je prvi ekran labirinta ("Zidovi se iscrtavaju")
    st.markdown('<p class="zelena-slova">Zidovi labirinta se iscrtavaju...</p>', unsafe_allow_all_html=True)
    st.markdown("Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.")
    st.markdown("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice a klice žile koje će izrasti u drvo plodno koje će davati plod grijeha.")
    st.markdown("Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još... **(koga?)**")

    # Pitanje s točnim odgovorom: "grijeha!"
    odgovor = st.text_input("Upišite točan odgovor:")
    if odgovor.lower().strip() == "grijeha":
        st.success("Točno! Tada se otvara nastavak teksta.")
        st.session_state['state'] = 'Q2_ANDJELI'
        st.session_state['score'] += 1
        time.sleep(2)
        st.rerun()
    elif odgovor.lower().strip() != "" :
        st.error("Pokušajte ponovno.")

def display_q2_andjeli():
    # Nastavak teksta i novo pitanje (Page 1 PDF)
    st.markdown("i srce polako postane prostor tame.")
    st.markdown("Oduvijek stvorenje ima nagon da bude: obožavan, slavan, moćan, i da bude poput boga.")
    st.markdown("U vrijeme pobune anđela, oni se nisu pobunili zbog 'zlata' nego nisu više željeli biti poslušni bogu. Jedan od anđela je u sebi stvarao želju da postane - **što?**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Budala!"):
            st.error("Krivo.")
    with col2:
        if st.button("Fizički radnik!"):
             st.error("Krivo.")
    with col3:
        if st.button("Bog!"):
            st.success("Točno! Odgovor je: bog.")
            st.session_state['state'] = 'Q3_DANAŠNJE_VRIJEME'
            st.session_state['score'] += 1
            time.sleep(2)
            st.rerun()

# Ovdje bi išle ostale funkcije (display_q3, display_q4...)
# ...

# --- GLAVNA NAVIGACIJA APLIKACIJE (ROUTER) ---

if st.session_state['state'] == 'INTRO':
    display_intro()
elif st.session_state['state'] == 'Q1_GRIJEH':
    display_q1_grijeh()
elif st.session_state['state'] == 'Q2_ANDJELI':
    display_q2_andjeli()
# Dodajte ostale elif blokove ovdje kako dodajete funkcije za pitanja
# elif st.session_state['state'] == 'Q3_DANAŠNJE_VRIJEME':
#     display_q3_danasnje_vrijeme()
