from lexer import Lexer
from parserRJ import Parser

text_input = """
Brota Aí! 

OBagulho EPar de Biscoito ÉOSeguinte: 
Menor de Meczada  n. 
Partiu! 
    QualFoi ((n%2) PapoReto 0) ? 
        Partiu! 
            Coé " É Par. ". 
        Jáé! 
    MeteOPé ! 
        Partiu! 
            Coé  "Não é Par.". 
        Jáé! 
Jáé! 

BrotaNaBase EPar Menor 10.

É Biscoito!
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

#for token in tokens:
#    print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()