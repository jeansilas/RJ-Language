<img src=https://github.com/jeansilas/RJ-Language/assets/39682690/a66bf3c6-4d73-47bd-9af1-3946c2fbe07a alt="Descrição da imagem" width=200 height=200 /> 

# RJ Language

## Introdução

A RJ Language é uma linguagem de programação intuitiva inspirada no "carioquês" projetada para o desenvolvimento de algortimos através de algo mais verbal e lúdico. Com sua sintaxe clara e recursos poderosos, a RJ Language permite que os desenvolvedores escrevam código de maneira eficiente.

## Características

* **Simplicidade**: A RJ Language foi projetada para ser fácil de aprender e usar, mesmo para iniciantes em programação. Sua sintaxe clara e intuitiva permite que você se concentre na lógica do seu código, em vez de se preocupar com detalhes complicados.

* **Expressividade**: Com a RJ Language, você pode expressar suas ideias de forma concisa e direta. A linguagem fornece construções de alto nível que permitem expressar a lógica do seu programa de maneira natural e intuitiva.

* **Versatilidade**: A RJ Language suporta uma ampla gama de recursos, incluindo declaração de variáveis, estruturas de controle, funções e expressões. Com esses recursos, você pode criar algoritmos complexos e poderosos de forma eficiente.

## Exemplos de Código
Aqui estão alguns exemplos de código escritos na RJ Language:

### Soma de Dois Números
```
OBagulho somaDeDoisNumeros ÉOSeguinte: Menor de Meczada x, Menor de Meczada y. Partiu! Coé x + y . Jáé!

BrotaNaBase somaDeDoisNumeros Menor 2, Menor 3 .
```
### Testa se é um Número é Par
```
Brota Aí ! 

OBagulho EPar de Biscoito ÉOSeguinte: Menor de Meczada  n. Partiu! QualFoi ((n%2) PapoReto 0) ? 
Partiu! Coé " É Par. " . Jáé! MeteOPé ! Partiu! Coé  "Não é Par.". Jáé! Jáé! 

BrotaNaBase EPar Menor 10 .

É Biscoito !
```
### Diz a paridade dos Números de 1 a 10

```
Brota Aí !

Coé "Hey" .
Meczada x é 1 .
OBagulho Aulas de Biscoito ÉOSeguinte: . Partiu! Coé "loop" . Jáé!

OBagulho Namoral de Biscoito ÉOSeguinte: Menor de Meczada animada . Partiu! QualFoi animada % 2 PapoReto 0 ? Partiu! Coé "par" . Jáé! MeteOPé !
Partiu! Coé "ímpar" . Jáé! Jáé!

OBagulho ChegaJunto de Meczada ÉOSeguinte: Menor de Meczada tilt, Menor de Meczada tiltado.
Partiu! tilt é tiltado + tilt. MandaBala tilt . Jáé!

MarcaUmDezAíSe x PapoTorto 10 ? Partiu! BrotaNaBase Namoral Menor x . BrotaNaBase Aulas . x é BrotaNaBase ChegaJunto Menor x, Menor 1 . Jáé! Coé "fim" .

É Biscoito !
```


## EBNF 

```


RJ = “Brota”, “Aí”, “!”, PROGRAM, “É”, “Biscoito”,”!” ;


PROGRAM = {FUNCTIONBUILD | RESOURCE} ;

RESOURCE = DECLARE | FUNCTIONCALL | CONDITION | LOOP | ATTRIBUITION | PRINTER  ;

VARIABLETYPES =  “Meczada” | “Letra” | “Biscoito” ;

EXECUTE = “Partiu!”, RESOURCE, “Jáé!” ;

ARGUMENTS = “Menor”, “de”, VARIABLETYPES , NAME , { "," , “Menor”, “de”, VARIABLETYPES , NAME } ;

FUNCTIONBUILD = ”OBagulho”, NAME, “de”, VARIABLETYPES, “ÉOSeguinte:”, {ARGUMENTS}, “.”, “Partiu!”, RESOURCE, {“MandaBala”, EXPRESSION}, “Jáé!” ;

DECLARE = VARIABLETYPES, NAME, “é”, EXPRESSION, “.”;

FUNCTIONCALL = “BrotaNaBase”, NAME, { (“Menor”, EXPRESSION),  { ",“ , "Menor”, EXPRESSION } } , “.” ;

CONDITION = “QualFoi”, EXPRESSION, “?”, EXECUTE, {“PegaAVisão”, EXPRESSION, “!”, EXECUTE},  (“MeteOPé”, “!”, EXECUTE)? ;

LOOP = “MarcaUmDezAíSe”, EXPRESSION, “?”, EXECUTE;

ATTRIBUTION = NAME, “é”, EXPRESSION, “.” ;

PRINTER = “Coé”, (EXPRESSION | STRING), “.” ;

EXPRESSION =  MATHEMATICAL | ( “(”, MATHEMATICAL, “)”) ;

MATHEMATICAL = TERM, { (“+” | “-”), TERM } ;

TERM = FACTOR, { ( “*” | “/” | “%” | BOOLEAN ), FACTOR } ;

FACTOR = ( ( “+” | “-”), FACTOR ) | ( “(“, MATHEMATICAL, “)” ) | NUMBER | NAME | FUNCTIONCALL ;

BOOLEAN = “e”| “ou” | “câo” | “PapoReto” | “PapoTorto” ;

STRING = “"”, {NAME}, “"” ;

NAME = LETTER, {LETTER};

LETTER = “a”| ”A”| “b”| “B”| …| “Z”| “_”| “@”| “-”| “?” | “!”| …| “.” ;

NUMBER = DIGIT, {DIGIT}; 

DIGIT = 0 | 1 | 2 | 3 | 3 | 5 | 6 | 7 | 8 | 9 | ;

```
### Dicionário

| **PapoReto** | **PapoTorto** | **Meczada** | **Biscoito** | **Letra**| 
|--------------|---------------|-------------|--------------|----------|
|                                                                      |
|  Igual (==)  | Diferente (!=)|Inteiro (Int)| Vazio (Void) |  String  |  

## Contribuição
Contribuições para a RJ Language são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests para melhorar a linguagem.

## Licença
A RJ Language é distribuída sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir a linguagem de acordo com os termos da licença.




