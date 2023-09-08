# Verbesserte Anmerkungen #

* Autoren: George Kerscher, Noelia Ruiz Martínez

Im DAISY-Konsortium werden Best Practices für Verlage und Autoren
entwickelt, um erweiterte (lange) Beschreibungen bereitzustellen.

Am besten verwenden Sie das HTML-Details-Element, das auf das Bild folgt,
oder einen Link zu einer anderen Datei, die die erweiterte Beschreibung
enthält.

Bei beiden Optionen müsste der Nutzer zu den Details oder dem Link gehen und
ihn aktivieren.

Ein Tastendruck, um den Fokus auf die Details oder den Link zu legen, ist
ideal.

Es wird empfohlen, dass die Details oder der Link unmittelbar auf das Bild
folgen, und wenn dem Link gefolgt wird, muss ein Backlink zum genauen
Standort angegeben werden. So wird sichergestellt, dass der Nutzer sich
nicht verirrt.

Es ist jedoch wahrscheinlich, dass viele Autoren die erweiterte (lange)
Beschreibung fast überall platzieren. In diesen Fällen würde der Benutzer zu
dem Bild zurückkehren wollen, und daher ist eine Möglichkeit erforderlich,
zum Originalbild zurückzukehren.

Diese NVDA-Erweiterung bietet beide Funktionen, um dies zu unterstützen
[Problem eingereicht im NVDA-Repository][2].

## Befehle ##

* NVDA+Alt+D: Zieht den Cursor auf das mit "aria-details" gekennzeichnete
  Element.
* NVDA+Alt+Umschalt+D: Bewegt den Cursor auf das ursprüngliche Element,
  z. B. ein Bild mit weiteren Details wie einer langen Beschreibung. Wenn
  Sie NVDA+Alt+D mehrmals gedrückt haben, um zu verwandten Anmerkungen zu
  gelangen, können Sie zu jedem Ursprung zurückkehren.

Die oben genannten Tastenbefehle können über die Einstellungen im NVDA-Menü
im Dialogfeld für die Tastenbefehle und dort in der Kategorie "Lesemodus"
geändert werden.

## Änderungen in 2.0 ##

* Sie können durch mehrere Anmerkungen wechseln.
* NVDA 2023.1 oder neuer wird benötigt.

[[!tag dev stable]]

[2]: https://github.com/nvaccess/nvda/issues/13940
