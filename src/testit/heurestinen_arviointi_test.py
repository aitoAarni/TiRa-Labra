import unittest
from tekoäly.heurestinen_arviointi import HeurestisenArvonLaskija, VOITTO_ARVO


class TestHeurestinenArviointi(unittest.TestCase):
    def setUp(self):
        self.arviointi = HeurestisenArvonLaskija("x", "0", 2, 2)

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.arviointi), HeurestisenArvonLaskija)

    def test_perakkaiset_ruudut_arvioidaan_oikein(self):
        arvo1 = self.arviointi.perakkaisten_ruutujen_arvot(2, True)
        arvo2 = self.arviointi.perakkaisten_ruutujen_arvot(1)
        arvo3 = self.arviointi.perakkaisten_ruutujen_arvot(7)
        self.assertTupleEqual((arvo1, arvo2, arvo3), (100, 0, VOITTO_ARVO))

    def test_laske_arvo_metodin_testaus(self):
        rivin_esitys = "-0-xxx0-xxx-000-x00x-0xx0-x-"
        self.arviointi.laskemisen_alustus()
        for alkio in rivin_esitys:
            self.arviointi.laske_arvo(alkio, (0, 0))
        self.arviointi.viimeisen_ruudun_tarkistus()
        self.assertEqual(self.arviointi.heurestinen_arvo, 90)
