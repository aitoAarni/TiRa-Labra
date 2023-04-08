from peli.ihmis_pelaaja import Pelaaja
from unittest.mock import Mock
from konfiguraatio import LEVEYS, KORKEUS, RUUTUJEN_MAARA
import unittest
import sys
sys.path.append("./src")


class TestPelaaja(unittest.TestCase):

    def test_palauttaa_oikean_ruudun(self):
        hiiren_klikki_mock = Mock(return_value=True)
        hiiren_paikka_mock = Mock(return_value=(0, 0))
        pelaaja = Pelaaja(hiiren_klikki_mock, hiiren_paikka_mock)
        ruutu1 = pelaaja.get_ruutu()
        hiiren_paikka_mock.return_value = (LEVEYS, KORKEUS)
        ruutu2 = pelaaja.get_ruutu()
        self.assertTupleEqual(
            (ruutu1, ruutu2), ((0, 0), (RUUTUJEN_MAARA - 1, RUUTUJEN_MAARA - 1)))

    def test_ei_palauta_ruutua_jos_ei_klikkia(self):
        hiiren_klikki_mock = Mock(return_value=False)
        hiiren_paikka_mock = Mock(return_value=(0, 0))
        pelaaja = Pelaaja(hiiren_klikki_mock, hiiren_paikka_mock)
        ruutu = pelaaja.get_ruutu()
        self.assertEqual(ruutu, None)
