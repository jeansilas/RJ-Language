
import sys
from abc import ABC, abstractmethod

# -*- coding: utf-8 -*-

RESERVED_WORDS = ["Brota", "Aí", "É", "Biscoito", "Meczada", "VoaMlk","TaLigado","Letra","Letrinha","Biscoito", "BondeDos", "Partiu!","Jáé","Menor","de","OBagulho","ÉOSeguinte:","MandaBala","QualFoi","PegaAVisão","MeteOPé","Coé","MarcaUmDezAíSe","BrotaNaBase",]
VAR_TYPES = [ "Meczada", "VoaMlk","TaLigado","Letra","Letrinha","Biscoito", "BondeDos"]
ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_=áéíóúâêîôûãõÁÉÍÓÚÂÊÎÔÛÃÕ.!?"
def read_archive(archive_path):
    text = ""
    with open(archive_path, encoding="utf-8") as file:
        text = file.read()
    return text

class Token:

    def __init__(self, string, value):
        self.string = string
        self.value = value

class PrePro:

    def filter(self,code):
        lines = code.split("\n")
        lines_no_comment = [line.split("#")[0] for line in lines]
        code_no_comment = ''
        for line in lines_no_comment:
            code_no_comment+= line + "\n"
        
        return code_no_comment[:-1]

class Node(ABC):
     
    @abstractmethod
    def evaluate(self, SymbolTable):
        pass

class UnOp(Node):
     
    def __init__(self,value,children):
        self.value = value
        self.children = children
    
    def evaluate(self, SymbolTable):
         
        unop_type = self.children[0].evaluate(SymbolTable)[1]
        unop_value = self.children[0].evaluate(SymbolTable)[0]

        if unop_type == "Int":
         
            if self.value == '-':
                return [int(-unop_value),"Int"]
            elif self.value == '!':
                return [int(not(unop_value)),"Int"]
            else:
                return [int(unop_value),"Int"]
        else:
            raise TypeError("Precisa ser Int ")

class BinOp(Node):
     
    def __init__(self,value,children):
        self.value = value
        self.children = children
    
    def evaluate(self, SymbolTable):

        left = self.children[0].evaluate(SymbolTable)
        right = self.children[1].evaluate(SymbolTable)


        var_right,type_right = right
        var_left,type_left = left

        if (type_left == type_right):
            if self.value == '-':
                return [int(var_left - var_right),"Int"]
            elif self.value == '+':
                return [int(var_left + var_right),"Int"]
            elif self.value == '*':
                return [int(var_left * var_right),"Int"]
            elif self.value == '/':
                return [int(var_left / var_right),"Int"]
            elif self.value == '%':
                return [int(var_left % var_right),"Int"]
            elif self.value == "PapoReto":
                return [int(var_left == var_right),"Int"]
            elif self.value == "e":
                return [int(var_left and var_right),"Int"]
            elif self.value == "ou":
                return [int(var_left or var_right),"Int"]
            elif self.value == "PapoTorto":
                return [int(var_left != var_right),"Int"]
            else:
                pass
        else:
            if self.value == "PapoReto":
                return [int(var_left == var_right),"Int"]
            elif self.value == "e":
                return [int(var_left and var_right),"Int"]
            elif self.value == "ou":
                return [int(var_left or var_right),"Int"]
            elif self.value == "PapoTorto":
                return [str(var_left) != str(var_right),"String"]

class IntVal(Node):
     
    def __init__(self,value):
        self.value = value
    
    def evaluate(self, SymbolTable):
        return [int(self.value),"Int"]

class StringVal(Node):

    def __init__(self,value):
        self.value = value
    
    def evaluate(self, SymbolTable):
        return [str(self.value),"String"]


class NoOp(Node):
     
    def __init__(self):
        pass
    
    def evaluate(self, SymbolTable):
        pass

class IdentifierOp(Node):
    def __init__(self,value):
        self.value = value
    
    def evaluate(self, SymbolTable):
        try:
            return SymbolTable.getter(self.value.string)
        except:
            return SymbolTable.getter(self.value)

class BlockOp(Node):
    def __init__(self,children):
        self.children = children 
    
    def evaluate(self, SymbolTable):
        for child in self.children:
            if type(child) == ReturnOp:
                return child.evaluate(SymbolTable)
                break
            child.evaluate(SymbolTable)

class AssignmentOp(Node):

    def __init__(self, children):
        self.children = children
    
    def evaluate(self, SymbolTable):
        SymbolTable.setter(self.children[0].value.string,self.children[1].evaluate(SymbolTable))

class PrintOp(Node):

    def __init__(self,children):
        self.children = children
    
    def evaluate(self, SymbolTable):
        print(self.children.evaluate(SymbolTable)[0])

class ReadOp(Node):

    def __init__(self):

        return

    def evaluate(self, SymbolTable):

        return [int(input()),"Int"]

class WhileOp(Node):

    def __init__(self,children):
        self.children = children

    
    def evaluate(self, SymbolTable):
        while self.children[0].evaluate(SymbolTable)[0]:
            self.children[1].evaluate(SymbolTable)

class ifOp(Node):

    def __init__(self, children):
        self.children = children

    def evaluate(self, SymbolTable):
        
        if self.children[0].evaluate(SymbolTable)[0]:
            self.children[1].evaluate(SymbolTable)
        else:
            if len(self.children) > 2:
                self.children[2].evaluate(SymbolTable)

class VarDecOp(Node):

    def __init__ (self, children,value):
        self.children = children
        self.value = value
    
    def evaluate(self, SymbolTable):
        if len(self.children) == 1:
            if self.value == "Meczada":
                self.children.append(IntVal(0))
            elif self.value == "String":
                self.children.append(StringVal(""))
        
        SymbolTable.create(self.children[0].value.string,self.children[1].evaluate(SymbolTable))


class FuncDec(Node):
    
        def __init__(self, children, value):
            self.children = children
            self.value = value
        
        def evaluate(self, SymbolTable):
            FuncTable.create(self.children[0].value.string,self)

class ReturnOp(Node):

        def __init__(self, children):
            self.children = children

        def evaluate(self, SymbolTable):
            return self.children.evaluate(SymbolTable)

class FunctionCall(Node):
    
        def __init__(self, children, value):
            self.children = children
            self.value = value
        
        def evaluate(self, symbolTable):
            function = FuncTable.getter(self.value)
            symboltable = SymbolTable()
            identifier, args, block = function.children

            if len(args) != len(self.children):
                raise NameError("numero de argumentos invalido")
            
            for var, arg in zip(args, self.children):
                var.evaluate(symboltable)
                symboltable.setter(var.children[0].value.string, arg.evaluate(symbolTable))
            
            return block.evaluate(symboltable)


            

          

class FuncTable:

    VARIABLES = {}

    def getter(name):
        return FuncTable.VARIABLES[name]
    
    def setter(name,value):
        if FuncTable.VARIABLES[name][1] == value[1]:
            FuncTable.VARIABLES[name] = value
        else:
            raise NameError("tipo de variavel e valor novo com tipagens divergentes")
    
    def create(name,value):
        if name in FuncTable.VARIABLES.keys():
            raise NameError("variável já foi declarada ")
        else:
            FuncTable.VARIABLES[name] = value


class SymbolTable:

    
    #value = [varValue, varType]

    def __init__(self):
        self.VARIABLES = {}

    def getter(self,name):
        return self.VARIABLES[name]
    
    def setter(self,name,value):
        if self.VARIABLES[name][1] == value[1]:
            self.VARIABLES[name] = value
        else:
            raise NameError("tipo de variavel e valor novo com tipagens divergentes")
    
    def create(self,name,value):
        if name in self.VARIABLES.keys():
            raise NameError("variável já foi declarada ")
        else:
            self.VARIABLES[name] = value




class Tokenizer:

    def __init__(self, source, position):
        self.source = source
        self.position = position
        self.next = ""

    def selectNext(self):
        next = ""
        chain_not_formed = True

        while chain_not_formed:
                
                if len(self.source) <= self.position:
                    chain_not_formed = False
                    self.next  = Token(next, "EOF")

        
                elif self.source[self.position] == " ": #Espaço
                    self.position += 1

                elif self.source[self.position] == "\n": #Espaço
                    self.position += 1
                    
                elif self.source[self.position] in "+-%/*" : # Operador Bool Operator
                    next = self.source[self.position]
                    self.position += 1
                    chain_not_formed = False
                    self.next = Token(next,"OPERATOR")


                elif (self.source[self.position] == "("):
                    next = self.source[self.position]
                    self.position += 1
                    chain_not_formed = False
                    self.next = Token(next,"OPEN_PAR")
                
                elif (self.source[self.position] == ")"):
                    next = self.source[self.position]
                    self.position += 1
                    chain_not_formed = False
                    self.next = Token(next,"CLOSE_PAR")
                
                elif self.source[self.position] in  "0123456789" : #INT

                    while chain_not_formed:
                        next += self.source[self.position]
                        self.position += 1
                        if len(self.source) == self.position:
                            chain_not_formed  = False
                            self.next = Token(next,"INT")
                        elif self.source[self.position] == " ":
                            self.position += 1
                            chain_not_formed = False
                            self.next = Token(next,"INT")
                        elif (self.source[self.position] in "+-*/=><%&.,"):
                            chain_not_formed = False
                            self.next = Token(next,"INT")
                        elif self.source[self.position] == "":
                            chain_not_formed = False
                            self.next = Token(next,"INT")
                        elif (self.source[self.position] == "(") or (self.source[self.position] == ")") :
                            chain_not_formed = False
                            self.next = Token(next,"INT")
                        elif self.source[self.position] == "\n":
                            chain_not_formed = False
                            self.next = Token(next,"INT")
                        elif self.source[self.position] in ALFABETO:
                            chain_not_formed = False
                            self.next = Token(next,"INT")

                elif self.source[self.position] in ALFABETO :
                    while chain_not_formed:
                        next += self.source[self.position]
                        self.position += 1
                        if len(self.source) == self.position:
                            chain_not_formed  = False
                            self.next = Token(next,"IDENTIFIER")
                        elif self.source[self.position] == " ":
                            self.position += 1
                            chain_not_formed = False
                            self.next = Token(next,"IDENTIFIER")
                        elif (self.source[self.position] in "+-*/%=><&.,"):
                            chain_not_formed = False
                            self.next = Token(next,"IDENTIFIER")
                        elif self.source[self.position] == "":
                            chain_not_formed = False
                            self.next = Token(next,"IDENTIFIER")
                        elif (self.source[self.position] == "(") or (self.source[self.position] == ")") :
                            chain_not_formed = False
                            self.next = Token(next,"IDENTIFIER")
                        elif self.source[self.position] == "\n":
                            chain_not_formed = False
                            self.next = Token(next,"IDENTIFIER")
                        elif self.source[self.position:self.position+2] == "::":
                            chain_not_formed = False
                            self.next = Token(next,"IDENTIFIER")
                
                elif self.source[self.position] == '"'   :
                    #next += self.source[self.position]
                    self.position += 1
                    while self.source[self.position] != '"':
                        next += self.source[self.position]
                        self.position += 1
                    #next += self.source[self.position]
                    self.position += 1
                    chain_not_formed = False
                    self.next = Token(next,"STRING")

                elif self.source[self.position] == ".":  #OperatorConcatenate
                    next += self.source[self.position]
                    self.position += 1
                    chain_not_formed = False
                    self.next = Token(next,"OPERATOR")

                elif self.source[self.position] == ",":  #Comma
                    next += self.source[self.position]
                    self.position += 1
                    chain_not_formed = False
                    self.next = Token(next,"COMMA")

                elif self.source[self.position] == "\n":
                    next += self.source[self.position]
                    self.position +=1
                    self.next = Token(next,"LINHA")
                    chain_not_formed = False
                    

                elif self.source[self.position] == "": # EOF
                    chain_not_formed = False
                    self.next = Token(next,"EOF")
                else:
                    raise SyntaxError
                
                
        if next in ["PapoReto","PapoTorto","e","ou","câo"]:
            self.next = Token(next,"OPERATOR")
            return self.next
        
        else:
            return self.next
    
class Parser:

    def __init__(self):
        self.tokenizer = Tokenizer("test","test")

    def run(self,code):

        

        self.tokenizer.source = code
        self.tokenizer.position = 0
        self.tokenizer.selectNext()

        if self.tokenizer.next.string == "Brota":
            self.tokenizer.selectNext()
        else:
            raise ValueError("Brota não encontrado")
        if self.tokenizer.next.string == "Aí":
            self.tokenizer.selectNext()
        else:
            raise ValueError("Aí não encontrado")
        if self.tokenizer.next.string == "!":
            self.tokenizer.selectNext()
        else:
            raise ValueError("! não encontrado")

        result = self.parseBlock()

        if self.tokenizer.next.value != "EOF":
            raise ValueError

        return result
    
    def parserRealExpression(self):

        result = self.parserExpression()
        while self.tokenizer.next.value == "OPERATOR":
            if self.tokenizer.next.string == "PapoReto":
                    self.tokenizer.selectNext()
                    result = BinOp('PapoReto',[result,self.parserExpression()])
            
            elif self.tokenizer.next.string == "PapoTorto":
                    self.tokenizer.selectNext()
                    result = BinOp('PapoTorto',[result,self.parserExpression()])
            
            elif self.tokenizer.next.string == ">":
                    self.tokenizer.selectNext()
                    result = BinOp('>',[result,self.parserExpression()])
            
            elif self.tokenizer.next.string == "<":
                    self.tokenizer.selectNext()
                    result = BinOp('<',[result,self.parserExpression()])
        
        
        return result
    
    def parserExpression(self):

        result = self.parserTerm()
        while self.tokenizer.next.value == "OPERATOR":
            if self.tokenizer.next.string == "+":
                self.tokenizer.selectNext()
                result = BinOp('+',[result,self.parserTerm()])
            
            elif self.tokenizer.next.string == "-":
                self.tokenizer.selectNext()
                result = BinOp('-',[result,self.parserTerm()])
            
            elif self.tokenizer.next.string == "ou":
                self.tokenizer.selectNext()
                result = BinOp('ou',[result,self.parserTerm()])
            
            elif self.tokenizer.next.string == ".":
                self.tokenizer.selectNext()
                result = BinOp('.',[result,self.parserTerm()])
            else:
                break
            
        
        
        return result

    def parserTerm(self):
        result = self.parseFactor()

        while self.tokenizer.next.value == "OPERATOR":
            if self.tokenizer.next.string == "*":
                    self.tokenizer.selectNext()
                    result = BinOp('*',[result,self.parseFactor()])

            elif self.tokenizer.next.string == "/":
                    self.tokenizer.selectNext()
                    result = BinOp('/',[result,self.parseFactor()])
            
            elif self.tokenizer.next.string == "e":
                    self.tokenizer.selectNext()
                    result = BinOp('e',[result,self.parseFactor()])

            elif self.tokenizer.next.string == "%":
                    self.tokenizer.selectNext()
                    result = BinOp('%',[result,self.parseFactor()])
            
            else:
                break
            
        return result
        
    def parseFactor(self):
        token = self.tokenizer.next
        if token.value == "INT":
                result = IntVal(int(token.string))
                self.tokenizer.selectNext()
                return result
        elif token.value == "OPERATOR":
             if token.string == "+":
                  self.tokenizer.selectNext()
                  return UnOp("+",[self.parseFactor()])
             elif token.string == "-":
                  self.tokenizer.selectNext()
                  return UnOp("-",[self.parseFactor()])
             elif token.string == "!":
                  self.tokenizer.selectNext()
                  return UnOp("!",[self.parseFactor()])

             else:
                  raise SyntaxError
        
        elif token.value == "OPEN_PAR":
             self.tokenizer.selectNext()
             result_temp = self.parserRealExpression()

             if self.tokenizer.next.value == "CLOSE_PAR":
                  self.tokenizer.selectNext()
                  return result_temp
             else:
                  raise SyntaxError("Parênteses não fecha")
        elif token.string in RESERVED_WORDS:
            if token.string == "readline":
                self.tokenizer.selectNext()
                if self.tokenizer.next.value == "OPEN_PAR":
                  self.tokenizer.selectNext()
                  result_temp = ReadOp()

                  if self.tokenizer.next.value == "CLOSE_PAR":
                      self.tokenizer.selectNext()
                      return result_temp
                  else:
                      raise SyntaxError("Parênteses do Readln não fecha")
                      
                else:
                  raise SyntaxError("Falta Parênteses depois do readln")
            elif token.string == "BrotaNaBase":
                self.tokenizer.selectNext()
                if self.tokenizer.next.value == "IDENTIFIER":
                    temp_var_op = IdentifierOp(self.tokenizer.next)
                    function_arguments = []
                    self.tokenizer.selectNext()

                    if self.tokenizer.next.string == "Menor":
                        self.tokenizer.selectNext()
                        function_arguments.append(self.parserRealExpression())
                        while self.tokenizer.next.value == "COMMA":
                            self.tokenizer.selectNext()
                            if self.tokenizer.next.string == "Menor":
                                self.tokenizer.selectNext()
                            else:
                                raise SyntaxError("Faltou o Menor")
                            function_arguments.append(self.parserRealExpression())
                        if self.tokenizer.next.string == ".":
                            return FunctionCall(function_arguments,temp_var_op.value.string)
                        else:
                            raise SyntaxError("Faltou o .  do final da função")
                    else:
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.string != ".":
                            raise SyntaxError("Faltou o .  do final da função")
                        return FunctionCall(function_arguments,temp_var_op.value.string)
        
        elif token.value == "IDENTIFIER":
            self.tokenizer.selectNext()
            return IdentifierOp(token.string)
        
        
        elif token.value == "STRING":
            self.tokenizer.selectNext()
            return StringVal(token.string)
        

       
                
              
        else :
            raise SyntaxError
        
    def parseStatement(self):
        
        if self.tokenizer.next.value == "IDENTIFIER":
            if self.tokenizer.next.string in RESERVED_WORDS and not(self.tokenizer.next.string in VAR_TYPES):
                if self.tokenizer.next.string == "Coé":
                    self.tokenizer.selectNext()
                    result = self.parserRealExpression()
                    if (self.tokenizer.next.string != ".") :
                        raise SyntaxError("faltou o .")
                    self.tokenizer.selectNext()
                    return PrintOp(result)
                        
                elif self.tokenizer.next.string == "MarcaUmDezAíSe":
                    self.tokenizer.selectNext()
                    Realexpression = self.parserRealExpression()


                    if self.tokenizer.next.string != "?":
                        raise SyntaxError("Falou o pular linha depois da expressão booleana do while")

                    Block = []

                    self.tokenizer.selectNext()
                    if self.tokenizer.next.string != "Partiu!":
                        raise SyntaxError("Faltou o Partiu! depois do ?")
                    
                    self.tokenizer.selectNext()
                    while self.tokenizer.next.string != "Jáé!":
                        Block.append(self.parseStatement())
                    
                    self.tokenizer.selectNext()

                    return WhileOp([Realexpression,BlockOp(Block)])
                
                elif self.tokenizer.next.string == "QualFoi":
                    self.tokenizer.selectNext()
                    Block = []
                    Realexpression = self.parserRealExpression()
                    Block.append(Realexpression)

                    if self.tokenizer.next.string  != "?":
                        raise SyntaxError("Faltou o ? depois da expressão do if")
                    
                    self.tokenizer.selectNext()
                    
                    Block_if = []

                    if self.tokenizer.next.string != "Partiu!":
                        raise SyntaxError("Faltou o Partiu! depois do ?")
                    
                    self.tokenizer.selectNext()
                    while self.tokenizer.next.string != "Jáé!":
                        Block_if.append(self.parseStatement())
                        
                    
                    Block.append(BlockOp(Block_if))
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.string == "MeteOPé":
                        self.tokenizer.selectNext()

                        if self.tokenizer.next.string != "!":
                            raise SyntaxError("Falou o ! depois do else")
                        
                        self.tokenizer.selectNext()
                        Block_else = []

                        if self.tokenizer.next.string != "Partiu!":
                            raise SyntaxError("Faltou o Partiu! depois do ?")
                    
                        self.tokenizer.selectNext()

                        while self.tokenizer.next.string != "Jáé!":
                            Block_else.append(self.parseStatement())
                        Block.append(BlockOp(Block_else))
                    
                        self.tokenizer.selectNext() # Consome esse Jáé!

                    return ifOp(Block)
                
                elif self.tokenizer.next.string == "MandaBala":
                    self.tokenizer.selectNext()
                    result = self.parserRealExpression()

                    if self.tokenizer.next.string != ".":
                        raise SyntaxError("Faltou o . depois do MandaBala")
                    
                    self.tokenizer.selectNext()
                    
                    return ReturnOp(result)
                
                elif self.tokenizer.next.string == "OBagulho":
                    variables = []
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.value == "IDENTIFIER":
                        function_name = IdentifierOp(self.tokenizer.next)
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.string != "de":  
                            raise SyntaxError("Falta depois do nome da função")
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.string in VAR_TYPES:
                            function_type = self.tokenizer.next.string
                        else:
                            raise SyntaxError("Falta a tipagem do retorno da função")
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.string == "ÉOSeguinte:":
                            self.tokenizer.selectNext()
                            if self.tokenizer.next.string == "Menor":
                                variables = []
                                var_name = ""
                                var_type = ""
                                self.tokenizer.selectNext()
                                if self.tokenizer.next.string != "de":  
                                    raise SyntaxError("Falta depois do nome da função")
                                self.tokenizer.selectNext()
                                if self.tokenizer.next.string in VAR_TYPES:
                                    var_type = self.tokenizer.next.string
                                else:
                                    raise SyntaxError("Falta a tipagem da variável")
                                self.tokenizer.selectNext()

                                if self.tokenizer.next.value == "IDENTIFIER":
                                    var_name = self.tokenizer.next
                                    variables.append(VarDecOp([IdentifierOp(var_name)],var_type))
                                else:
                                    raise SyntaxError("Falta o nome da variável")
                        
                                self.tokenizer.selectNext()
                                while self.tokenizer.next.value == "COMMA":
                                    self.tokenizer.selectNext()
                                    if self.tokenizer.next.string == "Menor":
                                        self.tokenizer.selectNext()
                                    else:
                                        raise SyntaxError("Falta o Menor")
                                    if self.tokenizer.next.string != "de":  
                                        raise SyntaxError("Falta depois do nome da função")
                                    self.tokenizer.selectNext()
                                    if self.tokenizer.next.string in VAR_TYPES:
                                        var_type = self.tokenizer.next.string
                                    else:
                                        raise SyntaxError("Falta a tipagem da variável")
                                    self.tokenizer.selectNext()

                                    if self.tokenizer.next.value == "IDENTIFIER":
                                        var_name = self.tokenizer.next
                                        variables.append(VarDecOp([IdentifierOp(var_name)],var_type))
                                        self.tokenizer.selectNext()
                                    else:
                                        raise SyntaxError("Falta o nome da variável")
                                
                                if self.tokenizer.next.string != ".":
                                    raise SyntaxError("Falta o .")
                                
                            
                            if self.tokenizer.next.string != ".":
                                raise SyntaxError("Falta o .")
                            
                            self.tokenizer.selectNext()
                            
                            if self.tokenizer.next.string != "Partiu!":
                                raise SyntaxError("Faltou o Partiu! depois do .")
                    
                            self.tokenizer.selectNext()

                            
                            function_Blocks = []
                            while self.tokenizer.next.string != "Jáé!":
                                function_Blocks.append(self.parseStatement())
                               # self.tokenizer.selectNext()
                            self.tokenizer.selectNext()
                            return FuncDec([function_name,variables,BlockOp(function_Blocks)],function_type)
                            

                                

                        else:
                            raise SyntaxError("Falta abrir parenteses depois do nome da função")
                    else:
                        raise SyntaxError("Falta o nome da função")
                
                elif self.tokenizer.next.string == "BrotaNaBase":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.value == "IDENTIFIER":
                        temp_var_op = IdentifierOp(self.tokenizer.next)
                        function_arguments = []
                        self.tokenizer.selectNext()

                        if self.tokenizer.next.string == "Menor":
                            self.tokenizer.selectNext()
                            function_arguments.append(self.parserRealExpression())
                            while self.tokenizer.next.value == "COMMA":
                                function_arguments.append(self.parserRealExpression())
                                self.tokenizer.selectNext()
                            if self.tokenizer.next.string == ".":
                                self.tokenizer.selectNext()
                                return FunctionCall(function_arguments,temp_var_op.value.string)
                            else:
                                raise SyntaxError("Faltou o .  do final da função")
                        else:
                        
                            if self.tokenizer.next.string != ".":

                                raise SyntaxError("Faltou o .  do final da função")
                            self.tokenizer.selectNext()
                            return FunctionCall(function_arguments,temp_var_op.value.string)
                
                
           

                    


            else:
                if self.tokenizer.next.string in VAR_TYPES:
                    var_type = self.tokenizer.next.string
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.value == "IDENTIFIER":
                        temp_var_op = IdentifierOp(self.tokenizer.next)
                        self.tokenizer.selectNext() 
                        if self.tokenizer.next.string == "é":
                            self.tokenizer.selectNext()
                            result =  VarDecOp([temp_var_op,self.parserRealExpression()],var_type)

                            if self.tokenizer.next.string != ".":
                                raise SyntaxError("Faltou o .  da declaração da variável")
                            else:
                                self.tokenizer.selectNext()
                                return result
                        
                        else:
                            raise SyntaxError("Após a variável vem a atribuição ")
                else:
                    temp_var_op = IdentifierOp(self.tokenizer.next)
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.string == "é":
                        self.tokenizer.selectNext()
                        result = AssignmentOp([temp_var_op,self.parserRealExpression()])
                        if self.tokenizer.next.string != ".":
                                raise SyntaxError("Faltou o .  da declaração da variável")
                        else:
                            self.tokenizer.selectNext()
                            return result


                        
                    else:
                        raise SyntaxError("Variavel sem atribuição")
           
            

        

        #elif self.tokenizer.next.value == "LINHA":
            #self.tokenizer.selectNext()
        result = NoOp()
        
       # else:
        #    raise SyntaxError("STATEMENT sem LINHA '\n' ")

        return result
        
    
    def parseBlock(self):

        children = []

        while self.tokenizer.next.value != "EOF":
            children.append(self.parseStatement())
            #self.tokenizer.selectNext()
        
        return BlockOp(children)

    
    
parser = Parser()

code = read_archive("teste1.jl")
#code = read_archive(sys.argv[1])
Filtering = PrePro()
code_filtered = Filtering.filter(code)
asl = parser.run(code_filtered)
symboltable = SymbolTable()
asl_evaluated = asl.evaluate(symboltable)