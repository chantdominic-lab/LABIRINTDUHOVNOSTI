import streamlit as st
import time

# 1. Konfiguracija s novom ikonom (oko koje sve vidi ili mračni krug)
st.set_page_config(page_title="Labirint Istine", page_icon="👁️", layout="centered")

# 2. Custom CSS za zelena slova i mračnu atmosferu
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .serijal-naslov {
        color: #00FF00; /* Zelena boja */
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        text-align: center;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #00FF00;
        margin-bottom: 5px;
    }
    .autor-naslov {
        color: #008000;
        font-family: 'Georgia', serif;
        font-size: 1rem;
        text-align: center;
        font-style: italic;
        margin-bottom: 50px;
    }
    .uvod-animacija {
        color: #d3d3d3;
        font-size: 1.8rem;
        font-family: 'Garamond', serif;
        text-align: center;
        min-height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    /* Sakrivanje Streamlit elemenata za bolji fokus */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Fiksni zeleni naslov
st.markdown('<p class="serijal-naslov">IZ SERIJALA: U POTRAZI ZA ISTINOM</p>', unsafe_allow_html=True)
st.markdown('<p class="autor-naslov">By Dominic Chant</p>', unsafe_allow_html=True)

# 4. Lista rečenica iz uvoda PDF-a koje će se izmjenjivati
uvodne_recenice = [
    "Nisu svi putevi prema Bogu.",
    "Nisu svi koji pričaju o Bogu od Boga.",
    "Nisu svi prema Božjoj volji.",
    "Nisu sve kamene ustanove od Boga.",
    "Tama je gusta."
]

# 5. Animacija koja se pokretno mijenja
placeholder = st.empty()

# Prvo prikazujemo rečenice jednu po jednu
for recenica in uvodne_recenice:
    placeholder.markdown(f"<div class='uvod-animacija'>{recenica}</div>", unsafe_allow_html=True)
    time.sleep(2.5) # Koliko dugo svaka rečenica stoji

# Nakon animacije, ostavljamo zadnju poruku i gumb za ulaz
placeholder.markdown(f"<div class='uvod-animacija'>Čvršće nego ikad prije moramo držati Božju riječ.</div>", unsafe_allow_html=True)

st.write("")
if st.button("UĐI U LABIRINT"):
    st.session_state.korak = "pitanje_1" # Priprema za sljedeći dio iz PDF-a
    st.rerun()
