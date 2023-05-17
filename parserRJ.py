from rply import ParserGenerator


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['BROTA', 'AI','BISCOITO', 'MENOR','DE', 'DEF', 'ARGUMENT', 'RETURN','FUNCTION_CALL','IF','ELIF','PRINT',
             'WHILE/LOOP','ELSE','OPEN_PAREN', 'CLOSE_PAREN','OPEN_BRACE','CLOSE_BRACE','TYPE','TYPE_VECTOR','COMMA','ASSIGN','DOT',
             'É','QUESTION_MARK', 'EXCLAMATION_MARK', 'SUM','MINUS','MULTIPLIER','DIVIDER','MOD','BOOLEAN','STRING','NUMBER','NAME']
        )

    def parse(self):
        @self.pg.production('rj : BROTA AI program É BISCOITO')
        def rj(p):
            return p
        
        @self.pg.production('program : functionbuild program')
        @self.pg.production('program : resource program ')
        @self.pg.production('program : ')
        def program(p):
            return p
        
        @self.pg.production('resource : declare')
        @self.pg.production('resource : functioncall')
        @self.pg.production('resource : condition')
        @self.pg.production('resource : loop')
        @self.pg.production('resource : attribuition')
        @self.pg.production('resource : printer')
        def resource(p):
            return p
        
        @self.pg.production('variabletypes : TYPE')
        @self.pg.production('variabletypes : TYPE_VECTOR variabletypes')
        def variabletypes(p):
            return p
        
        @self.pg.production('execute : OPEN_BRACE resource CLOSE_BRACE')
        def execute(p):
            return p
        
        
        @self.pg.production('arguments : MENOR DE variabletypes NAME argumentlist')
        def arguments(p):
            return p

        @self.pg.production('argumentlist : COMMA MENOR DE variabletypes NAME argumentlist')
        @self.pg.production('argumentlist : ')
        def argumentlist(p):
            return p


        @self.pg.production('functionbuild : DEF NAME DE variabletypes ARGUMENT arguments DOT OPEN_BRACE resource RETURN expression CLOSE_BRACE')
        @self.pg.production('functionbuild : DEF NAME DE variabletypes ARGUMENT arguments DOT OPEN_BRACE resource CLOSE_BRACE')
        def functionbuild(p):
            return p
        
        
        @self.pg.production('declare : variabletypes NAME ASSIGN expression DOT')
        def declare(p):
            return p
        
        @self.pg.production('loop_functioncall : COMMA MENOR expression loop_functioncall')
        @self.pg.production('loop_functioncall : ')
        def loop_functioncall(p):
            return p
        
        @self.pg.production('functioncall : FUNCTION_CALL NAME MENOR expression loop_functioncall DOT')
        def functioncall(p):
            return p
        
        @self.pg.production('condition : IF expression QUESTION_MARK execute blockelif blockelse')
        def condition(p):
            return p
        
        @self.pg.production('blockelif : ELIF expression EXCLAMATION_MARK execute blockelif')
        @self.pg.production('blockelif : ')
        def blockelif(p):
            return p
        
        @self.pg.production('blockelse : ELSE EXCLAMATION_MARK execute')
        @self.pg.production('blockelse : ')
        def blockelse(p):
            return p        

        
        @self.pg.production('loop : WHILE/LOOP expression QUESTION_MARK execute')
        def loop(p):
            return p
        
        @self.pg.production('attribuition : NAME ASSIGN expression DOT')
        def attribuition(p):
            return p
        
        
        @self.pg.production('printer : PRINT expression DOT')
        @self.pg.production('printer : PRINT STRING DOT')
        def printer(p):
            return p
        
        @self.pg.production('expression : OPEN_PAREN mathematical CLOSE_PAREN')
        @self.pg.production('expression : mathematical')
        def expression(p):
            return p
        
        
        @self.pg.production('mathematical : term')
        @self.pg.production('mathematical : term add_sub_term')
        def mathematical(p):
            return p

        @self.pg.production('term : factor')
        @self.pg.production('term : factor mul_div_factor')
        def term(p):
            return p

        @self.pg.production('factor : SUM factor')
        @self.pg.production('factor : MINUS factor')
        @self.pg.production('factor : OPEN_PAREN mathematical CLOSE_PAREN')
        @self.pg.production('factor : NUMBER')
        @self.pg.production('factor : NAME')
        def factor(p):
            return p 

        @self.pg.production('add_sub_term : SUM term')
        @self.pg.production('add_sub_term : MINUS term')
        def add_sub_term(p):
            return 

        @self.pg.production('mul_div_factor : MULTIPLIER factor')
        @self.pg.production('mul_div_factor : DIVIDER factor')
        @self.pg.production('mul_div_factor : MOD factor')
        @self.pg.production('mul_div_factor : BOOLEAN factor') 
        def mul_div_factor(p):
            return p
        


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()