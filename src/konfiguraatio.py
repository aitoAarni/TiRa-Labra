import json
from dotenv import load_dotenv
import os

print("konfigissss123")
tiedoston_nimi = os.path.dirname(__file__)


try:
    load_dotenv()
    print("dotenv found")
except FileNotFoundError:
    print("dotenv not found")


try:
    konfiguraatiotiedoston_nimi = os.getenv("KONFIGURAATIO")
    konfiguraatiotiedoston_polku = os.path.join(
        "materiaalit",
        konfiguraatiotiedoston_nimi)
    
except TypeError:
    konfiguraatiotiedoston_polku = os.path.join(
        tiedoston_nimi,
        "..",
        "materiaalit",
        "testaus_konfiguraatio.json")



def rakenna_konfiguraatio():
    konfiguraatio = {
        "ruutujen_määrä": 15,
        "laudan_väri": (0, 0, 0),
        "laudan_viivojen_väri": (255, 255, 255),
        "korkeus": 500,
        "leveys": 500,
        "nappuloiden_väri": (0, 0, 255),
        "peli_ohi_väri": (192, 192, 192),
        "voitto_tekstin_väri": (0, 0, 0),
        "fontti": 30,
        "nappien_väri": (0, 0, 220)
    }
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        json.dump(konfiguraatio, tiedosto)


def lataa_konfiguraatio():
    with open(konfiguraatiotiedoston_polku, "r") as tiedosto:
        konfiguraatio = json.load(tiedosto)
    return konfiguraatio


def set_konfiguraatio(konfiguraatio_tietokirja):
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        tiedosto.write(json.dumps(konfiguraatio_tietokirja))


def get_konfiguraatio():
    print("polku:", konfiguraatiotiedoston_polku)
    with open(konfiguraatiotiedoston_polku, "r") as tiedosto:
        konfiguraatio = json.load(tiedosto)
    return konfiguraatio


def main():
    rakenna_konfiguraatio()
