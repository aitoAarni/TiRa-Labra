# Toteutusdokumentti

## Aika ja tilavaativuudet

- minimax algoritmin aikavaativuus on tällä hetkellä O(n<sup>3</sup>), sillä sen syvyys on 3 ja n on ristien ja nollien määrä, sillä vain niiden lähteltä etsitään siirtoja.
- Heurestisen funktion aikavaativuus tällä hetkellä on O(1), sillä se käy läpi vain viimeisimmän valitun merkin ruudusta lähtien vakaa, pysty sekä vinot rivit (sama myös pätee voiton tarkistus funktiolle).

## Työn mahdolliset puutteet ja parannusehdotukset

Tällä hetkellä ristinollassa ei ole valikkoa. Minimax algoritmin heurestisessa arvioinnissa on pieni bugi vinoja rivejä koskien.


lähteet: [minimax.pdf](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf)
