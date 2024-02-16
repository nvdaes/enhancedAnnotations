# Anotações Melhoradas #

* Authors: George Kerscher, Noelia Ruiz Martínez

No DAISY Consortium, são desenvolvidas as melhores práticas para editores e
autores para fornecer descrições (longas) alargadas.

As melhores práticas utilizam o elemento de detalhes HTML que segue a
imagem, ou um link para outro ficheiro que contém a descrição alargada.

Em ambas as opções, o utilizador teria de passar para os detalhes ou para a
ligação e activá-la.

Ter uma tecla para colocar o foco nos detalhes ou a ligação é o ideal.

As nossas melhores práticas recomendam que os detalhes ou a ligação sigam
imediatamente a imagem, e se a ligação for seguida, deve ser fornecida uma
ligação de retorno para o local exacto. Isto torna seguro que o utilizador
não se perderá.

No entanto, é provável que os autores na natureza coloquem a descrição
extensa (longa) em quase qualquer lugar. Nestes casos, o utilizador gostaria
de regressar à imagem e, por conseguinte, à necessidade de uma forma de
regressar à imagem original.

Este extra fornece ambas as características, em apoio a esta [questão aberta
no repositório da NVDA][2].

## Comandos: ##

* NVDA+alt+d: move o cursor para o elemento identificado com aria-detalhes.
* NVDA+alt+shift+d: moves the cursor to the original element, for example,
  an image with furter details like a long description. If NVDA+alt+d has
  been pressed several times to move to related annotations, it'll be
  possible to go back to each origin.

Os comandos acima podem ser modificados a partir do menu da NVDA, submenu
Preferências, diálogo definir comandos, categoria Modo de navegação.

## Changes for 2.0 ##

* Added ability to move back through multiple annotation origins.
* Requires NVDA 2023.1 or later.

[[!tag dev stable]]

[2]: https://github.com/nvaccess/nvda/issues/13940
