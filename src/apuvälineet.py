from time import perf_counter
from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio
VUORON_AIKA = konffi.vuoron_aika_sekunteina


def lautaus_baari_cli(osamaara, koko_maara):
    prosenttia = 100 * (osamaara / float(koko_maara))
    baari = "|" * round(prosenttia) + "-" * round(100 - prosenttia)
    print(f"\[{baari}] {prosenttia:.2f}%", end="\r")


def palauta_aika(self):
    return perf_counter()


def vuoron_aika_paattynyt(alku):
    return VUORON_AIKA < perf_counter() - alku
