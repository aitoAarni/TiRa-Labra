import unittest
import pygame
pygame.init()
from peli.tapahtumat import Tapahtumat



def lisaa_eventti(tyyppi, nappi=None):
    pygame.init()
    nappaimisto = {"key": nappi}
    tapahtuma = pygame.event.Event(tyyppi, nappaimisto)
    pygame.event.post(tapahtuma)


class TestTapahtumat(unittest.TestCase):
    def setUp(self):
        self.tapahtumat = Tapahtumat()

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.tapahtumat), Tapahtumat)

    def test_get_tapahtumat_kaikki_napit_toimii(self):
        oikea_vastaus = {
            "lopeta": True,
            "takaisin": True,
            "pelaa_uudelleen": True
        }
        lisaa_eventti(pygame.KEYDOWN, pygame.K_r)
        lisaa_eventti(pygame.KEYDOWN, pygame.K_ESCAPE)
        lisaa_eventti(pygame.QUIT, "")
        tapahtumat = self.tapahtumat.get_tapahtumat()
        self.assertDictEqual(tapahtumat, oikea_vastaus)

    def test_get_tapahtumat_palauttaa_oikean_sanakrijan(self):
        oikea_vastaus = {
            "lopeta": False,
            "takaisin": False,
            "pelaa_uudelleen": False
        }
        tapahtumat = self.tapahtumat.get_tapahtumat()
        self.assertDictEqual(tapahtumat, oikea_vastaus)

    def test_hiiren_klikki_toimii(self):
        lisaa_eventti(pygame.MOUSEBUTTONDOWN)
        self.tapahtumat.get_tapahtumat()
        hiirta_klikattu = self.tapahtumat.hiirta_klikattu()
        self.assertTrue(hiirta_klikattu)

    def test_palauta_nappaimiston_komento_metodi_toimii_kun_nappaimistoa_painettu(
            self):
        lisaa_eventti(pygame.KEYDOWN, pygame.K_ESCAPE)
        paluuarvo = self.tapahtumat.palauta_nappaimiston_komento()
        self.assertEqual(paluuarvo, "takaisin")

    def test_palauta_nappaimiston_komento_metodi_toimii_kun_nappaimistoa_ei_painettu(
            self):
        paluuarvo = self.tapahtumat.palauta_nappaimiston_komento()
        self.assertEqual(paluuarvo, None)
