import unittest
from tekoäly.heuristinen_arviointi import HeurestisenArvonLaskija


class TestheuristinenArviointi(unittest.TestCase):
    def setUp(self):
        self.arviointi = HeurestisenArvonLaskija("x", "0", 3)

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.arviointi), HeurestisenArvonLaskija)

    def test_perakkaiset_ruudut_arvioidaan_oikein(self):
        arvo1 = self.arviointi.perakkaisten_ruutujen_arvot(2, 3, True)
        arvo2 = self.arviointi.perakkaisten_ruutujen_arvot(1, 2)
        arvo3 = self.arviointi.perakkaisten_ruutujen_arvot(7, 3)
        self.assertTupleEqual((arvo1, arvo2, arvo3), (100, 0, 99999999999))

    def test_laske_arvo_metodin_testaus(self):
        rivin_esitys = "-0-xxx0-x-xx-x000-0--x00x-0xx0-x-"
        rivi = list(rivin_esitys)
        h_arvo = self.arviointi.laske_heuristinen_arvo(rivi, 3)
        self.assertEqual(h_arvo, 100.0)
