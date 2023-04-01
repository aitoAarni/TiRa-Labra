from config import RUUTUJEN_MAARA


class Pelaaja:
    def __init__(self, hiiren_klikki, hiiren_paikka) -> None:
        self.hiirta_klikattu = hiiren_klikki
        self.hiiren_paikka = hiiren_paikka

    def get_ruutu(self):
        if self.hiirta_klikattu():
            x, y = self.hiiren_paikka()
            return (x // RUUTUJEN_MAARA, y // RUUTUJEN_MAARA)

        return None
