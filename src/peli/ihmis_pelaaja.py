from konfiguraatio import RUUTUJEN_MAARA, LEVEYS, KORKEUS


class Pelaaja:
    def __init__(self, hiiren_klikki, hiiren_paikka) -> None:
        self.hiirta_klikattu = hiiren_klikki
        self.hiiren_paikka = hiiren_paikka

    def get_ruutu(self):
        if self.hiirta_klikattu():
            print("hiirtä klikattu1234")
            x, y = self.hiiren_paikka()
            return (round(x // (LEVEYS / RUUTUJEN_MAARA)), round(y // (KORKEUS / RUUTUJEN_MAARA)))
        return None
