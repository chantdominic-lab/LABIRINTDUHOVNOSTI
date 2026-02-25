import streamlit as st
import time

# Osnovna konfiguracija
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- STIL (Zelena/Crna/Bijela - Bez plave) ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; padding: 10px; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    .autor-box { border: 1px solid #00ff00; padding: 20px; border-radius: 10px; background-color: #002616; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKCIJA ZA KAZNU (NEVJERNICI) ---
def kazna_tama():
    st.markdown("<h1 style='color:red; text-align:center;'>VI STE TAMA I OSTAJETE U TAMI...</h1>", unsafe_allow_html=True)
    ph = st.empty()
    for i in range(7, -1, -1):
        ph.markdown(f"<h1 style='text-align: center; color: red;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    for key in list(st.session_state.keys()): del st.session_state[key]
    st.rerun()

def main():
    if 'stage' not in st.session_state: st.session_state.stage = "naslov"
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'odgovoreno' not in st.session_state: st.session_state.odgovoreno = {}

    # --- 1. NASLOV ---
    if st.session_state.stage == "naslov":
        st.markdown("<h1 style='text-align:center; color:#00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Iz serijala: U potrazi za istinom<br>By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI KROZ VRATA"):
            st.session_state.stage = "uvod"
            st.rerun()

    # --- 2. UVODNI TEKST (Sada je stalan!) ---
    elif st.session_state.stage == "uvod":
        st.markdown("""<div class='autor-box'>
        Nisu svi putevi prema Bogu.<br>Nisu svi koji pričaju o Bogu od Boga.<br>
        Nisu svi prema Božjoj volji.<br>Nisu sve kamene ustanove od Boga.<br><br>
        <b>Tama je gusta.</b><br>Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku.
        </div>""", unsafe_allow_html=True)
        if st.button("DALJE"):
            st.session_state.stage = "pitanje_1"
            st.rerun()

    # --- 3. PITANJE 1: GRIJEH ---
    elif st.session_state.stage == "pitanje_1":
        st.markdown("""<div class='autor-box'>
        Grijeh nije otkrivati lažne puteve i skidati maske koje kriju lažni put prema Bogu a vodi u smrt.<br><br>
        Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još...
        </div>""", unsafe_allow_html=True)
        odg1 = st.text_input("KOGA? (Unesi odgovor i klikni Enter)", key="q1")
        if odg1:
            if "ne vjerujem u boga" in odg1.lower(): kazna_tama()
            if odg1.lower() == "grijeha":
                st.success("i srce polako postane prostor tame.")
                if st.button("NASTAVI"): st.session_state.stage = "pitanje_2"; st.rerun()

    # --- 4. PITANJE 2: ANĐELI ---
    elif st.session_state.stage == "pitanje_2":
        st.markdown("""<div class='autor-box'>
        Jedan od anđela je u sebi stvarao želju da postane - što?
        </div>""", unsafe_allow_html=True)
        izbor2 = st.radio("Odaberi:", ["Budala!", "Bog", "Fizički radnik!"], index=None)
        if izbor2 == "Bog":
            if st.button("TOČNO"): st.session_state.stage = "pitanje_3"; st.rerun()
        elif izbor2:
            st.error("KRIVO. Odgovor je BOG.")
            time.sleep(1); st.session_state.stage = "pitanje_3"; st.rerun()

    # --- 5. PITANJE 3: AI ---
    elif st.session_state.stage == "pitanje_3":
        st.write("Tko još uz pale anđele slično razmišlja?")
        c1, c2 = st.columns(2)
        if c1.button("ZNAM"): st.session_state.q3 = "znam"
        if c2.button("NE ZNAM"): st.session_state.q3 = "neznam"
        
        if st.session_state.get('q3') == "neznam":
            st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
            if st.button("DALJE"): st.session_state.stage = "pitanje_4"; st.rerun()
        elif st.session_state.get('q3') == "znam":
            pog = st.radio("Pogodi tko:", ["Majmuni", "AI & Antena riblja kost!"], index=None)
            if pog == "AI & Antena riblja kost!":
                if st.button("TOČNO"): st.session_state.stage = "pitanje_4"; st.rerun()

    # --- 6. PITANJE 4: OTAC LAŽI ---
    elif st.session_state.stage == "pitanje_4":
        st.write("Tko je Otac Laži?")
        odg4 = st.text_input("", key="q4")
        if odg4.lower() == "sotona":
            st.markdown("<i>Zašto mislimo da je sve što vidimo istina?</i>", unsafe_allow_html=True)
            if st.button("Odmori mozak ili klikni ovdje za dalje"): st.session_state.stage = "pakao"; st.rerun()

    # --- 7. PAKAO NA ZEMLJI ---
    elif st.session_state.stage == "pakao":
        st.markdown("""<div class='autor-box'>
        Naučeni smo na molitvu: <b>Kako na nebu tako i na zemlji.</b><br>
        Može biti i: <b>Kako u paklu tako i na zemlji.</b> Zašto?<br><br>
        Ljubav hladi, a ljudi traže ljubav u hladnim predmetima.
        </div>""", unsafe_allow_html=True)
        if st.button("UĐI U SOBE"): st.session_state.stage = "sobe"; st.rerun()

    # --- 8. SOBE ---
    elif st.session_state.stage == "sobe":
        col1, col2 = st.columns(2)
        if col1.button("GENERACIJE"): st.session_state.s = "Biblija neće postojati."
        if col2.button("SOTONA NE MIRUJE"): st.session_state.s = "Zarobljava ljude od zapovijedi Isusa Krista."
        if 's' in st.session_state:
            st.warning(st.session_state.s)
            if st.button("VRIJEME JE SVETO"): st.session_state.stage = "final"; st.rerun()

    # --- 9. FINALNI TEST (10 PITANJA) ---
    elif st.session_state.stage == "final":
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", "Biblija je Božja riječ?",
            "Sotona je Lažac?", "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?",
            "Sve Laži su opasne?", "Danas čitam Bibliju?", "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]
        curr = len(st.session_state.odgovoreno)
        if curr < 10:
            st.subheader(f"Pitanje {curr+1}/10")
            st.write(pitanja[curr])
            cDA, cNE = st.columns(2)
            if cDA.button("DA", key=f"d{curr}"):
                st.session_state.score += (1 if curr != 8 else -1)
                st.session_state.odgovoreno[curr] = "DA"; st.rerun()
            if cNE.button("NE", key=f"n{curr}"):
                st.session_state.score += (-1 if curr != 8 else 1)
                st.session_state.odgovoreno[curr] = "NE"; st.rerun()
        else:
            if st.session_state.score >= 6:
                st.success("ČESTITAMO! DOBRO DOŠLI U SVJETLO. ZNAČKA VJERNIKA 🛡️")
                st.markdown("[SVE MOJE APP](https://share.streamlit.io)")
                if st.button("KRAJ"):
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()
            else:
                kazna_tama()

if __name__ == "__main__": main()
