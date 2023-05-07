from valikko.nappien_hallinta import Napit


class Valikko:
    def __init__(
        self,
        tapahtumat,
        naytto,
        kayttoliittyma,
        ruudukon_hallinta,
        pelaaja1,
        pelaaja2,
        pelin_hallinta,
    ) -> None:
        self.tapahtumat = tapahtumat
        self.ruudukon_hallinta = ruudukon_hallinta
        self.pelaaja1 = pelaaja1
        self.pelaaja2 = pelaaja2
        self.pelin_hallinta = pelin_hallinta(ruudukon_hallinta)
        self.napit = Napit(ruudukon_hallinta, pelaaja1, pelaaja2, self.pelin_hallinta)
        self.aloita_peli = False
        self.kayttoliittyma = kayttoliittyma(naytto, self.napit.napit)

    def aloita(self):
        while True:
            tapahtumat = self.tapahtumat.get_tapahtumat()
            if tapahtumat["lopeta"] or tapahtumat["takaisin"]:
                break
            self.napit.tarkista_onko_hiiri_napin_paalla(
                self.tapahtumat.get_hiiren_paikka()
            )
            if self.tapahtumat.hiirta_klikattu():
                self.napit.aktivoi_klikattu_nappi()
            if self.pelin_hallinta.aloita_peli:
                self.aloita_peli = True
                break
            self.kayttoliittyma.piirra_valikko(
                self.napit.nappi_jonka_paalla_on_hiiri,
                self.pelaaja1.valittu_pelaaja.nimi(),
                self.pelaaja2.valittu_pelaaja.nimi(),
                str(self.ruudukon_hallinta.ruutujen_maara),
            )
