import pygame
from konfiguraatio import get_konfiguraatio
from peli.tapahtumat import Tapahtumat
from peli.peli_logiikka import Peli
from peli.ihmis_pelaaja import Pelaaja
from käyttöliittymä.lauta import LautaUI
from peli.tekoäly_pelaaja import TekoalyPelaaja
from peli.peli_silmukka import peli_silmukka
FPS = 20

konffi = get_konfiguraatio()

LEVEYS = konffi["leveys"]
KORKEUS = konffi["korkeus"]



class Sovellus:
    def __init__(self) -> None:
        pygame.init()
        ikkuna = pygame.display.set_mode((LEVEYS, KORKEUS))
        pygame.display.set_caption("Ristinolla")
        self.tapahtumat = Tapahtumat()
        self.peli = Peli(
            self.tapahtumat,
            Pelaaja,
            TekoalyPelaaja,
            LautaUI,
            ikkuna
        )

    def main(self):
        kello = pygame.time.Clock()
        
        kello.tick(FPS)
        return peli_silmukka(self.peli)


if __name__ == "__main__":
    while True:
        sovellus = Sovellus()
        paluuarvo = sovellus.main()
        if paluuarvo == "pelaa_uudelleen":
            continue
        print("see you later, alligator")
        break
