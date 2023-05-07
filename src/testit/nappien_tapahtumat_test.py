import unittest
from unittest.mock import Mock
from valikko.nappien_tapahtumat import ValitsePelaaja, RuudukonKoko, PelinHallinta


class TestValitsePelaaja(unittest.TestCase):
    def setUp(self):
        self.pelaaja1 = Mock()
        self.pelaaja2 = Mock()
        self.valitse_pelaaja = ValitsePelaaja(self.pelaaja1, self.pelaaja2)

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.valitse_pelaaja), ValitsePelaaja)

    def test_vaihda_pelaaja_toimii(self):
        valittu_pelaaja1 = self.valitse_pelaaja.valittu_pelaaja
        self.valitse_pelaaja.vaihda_pelaajaa()
        valittu_pelaaja2 = self.valitse_pelaaja.valittu_pelaaja
        self.valitse_pelaaja.vaihda_pelaajaa()

        self.assertEqual(
            (valittu_pelaaja1, valittu_pelaaja2), (self.pelaaja1, self.pelaaja2)
        )


class TestRuudukonKoko(unittest.TestCase):
    def setUp(self):
        self.ruudukko = RuudukonKoko(10)

    def test_konstruktori_toimii(self):
        self.assertEqual(type(self.ruudukko), RuudukonKoko)

    def test_lisaa_ruutuja_toimii(self):
        self.ruudukko._ruutujen_maara = 48

        ruudukon_koko_lista = []
        for _ in range(4):
            self.ruudukko.lisaa_ruutuja()
            ruudukon_koko_lista.append(self.ruudukko.ruutujen_maara)

        self.assertEqual(ruudukon_koko_lista, [49, 50, 50, 50])

    def test_vahenna_ruutuja_toimii(self):
        ruudukon_koko_lista = []
        for _ in range(4):
            self.ruudukko.vahenna_ruutuja()
            ruudukon_koko_lista.append(self.ruudukko.ruutujen_maara)

        self.assertEqual(ruudukon_koko_lista, [9, 8, 7, 7])


class TestPelinHallinta(unittest.TestCase):
    def setUp(self):
        ruutujen_hallinta = Mock()
        self.get_konf = Mock()
        self.set_konf = Mock()
        self.paivita_konf = Mock()
        self.hallinta = PelinHallinta(
            ruutujen_hallinta, self.get_konf, self.set_konf, self.paivita_konf
        )

    def test_aloita_peli_getter_tomiii(self):
        paluuarvo1 = self.hallinta.aloita_peli
        self.hallinta._aloita_peli = True
        paluuarvo2 = self.hallinta.aloita_peli

        self.assertEqual(
            (paluuarvo1, paluuarvo2, self.hallinta._aloita_peli), (False, True, False)
        )

    def test_aloita_peli_tapahtuma_toimii(self):
        self.hallinta.aloita_peli_tapahtuma()
        self.get_konf.assert_called_once()
        self.set_konf.assert_called_once()
        self.paivita_konf.assert_called_once()
