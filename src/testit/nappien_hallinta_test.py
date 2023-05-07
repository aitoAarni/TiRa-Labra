import unittest
from unittest.mock import Mock
from valikko.nappien_hallinta import Napit
from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()


LEVEYS, KORKEUS = konffi.leveys, konffi.korkeus


class TestNapit(unittest.TestCase):
    def setUp(self):
        self.ruudukon_hallinta = Mock()
        self.pelaaja1 = Mock()
        self.pelaaja2 = Mock()
        self.pelin_hallinta = Mock()
        self.napit = Napit(
            self.ruudukon_hallinta, self.pelaaja1, self.pelaaja2, self.pelin_hallinta
        )

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.napit), Napit)

    def test_nappeja_luotu_oikea_maara(self):
        self.assertEqual(len(self.napit.napit), 7)

    def test_tarkista_onko_hiiri_napin_paalla_toimii(self):
        self.napit.tarkista_onko_hiiri_napin_paalla((0, 0))

        tulos1 = self.napit.nappi_jonka_paalla_on_hiiri

        self.napit.tarkista_onko_hiiri_napin_paalla((600, 800))

        tulos2 = self.napit.nappi_jonka_paalla_on_hiiri

        self.assertEqual((tulos1, tulos2), (None, self.napit.napit.sprites()[-1]))

    def test_aktivoi_klikattu_nappi_toimii(self):
        self.napit.aktivoi_klikattu_nappi()

        self.napit.nappi_jonka_paalla_on_hiiri = self.napit.napit.sprites()[-1]

        self.napit.aktivoi_klikattu_nappi()

        self.pelin_hallinta.aloita_peli_tapahtuma.assert_called_once()
