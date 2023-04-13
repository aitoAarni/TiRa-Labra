from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()


class Pelaaja:
    def __init__(
            self,
            hiiren_klikki,
            hiiren_paikka,
            merkki,
            merkit,
            ruutujen_maara) -> None:
        self.hiirta_klikattu = hiiren_klikki
        self.hiiren_paikka = hiiren_paikka
        self.merkki = merkki
        self.merkit = merkit
        self.ruutujen_maara = ruutujen_maara

    def valitse_ruutu(self):
        if self.hiirta_klikattu():
            x, y = self.hiiren_paikka()
            return (round(x //
                          (konffi["leveys"] /
                           self.ruutujen_maara)), round(y //
                                                        (konffi["korkeus"] /
                                                         self.ruutujen_maara)))
        return None
