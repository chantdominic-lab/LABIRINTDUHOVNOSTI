import streamlit as st
import time

# Konfiguracija stranice s ikonom vrata 🚪
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- CUSTOM CSS (Bez plave boje, tamnozelena tema, bijeli tekst) ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; border-radius: 5px; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    .stRadio [data-testid="stMarkdownContainer"] p { color: white !important; font-weight: bold; }
    /* Uklanjanje plavih detalja s radio buttona */
    div[data-baseweb="radio"] div { background-color: #004d33 !important; }
    </style>
    """, unsafe_allow_html=True)

def reset_app():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

def main():
    # Inicijalizacija session state-a
    if 'stage' not in st.session_state:
        st.session_state.stage = "naslov"
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'odgovoreno_final' not in st.session_state:
        st.session_state.odgovoreno_final = [None] * 10

    # --- FAZA 1: NASLOV ---
    if st.session_state.stage == "naslov":
        st.markdown("<h1 style='text-align: center; color: #00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("KRENI"):
            st.session_state.stage = "uvod_1"
            st.rerun()

    # --- FAZA 2: UVOD ---
    elif st.session_state.stage == "uvod_1":
        st.markdown("<div style='text-align: center;'>Nisu svi putevi prema Bogu.<br>Nisu svi koji pričaju o Bogu od Boga.<br>Nisu svi prema Božjoj volji.<br>Nisu sve kamene ustanove od Boga.</div>", unsafe_allow_html=True)
        if st.button("DALJE"):
            st.session_state.stage = "tama"
            st.rerun()

    elif st.session_state.stage == "tama":
        st.markdown("<h2 style='text-align: center; color: #555;'>TAMA</h2>", unsafe_allow_html=True)
        time.sleep(1)
        st.markdown("<h3 style='text-align: center;'>Tama je gusta.</h3>", unsafe_allow_html=True)
        st.write("Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.")
        if st.button("UĐI U LABIRINT"):
            st.session_state.stage = "pitanje_1"
            st.rerun()

    # --- PITANJE 1: GRIJEH ---
    elif st.session_state.stage == "pitanje_1":
        st.write("Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još...")
        st.markdown("**Unesi odg klikni enter**")
        odg1 = st.text_input("KOGA?", key="q1").strip().lower()
        if odg1 == "grijeha":
            st.success("...i srce polako postane prostor tame.")
            if st.button("NASTAVI"):
                st.session_state.stage = "pitanje_2"
                st.rerun()
        elif "ne vjerujem u boga" in odg1:
            st.error("OSTAJEŠ U TAMI")
            time.sleep(2)
            reset_app()

    # --- PITANJE 2: BOG ---
    elif st.session_state.stage == "pitanje_2":
        st.write("Jedan od anđela je u sebi stvarao želju da postane - što?")
        izbor2 = st.radio("", ["Budala!", "Bog", "Fizički radnik!"], index=None)
        if izbor2 == "Bog":
            st.success("Točno.")
            if st.button("DALJE"): st.session_state.stage = "pitanje_3"; st.rerun()
        elif izbor2:
            st.error("KRIVO. Odgovor je BOG.")
            time.sleep(1); st.session_state.stage = "pitanje_3"; st.rerun()

    # --- PITANJE 3: DANAŠNJE VRIJEME ---
    elif st.session_state.stage == "pitanje_3":
        st.write("Što se događa u današnje vrijeme? Težnja nagona da čovjek postane?")
        odg3 = st.text_input("Tko?", key="q3").strip().lower()
        if odg3 == "bog":
            st.success("ISTINA.")
            if st.button("IDEM DALJE"): st.session_state.stage = "pitanje_4"; st.rerun()

    # --- PITANJE 4: AI ---
    elif st.session_state.stage == "pitanje_4":
        st.write("Tko još uz pale anđele slično razmišlja?")
        colA, colB = st.columns(2)
        if colA.button("ZNAM"): st.session_state.q4_mode = "znam"
        if colB.button("NE ZNAM"): st.session_state.q4_mode = "neznam"
        
        if st.session_state.get('q4_mode') == "neznam":
            st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
            if st.button("NASTAVI"): st.session_state.stage = "pitanje_5"; st.rerun()
        elif st.session_state.get('q4_mode') == "znam":
            pogodi = st.radio("POGODI TKO:", ["Gorile i Majmuni!", "Tarzan i Jane!", "AI & Antena riblja kost!"], index=None)
            if pogodi == "AI & Antena riblja kost!":
                if st.button("TOČNO - DALJE"): st.session_state.stage = "pitanje_5"; st.rerun()

    # --- PITANJE 5: OTAC LAŽI ---
    elif st.session_state.stage == "pitanje_5":
        st.write("Tko je Otac Laži?")
        odg5 = st.text_input("", key="q5").strip().lower()
        if odg5 == "sotona":
            st.write("Zašto onda mislimo i vjerujemo da sve što vidimo i znamo je čista istina?")
            if st.button("Odmori mozak ili klikni ovdje za dalje"):
                st.session_state.stage = "pitanje_6"
                st.rerun()

    # --- PITANJE 6: BEZ BOGA SMO... ---
    elif st.session_state.stage == "pitanje_6":
        st.write("Bez Boga smo...?")
        izbor6 = st.radio("", ["mrtvi!", "slobodni!", "izgubljeni!"], index=None)
        if izbor6 == "mrtvi!":
            colS1, colS2 = st.columns(2)
            if colS1.button("Soba: GENERACIJE"): st.info("Biblija za njih neće postojati.")
            if colS2.button("Soba: SOTONA NE MIRUJE"): st.error("Zarobljava ljude od zapovijedi Isusa Krista.")
            if st.button("ŠTO JE POČETAK MUDROSTI?"): st.session_state.stage = "mudrost"; st.rerun()

    elif st.session_state.stage == "mudrost":
        izborM = st.radio("", ["Gospodnji strah...", "Probudit se poslije podne.", "Dremnuti"], index=None)
        if izborM and "Gospodnji strah" in izborM:
            if st.button("NASTAVI"): st.session_state.stage = "pitanje_7"; st.rerun()

    # --- PITANJE 7: POBJEDA ---
    elif st.session_state.stage == "pitanje_7":
        st.write("Ako se okrenemo izvoru života, pobjeđujemo...?")
        izbor7 = st.radio("", ["Tamu.", "Sami sebe.", "Hladne dane."], index=None)
        if izbor7 == "Tamu.":
            if st.button("DALJE"): st.session_state.stage = "pitanje_8"; st.rerun()

    # --- PITANJE 8: ZLE STVARI ---
    elif st.session_state.stage == "pitanje_8":
        colX, colY = st.columns(2)
        if colX.button("Zašto se događaju zle stvari?"): st.session_state.q8_v = "zlo"
        if colY.button("Sve je u snazi vjere"): st.session_state.q8_v = "vjera"
        
        if st.session_state.get('q8_v') == "zlo":
            izbor8 = st.radio("Što spašava?", ["Prijatelji.", "Dobar posao.", "Ljubav i Isus."], index=None)
            if izbor8 == "Ljubav i Isus.": 
                if st.button("NA 9. POSTAJU"): st.session_state.stage = "pitanje_9"; st.rerun()
        elif st.session_state.get('q8_v') == "vjera":
            st.write("Isus može protjerati zlo svojom milošću.")
            if st.button("NA 9. POSTAJU"): st.session_state.stage = "pitanje_9"; st.rerun()

    # --- PITANJE 9: LEGIJA ---
    elif st.session_state.stage == "pitanje_9":
        st.write("Koga je Isus istjerao iz mladića?")
        izbor9 = st.radio("", ["To su laži!", "To je bila magija!", "Legiju!"], index=None)
        if izbor9 == "Legiju!":
            if st.radio("Vjeruješ li u Boga?", ["Vjerujem!", "Ne vjerujem!"], index=None) == "Vjerujem!":
                if st.button("ŽELIM DALJE"): st.session_state.stage = "final_pitanja"; st.rerun()

    # --- FINALNA PITANJA ---
    elif st.session_state.stage == "final_pitanja":
        st.write("Ne pravi sebi Boga i ne klanjaj mu se...")
        if st.button("Vrijeme je sveto"):
            st.session_state.stage = "test_istine"
            st.rerun()

    elif st.session_state.stage == "test_istine":
        pitanja = ["Vjeruješ li u Boga?", "Prihvaćaš li Isusa?", "Biblija je Božja riječ?", "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?", "Sve laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"]
        
        for i, p in enumerate(pitanja):
            c1, c2 = st.columns([3, 1])
            c1.write(p)
            if c2.button("DA", key=f"d{i}"): st.session_state.score += (1 if i!=8 else -1); st.session_state.odgovoreno_final[i]=True
            if c2.button("NE", key=f"n{i}"): st.session_state.score += (-1 if i!=8 else 1); st.session_state.odgovoreno_final[i]=False

        if None not in st.session_state.odgovoreno_final:
            if st.session_state.score > 5:
                st.success("ČESTITAMO! ZNAČKA VJERNIKA 🛡️")
                st.write("Osvježi stranicu, uzmi Bibliju. Sjeti se: laži su grijeh.")
                st.markdown("[Sve moje aplikacije](https://share.streamlit.io)")
            else:
                st.error("Tama je u vama. Samo Isus donosi svjetlo.")
                ph = st.empty()
                for i in range(7, -1, -1):
                    ph.write(f"Povratak za {i}...")
                    time.sleep(1)
                reset_app()

if __name__ == "__main__":
    main()
