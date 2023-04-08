import json
from dotenv import load_dotenv
import os

tiedoston_nimi = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(tiedoston_nimi, "..", ".env"))
except FileNotFoundError:
    print("dotenv not found")

konfiguraatiotiedoston_nimi = os.getenv("TUOTANTO_KONFIGURAATIO")
konfiguraatiotiedoston_polku = os.path.join(
    tiedoston_nimi, "..", "materiaalit", konfiguraatiotiedoston_nimi)


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
        "fontti": 30
    }
    with open(konfiguraatiotiedoston_polku, "w") as tiedosto:
        json.dump(konfiguraatio, tiedosto)


def lataa_konfiguraatio():
    with open(konfiguraatiotiedoston_polku, "r") as tiedosto:
        konfiguraatio = json.load(tiedosto)
    return konfiguraatio


konffi = lataa_konfiguraatio()


def set_konfiguraatio(avain, arvo):
    konffi[avain] = arvo
    with open(konfiguraatiotiedoston_polku, "w") as file:
        json.dump(konffi, konfiguraatiotiedoston_polku)


def get_konfiguraatio():
    return konffi


def main():
    rakenna_konfiguraatio()
