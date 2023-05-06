from konfiguraatio import rakenna_konfiguraatio


with open(".env", "w") as tiedosto:
    tiedosto.write("KONFIGURAATIO=tuotanto_konfiguraatio.json")

rakenna_konfiguraatio()


print("Alustus tehty")
