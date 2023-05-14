# Määrittelydokumentti

Tässä projektissa käytetään ohjelmointikielenä Pythonia. Kyseinen ohjelmoija hallitsee jokseenkin kielen Python vertaisarviointimielessä.

Tässä työssä tullaan käyttämään minimax algoritmia ja sitä tullaan tehostamaan Alfa-beta-karsinnalla sekä muilla mahdollisilla konsteilla. 
Pelitilaa tullaan pitämään todennäköisesti kaksiulotteisessa listassa, sekä yksiulotteisia listoja tullaan tarvitsemaan myös mahdollisesti hajautustauluja

Ongelma joka on ratkaistavana on ristinollalle tekoäly joka osaa suhteellisen hyvin pelata, 
minimax algoritmi on erinomainen tämän tapaisiin ongelmiin. Valitsin tämän ongelman sillä sekä pienen pelin sekä tekoälyn pelille tekeminen ovat erittäin miellyttävä aihe mielestäni.

Ohjelma tulee saamaan syötteitä käyttäjältä hiiren välityksellä. 
Hiiren kursoria liikuttamalla ja sen jälkeen vasenta nappia (mouse1) painamalla peli saa tiedon siitä, 
mihin ruutuun käyttäjä haluaa oman ristin tai nollan asetettavan.

Oletetaan pelatut ruudut syötteeksi n (vakiokerroin max 24, sillä pelatun ruudun ympäriltä tekoäly etsii pahimmassa tapauksessa näin monta ruutua), jolloin saadaan aikavaativuus minimax algoritmissa on eksponentaalinen O(n<exp>a</exp>). 
MInimax algoritmia on tehostettu alfa-beta-karsinnalla sekä muilla pelikohtaisilla viilauksilla, mutta aikavaativuus silti pysyy eksponentiaalisena. 
Tilavaativuus on minimaalinen verrattuna aikavaativuuteen se on luokkaa O(n), sillä jokaisella syvyydellä minimax algoritmissa säilytetään vain edellisen syvyyden pelitilanne, eikä esim. jokaista tulevaa pelitilannetta.

lähde: [minmax moniste](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)

opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)

dokumentaatiossa tullaan käyttämään suomenkieltä.
