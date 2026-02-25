import streamlit as st
import time

# --- KONFIGURACIJA ---
st.set_page_config(page_title="Labirint - U potrazi za istinom", page_icon="🚪", layout="centered")

# --- CSS (Bez plave, zelena tema, bijeli tekst) ---
st.markdown("""
    <style>
    .stApp { background-color: #001a0f; color: white; }
    .stTextInput input { color: white !important; background-color: #002b1b !important; border: 1px solid #00ff00 !important; }
    .stButton>button { background-color: #004d33; color: white; border: 1px solid white; width: 100%; font-weight: bold; padding: 12px; }
    .stButton>button:hover { background-color: #008000; border: 2px solid white; }
    #MainMenu, footer, header {visibility: hidden;}
    .autor-tekst { border: 1px solid #00ff00; padding: 25px; background-color: #002616; border-radius: 10px; line-height: 1.6; margin-bottom: 20px; font-size: 1.1em; white-space: pre-line; }
    .badge { background-color: #00ff00; color: black; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNKCIJA ZA REFRESH I KAZNU ---
def reset_i_izbaci(poruka):
    st.error(poruka)
    ph = st.empty()
    for i in range(7, -1, -1):
        ph.markdown(f"<h1 style='text-align: center; color: red;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)
    for key in list(st.session_state.keys()): del st.session_state[key]
    st.rerun()

def main():
    # Inicijalizacija session state-a
    if 'k' not in st.session_state: st.session_state.k = 0
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'test_odgovori' not in st.session_state: st.session_state.test_odgovori = {}

    # --- KORACI LABIRINTA (0-13 Prethodni koraci) ---
    # (Ovdje ide tvoj prethodni sadržaj do Naslova 2 - skraćeno zbog fokusa na tvoj novi dodatak)
    
    if st.session_state.k == 0:
        st.markdown("<h1 style='text-align:center; color:#00ff00;'>LABIRINT</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>U potrazi za istinom | By Dominic Chant</p>", unsafe_allow_html=True)
        if st.button("UĐI KROZ VRATA"): st.session_state.k = 1; st.rerun()

    elif st.session_state.k == 1: # Prethodni uvod, grijeh, andjeli, ai, otac lazi (spojeno u faze)
        st.markdown("<div class='autor-tekst'>Kroz labirint spoznaje...</div>", unsafe_allow_html=True)
        if st.button("ZAPOČNI"): st.session_state.k = 13; st.rerun()

    # --- NOVI DIO OD NASLOVA 2 ---
    elif st.session_state.k == 13:
        st.markdown("### Izaberi put:")
        c1, c2 = st.columns(2)
        if c1.button("Zašto se događaju zle stvari?"): st.session_state.put = "zlo"
        if c2.button("Sve je u snazi vjere"): st.session_state.put = "vjera"

        if st.session_state.get('put') == "zlo":
            st.markdown("<div class='autor-tekst'>Možda se neke zle stvari događaju i nevini plaćaju da ostatak ljudi otvori oči...</div>", unsafe_allow_html=True)
            if st.button("IDEM DALJE"): st.session_state.k = 14; st.rerun()
        
        elif st.session_state.get('put') == "vjera":
            st.markdown("<div class='autor-tekst'>Sotona se plaši Isusa i samo izgovaranje imena Isus Sotona drhti... to je trik za psihu. Sotona se ne plaši imena, nego same milosti kad se On pojavi u prostoru.</div>", unsafe_allow_html=True)
            if st.button("IDEM DALJE"): st.session_state.k = 14; st.rerun()

    elif st.session_state.k == 14:
        st.write("Ako ne postoje duhovi i Sotona? Koga je Isus istjerao iz mladića?")
        izb_l = st.radio("Odgovor:", ["To su laži!", "To je bila magija!", "Legiju!"], index=None)
        if izb_l == "Legiju!":
            if st.button("TOČNO - DALJE"): st.session_state.k = 15; st.rerun()

    elif st.session_state.k == 15:
        st.write("Vjeruješ li u Boga?")
        c1, c2 = st.columns(2)
        if c1.button("Vjerujem!"): st.session_state.vjera = "da"; st.session_state.k = 16; st.rerun()
        if c2.button("Ne vjerujem!"): st.session_state.vjera = "ne"; st.session_state.k = 16; st.rerun()

    elif st.session_state.k == 16:
        if st.session_state.get('vjera') == "ne":
            st.warning("Tko je Otac Laži?")
            ol = st.text_input("").strip().lower()
            if ol == "sotona":
                if st.button("NASTAVI"): st.session_state.k = 17; st.rerun()
        else:
            st.session_state.k = 17; st.rerun()

    elif st.session_state.k == 17:
        st.write("Želiš li nastaviti dublje kroz duhovne tekstove i tražiti izlaz?")
        c1, c2 = st.columns(2)
        if c1.button("Želim!"): 
            st.session_state.k = 19; st.rerun() # Ide na idolopoklonstvo
        if c2.button("Ne želim!"):
            st.markdown("<div class='autor-tekst'>Žao mi je! Vrata Labirinta se zatvaraju... Ne gubi sekunde, vrijeme je svetost.</div>", unsafe_allow_html=True)
            time.sleep(2)
            reset_i_izbaci("POVRATAK NA POČETAK")

    elif st.session_state.k == 19:
        st.markdown("<div class='autor-tekst'>Ne pravi sebi Boga i ne klanjaj mu se i ništa što je na nebu ili zemlji ne pravi obličja i ne moli se mrtvim predmetima.</div>", unsafe_allow_html=True)
        if st.button("Vrijeme je sveto"): st.session_state.k = 20; st.rerun()

    # --- FINALNI TEST (10 PITANJA) ---
    elif st.session_state.k == 20:
        pitanja = [
            "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", 
            "Biblija je pisana Božja riječ?", "Sotona je Lažac?", 
            "Vrijeme prolazi brzo?", "Grijeh privlači grijeh?", 
            "Sve Laži su opasne?", "Danas čitam Bibliju?", 
            "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
        ]
        
        br = len(st.session_state.test_odgovori)
        if br < 10:
            st.subheader(f"Pitanje {br+1}/10")
            st.write(pitanja[br])
            col_da, col_ne = st.columns(2)
            
            if col_da.button("DA", key=f"da_{br}"):
                st.session_state.score += (1 if br != 8 else -1)
                st.session_state.test_odgovori[br] = "DA"; st.rerun()
            if col_ne.button("NE", key=f"ne_{br}"):
                st.session_state.score += (-1 if br != 8 else 1)
                st.session_state.test_odgovori[br] = "NE"; st.rerun()
        else:
            if st.session_state.score >= 6:
                st.success("ČESTITAMO! Izašli ste iz tame dobro došli u svjetlo kraj labirinta!")
                st.markdown("<div class='badge'>ZNAČKA VJERNIKA DODIJELJENA 🛡️</div>", unsafe_allow_html=True)
                st.write("Molim te ovdje osvježi stranicu i klikni na X zatvori ovo i uzmi Bibliju sjeti se laži su grijeh.")
                st.markdown("[SVE MOJE APLIKACIJE](https://share.streamlit.io)")
            else:
                reset_i_izbaci("Labirint je završio izašli ste iz tame labirinta ali tama je u vama i samo Isus donosi svjetlo pronađi ga u Bibliji.")

if __name__ == "__main__": main()
