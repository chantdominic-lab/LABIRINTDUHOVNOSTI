# --- 6. LOGIKA LABIRINTA: OD GRIJEHA DO KRAJA ---

# FAZA: GRIJEH I SJEME
elif st.session_state.faza == 'GRIJEH':
    st.write("I treba pazit da od previše priče ne stvori se sjeme koje će pustit klice a klice žile koje će izrasti u drvo plodno koje će davati plod grijeha.")
    st.write("Previše priče ogovaranja i pametovanja protiv drugih pred drugima može polako stvarati grijeh a mali grijeh privuče još...")
    st.markdown('<p style="color:#00FF41;">(koga?)</p>', unsafe_allow_html=True)
    odg_g = st.text_input("", key="qg", placeholder="Upiši odgovor...").lower().strip()
    if odg_g == "grijeha":
        st.markdown('<p class="bijela-velika">...i srce polako postane prostor tame.</p>', unsafe_allow_html=True)
        if st.button("NASTAVI"): st.session_state.faza = 'ANDJELI'; st.rerun()

# FAZA: ANĐELI I POBUNA
elif st.session_state.faza == 'ANDJELI':
    st.write("Oduvijek stvorenje ima nagon da bude: obožavan, slavan, moćan, i da bude poput boga.")
    st.write("U vrijeme pobune anđela, oni se nisu pobunili zbog 'zlata' nego nisu više željeli biti poslušni bogu. Jedan od anđela je u sebi stvarao želju da postane - što?")
    c1, c2, c3 = st.columns(3)
    if c1.button("Budala!"): st.error("Krivo.")
    if c2.button("Fizički radnik!"): st.error("Krivo.")
    if c3.button("bog!"): st.session_state.faza = 'DANAŠNJE_VRIJEME'; st.rerun()

# FAZA: DANAŠNJE VRIJEME I AI
elif st.session_state.faza == 'DANAŠNJE_VRIJEME':
    st.markdown('<p class="zelena-autor" style="font-size:30px;">Što se događa u današnje vrijeme?</p>', unsafe_allow_html=True)
    st.markdown('<p class="bijela-velika">Težnja nagona da čovjek postane bog.</p>', unsafe_allow_html=True)
    st.write("Tko još uz pale anđele slično razmišlja?")
    c1, col2 = st.columns(2)
    if c1.button("Znam."): st.session_state.ai_put = 'znam'
    if col2.button("Ne znam."):
        st.info("Umjetna inteligencija prije ili poslije će razviti svijest i ideju da postane bog.")
        if st.button("IDEMO DALJE"): st.session_state.faza = 'OTAC_LAZI'; st.rerun()
    if st.session_state.get('ai_put') == 'znam':
        izb = st.radio("Pogodi:", ["Gorile i Majmuni!", "Tarzan i Jane!", "AI & Antena riblja kost!"])
        if izb == "AI & Antena riblja kost!" and st.button("OTVORI PUT"):
            st.session_state.faza = 'OTAC_LAZI'; st.rerun()

# FAZA: OTAC LAŽI I ISTINA
elif st.session_state.faza == 'OTAC_LAZI':
    st.write("Tko je Otac Laži?")
    odg_ol = st.text_input("", key="ol", placeholder="...").lower().strip()
    if odg_ol == "sotona":
        st.markdown('<p class="bijela-velika">Zašto onda mislimo i vjerujemo da sve što vidimo i znamo je čista istina?</p>', unsafe_allow_html=True)
        if st.button("Odmori mozak ili klikni ovdje za dalje"): st.session_state.faza = 'PAKAL'; st.rerun()

# FAZA: PAKAL I HLADNOĆA
elif st.session_state.faza == 'PAKAL':
    st.write("Naučeni smo na molitvu Oče Naš u kojoj kaže: Kako na nebu tako i na zemlji.")
    st.markdown('Nitko ne govori da lako može biti i ovo: Kako u <span style="color:red; font-weight:bold;">paklu</span> tako i na zemlji. Zašto?', unsafe_allow_html=True)
    st.write("Otvori oči i prvo što ćeš vidjeti da ljubav hladi i da istinu upotpuni ono što je kao predmet hladno u tome ljudi traže ljubav.")
    if st.button("NOVI TEKST"): st.session_state.faza = 'GLAD'; st.rerun()

# FAZA: GLAD I MRTVI
elif st.session_state.faza == 'GLAD':
    st.write("Bez Boga i duhovne tematike će ljudi biti gladni... Bez Boga smo...?")
    c1, c2, c3 = st.columns(3)
    if c1.button("mrtvi!"): st.session_state.faza = 'SOBE'; st.rerun()
    if c2.button("slobodni!") or c3.button("izgubljeni!"): st.error("Krivo.")

# FAZA: SOBE (GENERACIJE / SOTONA)
elif st.session_state.faza == 'SOBE':
    cl, cd = st.columns(2)
    if cl.button("Generacije"): st.info("Generacije koje dolaze neće tražiti Boga... Biblija neće postojati.")
    if cd.button("Sotona ne miruje"): st.info("Sotona lagano zarobljava ljude i udaljava ih od zapovijedi Isusa Krista.")
    if st.button("ŠTO JE POČETAK MUDROSTI?"): st.session_state.faza = 'MUDROST'; st.rerun()

# FAZA: MUDROST I TAMU
elif st.session_state.faza == 'MUDROST':
    st.write("Početak mudrosti je?")
    odg = st.radio("", ["Gospodnji strah početak je mudrosti...", "Dremnuti.", "Kasno se probuditi."])
    if st.button("POTVRDI"):
        if "Gospodnji strah" in odg: st.session_state.faza = 'UNUTRAŠNJI_RAT'; st.rerun()
        else: izbaci_u_tamu("Krivo. Labirint se zatvara!")

elif st.session_state.faza == 'UNUTRAŠNJI_RAT':
    st.write("Strah Božji je početak mudrosti. Čovjek može biti uništen iznutra i bez rata. Ako se okrenemo izvoru života i primamo snagu od svjetlosti tada možda i pobijedimo...?")
    odg_t = st.radio("", ["Tamu.", "Sami sebe.", "Hladne dane."])
    if odg_t == "Tamu." and st.button("IDEMO DALJE"): st.session_state.faza = 'DVA_NASLOVA'; st.rerun()

# FAZA: DVA NASLOVA
elif st.session_state.faza == 'DVA_NASLOVA':
    c1, c2 = st.columns(2)
    if c1.button("Zašto se događaju zle stvari?"): st.session_state.naslov = 'ZLO'
    if c2.button("Sve je u snazi vjere"): st.session_state.naslov = 'VJERA'

    if st.session_state.get('naslov') == 'ZLO':
        st.write("Materijalno ne spašava, nego?")
        if st.radio("", ["Prijatelji.", "Dobar posao.", "Ljubav i Isus."]) == "Ljubav i Isus." and st.button("DALJE"): st.session_state.faza = 'LEGIJA'; st.rerun()
    elif st.session_state.get('naslov') == 'VJERA':
        st.write("Sotona se ne plaši imena Isus, samo Isus može protjerati zlo svojom milošću...")
        if st.button("KOGA JE ISUS ISTJERAO?"): st.session_state.faza = 'LEGIJA'; st.rerun()

# FAZA: LEGIJA I TEST VJERE (TVOJ ZAHTJEV ZA IZBACIVANJE)
elif st.session_state.faza == 'LEGIJA':
    st.write("Koga je Isus istjerao iz mladića u krdo svinja?")
    odg_l = st.radio("", ["To su laži!", "To je bila magija!", "Legiju!"])
    if st.button("PROVJERI"):
        if odg_l == "Legiju!": st.session_state.faza = 'FINALNI_TEST_VJERE'; st.rerun()
        else: izbaci_u_tamu("Nevjera zatvara vrata Labirinta!")

elif st.session_state.faza == 'FINALNI_TEST_VJERE':
    st.markdown('<p class="bijela-velika">Vjeruješ li u Boga?</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("Vjerujem!"): st.session_state.faza = 'ZADNJA_SOBA'; st.rerun()
    if c2.button("Ne vjerujem!"):
        st.write("Tko je Otac Laži?")
        ol = st.text_input("", key="ol_kraj").lower().strip()
        if ol == "sotona": izbaci_u_tamu("Vi ste tama i ostajete u Tami. Labirint se zatvara!")

elif st.session_state.faza == 'ZADNJA_SOBA':
    st.write("Želiš li nastaviti dublje kroz duhovne tekstove?")
    c1, c2 = st.columns(2)
    if c1.button("Želim!"): st.session_state.faza = 'VRIJEME_SVETO'; st.rerun()
    if c2.button("Ne želim!"): izbaci_u_tamu("Žao mi je! Vrata se zatvaraju... Svjetlo potraži u Bibliji.")
