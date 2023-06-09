# RJ-Language

# EBNF

```

RJ = “Brota”, “Aí”, “!”, PROGRAM, “É”, “Biscoito”,”!” ;


PROGRAM = {FUNCTIONBUILD | RESOURCE} ;

RESOURCE = DECLARE | FUNCTIONCALL | CONDITION | LOOP | ATTRIBUITION | PRINTER  ;

VARIABLETYPES =  “Meczada” | “VoaMlk” | “TaLigado?” | “Letra” | “Letrinha” | “Biscoito” |  (“BondeDos”, VARIABLETYPES)   ;

EXECUTE = “Partiu!”, RESOURCE, “Jáé!” ;

ARGUMENTS = “Menor”, “de”, VARIABLETYPES , NAME , { "," , “Menor”, “de”, VARIABLETYPES , NAME } ;

FUNCTIONBUILD = ”OBagulho”, NAME, “de”, VARIABLETYPES, “ÉOSeguinte:”, ARGUMENTS, “.”, “Partiu!”, RESOURCE, {“MandaBala”, EXPRESSION}, “Jáé!” ;

DECLARE = VARIABLETYPES, NAME, “é”, EXPRESSION, “.”;

FUNCTIONCALL = “BrotaNaBase”, NAME, “Menor”, EXPRESSION,  { ",“ , "Menor”, EXPRESSION } , “.” ;

CONDITION = “QualFoi”, EXPRESSION, “?”, EXECUTE, {“PegaAVisão”, EXPRESSION, “!”, EXECUTE},  (“MeteOPé”, “!”, EXECUTE)? ;

LOOP = “MarcaUmDezAíSe”, EXPRESSION, “?”, EXECUTE;

ATTRIBUTION = NAME, “é”, EXPRESSION, “.” ;

PRINTER = “Coé”, (EXPRESSION | STRING), “.” ;

EXPRESSION =  MATHEMATICAL | ( “(”, MATHEMATICAL, “)”) ;

MATHEMATICAL = TERM, { (“+” | “-”), TERM } ;

TERM = FACTOR, { ( “*” | “/” | “%” | BOOLEAN ), FACTOR } ;

FACTOR = ( ( “+” | “-”), FACTOR ) | ( “(“, MATHEMATICAL, “)” ) | NUMBER | NAME ;

BOOLEAN = “e”| “ou” | “câo” | “PapoReto” | “PapoTorto” ;

STRING = “"”, {NAME}, “"” ;

NAME = LETTER, {LETTER};

LETTER = “a”| ”A”| “b”| “B”| …| “Z”| “_”| “@”| “-”| “?” | “!”| …| “.” ;

NUMBER = DIGIT, {DIGIT}; 

DIGIT = 0 | 1 | 2 | 3 | 3 | 5 | 6 | 7 | 8 | 9 | ;

```




