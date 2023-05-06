import unittest
from peli.peli_logiikka import Peli
from peli.ihmis_pelaaja import Pelaaja
from peli.tekoäly_pelaaja import TekoalyPelaaja
from konfiguraatio import get_konfiguraatio
from unittest.mock import Mock


konffi = get_konfiguraatio()
RUUTUJEN_MAARA = konffi.ruutujen_maara


class TestPeliLogiikka(unittest.TestCase):
    def setUp(self):
        self.tapahtumat_mock = Mock()
        self.pelaaja1_mock = Pelaaja
        self.pelaaja2_mock = TekoalyPelaaja
        self.lauta_ui_mock = Mock
        self.ikkuna_mock = Mock()

        self.peli = Peli(
            self.tapahtumat_mock,
            self.pelaaja1_mock,
            self.pelaaja2_mock,
            self.lauta_ui_mock,
            self.ikkuna_mock,
        )

    def test_konstruktori_toimii(self):
        self.assertTrue(isinstance(self.peli, Peli))

    def test_alusta_pelaaja_metodi_toimii(self):
        pelaaja1 = self.peli._alusta_pelaaja(Pelaaja, "x", [])
        pelaaja2 = self.peli._alusta_pelaaja(TekoalyPelaaja, "0", [])
        self.assertEqual((type(pelaaja1), type(pelaaja2)), (Pelaaja, TekoalyPelaaja))

    def test_tarkista_tasapeli_toimii(self):
        siirrot = [(0, 0) for _ in range(RUUTUJEN_MAARA**2 - 1)]
        self.peli.siirrot = siirrot
        tulos1 = self.peli.tarkista_tasapeli()
        siirrot.append((0, 0))
        tulos2 = self.peli.tarkista_tasapeli()
        siirrot.append((0, 0))
        tulos3 = self.peli.tarkista_tasapeli()

        self.assertEqual((tulos1, tulos2, tulos3), (False, True, True))
