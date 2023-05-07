from valikko.nappi import Nappi
from konfiguraatio import get_konfiguraatio
import pygame

konffi = get_konfiguraatio()


class Napit:
    """Luokka on valikon nappien hallintaa varten"""

    def __init__(self, ruudukon_hallinta, pelaaja1, pelaaja2, pelin_hallinta) -> None:
        """konstruktori

        Args:
            ruudukon_hallinta (Object): Ruutujen määrää hallitseva olio
            pelaaja1 (Object): Ristejä pelaavan pelaajan valinta
            pelaaja2 (Object): Nollia pelaavan pelaajan valinta
            pelin_hallinta (Object): konfiguraation ja pelin aloitusta varten
        """
        self.napit = muodosta_napit(
            konffi.leveys,
            konffi.korkeus,
            ruudukon_hallinta,
            pelaaja1,
            pelaaja2,
            pelin_hallinta,
        )
        self.nappi_jonka_paalla_on_hiiri = None

    def tarkista_onko_hiiri_napin_paalla(self, hiiri_pos):
        """Tarkistaa onko hiiri minkään napin päällä"""
        for nappi in self.napit.sprites():
            if nappi.havaitse_hiiren_leijuminen(hiiri_pos):
                self.nappi_jonka_paalla_on_hiiri = nappi
                return
        self.nappi_jonka_paalla_on_hiiri = None

    def aktivoi_klikattu_nappi(self):
        """aktvoi napin tapahtuma 'onClick' efekti"""
        if self.nappi_jonka_paalla_on_hiiri:
            self.nappi_jonka_paalla_on_hiiri.aktivoi_tapahtuma()


def muodosta_nappi(leveys, korkeus, keskipiste, napin_tapahtuma, teksti):
    """Muodostaa napin saatujen parametrien avulla"""
    return Nappi(leveys, korkeus, keskipiste, napin_tapahtuma, teksti)


def muodosta_napit(
    leveys, korkeus, ruudukon_hallinta, pelaaja1, pelaaja2, pelin_hallinta
):
    """Muodostaa valikon napit ja laittaa ne oikeaan kohtaan"""
    n_leveys = leveys / 30
    n_korkeus = korkeus / 30

    keski_x = leveys / 2
    keski_y = korkeus / 2

    x_offsetti = 7.5 * n_leveys
    y_alkukorkeus = keski_y - n_korkeus * 8

    napit = []

    napit.append(
        muodosta_nappi(
            n_leveys,
            n_korkeus,
            (keski_x - x_offsetti, y_alkukorkeus),
            ruudukon_hallinta.vahenna_ruutuja,
            "<",
        )
    )
    napit.append(
        muodosta_nappi(
            n_leveys,
            n_korkeus,
            (keski_x + x_offsetti, y_alkukorkeus),
            ruudukon_hallinta.lisaa_ruutuja,
            ">",
        )
    )

    napit.append(
        muodosta_nappi(
            n_leveys,
            n_korkeus,
            (keski_x - x_offsetti, y_alkukorkeus + n_korkeus * 6),
            pelaaja1.vaihda_pelaajaa,
            "<",
        )
    )
    napit.append(
        muodosta_nappi(
            n_leveys,
            n_korkeus,
            (keski_x + x_offsetti, y_alkukorkeus + n_korkeus * 6),
            pelaaja1.vaihda_pelaajaa,
            ">",
        )
    )

    napit.append(
        muodosta_nappi(
            n_leveys,
            n_korkeus,
            (keski_x - x_offsetti, y_alkukorkeus + n_korkeus * 12),
            pelaaja2.vaihda_pelaajaa,
            "<",
        )
    )
    napit.append(
        muodosta_nappi(
            n_leveys,
            n_korkeus,
            (keski_x + x_offsetti, y_alkukorkeus + n_korkeus * 12),
            pelaaja2.vaihda_pelaajaa,
            ">",
        )
    )

    napit.append(
        muodosta_nappi(
            10 * n_leveys,
            4 * n_korkeus,
            (keski_x, y_alkukorkeus + n_korkeus * 18),
            pelin_hallinta.aloita_peli_tapahtuma,
            "Pelaa",
        )
    )

    return pygame.sprite.Group(napit)
