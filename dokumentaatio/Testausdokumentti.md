# Testausdokumentaatio

kattavuusraportti yksikkötesteistä: [![codecov](https://codecov.io/gh/aitoAarni/TiRa-Labra/branch/main/graph/badge.svg?token=G521CJR0IT)](https://codecov.io/gh/aitoAarni/TiRa-Labra)

![testien kattavuus raportti](https://github.com/aitoAarni/TiRa-Labra/assets/13611438/88c28b84-0e59-40e7-9f3d-9fa36e7d1f38)


Projektia on testattu yksikkötesteillä. Yksikkötestit toteutettin automaattisella ohjelmalla. Testauksen syötteet katsovat osittain myös ääritapauksia ja niitä on lisätty viikosta 5 eteenpäin. 

Yksikkötesteillä testataan kaikkea muuta ohjelmasta paitsi konfiguraatio koodia sekä käyttöliittymää. Ohjelmassa on pääsääntöisesti koitettu testeata jokaisen luokan jokaista metodia yhdellä tai useammalla syötteellä. Ohjelman melkein jokainen "branchi" on koitettu testata ainakin yhdellä syötteellä. Heuristista arviontia ollaan jokseenkin testattu, mutta minimax algoritmin oikeellisuutta ei olla oikein testatttu monimutkaisiisa tapauksissa. Testauksessa on mukana testaus konfiguraatio tiedosto, joka eroaa tuotanto konfiguraatio tiedostosta, joten muutos toiseen ei sotke konfiguraatiota toisessa.
