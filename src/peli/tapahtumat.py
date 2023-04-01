import pygame


class Tapahtumat:
    def __init__(self) -> None:
        self.hiiren_paikka = None

    def get_tapahtumat(self):
        tapahtumat = {
            "lopeta": False,
            "takaisin": False
        }
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                tapahtumat["lopeta"] = True

            if tapahtuma.type == pygame.KEYDOWN:
                tapahtumat["takaisin"]

        return tapahtumat

    def hiirta_klikattu(self):
        return pygame.event.peek(pygame.MOUSEBUTTONDOWN)

    def get_hiiren_paikka(self):
        self.hiirta_klikattu = False
        return self.hiiren_paikka
