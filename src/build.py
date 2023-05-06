from konfiguraatio import rakenna_konfiguraatio

rakenna_konfiguraatio()

with open(".env", "w") as tiedosto:
    tiedosto.write("KONFIGURAATIO=tuotanto_konfiguraatio.json")

print("Alustus tehty")
