# --- 18. FINALNA SOBA: VRIJEME JE SVETO (KRAJ LABIRINTA) ---
elif st.session_state.faza == 'VRIJEME_SVETO':
    st.markdown('<p class="zelena">VRIJEME JE SVETO</p>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="bijela-it">Ne pravi sebi Boga i ne klanjaj mu se i ništa što je na nebu ili zemlji ne pravi obličja i ne moli se mrtvim predmetima.</p>', unsafe_allow_html=True)
    
    # Lista pitanja za duhovni test
    pitanja_test = [
        "Vjeruješ li u Boga?", "Prihvaćaš li Isusa za spasitelja?", 
        "Biblija je pisana Božja riječ?", "Sotona je Lažac?", 
        "Vrijeme prolazi brzo?", "Grijeh privlači grijeh", 
        "Sve Laži su opasne?", "Danas čitam Bibliju?", 
        "Kada umremo tada je kraj?", "Ne čekaj uzmi Bibliju?"
    ]
    
    # Koristimo formu kako bismo obradili sve odjednom
    with st.form("duhovni_test"):
        rezultati = []
        for i, pitanje in enumerate(pitanja_test):
            # Da ili Ne butoni (radio)
            odg = st.radio(pitanje, ["Ne", "Da"], key=f"final_{i}", horizontal=True)
            rezultati.append(odg)
        
        submit = st.form_submit_button("ZAVRŠI I IZAĐI IZ LABIRINTA")
        
        if submit:
            # Zbrajanje pozitivnih odgovora
            # (Pitanje "Kada umremo tada je kraj?" je trik pitanje, ali ovdje zbrajamo čiste 'Da' odgovore za vjeru)
            broj_da = rezultati.count("Da")
            
            if broj_da >= 7: # Prag za izlazak u svjetlo
                st.balloons()
                st.markdown('<p class="zelena" style="font-size: 30px;">ČESTITAMO!</p>', unsafe_allow_html=True)
                st.success("Izašli ste iz tame, dobro došli u svjetlo!")
                
                # Značka vjernika
                st.markdown("""
                    <div style="border: 2px solid #00FF41; padding: 20px; text-align: center; border-radius: 10px;">
                        <h2 style="color: #00FF41;">🛡️ ZNAČKA VJERNIKA</h2>
                        <p style="color: white;">Molim te ovdje osvježi stranicu i klikni na x zatvori ovo i uzmi Bibliju.<br>
                        <b>Sjeti se: laži su grijeh.</b></p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.write("---")
                st.markdown(f'<p class="autor-tekst">Sve aplikacije: <a href="https://share.streamlit.io" target="_blank" style="color:#00FF41;">🔗 MOJI PROJEKTI</a></p>', unsafe_allow_html=True)
            
            else:
                # Korisnik je ostao u tami
                st.warning("Labirint je završio. Izašli ste iz tame labirinta ali tama je u vama i samo Isus donosi svjetlo, pronađi ga u Bibliji.")
                
                # Odbrojavanje od sedam prema nuli
                placeholder_kraj = st.empty()
                for i in range(7, -1, -1):
                    placeholder_kraj.markdown(f'<p class="odbrojavanje">{i}</p>', unsafe_allow_html=True)
                    time.sleep(1)
                
                # Reset na početak igre
                st.session_state.clear()
                st.rerun()

# --- KRAJ LABIRINTA DUHOVNOSTI ---
