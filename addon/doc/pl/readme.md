# Rozszerzone adnotacje #

* Authors: George Kerscher, Noelia Ruiz Martínez

W konsorcjum DAISY opracowywane są najlepsze praktyki dla wydawców i autorów
w zakresie dostarczania rozszerzonych (długich) opisów.

Najważniejsze wskazówki wykorzystują element HTML details następujący po
obrazie lub łącze do innego pliku zawierającego opis rozszerzony.

W obu opcjach użytkownik musiałby przejść do szczegółów lub linku i
aktywować go.

Idealne jest naciśnięcie, aby skupić się na szczegółach lub łączu.

Nasze najlepsze praktyki zalecają, aby szczegóły lub link znajdowały się
bezpośrednio po obrazie, a jeśli link jest przestrzegany, należy podać link
zwrotny do dokładnej lokalizacji. Dzięki temu masz pewność, że użytkownik
się nie zgubi.

Jest jednak prawdopodobne, że autorzy na wolności umieszczą rozszerzony
(długi) opis niemal wszędzie. W takich przypadkach użytkownik chciałby
powrócić do obrazu, a tym samym potrzeba powrotu do oryginalnego obrazu.

Ten dodatek zapewnia obie funkcje, wspierając ten [problem otwarty w
repozytorium NVDA][2].

## Polecenia ##

* NVDA+alt+d: przesuwa kursor do elementu identyfikowanego za pomocą
  aria-details.
* NVDA+alt+shift+d: przesuwa kursor do oryginalnego elementu, na przykład
  obrazu z szczegółami furter, takimi jak długi opis. Jeśli NVDA+alt+d
  został naciśnięty kilka razy, aby przejść do powiązanych adnotacji, będzie
  można wrócić do każdego źródła.

Powyższe polecenia można modyfikować z poziomu menu NVDA, podmenu
Preferencje, okna dialogowego Gesty wejściowe, kategorii Tryb przeglądania.

## Zmiany dla 2.0 ##

* Dodano możliwość przechodzenia wstecz przez wiele źródeł adnotacji.
* Wymaga NVDA 2023.1 lub nowszego.

[[!tag dev stable]]

[2]: https://github.com/nvaccess/nvda/issues/13940
