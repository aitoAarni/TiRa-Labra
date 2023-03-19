# Määrittelydokumentti

Tässä projektissa käytetään ohjelmointikielenä Pythonia. Kyseinen ohjelmoija hallitsee jokseenkin kielen Python vertaisarviointimielessä.

Tässä työssä tullaan käyttämään minimax algoritmia ja sitä tullaan tehostamaan Alfa-beta-karsinnalla sekä muilla mahdollisilla konsteilla. 
Pelitilaa tullaan pitämään todennäköisesti kaksiulotteisessa listassa, sekä yksiulotteisia listoja tullaan tarvitsemaan myös mahdollisesti hajautustauluja

Ongelma joka on ratkaistavana on ristinollalle tekoäly joka osaa suhteellisen hyvin pelata, 
minimax algoritmi on erinomainen tämäntapaisiin ongelmiin. Valitsin tämän ongelman sillä shakki tuntui liian isolta projektilta, 
sillä siinä on paljon enemmän sääntöjä.

Ohjelma tulee saamaan syötteitä käyttäjältä hiiren välityksellä. 
Hiiren kursoria liikuttamalla ja sen jälkeen vasenta nappia (mouse1) painamalla peli saa tiedon siitä, 
mihin ruutuun käyttäjä haluaa oman ristin tai nollan asetettavan.

Oletetaan pelilauta syötteeksi, jolloin saadaan aikavaativuus minimax algoritmissa on eksponentaalinen O(n^a), 
mutta sitä voidaan parantaa alfa-beta-karsinnalla sekä muilla pelikohtaisilla viilauksilla, mutta se silti pysyy eksponentiaalisena. 
Tilavaativuus on minimaalinen verrattuna aikavaativuuteen se on todennäköisesti luokkaa O(n).

lähde: [minmax moniste](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)

opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)

dokumentaatiossa tullaan käyttämään suomenkiletä.
