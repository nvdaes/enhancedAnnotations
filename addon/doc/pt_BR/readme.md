# Enhanced Annotations #

* Autores: George Kerscher, Noelia Ruiz Martínez

No DAISY Consortium, as práticas recomendadas são desenvolvidas para
editores e autores para fornecer descrições estendidas (longas).

As práticas recomendadas usam o elemento de detalhes HTML que segue a imagem
ou um link para outro arquivo que contém a descrição estendida.

Em ambas as opções, o usuário precisaria ir até os detalhes ou o link e
ativá-lo.

O ideal é ter um pressionamento de tecla para colocar o foco nos detalhes ou
no link.

Nossas práticas recomendadas recomendam que os detalhes ou o link sigam
imediatamente a imagem e, se o link for seguido, deve ser fornecido um link
de retorno para o local exato. Isso garante que o usuário não se perderá.

No entanto, é provável que os autores coloquem a descrição estendida (longa)
em praticamente qualquer lugar. Nesses casos, o usuário desejaria retornar à
imagem e, por isso, a necessidade de uma maneira de retornar à imagem
original.

Esse complemento fornece ambos os recursos, em apoio a esse [problema aberto
no repositório do NVDA][1].

## Comandos ##

* NVDA+alt+d: move o cursor para o elemento identificado com aria-details.
* NVDA+alt+shift+d: move o cursor para o elemento original, por exemplo, uma
  imagem com detalhes mais precisos, como uma descrição longa. Se NVDA+alt+d
  tiver sido pressionado várias vezes para mover para anotações
  relacionadas, será possível voltar a cada origem.

Os comandos acima podem ser modificados no menu do NVDA, submenu
Preferências, caixa de diálogo Gestos de entrada, categoria Modo de
navegação.

## Alterações para a versão 2.0 ##

* Adicionada a capacidade de retroceder em várias origens de anotações.
* Requer o NVDA 2023.1 ou posterior.

[[!tag dev stable]]

[1]: https://github.com/nvaccess/nvda/issues/13940
