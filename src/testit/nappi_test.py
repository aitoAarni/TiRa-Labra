from valikko.nappi import Nappi
import unittest
from unittest.mock import Mock

NAPIN_LEVEYS = 35
NAPIN_KORKEUS = 30


class TestNappi(unittest.TestCase):
    def setUp(self):
        self.tapahtuma = Mock()
        self.nappi = Nappi(
            NAPIN_LEVEYS, NAPIN_KORKEUS, (500, 500), self.tapahtuma, "None"
        )

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.nappi), Nappi)

    def test_havaitse_hiiren_leijuminen_toimii(self):
        paluuarvo1 = self.nappi.havaitse_hiiren_leijuminen((0, 0))
        paluuarvo2 = self.nappi.havaitse_hiiren_leijuminen((511, 513))

        self.assertEqual((paluuarvo1, paluuarvo2), (None, self.nappi.rect))

    def test_aktivoi_tapahtuma_toimii(self):
        self.nappi.aktivoi_tapahtuma()

        self.tapahtuma.assert_called_once()
