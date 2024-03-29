import os
import pygame

tiedoston_nimi = os.path.dirname(__file__)
if ".env" not in os.listdir(os.path.join(tiedoston_nimi, "..")):
    os.system("poetry run invoke build")

from konfiguraatio import get_konfiguraatio, paivita_konfiguraatio

paivita_konfiguraatio()
from tapahtumat import Tapahtumat
from peli.peli_logiikka import Peli
from peli.ihmis_pelaaja import Pelaaja
from käyttöliittymä.lauta_ui import LautaUI
from peli.tekoäly_pelaaja import TekoalyPelaaja
from peli.peli_silmukka import peli_silmukka
from valikko.valikko import Valikko
from käyttöliittymä.valikko_ui import ValikkoUI
from valikko.nappien_tapahtumat import ValitsePelaaja, PelinHallinta, RuudukonKoko

FPS = 20

konffi = get_konfiguraatio()


class Sovellus:
    def __init__(self) -> None:
        pygame.init()
        self.naytto = pygame.display.set_mode((konffi.leveys, konffi.korkeus))
        pygame.display.set_caption("Ristinolla")
        self.tapahtumat = Tapahtumat()

    def main(self):
        pelaaja1 = ValitsePelaaja(TekoalyPelaaja, Pelaaja)
        pelaaja2 = ValitsePelaaja(Pelaaja, TekoalyPelaaja)
        ruudukon_hallinta = RuudukonKoko(konffi.ruutujen_maara)
        kello = pygame.time.Clock()
        kello.tick(FPS)
        while True:
            valikko = Valikko(
                self.tapahtumat,
                self.naytto,
                ValikkoUI,
                ruudukon_hallinta,
                pelaaja1,
                pelaaja2,
                PelinHallinta,
            )
            valikko.aloita()
            if valikko.aloita_peli:
                while True:
                    peli = Peli(
                        self.tapahtumat,
                        pelaaja1.valittu_pelaaja,
                        pelaaja2.valittu_pelaaja,
                        LautaUI,
                        self.naytto,
                    )
                    tapahtuma = peli_silmukka(peli)
                    if tapahtuma == "pelaa uudelleen":
                        continue
                    if tapahtuma == "takaisin":
                        break
                    if tapahtuma == "lopeta":
                        return
            else:
                return


if __name__ == "__main__":
    sovellus = Sovellus()
    sovellus.main()
    print()
    print("see you later, alligator")
