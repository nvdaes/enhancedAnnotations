# Разширени анотации (Enhanced Annotations) #

* Автори: George Kerscher, Noelia Ruiz Martínez
* [изтегляне на стабилна версия][1] (съвместима с NVDA 2022.1 и по-нови
  версии)

В консорциума DAISY са разработени най-добри практики за издатели и автори
за предоставяне на разширени (дълги) описания.

Най-добрите практики използват елемента HTML details, който следва
изображението, или връзка към друг файл, който съдържа разширеното описание.

И в двата варианта потребителят ще трябва да премине към подробностите или
към връзката и да я задейства.

Наличието на клавишна команда за преместване на фокуса върху подробностите
или връзката е идеално.

Нашите най-добри практики препоръчват подробностите или връзката да следват
непосредствено изображението и ако връзката бъде последвана, трябва да се
предостави обратна връзка към точното местоположение. Това гарантира, че
потребителят няма да се изгуби.

Въпреки това е вероятно авторите в тази област да поставят разширеното
(дълго) описание почти навсякъде. В тези случаи потребителят би искал да се
върне към изображението и оттук необходимостта от начин за връщане към
оригиналното изображение.

Тази добавка предоставя и двете функции в подкрепа на този [доклад,
публикуван в хранилището на NVDA][2].

## Команди ##

* NVDA+Alt+D: Премества курсора към елемента, идентифициран с aria-details.
* NVDA+Alt+Shift+D: Премества курсора към оригиналния елемент, например
  изображение с допълнителни подробности като дълго описание.

Гореизброените команди могат да се променят от менюто на NVDA -> подменюто
"Настройки" -> диалоговия прозорец "Жестове на въвеждане" -> категорията
"Режим на разглеждане".

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940