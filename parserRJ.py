from rply import ParserGenerator


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['BROTA', 'AI','BISCOITO', 'MENOR','DE', 'DEF', 'ARGUMENT', 'RETURN','FUNCTION_CALL','IF','ELIF','PRINT',
             'WHILE/LOOP','ELSE','OPEN_PAREN', 'CLOSE_PAREN','OPEN_BRACE','CLOSE_BRACE','TYPE','TYPE_VECTOR''COMMA','ASSIGN','DOT',
             'É','QUESTION_MARK', 'EXCLAMATION_MARK', 'SUM','MINUS','MULTIPLIER','DIVIDER','MOD','BOOLEAN','STRING','NUMBER','NAME']
        )

    def parse(self):
        @self.pg.production('rj : BROTA AI program É BISCOITO')
        def rj(p):
            return p
        
        @self.pg.production('functionbuild : DEF NAME DE variabletypes ARGUMENT arguments OPEN_BRACE resource RETURN expression CLOSE_BRACE')
        def functionbuild(p):
            return p
        
        @self.pg.production('variabletypes : TYPE')
        @self.pg.production('variabletypes : TYPE_VECTOR variabletypes')
        def variabletypes(p):
            return p
        
        
        @self.pg.production('declare : variabletypes NAME ASSIGN expression DOT')
        def declare(p):
            return p
        
        @self.pg.production('loop_functioncall : COMMA MENOR NAME loop_functioncall')
        @self.pg.production('loop_functioncall : ')
        def loop_functioncall(p):
            return p
        
        @self.pg.production('functioncall : FUNCTION_CALL NAME MENOR NAME loop_functiocall DOT')
        def functioncall(p):
            return p
        
        @self.pg.production('condition : IF expression QUESTION_MARK execute {ELIF expression EXCLAMATION_MARK execute } (ELSE EXCLAMATION_MARK execute)')
        def condition(p):
            return p
        
        @self.pg.production('loop : WHILE/LOOP expression QUESTION_MARK execute')
        def loop(p):
            return p
        
        @self.pg.production('attribuition : NAME ASSIGN expression DOT')
        def attribuition(p):
            return p
        
        @self.pg.production('resource : declare| functioncall | condition | loop | attribuition')
        def resource(p):
            return p

        @self.pg.production('program : {functionbuild | resource}')
        def program(p):
            return p


        
        @self.pg.production('arguments : MENOR DE variabletypes NAME {COMMA MENOR DE variabletypes NAME}')
        def arguments(p):
            return p
        
        
        
        
        @self.pg.production('printer : PRINT expression DOT')
        def printer(p):
            return p
        
        @self.pg.production('expression : OPEN_PAREN STRING | NAME | booleans | mathematical CLOSE_PAREN')
        def expression(p):
            return p
        
        @self.pg.production('booleans : expression BOOOLEAN expression')
        def booleans(p):
            return p
        
        @self.pg.production('mathematical : term { (SUM | MINUS) term}')
        def mathematical(p):
            return p
        
        @self.pg.production('term : factor { (MULTIPLIER | DIVIDER | MOD) factor}')
        def term(p):
            return p
        
        @self.pg.production('factor : (SUM | MINUS) factor | OPEN_PAREN mathematical CLOSE_PAREN | NUMBER')
        def factor(p):
            return p
        


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()