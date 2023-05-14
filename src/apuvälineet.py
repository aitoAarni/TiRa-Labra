from time import perf_counter
from konfiguraatio import get_konfiguraatio

konffi = get_konfiguraatio()
VUORON_AIKA = konffi.vuoron_aika_sekunteina


def lataus_baari_cli(osoittaja: int, nimittaja: int, syvyys: int):
    """Piirtää latauspalkin konsoliin

    Args:
        osoittaja (int): jaettava
        nimittaja (int): jakaja
        syvyys (int): mitä syvyyttä lasketaan
    """
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
    """Jarjestää ensimmäisen listan toisen listan arvojen perusteella,
    listojen samoilla indekseillä olevat arvot vastaavat toisiaan

    Args:
        jarjestettava_lista (list): lista joka pitää järjestää
        noudatettava_jarjestys (list): antaa järjestyksen listalle

    Returns:
        list: lista järjestetynä
    """
    pari_lista = zip(noudatettava_jarjestys, jarjestettava_lista)

    return [x for _, x in sorted(pari_lista)]
