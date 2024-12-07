# Enhanced Annotations #

* Auteurs : George Kerscher, Noelia Ruiz Martínez

Dans le consortium DAISY, les meilleures pratiques sont développées pour les
éditeurs et les auteurs pour avoir fourni des descriptions étendues
(longues).

Les meilleures pratiques utilisent l'élément details HTML qui suit l'image,
ou un lien vers un autre fichier qui contient la description étendue.

Dans les deux options, l'utilisateur devrait se déplacer vers les détails ou
le lien et l'activer.

Avoir un raccourci clavier pour mettre le focus sur les détails ou le lien
est idéal.

Nos meilleures pratiques recommandent que les détails ou le lien suivent
immédiatement l'image, et si le lien est suivi, un lien de retour à
l'emplacement exact doit être fourni. Cela garantit que l'utilisateur ne se
perdra pas.

Cependant, les auteurs sont susceptibles de placer la description étendue
(longue) presque partout. Dans ces cas, l'utilisateur voudrait revenir à
l'image, d'où la nécessité d'un moyen de revenir à l'image d'origine.

This add-on provides both features, in support of this [issue opened in
NVDA's repository][1].

## Commandes ##

* NVDA+alt+d : déplace le curseur vers l'élément identifié avec
  Aria-Details.
* NVDA+alt+Maj+d : déplace le curseur vers l'élément d'origine, par exemple,
  une image avec plus de détails comme une description longue. Si NVDA+alt+d
  a été pressé plusieurs fois pour se déplacer vers des annotations
  connexes, il sera possible de revenir à chaque origine.

Les commandes ci-dessus peuvent être modifiées à partir du menu NVDA,
Préférences sous-menu, dans le dialogue Gestes de commandes, sous la
catégorie Mode navigation.

## Changements pour la version 2.0 ##

* Ajout de la possibilité de revenir à travers de plusieurs annotations
  d'origine.
* Nécessite NVDA 2023.1 ou version ultérieure.

[[!tag dev stable]]

[1]: https://github.com/nvaccess/nvda/issues/13940
