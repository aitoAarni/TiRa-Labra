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
        self.peli.lauta = [
            ["x" for _ in range(RUUTUJEN_MAARA)] for _ in range(RUUTUJEN_MAARA)
        ]
        self.peli.lauta[5][5] = None
        tulos1 = self.peli.tarkista_tasapeli()
        self.peli.lauta[5][5] = "0"
        tulos2 = self.peli.tarkista_tasapeli()

        self.assertEqual((tulos1, tulos2), (False, True))

    def test_tarkista_onko_peli_paattynyt(self):
        lauta = self.peli.lauta
        lauta[0][0] = "x"
        paluuarvo1 = self.peli.tarkista_onko_peli_paattynyt((0, 0), "x", lauta)

        for i in range(5):
            lauta[0][i] = "x"
        paluuarvo2 = self.peli.tarkista_onko_peli_paattynyt((4, 0), "x", lauta)

        lauta = [["x" for _ in range(RUUTUJEN_MAARA)] for _ in range(RUUTUJEN_MAARA)]

        lauta[0][0] = "0"
        self.peli.lauta = lauta
        paluuarvo3 = self.peli.tarkista_onko_peli_paattynyt((0, 0), "0", lauta)

        self.assertEqual(
            (paluuarvo1, paluuarvo2, paluuarvo3),
            ((False, None), (True, "x"), (True, "-")),
        )

    def test_valitse_ruutu_toimii(self):
        pelaaja1 = Mock()
        pelaaja2 = Mock()
        pelaaja1.valitse_ruutu.return_value = None
        pelaaja2.valitse_ruutu.return_value = (4, 5)
        self.peli.pelaajat = [pelaaja1, pelaaja2]

        paluuarvo1 = self.peli.valitse_ruutu(0)
        paluuarvo2 = self.peli.valitse_ruutu(1)

        self.assertEqual(
            (paluuarvo1, paluuarvo2, self.peli.siirrot, len(self.peli.vapaat_ruudut)),
            (None, (4, 5), [(4, 5)], RUUTUJEN_MAARA**2 - 1),
        )

    def test_valitse_ruutu_toimii(self):
        pelaaja = Mock()
        pelaaja.valitse_ruutu.return_value = (1, 1)
        self.peli.pelaajat = [pelaaja, None]
        paluu_arvo = self.peli.pelaa_vuoro(0)

        self.assertEqual(paluu_arvo, (1, 1))

    def test_vaihda_vuoroa_toimii(self):
        vuoro1 = self.peli.vaihda_vuoroa(1)
        vuoro2 = self.peli.vaihda_vuoroa(0)

        self.assertEqual((vuoro1, vuoro2), (0, 1))
