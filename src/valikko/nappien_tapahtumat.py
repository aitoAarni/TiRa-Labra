from konfiguraatio import get_konfiguraatio, set_konfiguraatio, paivita_konfiguraatio


class ValitsePelaaja:
    def __init__(self, pelaaja1, pelaaja2) -> None:
        self._pelaaja1 = pelaaja1
        self._pelaaja2 = pelaaja2
        self._valittu_pelaaja = pelaaja1

    def vaihda_pelaajaa(self):
        self._valittu_pelaaja = (
            self._pelaaja1
            if self._valittu_pelaaja == self._pelaaja2
            else self._pelaaja2
        )

    @property
    def valittu_pelaaja(self):
        return self._valittu_pelaaja


class RuudukonKoko:
    def __init__(self, ruutujen_maara) -> None:
        self._ruutujen_maara = ruutujen_maara

    def lisaa_ruutuja(self):
        if self.ruutujen_maara < 50:
            self._ruutujen_maara += 1

    def vahenna_ruutuja(self):
        if self.ruutujen_maara > 7:
            self._ruutujen_maara -= 1

    @property
    def ruutujen_maara(self):
        return self._ruutujen_maara


class PelinHallinta:
    def __init__(
        self,
        ruutujen_hallinta,
        get_konf=get_konfiguraatio,
        set_konf=set_konfiguraatio,
        paivita_konf=paivita_konfiguraatio,
    ) -> None:
        self.ruutujen_hallinta = ruutujen_hallinta
        self.get_konf = get_konf
        self.set_konf = set_konf
        self.paivita_konf = paivita_konf
        self._aloita_peli = False

    @property
    def aloita_peli(self):
        if self._aloita_peli:
            self._aloita_peli = False
            return True
        return False

    def aloita_peli_tapahtuma(self):
        self._aloita_peli = True
        konffi = self.get_konf()
        konffi.ruutujen_maara = self.ruutujen_hallinta.ruutujen_maara
        self.set_konf(konffi)
        self.paivita_konf()
