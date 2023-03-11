# Napredne zabilješke (Enhanced Annotations) #

*	Authors: George Kerscher, Noelia Ruiz Martínez
* [download stable version][1] (compatible with NVDA 2023.1 and beyond)

U konzorciju DAISY razvijaju se najbolje prakse za izdavače i autore za
pružanje opsežnih opisa.

Najbolji postupci koriste element HTML detalja koji slijedi nakon slike ili
poveznice na drugu datoteku koja sadrži opsežnan opis.

U objim opcijama, korisnik bi se trebao premjestiti na detalje ili poveznicu
i aktivirati je.

Imati tipkovni prečac za fokusiranje na detalje ili vezu je idealno.

Iz naše prakse preporučujemo da detalji ili poveznica slijede odmah nakon
slike, a ako se poveznica slijedi, mora se navesti povratna poveznica na
točnu lokaciju. Time se osigurava da se korisnik neće izgubiti.

Međutim, vjerojatno je da će razni autori staviti opsežan opis gotovo bilo
gdje. U tim slučajevima, korisnik bi se želio vratiti na sliku i otuda
potreba za načinom vraćanja na izvornu sliku.

Ovaj dodatak pruža obje funkcije kao podršku ovom [problemu koji je otvoren
u NVDA repozitoriju][2].

## Naredbe ##

* NVDA+alt+d: pomiče kursor na element koji je identificiran s
  aria-detaljima.
* NVDA+alt+shift+d: moves the cursor to the original element, for example,
  an image with furter details like a long description. If NVDA+alt+d has
  been pressed several times to move to related annotations, it'll be
  possible to go back to each origin.

Gornje naredbe mogu se promijeniti u NVDA izborniku, podizbornik Postavke,
dijalošk okvir za ulazne geste, kategorija modus čitanja.

## Changes for 2.0 ##

* Added ability to move back through multiple annotation origins.
* Requires NVDA 2023.1 or later.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
