%{
#include <stdio.h>
#include <stdlib.h>
#include "RJ.tab.h"


%}

numbers ([0-9])+
name [a-zA-Z_][a-zA-Z0-9_]*
operator "+"|"-"|">="|"<="|">"|"<"|"=="|"%"
%%;
"Brota"           {printf("BROTA\n");return BROTA; }
"Aí"              {printf("Aí\n");return AI; }
"É"               {printf("É\n");return E; }
"!"               {printf("!\n");return EXCLAMATION; }
"Biscoito"        {printf("Biscoiton");return BISCOITO; }
"Meczada"         {printf("Meczada\n");return MECZADA; }
"VoaMlk"          {printf("VoaMlk\n");return VOA_MLK; }
"Letra"           {printf("Letra\n");return LETRA; }
"Letrinha"        {printf("Letrinha\n");return LETRINHA; }
"BondeDos"        {printf("BondeDos\n");return BONDE_DOS; }
"Partiu!"         {printf("Partiu!\n");return PARTIU; }
"Jáé!"            {printf("Jáé!\n");return JAE; }
"Menor"           {printf("Menor\n");return MENOR; }
"OBagulho"        {printf("OBagulho\n");return O_BAGULHO; }
"de"              {printf("de\n");return DE; }
"ÉOSeguinte:"     {printf("ÉOSeguinte:\n");return E_O_SEGUINTE; }
"MandaBala"       {printf("MandaBala\n");return MANDA_BALA;}
"é"               {printf("é\n");return E_; }
"BrotaNaBase"     {printf("BrotaNaBase\n");return BROTA_NA_BASE; }
"QualFoi"         {printf("QualFoi\n");return QUAL_FOI; }
"PegaAVisão"      {printf("PegaAVisão\n");return PEGA_A_VISAO; }
"MeteOPé"         {printf("MeteOPé\n");return METE_O_PE; }
"MarcaUmDezAíSe"  {printf("MarcaUmDezAíSe\n");return MARCA_UM_DEZ_AI_SE; }
"e"               {printf("e\n");return E_LOGICO; }
"ou"              {printf("ou\n");return OU_LOGICO; }
"câo"             {printf("câo\n");return CAO_LOGICO; }
"PapoReto"        {printf("PapoReto\n");return PAPO_RETO; }
"PapoTorto"       {printf("PapoTorto\n");return PAPO_TORTO; }
","               {printf(",\n");return VIRGULA; }
"("               {printf("(\n");return ABRE_PARENTESE; }
")"               {printf(")\n");return FECHA_PARENTESE; }
"{"               {printf("{\n");return ABRE_CHAVES; }
"}"               {printf("}\n");return FECHA_CHAVES; }
"TaLigado?"       {printf("TaLigado\n");return TA_LIGADO; }
"Coé"             {printf("Coé\n");return COE_PRINT; }
"-"               {printf("-\n");return HIFEN; }
"?"               {printf("?\n");return INTERROGACAO; }
"@"               {printf("@\n");return ARROBA; }
"."               {printf(".\n");return PONTO; }
{operator}        {printf("operador\n");return OPERATOR;}
{name}            {printf("nome\n");return NAME; }
{numbers}         {printf("numero\n");return NUMBER; }
\"[^\"\n]*\"      { printf("STRING: %s\n", yytext); return STRING; }
[ \t\n]+          { /* ignore whitespace */ }
.                 { printf("Invalid character: %s\n", yytext); }
%%

int yywrap() {
    return 1;
}
