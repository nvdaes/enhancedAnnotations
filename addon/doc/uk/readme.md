# Enhanced Annotations (Розширені Анотації) #

* Authors: George Kerscher, Noelia Ruiz Martínez

Консорціум DAISY розробляє найкращі практики для видавців і авторів щодо
надання розширених (довгих) описів.

Найкращі практики використовують елемент деталей HTML, який слідує за
зображенням, або посилання на інший файл, який містить розширений опис.

В обох варіантах користувачеві потрібно перейти до деталей або посилання та
активувати його.

Ідеальним є натискання клавіші, щоб зосередитися на деталях або на
посиланні.

Наші найкращі практики рекомендують розміщувати деталі або посилання
безпосередньо після зображення, а якщо перейти за посиланням, потрібно
надати зворотне посилання на точне місцезнаходження. Це гарантує, що
користувач не заблукає.

Проте дуже часто автори  розміщують розширені (довгі) описи майже скрізь. У
цих випадках користувач захоче повернутися до зображення, а отже, потрібен
спосіб повернутися до початкового зображення.

This add-on provides both features, in support of this [issue opened in
NVDA's repository][1].

## Команди ##

* NVDA+alt+d: переміщує курсор до елемента, ідентифікованого як
  aria-details.
* NVDA+alt+shift+d: moves the cursor to the original element, for example,
  an image with furter details like a long description. If NVDA+alt+d has
  been pressed several times to move to related annotations, it'll be
  possible to go back to each origin.

Наведені вище команди можна змінити в меню NVDA, підменю «Параметри»,
діалозі «Жести вводу», категорії «Режим огляду».

## Changes for 2.0 ##

* Added ability to move back through multiple annotation origins.
* Requires NVDA 2023.1 or later.

[[!tag dev stable]]

[1]: https://github.com/nvaccess/nvda/issues/13940
