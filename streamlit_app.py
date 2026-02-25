import streamlit as st
import time

# Postavke stranice
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# CSS za zelenu temu i bijeli tekst (bez plave)
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; padding: 10px; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    .tekst-okvir { border: 1px solid #00ff00; padding: 20px; background-color: #002616; margin-bottom: 20px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# Funkcija za izbacivanje nevjernika (7 sekundi mraka)
def kazna_izbacivanje(poruka):
    st.error(poruka)
    st.markdown("<h2 style='color:red; text-align:center;'>OSTAJEŠ U TAMI...</h2>", unsafe_allow_html=True)
    ph = st.empty()
    for i in range(7, -1, -1):
        ph.markdown(f"<h1 style='text-align: center; color: red;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

def main():
    # Inicijalizacija faza
    if 'faza' not in st.session_state: st.session_state.faza = "pocetak"
    if 'bodovi' not in st.session_state: st.session_state.bodovi = 0
    if 'odgovoreno_test' not in st.session_state: st.session_state.odgovoreno_test = {}

    # --- 1. NASLOV ---
    if st.session_state.faza == "pocetak":
        st.markdown("<h1 style='text-align:center; color:#00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>U potrazi za istinom | By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI KROZ VRATA"):
            st.session_state.faza = "uvod_tekst"
            st.rerun()

    # --- 2. UVODNI TEKST (Sada stoji dok ne klikneš!) ---
    elif st.session_state.faza == "uvod_tekst":
        st.markdown("""<div class='tekst-okvir'>
        Nisu svi putevi prema Bogu.<br>Nisu svi koji pričaju o Bogu od Boga.<br>
        Nisu svi prema Božjoj volji.<br>Nisu sve kamene ustanove od Boga.<br><br>
        <b>Tama je gusta.</b><br>Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.
        </div>""", unsafe_allow_html=True)
        if st.button("KRENI DALJE"):
            st.session_state.faza = "pitanje_grijeh"
            st.rerun()

    # --- 3. PITANJE O GRIJEHU ---
    elif st.session_state.faza == "pitanje_grijeh":
        st.markdown("""<div class='tekst-okvir'>
        Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.<br><br>
        I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice a klice žile koje će izrasti u drvo plodno koje će davati plod grijeha.<br><br>
        Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još...
        </div>""", unsafe_allow_html=True)
        odg = st.text_input("KOGA? (Unesi i Enter)", key="input_g").strip().lower()
        if odg:
            if "ne vjerujem u boga" in odg: kazna_izbacivanje("VI STE TAMA I OSTAJETE U TAMI")
            if odg == "grijeha":
                st.success("...i srce polako postane prostor tame.")
                if st.button("NASTAVI U LABIRINT"):
                    st.session_state.faza = "pitanje_andjeli"
                    st.rerun()

    # --- 4. PITANJE O ANĐELIMA ---
    elif st.session_state.faza == "pitanje_andjeli":
        st.markdown("<div class='tekst-okvir'>Jedan od anđela je u sebi stvarao želju da postane - što?</div>", unsafe_allow_html=True)
        izbor = st.radio("Odgovor:", ["Budala!", "Bog", "Fizički radnik!"], index=None)
        if izbor == "Bog":
            if st.button("TOČNO - DALJE"):
                st.session_state.faza = "pitanje_ai"
                st.rerun()
        elif izbor:
            st.error("KRIVO. Istina je samo jedna: BOG.")
            time.sleep(1.5)
            st.session_state.faza = "pitanje_ai"; st.rerun()

    # --- 5. PITANJE O AI ---
    elif st.session_state.faza == "pitanje_ai":
        st.markdown("<div class='tekst-okvir'>Tko još uz pale anđele slično razmišlja?</div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        if c1.button("ZNAM"): st.session_state.ai_zna = "da"
        if c2.button("NE ZNAM"): st.session_state.ai_zna = "ne"
        
        if st.session_state.get('ai_zna') == "ne":
            st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
            if st.button("DALJE"): st.session_state.faza = "otac_lazi"; st.rerun()
        elif st.session_state.get('ai_zna') == "da":
            pog = st.radio("POGODI TKO:", ["Majmuni", "AI & Antena riblja kost!"], index=None)
            if pog == "AI & Antena riblja kost!":
                if st.button("POTVRDI"): st.session_state.faza = "otac_lazi"; st.rerun()

    # --- 6. OTAC LAŽI I PAKAO ---
    elif st.session_state.faza == "otac_lazi":
        st.write("Tko je Otac Laži?")
        ol = st.text_input("Unesi ime:", key="input_ol").strip().lower()
        if ol == "sotona":
            st.markdown("""<div class='tekst-okvir'>
            <b>Zašto vjerujemo da je sve što znamo čista istina?</b><br><br>
            Naučeni smo: Kako na nebu tako i na zemlji. Može biti i: Kako u paklu tako i na zemlji.<br>
            Ljubav hladi, a ljudi traže ljubav u hladnim predmetima.
            </div>""", unsafe_allow_html=True)
            if st.button("IDEM DALJE"): st.session_state.faza = "sobe_izbor"; st.rerun()

    # --- 7. SOBE ---
    elif st.session_state.faza == "sobe_izbor":
        st.write("Odaberi jedna vrata:")
        col1, col2 = st.columns(2)
        if col1.button("Soba: GENERACIJE"): st.session_state.soba_msg = "Biblija neće postojati. Generacije neće tražiti Boga."
        if col2.button("Soba: SOTONA NE MIRUJE"): st.session_state.soba_msg = "Sotona zarobljava ljude i udaljava ih od zapovijedi Isusa Krista."
        if 'soba_msg' in st.session_state:
            st.warning(st.session_state.soba_msg)
            if st.button("VRIJEME JE SVETO"):
                st.session_state.faza = "finalni_test"
                st.rerun()

    # --- 8. FINALNI TEST (10 PITANJA) ---
    elif st.session_state.faza == "finalni_test":
        st.markdown("<h3 style='text-align:center;'>FINALNI TEST ISTINE</h3>", unsafe_allow_html=True)
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?",
            "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?",
            "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]
        
        br = len(st.session_state.odgovoreno_test)
        if br < 10:
            st.subheader(f"Pitanje {br+1} / 10")
            st.write(pitanja[br])
            da, ne = st.columns(2)
            if da.button("DA", key=f"da{br}"):
                st.session_state.bodovi += (1 if br != 8 else -1)
                st.session_state.odgovoreno_test[br] = "DA"; st.rerun()
            if ne.button("NE", key=f"ne{br}"):
                st.session_state.bodovi += (-1 if br != 8 else 1)
                st.session_state.odgovoreno_test[br] = "NE"; st.rerun()
        else:
            # Kraj testa
            if st.session_state.bodovi >= 6:
                st.balloons()
                st.success("ČESTITAMO! IZAŠLI STE IZ TAME. DOBRO DOŠLI U SVJETLO. ZNAČKA VJERNIKA 🛡️")
                st.markdown("[SVE MOJE APLIKACIJE](https://share.streamlit.io)")
                if st.button("VRATI SE NA POČETAK"):
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()
            else:
                kazna_izbacivanje("Labirint je završio, ali TAMA JE U VAMA.")

if __name__ == "__main__":
    main()
