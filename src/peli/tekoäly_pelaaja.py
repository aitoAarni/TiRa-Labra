from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio

class Tekoaly:
    def __init__(self, pelitilanne) -> None:
        self.pelitilanne = pelitilanne

    def minimax(self, syvyys, a, b, maksimoiva_pelaaja):
        if syvyys == 0:
            return None