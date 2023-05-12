# Toteutusdokumentti

## Yleisrakenne

Pelissä on valikko, josta voi risteille ja nollille joko ihmis- tai tekoälypelaajan, sekä pelilaudan ruutujen määrän. Pelin tekoäly käyttää minimax algoritmia (pienellä muunnelmalla), joka on raa'an voiman algoritmi.

### minimax

Minimax algoritmin muunnelma on sen heuristisen arvion kanssa. Heuristista arvoa ei arvioida vain syvyydellä 0 tai kun jompi kumpi pelaaja on voittanut, niin kuin normaalissa minimax algoritmissa, vaan jokaisen siirron jälkeen.
Aluksi ennen miminax algoritmin kutsua arvioidaan `heuristinen_funktio` metodilla, joka arvioi kaikki pelilaudan oleelliset ruudut. Tämä arvio `heuristinen_arvo` annetaan minimaxille parametriksi. Jokaisen siirron jälkeen `for siirto in siirrot[::-1]:` arvioidaan siirron vaikutus ennen uutta minimax kutsua laudalla koomennolla: 
```
uusi_heuristinen_arvo = heuristinen_arvo + self.heurstisen_arvon_delta(pelilauta, syvyys, siirto)
```
ja `uusi_heuristinen_arvo` annetaan minimax metodille parametriin `heuristinen_arvo`. Miksi näin tehdään eikä vain arvioida pelitilannetta syvyydellä 0 tai kun jompi kumpi on saanut yli 4 peräkkäin? Tähän on kaksi syytä

- Arvioitaessa pelitilannetta voidaan arvioon liittää aina kerroin, joka riippuu syvyydestä, sillä tiedetään helpisti millä syvyydellä aina mikäkin liike on tehty ja sen vaikutus arviointiin. Tämä on hyödyllistä sillä jos minimaxin maksimi syvyys on pariton, niin maksimioija saa aina yhden siirron enemmän, jolloinka se saisi yhtä monta merkkiä peräkkäin vaikka lähtötilanteessa minimoijalla olisi yksi merkki enemmän peräkkäin.
- Tämä on oikeastaan nopeampaa, sillä arvioidaan vähemmän ruutuja, sillä normaalisti arvioitaisiin kaikki ruudut tai minimissään pitäisi arvoida suuri osa ruuduista. Seuraava kappale selittää miten `heurstisen_arvon_delta` toimii karkeasti.

metodi `heurstisen_arvon_delta` arvioi vain vaaka pysty ja molemmat vinot rivit jotka kulkevat juuri äskeisen siirron ruudun kautta (eli 4 riviä). Metodi ensin arvioi edellämainitut 4 riviä ilman äskeistä siirtoa laittamalla sirron ruutuun tyhjän ruudun ja sen jälkeen siirron kanssa, jolloin ruutuun ollaan laitettu äskeisen siirron merkki (eli 4 riviä 2 kertaa arvioitu). Metodi ottaa molemmista pelitilanteista arvion ja palauttaa `jälkimmäinen arvio - ensimmäinen arvio` ja kertoo tämän viellä kertoimella, joka vähänee mitä syvemmällä ollaan menty minimax algoritmissa, eli syvemmällä tehdyt liikkeet vaikuttavat minimaxin heuristiseen arvoon vähemmän.

## Aika ja tilavaativuudet

- minimax algoritmin aikavaativuus on tällä hetkellä O(n<sup>3</sup>), sillä sen syvyys on 3 ja n on syötteen, eli ristien ja nollien määrä.
- Heurestisen funktion aikavaativuus tällä hetkellä on O(1), sillä se käy läpi vain viimeisimmän valitun merkin ruudusta lähtien vakaa, pysty sekä vinot rivit (sama myös pätee voiton tarkistus funktiolle).

## Työn mahdolliset puutteet ja parannusehdotukset




lähteet: [minimax.pdf](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)
