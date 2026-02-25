import streamlit as st
import time

# Konfiguracija
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- CSS (Zelena tema, bez plave) ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- FUNKCIJA ZA KAZNU (TAMA I REFRESH) ---
def kazna_tama():
    st.error("VI STE TAMA I OSTAJETE U TAMI...")
    placeholder = st.empty()
    for i in range(7, -1, -1):
        placeholder.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

def main():
    if 'stage' not in st.session_state:
        st.session_state.stage = "naslov"
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'odgovoreno' not in st.session_state:
        st.session_state.odgovoreno = {}

    # --- SVI UNOSI TEKSTA PROVJERAVAJU "NE VJERUJEM" ---
    def provjeri_nevjernika(tekst):
        if "ne vjerujem u boga" in tekst.lower():
            kazna_tama()

    # 1. NASLOV I UVOD (Skraćeno za preglednost koda)
    if st.session_state.stage == "naslov":
        st.markdown("<h1 style='text-align: center; color: #00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        if st.button("KRENI"): st.session_state.stage = "pitanje_1"; st.rerun()

    # 2. PITANJE 1 (Primjer provjere unosa)
    elif st.session_state.stage == "pitanje_1":
        st.write("Mali grijeh privuče još... KOGA?")
        odg1 = st.text_input("Unesi odgovor:", key="q1")
        provjeri_nevjernika(odg1)
        if odg1.lower() == "grijeha":
            if st.button("DALJE"): st.session_state.stage = "pitanje_10_final"; st.rerun()

    # --- FINALNIH 10 PITANJA (POPRAVLJENA LOGIKA) ---
    elif st.session_state.stage == "pitanje_10_final":
        st.markdown("<h3 style='text-align: center;'>FINALNI TEST</h3>", unsafe_allow_html=True)
        
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?",
            "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?",
            "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]

        for i, p in enumerate(pitanja):
            if i not in st.session_state.odgovoreno:
                st.write(f"**{p}**")
                c1, c2 = st.columns(2)
                if c1.button("DA", key=f"da_{i}"):
                    # i=8 je "Kraj nakon smrti" - tu je DA negativno
                    st.session_state.score += (1 if i != 8 else -1)
                    st.session_state.odgovoreno[i] = "DA"
                    st.rerun()
                if c2.button("NE", key=f"ne_{i}"):
                    st.session_state.score += (-1 if i != 8 else 1)
                    st.session_state.odgovoreno[i] = "NE"
                    st.rerun()
                st.stop() # Zaustavlja ispis dok se ne klikne trenutno pitanje

        # KRAJ TESTA
        if len(st.session_state.odgovoreno) == 10:
            if st.session_state.score >= 6: # Više od pola točno
                st.success("ČESTITAMO! IZAŠLI STE IZ TAME. DOBRO DOŠLI U SVJETLO.")
                st.write("ZNAČKA VJERNIKA DODIJELJENA 🛡️")
                st.markdown(f"[MOJE APLIKACIJE]({st.secrets['linkovi']['portal']})")
                if st.button("OSVJEŽI I ZATVORI"): reset_app()
            else:
                st.error("LABIRINT JE ZAVRŠIO, ALI TAMA JE U VAMA.")
                time.sleep(2)
                kazna_tama()

if __name__ == "__main__":
    main()
