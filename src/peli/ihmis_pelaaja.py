from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()


class Pelaaja:
    def __init__(self, hiiren_klikki, hiiren_paikka) -> None:
        self.hiirta_klikattu = hiiren_klikki
        self.hiiren_paikka = hiiren_paikka

    def valitse_ruutu(self):
        if self.hiirta_klikattu():
            x, y = self.hiiren_paikka()
            return (round(x //
                          (konffi["leveys"] /
                           konffi["ruutujen_määrä"])), round(y //
                                                             (konffi["korkeus"] /
                                                              konffi["ruutujen_määrä"])))
        return None
