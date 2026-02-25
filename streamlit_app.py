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
    ph = st.empty()
    for i in range(7, -1, -1):
        ph.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

def main():
    # Inicijalizacija stanja - VAŽNO: redoslijed faza
    if 'stage' not in st.session_state:
        st.session_state.stage = "naslov"
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'odgovoreno' not in st.session_state:
        st.session_state.odgovoreno = {}

    # --- FAZA 1: NASLOV ---
    if st.session_state.stage == "naslov":
        st.markdown("<h1 style='text-align: center; color: #00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI"):
            st.session_state.stage = "pitanje_1"
            st.rerun()

    # --- FAZA 2: PITANJE O GRIJEHU ---
    elif st.session_state.stage == "pitanje_1":
        st.write("Mali grijeh privuče još... KOGA?")
        odg = st.text_input("Odgovor:", key="q_tekst")
        if "ne vjerujem u boga" in odg.lower(): kazna_tama()
        if odg.lower() == "grijeha":
            if st.button("POTVRDI"):
                st.session_state.stage = "pitanje_final_uvod"
                st.rerun()

    # --- FAZA 3: UVOD U FINALNI TEST ---
    elif st.session_state.stage == "pitanje_final_uvod":
        st.write("Ne pravi sebi Boga i ne klanjaj mu se...")
        if st.button("Vrijeme je sveto"):
            st.session_state.stage = "test_istine"
            st.rerun()

    # --- FAZA 4: FINALNI TEST (10 PITANJA) ---
    elif st.session_state.stage == "test_istine":
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?",
            "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?",
            "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]

        # Brojač trenutnog pitanja
        trenutno = len(st.session_state.odgovoreno)

        if trenutno < 10:
            p = pitanja[trenutno]
            st.markdown(f"### Pitanje {trenutno + 1}/10")
            st.write(f"**{p}**")
            
            c1, c2 = st.columns(2)
            if c1.button("DA", key=f"btn_da_{trenutno}"):
                # i=8 (Kraj nakon smrti) - DA je krivi odgovor (-1)
                st.session_state.score += (1 if trenutno != 8 else -1)
                st.session_state.odgovoreno[trenutno] = "DA"
                st.rerun()
            if c2.button("NE", key=f"btn_ne_{trenutno}"):
                st.session_state.score += (-1 if trenutno != 8 else 1)
                st.session_state.odgovoreno[trenutno] = "NE"
                st.rerun()
        else:
            # Sva pitanja su odgovorena
            if st.session_state.score >= 6:
                st.success("ČESTITAMO! IZAŠLI STE IZ TAME. SVJETLO JE TU.")
                st.write("ZNAČKA VJERNIKA DODIJELJENA 🛡️")
                st.markdown(f"[MOJE APLIKACIJE]({st.secrets['linkovi']['portal']})")
                if st.button("POČETAK"): 
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()
            else:
                st.error("LABIRINT JE ZAVRŠIO, ALI TAMA JE U VAMA.")
                time.sleep(2)
                kazna_tama()

if __name__ == "__main__":
    main()
