from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()
LEVEYS = konffi["leveys"]
KORKEUS = konffi["korkeus"]

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
        x, y = self.hiiren_paikka()

        if self.hiirta_klikattu():
            x, y = self.hiiren_paikka()
            ruudun_leveys = LEVEYS / self.ruutujen_maara
            ruudun_korkeus = KORKEUS / self.ruutujen_maara
            rivi = round(x // ruudun_leveys)
            sarake = round(y // ruudun_korkeus)
            
            return rivi, sarake
        return None
