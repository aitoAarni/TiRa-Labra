from valikko.nappi import Nappi
from konfiguraatio import get_konfiguraatio
import pygame

konffi = get_konfiguraatio()
LEVEYS, KORKEUS, RUUTUJEN_MAARA = konffi["leveys"], konffi["korkeus"], konffi["ruutujen_määrä"]

class Napit:
    def __init__(self, ruudukon_hallinta, pelaaja1, pelaaja2, pelin_hallinta) -> None:
        self.napit = muodosta_napit(LEVEYS, KORKEUS, ruudukon_hallinta, pelaaja1, pelaaja2, pelin_hallinta)
        self.nappi_jonka_paalla_on_hiiri = None


    def tarkista_onko_hiiri_napin_paalla(self, hiiri_pos):
        for nappi in self.napit.sprites():
            if nappi.havaitse_hiiren_leijuminen(hiiri_pos):
                self.nappi_jonka_paalla_on_hiiri = nappi
                return
        self.nappi_jonka_paalla_on_hiiri = None

    def aktivoi_klikattu_nappi(self):
        if self.nappi_jonka_paalla_on_hiiri:
            self.nappi_jonka_paalla_on_hiiri.aktivoi_tapahtuma()





def muodosta_napit(leveys, korkeus, ruudukon_hallinta, pelaaja1, pelaaja2, pelin_hallinta):
    n_leveys = leveys / 40
    n_korkeus = korkeus / 40

    keski_x = leveys /2
    keski_y = korkeus / 2

    x_offsetti = 7.5 * n_leveys
    y_alkukorkeus = keski_y - n_korkeus * 4

    ruutuja_vahemman_nappi = Nappi(n_leveys, n_korkeus, (keski_x - x_offsetti, y_alkukorkeus), ruudukon_hallinta.vahenna_ruutuja, "<")
    ruutuja_enemman_nappi = Nappi(n_leveys, n_korkeus, (keski_x + x_offsetti, y_alkukorkeus), ruudukon_hallinta.lisaa_ruutuja, ">")
    
    vasen_vaihda_pelaajaa1_nappi = Nappi(n_leveys, n_korkeus, (keski_x - x_offsetti, y_alkukorkeus + n_korkeus * 4), pelaaja1.vaihda_pelaajaa, "<")
    oikea_vaihda_pelaajaa1_nappi = Nappi(n_leveys, n_korkeus, (keski_x + x_offsetti, y_alkukorkeus + n_korkeus * 4), pelaaja1.vaihda_pelaajaa, ">")

    vasen_vaihda_pelaajaa2_nappi = Nappi(n_leveys, n_korkeus, (keski_x - x_offsetti, y_alkukorkeus + n_korkeus * 8), pelaaja2.vaihda_pelaajaa, "<")
    oikea_vaihda_pelaajaa2_nappi = Nappi(n_leveys, n_korkeus, (keski_x + x_offsetti, y_alkukorkeus + n_korkeus * 8), pelaaja2.vaihda_pelaajaa, ">")

    pelaa_nappi = Nappi(10*n_leveys, 4 * n_korkeus, (keski_x, y_alkukorkeus + n_korkeus * 12), pelin_hallinta.aloita_peli_tapahtuma, "Pelaa")

    napit = pygame.sprite.Group(ruutuja_vahemman_nappi, ruutuja_enemman_nappi, vasen_vaihda_pelaajaa1_nappi, oikea_vaihda_pelaajaa1_nappi, vasen_vaihda_pelaajaa2_nappi, oikea_vaihda_pelaajaa2_nappi, pelaa_nappi)

    return napit
