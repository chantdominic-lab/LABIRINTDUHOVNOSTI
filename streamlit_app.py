import pygame
import sys
import time

# Inicijalizacija
pygame.init()
ekran = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Labirint Duhovnosti - Dominic Chant")

# Boje i Fontovi
ZELENA = (0, 255, 65)
BIJELA = (255, 255, 255)
CRNA = (0, 0, 0)
font_misterij = pygame.font.SysFont("Courier", 22, bold=True)
font_citat = pygame.font.SysFont("Georgia", 24, italic=True) # Georgia daje svečaniji ton

def uvodna_sekvenca():
    # 1. Zeleni dio - Tama je gusta
    ekran.fill(CRNA)
    
    # Efekt pojavljivanja (Fade-in) za "Tama je gusta."
    for alpha in range(0, 255, 3):
        ekran.fill(CRNA)
        tekst = font_misterij.render("Tama je gusta.", True, ZELENA)
        tekst.set_alpha(alpha)
        rect = tekst.get_rect(center=(400, 300))
        ekran.blit(tekst, rect)
        pygame.display.flip()
        pygame.time.delay(20)
    
    time.sleep(3) # Ostaje na ekranu 3 sekunde

    # Efekt nestajanja (Fade-out)
    for alpha in range(255, 0, -5):
        ekran.fill(CRNA)
        tekst = font_misterij.render("Tama je gusta.", True, ZELENA)
        tekst.set_alpha(alpha)
        ekran.blit(tekst, rect)
        pygame.display.flip()
        pygame.time.delay(20)

    time.sleep(1) # Kratka potpuna tama prije bijelih slova

    # 2. Bijeli dio - Božja riječ
    poruka_bijela = "Čvršće nego ikad prije moramo držati Božju riječ u ruku i srcu, umu i na jeziku."
    
    # Funkcija za prijelom teksta (da ne izađe izvan ekrana)
    words = poruka_bijela.split(' ')
    lines = [" ".join(words[:7]), " ".join(words[7:])] # Dijelimo rečenicu u dva reda
    
    for alpha in range(0, 255, 2):
        ekran.fill(CRNA)
        y_offset = -20
        for line in lines:
            tekst_bijeli = font_citat.render(line, True, BIJELA)
            tekst_bijeli.set_alpha(alpha)
            rect_bijeli = tekst_bijeli.get_rect(center=(400, 300 + y_offset))
            ekran.blit(tekst_bijeli, rect_bijeli)
            y_offset += 40
        pygame.display.flip()
        pygame.time.delay(30)

# Pokretanje
try:
    # Ovdje idu one uvodne poruke od ranije...
    # Zatim:
    uvodna_sekvenca()
    
    # Drži prozor otvorenim dok korisnik ne ugasi
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
finally:
    pygame.quit()
    sys.exit()
