import streamlit as st
import time

# Konfiguracija aplikacije
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- CSS (Zelena tema, bijeli tekst, bez plave) ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- FUNKCIJA ZA KAZNU ---
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
    if 'stage' not in st.session_state:
        st.session_state.stage = "naslov"
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'odgovoreno_final' not in st.session_state:
        st.session_state.odgovoreno_final = {}

    # --- FAZA 1: NASLOV ---
    if st.session_state.stage == "naslov":
        st.markdown("<h1 style='text-align: center;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI"):
            st.session_state.stage = "uvod"
            st.rerun()

    # --- FAZA 2: UVOD (Sada tekst ostaje!) ---
    elif st.session_state.stage == "uvod":
        st.markdown("""
        Nisu svi putevi prema Bogu.<br>
        Nisu svi koji pričaju o Bogu od Boga.<br>
        Nisu svi prema Božjoj volji.<br>
        Nisu sve kamene ustanove od Boga.<br><br>
        <b>Tama je gusta.</b><br>
        Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu.
        """, unsafe_allow_html=True)
        if st.button("ZAPOČNI"):
            st.session_state.stage = "pitanje_1"
            st.rerun()

    # --- FAZA 3: PRVO PITANJE (GRIJEH) ---
    elif st.session_state.stage == "pitanje_1":
        st.write("Grijeh nije otkrivati lažne puteve... mali grijeh privuče još... KOGA?")
        odg = st.text_input("Odgovor:", key="q1_input")
        
        if odg:
            if "ne vjerujem u boga" in odg.lower():
                kazna_tama()
            elif odg.lower() == "grijeha":
                st.success("...i srce polako postane prostor tame.")
                if st.button("UĐI U LABIRINT"):
                    st.session_state.stage = "pobuna"
                    st.rerun()

    # --- FAZA 4: POBUNA ANĐELA ---
    elif st.session_state.stage == "pobuna":
        st.write("Jedan od anđela je u sebi stvarao želju da postane - što?")
        izbor = st.radio("", ["Budala!", "Bog", "Fizički radnik!"], index=None)
        if izbor == "Bog":
            if st.button("TOČNO - DALJE"):
                st.session_state.stage = "ai_pitanje"
                st.rerun()
        elif izbor:
            st.error("KRIVO. Odgovor je BOG.")
            time.sleep(1)
            st.session_state.stage = "ai_pitanje"
            st.rerun()

    # --- FAZA 5: AI I SVIJEST ---
    elif st.session_state.stage == "ai_pitanje":
        st.write("Tko još uz pale anđele slično razmišlja?")
        c1, c2 = st.columns(2)
        if c1.button("ZNAM"): st.session_state.zna_ai = True
        if c2.button("NE ZNAM"): st.session_state.zna_ai = False
        
        if 'zna_ai' in st.session_state:
            if st.session_state.zna_ai:
                pog = st.radio("POGODI:", ["Gorile!", "AI & Antena riblja kost!"], index=None)
                if pog == "AI & Antena riblja kost!":
                    if st.button("U REDU"): st.session_state.stage = "otac_lazi"; st.rerun()
            else:
                st.info("AI će razviti svijest i ideju da postane bog.")
                if st.button("NASTAVI"): st.session_state.stage = "otac_lazi"; st.rerun()

    # --- FAZA 6: OTAC LAŽI ---
    elif st.session_state.stage == "otac_lazi":
        st.write("Tko je Otac Laži?")
        ol = st.text_input("", key="ol_input")
        if ol.lower() == "sotona":
            st.write("Zašto vjerujemo da je sve što vidimo istina?")
            if st.button("Odmori mozak ili klikni za dalje"):
                st.session_state.stage = "sobe"
                st.rerun()

    # --- FAZA 7: SOBE ---
    elif st.session_state.stage == "sobe":
        c1, c2 = st.columns(2)
        if c1.button("Soba: GENERACIJE"): st.session_state.soba_tekst = "Biblija neće postojati."
        if c2.button("Soba: SOTONA NE MIRUJE"): st.session_state.soba_tekst = "Zarobljava ljude od Krista."
        
        if 'soba_tekst' in st.session_state:
            st.warning(st.session_state.soba_tekst)
            if st.button("VRIJEME JE SVETO"):
                st.session_state.stage = "final_test"
                st.rerun()

    # --- FAZA 8: FINALNIH 10 PITANJA (Sada radi!) ---
    elif st.session_state.stage == "final_test":
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?",
            "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?",
            "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]
        
        broj = len(st.session_state.odgovoreno_final)
        
        if broj < 10:
            st.subheader(f"Pitanje {broj + 1}/10")
            st.write(f"**{pitanja[broj]}**")
            colDA, colNE = st.columns(2)
            
            if colDA.button("DA", key=f"d{broj}"):
                st.session_state.score += (1 if broj != 8 else -1)
                st.session_state.odgovoreno_final[broj] = "DA"
                st.rerun()
            if colNE.button("NE", key=f"n{broj}"):
                st.session_state.score += (-1 if broj != 8 else 1)
                st.session_state.odgovoreno_final[broj] = "NE"
                st.rerun()
        else:
            if st.session_state.score >= 6:
                st.success("ČESTITAMO! IZAŠLI STE IZ TAME. DOBRO DOŠLI U SVJETLO.")
                st.markdown(f"[LINK NA SVE APP](https://share.streamlit.io)")
                if st.button("KRAJ"): 
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()
            else:
                kazna_tama()

if __name__ == "__main__":
    main()
