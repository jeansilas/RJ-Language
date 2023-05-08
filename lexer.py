from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # RJ-Tokens
        self.lexer.add('BROTA',r'Brota')
        self.lexer.add('AI',r'Aí!')
        self.lexer.add("BISCOITO", r'Biscoito!')

        #Auxiliar Tokens
        self.lexer.add('MENOR', r'Menor')
        self.lexer.add('DE', r'de')

        # Function Builder
        self.lexer.add("DEF",r'OBagulho')
        self.lexer.add("ARGUMENT",r'ÉOSeguinte:')
        self.lexer.add("RETURN",r'MandaBala')

        # Function Call
        self.lexer.add("FUNCTION_CALL",r'BrotaNaBase')

        # Conditions
        self.lexer.add("IF",r'QualFoi')
        self.lexer.add("ELIF",r'PegaAVisão')
        self.lexer.add("ELSE",r'MeteOPé')

        # Print
        self.lexer.add('PRINT', r'Coé')

        # Loop
        self.lexer.add('WHILE/LOOP', r'MarcaUmDezAíSe')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Braces
        self.lexer.add('OPEN_BRACE', r'Partiu!')
        self.lexer.add('CLOSE_BRACE', r'Jáé!')

         # Variable Type
        self.lexer.add('TYPE', r'Meczada')
        self.lexer.add('TYPE',r'VoaMlk')  
        self.lexer.add('TYPE',r'TaLigado?') 
        self.lexer.add('TYPE',r'Letra') 
        self.lexer.add('TYPE',r'Letrinha')
        self.lexer.add('TYPE',r'Biscoito')
        self.lexer.add('TYPE_VECTOR',r'BondeDos')

        # Assingment
        self.lexer.add('ASSIGN', r'é')


        # Comma
        self.lexer.add('COMMA', r'\,')
        
        # Dot
        self.lexer.add('DOT', r'\.')

        # É
        self.lexer.add("É", r'É')

        # Question Mark
        self.lexer.add("QUESTION_MARK", r'\?')

        # Exclamation Mark
        self.lexer.add("EXCLAMATION_MARK", r'\!')


        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('MINUS', r'\-')
        self.lexer.add('MULTIPLIER', r'\*')
        self.lexer.add('DIVIDER', r'\/')
        self.lexer.add('MOD', r'\%') 

        # Booleans
        self.lexer.add('BOOLEAN', r'e') # and
        self.lexer.add('BOOLEAN', r'ou') # or
        self.lexer.add('BOOLEAN', r'câo') # not
        self.lexer.add('BOOLEAN', r'PapoReto') # ==
        self.lexer.add('BOOLEAN', r'PapoTorto') # != 


        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Name
        self.lexer.add('NAME', r'[a-zA-Z_][a-zA-Z0-9_]*')

        # String
        self.lexer.add('STRING', r'\".*?\"')

        # Ignore spaces
        self.lexer.ignore('\s+')

        # Ignore line jumps
        self.lexer.ignore('\n')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()