from peli.ihmis_pelaaja import Pelaaja
from unittest.mock import Mock
from konfiguraatio import konffi
import unittest

LEVEYS = konffi["leveys"]
KORKEUS = konffi["korkeus"]
RUUTUJEN_MAARA = konffi["ruutujen_määrä"]



class TestPelaaja(unittest.TestCase):

    def test_konstruktori_toimii(self):

        hiiren_klikki_mock = Mock(return_value=True)
        hiiren_paikka_mock = Mock(return_value=(0, 0))
        pelaaja = Pelaaja(hiiren_klikki_mock, hiiren_paikka_mock, "x", [], RUUTUJEN_MAARA)
        self.assertEqual(type(pelaaja), Pelaaja)

    def test_palauttaa_oikean_ruudun(self):
        hiiren_klikki_mock = Mock(return_value=True)
        hiiren_paikka_mock = Mock(return_value=(0, 0))

        pelaaja = Pelaaja(hiiren_klikki_mock, hiiren_paikka_mock, "x", [], RUUTUJEN_MAARA)
        ruutu1 = pelaaja.valitse_ruutu()
        hiiren_paikka_mock.return_value = (LEVEYS, KORKEUS)
        ruutu2 = pelaaja.valitse_ruutu()
        self.assertTupleEqual(
            (ruutu1, ruutu2), ((0, 0), (RUUTUJEN_MAARA - 1, RUUTUJEN_MAARA - 1)))

    def test_ei_palauta_ruutua_jos_ei_klikkia(self):
        hiiren_klikki_mock = Mock(return_value=False)
        hiiren_paikka_mock = Mock(return_value=(0, 0))
        pelaaja = Pelaaja(hiiren_klikki_mock, hiiren_paikka_mock, "x", [], RUUTUJEN_MAARA)
        ruutu = pelaaja.valitse_ruutu()
        self.assertEqual(ruutu, None)
