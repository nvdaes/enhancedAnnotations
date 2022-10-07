# Napredne zabilješke (Enhanced Annotations) #

* Autori: George Kerscher, Noelia Ruiz Martínez
* Preuzmi [stabilnu verziju][1] (kompatibilna s NVDA 2022.1 i novijom
  verzijom)

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
* NVDA+alt+shift+d: pomiče kursor na izvorni element, na primjer, sliku s
  daljnjim detaljima poput dugačkog opisa.

Gornje naredbe mogu se promijeniti u NVDA izborniku, podizbornik Postavke,
dijalošk okvir za ulazne geste, kategorija modus čitanja.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
