import streamlit as st
import time

# Konfiguracija aplikacije
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- CUSTOM CSS (Zelena tema, bijeli tekst, bez plave) ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    .stRadio [data-testid="stMarkdownContainer"] p { color: white !important; font-weight: bold; }
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
    # Inicijalizacija session state-a
    if 'stage' not in st.session_state:
        st.session_state.stage = "naslov"
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'odgovoreno_final' not in st.session_state:
        st.session_state.odgovoreno_final = {}

    # --- FUNKCIJA ZA PROVJERU NEVJERNIKA ---
    def provjeri_tekst(tekst):
        if "ne vjerujem u boga" in tekst.lower():
            kazna_tama()

    # --- FAZA 1: NASLOV ---
    if st.session_state.stage == "naslov":
        st.markdown("<h1 style='text-align: center; color: #00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI KROZ VRATA"):
            st.session_state.stage = "uvod_tekst"
            st.rerun()

    # --- FAZA 2: UVODNI TEKSTOVI ---
    elif st.session_state.stage == "uvod_tekst":
        st.write("Nisu svi putevi prema Bogu. Nisu svi koji pričaju o Bogu od Boga.")
        st.write("Nisu svi prema Božjoj volji. Nisu sve kamene ustanove od Boga.")
        if st.button("DALJE"):
            st.session_state.stage = "tama_uvod"
            st.rerun()

    elif st.session_state.stage == "tama_uvod":
        st.markdown("<h3 style='text-align: center;'>Tama je gusta.</h3>", unsafe_allow_html=True)
        st.write("Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.")
        if st.button("ZAPOČNI SPOZNAJU"):
            st.session_state.stage = "pitanje_1"
            st.rerun()

    # --- FAZA 3: PITANJA (LOGIKA LABIRINTA) ---
    elif st.session_state.stage == "pitanje_1":
        st.write("Previše priče ogovaranja i pametovanja... mali grijeh privuče još... KOGA?")
        odg1 = st.text_input("Odgovor:", key="q1")
        provjeri_tekst(odg1)
        if odg1.lower() == "grijeha":
            st.success("...i srce polako postane prostor tame.")
            if st.button("NASTAVI"): st.session_state.stage = "pitanje_2"; st.rerun()

    elif st.session_state.stage == "pitanje_2":
        st.write("Jedan od anđela je u sebi stvarao želju da postane - što?")
        izbor2 = st.radio("", ["Budala!", "Bog", "Fizički radnik!"], index=None)
        if izbor2 == "Bog":
            if st.button("TOČNO"): st.session_state.stage = "pitanje_3"; st.rerun()
        elif izbor2:
            st.error("KRIVO. Odgovor je BOG.")
            time.sleep(1); st.session_state.stage = "pitanje_3"; st.rerun()

    elif st.session_state.stage == "pitanje_3":
        st.write("Tko još uz pale anđele slično razmišlja?")
        c1, c2 = st.columns(2)
        if c1.button("ZNAM"): st.session_state.q4_mode = "znam"
        if c2.button("NE ZNAM"): st.session_state.q4_mode = "neznam"
        
        if st.session_state.get('q4_mode') == "neznam":
            st.info("AI će razviti svijest i ideju da postane bog.")
            if st.button("DALJE"): st.session_state.stage = "pitanje_4"; st.rerun()
        elif st.session_state.get('q4_mode') == "znam":
            pog = st.radio("POGODI TKO:", ["Gorile!", "AI & Antena riblja kost!"], index=None)
            if pog == "AI & Antena riblja kost!":
                if st.button("POTVRDI"): st.session_state.stage = "pitanje_4"; st.rerun()

    elif st.session_state.stage == "pitanje_4":
        st.write("Tko je Otac Laži?")
        odg4 = st.text_input("", key="q4")
        if odg4.lower() == "sotona":
            if st.button("Odmori mozak ili klikni za dalje"): st.session_state.stage = "sobe"; st.rerun()

    # --- FAZA 4: SOBE ---
    elif st.session_state.stage == "sobe":
        c1, c2 = st.columns(2)
        if c1.button("Soba: GENERACIJE"): st.session_state.soba = "Biblija neće postojati."
        if c2.button("Soba: SOTONA NE MIRUJE"): st.session_state.soba = "Zarobljava ljude od Krista."
        if 'soba' in st.session_state:
            st.warning(st.session_state.soba)
            if st.button("VRIJEME JE SVETO"): st.session_state.stage = "finalni_test"; st.rerun()

    # --- FAZA 5: FINALNI TEST (10 PITANJA JEDNO PO JEDNO) ---
    elif st.session_state.stage == "finalni_test":
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?",
            "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?",
            "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]
        
        trenutno = len(st.session_state.odgovoreno_final)
        
        if trenutno < 10:
            st.subheader(f"Pitanje {trenutno + 1}/10")
            st.write(f"**{pitanja[trenutno]}**")
            col1, col2 = st.columns(2)
            if col1.button("DA", key=f"d_{trenutno}"):
                st.session_state.score += (1 if trenutno != 8 else -1)
                st.session_state.odgovoreno_final[trenutno] = "DA"
                st.rerun()
            if col2.button("NE", key=f"n_{trenutno}"):
                st.session_state.score += (-1 if trenutno != 8 else 1)
                st.session_state.odgovoreno_final[trenutno] = "NE"
                st.rerun()
            st.stop()
        else:
            # REZULTAT
            if st.session_state.score >= 6:
                st.success("ČESTITAMO! IZAŠLI STE IZ TAME. DOBRO DOŠLI U SVJETLO.")
                st.write("ZNAČKA VJERNIKA DODIJELJENA 🛡️")
                st.markdown(f"[SVE MOJE APLIKACIJE]({st.secrets['linkovi']['portal']})")
                if st.button("POČETAK"):
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()
            else:
                st.error("LABIRINT JE ZAVRŠIO, ALI TAMA JE U VAMA.")
                time.sleep(2)
                kazna_tama()

if __name__ == "__main__":
    main()
