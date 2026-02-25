import streamlit as st
import time

# Osnovne postavke
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- CSS: Bez plave, samo tamnozelena i bijela ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; padding: 12px; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    .autor-tekst { border: 1px solid #00ff00; padding: 25px; background-color: #002616; border-radius: 10px; line-height: 1.6; margin-bottom: 20px; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKCIJA ZA KAZNU (TAMA I REFRESH) ---
def pokreni_kaznu(poruka):
    st.error(poruka)
    st.markdown("<h2 style='color:red; text-align:center;'>VI STE TAMA I OSTAJETE U TAMI...</h2>", unsafe_allow_html=True)
    ph = st.empty()
    for i in range(7, -1, -1):
        ph.markdown(f"<h1 style='text-align: center; color: red;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    for key in list(st.session_state.keys()): del st.session_state[key]
    st.rerun()

def main():
    # Inicijalizacija faza (Stages)
    if 'korak' not in st.session_state: st.session_state.korak = 0
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'finalni_odgovori' not in st.session_state: st.session_state.finalni_odgovori = {}

    # --- KORAK 0: NASLOV ---
    if st.session_state.korak == 0:
        st.markdown("<h1 style='text-align:center; color:#00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>U potrazi za istinom | By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI KROZ VRATA"):
            st.session_state.korak = 1
            st.rerun()

    # --- KORAK 1: UVODNI TEKST ---
    elif st.session_state.korak == 1:
        st.markdown("<div class='autor-tekst'>Nisu svi putevi prema Bogu.<br>Nisu svi koji pričaju o Bogu od Boga.<br>Nisu svi prema Božjoj volji.<br>Nisu sve kamene ustanove od Boga.</div>", unsafe_allow_html=True)
        if st.button("DALJE"):
            st.session_state.korak = 2
            st.rerun()

    # --- KORAK 2: TAMA ---
    elif st.session_state.korak == 2:
        st.markdown("<div class='autor-tekst'><b>Tama je gusta.</b><br><br>Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.</div>", unsafe_allow_html=True)
        if st.button("UĐI U DUBINU"):
            st.session_state.korak = 3
            st.rerun()

    # --- KORAK 3: PITANJE GRIJEH ---
    elif st.session_state.korak == 3:
        st.markdown("<div class='autor-tekst'>Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.<br><br>I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice a klice žile koje će izrasti u drvo plodno koje će davati plod grijeha.<br><br>Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još...</div>", unsafe_allow_html=True)
        un_g = st.text_input("KOGA? (Unesi odgovor i Enter)", key="g_in").strip().lower()
        if un_g:
            if "ne vjerujem u boga" in un_g: pokreni_kaznu("NEVJERA VODI U MRAK")
            if un_g == "grijeha":
                st.success("...i srce polako postane prostor tame.")
                if st.button("NASTAVI"): st.session_state.korak = 4; st.rerun()

    # --- KORAK 4: ANĐELI ---
    elif st.session_state.korak == 4:
        st.markdown("<div class='autor-tekst'>Jedan od anđela je u sebi stvarao želju da postane - što?</div>", unsafe_allow_html=True)
        izb = st.radio("Odgovor:", ["Budala!", "Bog", "Fizički radnik!"], index=None)
        if izb == "Bog":
            if st.button("TOČNO"): st.session_state.korak = 5; st.rerun()
        elif izb:
            st.error("KRIVO. Odgovor je BOG.")
            time.sleep(1.5); st.session_state.korak = 5; st.rerun()

    # --- KORAK 5: AI ---
    elif st.session_state.korak == 5:
        st.write("Tko još uz pale anđele slično razmišlja?")
        c1, c2 = st.columns(2)
        if c1.button("ZNAM"): st.session_state.ai = "zna"
        if c2.button("NE ZNAM"): st.session_state.ai = "nezna"
        
        if st.session_state.get('ai') == "nezna":
            st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
            if st.button("DALJE"): st.session_state.korak = 6; st.rerun()
        elif st.session_state.get('ai') == "zna":
            p = st.radio("POGODI TKO:", ["Majmuni", "AI & Antena riblja kost!"], index=None)
            if p == "AI & Antena riblja kost!":
                if st.button("POTVRDI"): st.session_state.korak = 6; st.rerun()

    # --- KORAK 6: OTAC LAŽI I PAKAO ---
    elif st.session_state.korak == 6:
        st.write("Tko je Otac Laži?")
        l_in = st.text_input("", key="l_in").strip().lower()
        if l_in == "sotona":
            st.markdown("<div class='autor-tekst'>Zašto vjerujemo da je sve što znamo čista istina?<br><br>Naučeni smo: Kako na nebu tako i na zemlji. Može biti i: Kako u paklu tako i na zemlji.<br><br>Ljubav hladi, a ljudi traže ljubav u hladnim predmetima.</div>", unsafe_allow_html=True)
            if st.button("Odmori mozak ili klikni ovdje za dalje"): st.session_state.korak = 7; st.rerun()

    # --- KORAK 7: SOBE ---
    elif st.session_state.korak == 7:
        st.write("Izaberi smjer:")
        col1, col2 = st.columns(2)
        if col1.button("Soba: GENERACIJE"): st.session_state.s_msg = "Biblija neće postojati. Generacije neće tražiti Boga."
        if col2.button("Soba: SOTONA NE MIRUJE"): st.session_state.s_msg = "Sotona udaljava ljude od zapovijedi Isusa Krista."
        if 's_msg' in st.session_state:
            st.warning(st.session_state.s_msg)
            if st.button("VRIJEME JE SVETO"): st.session_state.korak = 8; st.rerun()

    # --- KORAK 8: TEST OD 10 PITANJA (JEDNO PO JEDNO) ---
    elif st.session_state.korak == 8:
        pitanja = ["Vjeruješ li u Boga?", "Prihvaćaš li Isusa?", "Biblija je Božja riječ?", "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?", "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"]
        br = len(st.session_state.finalni_odgovori)
        
        if br < 10:
            st.subheader(f"Test Istine: {br+1}/10")
            st.write(f"**{pitanja[br]}**")
            da, ne = st.columns(2)
            if da.button("DA", key=f"d{br}"):
                # Na deveto pitanje (indeks 8), DA je netočan odgovor (-1)
                st.session_state.score += (1 if br != 8 else -1)
                st.session_state.finalni_odgovori[br] = "DA"; st.rerun()
            if ne.button("NE", key=f"n{br}"):
                # Na deveto pitanje (indeks 8), NE je točan odgovor (+1)
                st.session_state.score += (-1 if br != 8 else 1)
                st.session_state.finalni_odgovori[br] = "NE"; st.rerun()
        else:
            # POPRAVLJENO: st.session_state.score umjesto st.score
            if st.session_state.score >= 6:
                st.success("ČESTITAMO! DOBRO DOŠLI U SVJETLO. ZNAČKA VJERNIKA 🛡️")
                st.markdown("[SVE MOJE APLIKACIJE](https://share.streamlit.io)")
                if st.button("KRAJ"): 
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()
            else:
                pokreni_kaznu("Labirint je završio, ali TAMA JE U VAMA.")

if __name__ == "__main__":
    main()
