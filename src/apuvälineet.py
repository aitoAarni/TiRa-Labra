from time import perf_counter
from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()
VUORON_AIKA = konffi.vuoron_aika_sekunteina


def lataus_baari_cli(osoittaja, nimittaja, syvyys):
    prosenttia = 100 * (osoittaja / float(nimittaja))
    baari = ("|" * round(prosenttia) + "-" * round(100 - prosenttia)).strip()
    print(f"[{baari}] {prosenttia:.2f}% syvyys: {syvyys}", end="\r")


def palauta_aika():
    """Palauttaa ajastimen ajan

    Returns:
        float: aloitusaika sekunteina
    """
    return perf_counter()


def vuoron_aika_loppunut(alku):
    """Kertoo onko vuoron aika loppunut

    Args:
        alku (float): vuoron aloitusaika

    Returns:
        bool: kertoo onko vuoro loppunut
    """
    return VUORON_AIKA < perf_counter() - alku


def jarjesta_lista_toisen_listan_avulla(
    jarjestettava_lista: list, noudatettava_jarjestys: list
):
    pari_lista = zip(noudatettava_jarjestys, jarjestettava_lista)

    return [x for _, x in sorted(pari_lista)]
