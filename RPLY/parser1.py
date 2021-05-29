from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Block, Ident, PowNode
from ast import Positive, Invert, Mult, Div, Less, Greater, Equal
from ast import Assign, ReturnNode, NoOp, Negate, And, Or
from ast import IfNode, WhileNode, FuncCall, FuncDef, ArgList, Program
import lexer

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            lexer.tokens.keys(),
            precedence=[
                ('left', ['realexpression']),
                ('left', ['print'])
            ]
        )

    def parse(self):

        @self.pg.production('program : program block')
        def p_program(tokens):
            tokens[0].addChild(tokens[1])
            return tokens[0]
        
        @self.pg.production('program : block')
        def p_first_program(tokens):
            return Program(tokens[0])

        @self.pg.production('block : block command')
        def p_block(tokens):
            tokens[0].addChild(tokens[1])
            return tokens[0]
        
        @self.pg.production('block : command')
        def p_first_block(tokens):
            return Block(tokens[0])

        @self.pg.production('defcall : IDENTIFIER LPAR arguments RPAR')
        def p_defcall(tokens):
            return FuncCall(tokens[0].getstr(), tokens[2].getArgs())

        @self.pg.production('defcall : IDENTIFIER LPAR RPAR')
        def p_mono_defcall(tokens):
            return FuncCall(tokens[0].getstr(),[])

        @self.pg.production('arguments : arguments COMMA test')
        def p_arguments(tokens):
            tokens[0].addChild(tokens[2])
            return tokens[0]

        @self.pg.production('arguments : test')
        def p_mono_arguments(tokens):
            return ArgList(tokens[0])
        
        @self.pg.production('def : DEF IDENTIFIER LPAR defargs RPAR LCHAVES block RCHAVES')
        def p_def(tokens):
            return FuncDef(tokens[1].getstr(),tokens[3].getArgs(),tokens[6])
        
        @self.pg.production('def : DEF IDENTIFIER LPAR RPAR LCHAVES block RCHAVES')
        def p_mono_def(tokens):
            return FuncDef(tokens[1].getstr(),[],tokens[5])
            

        @self.pg.production('defargs : defargs COMMA IDENTIFIER')
        def p_defargs(tokens):
            tokens[0].addChild(tokens[2].getstr())
            return tokens[0]

        @self.pg.production('defargs : IDENTIFIER')
        def p_mono_defargs(tokens):
            return ArgList(tokens[0].getstr())
        
        
        @self.pg.production('command : def')
        @self.pg.production('command : print')
        @self.pg.production('command : assignment')
        @self.pg.production('command : if_command')
        @self.pg.production('command : while_command')
        @self.pg.production('command : return_command')
        @self.pg.production('command : test')
        def p_command(tokens):
            return tokens[0]

        @self.pg.production('while_command : WHILE LPAR test RPAR DOISP block ENDWHILE')
        def p_while_command(tokens):
            condition = tokens[2]
            blocktrue = tokens[5]
            return WhileNode(condition, blocktrue)
        

        @self.pg.production('if_command : IF LPAR test RPAR DOISP block ENDIF')
        def p_if_command(tokens):
            condition = tokens[2]
            blocktrue = tokens[5]
            return IfNode(condition, blocktrue)
        
        @self.pg.production('if_command : IF LPAR test RPAR DOISP block ENDIF ELSE DOISP block ENDIF')
        def p_ifelse_command(tokens):
            condition = tokens[2]
            blocktrue = tokens[5]
            blockfalse = tokens[9]
            return IfNode(condition, blocktrue, blockfalse)

        @self.pg.production('return_command : RETURN test')
        def p_return_command(tokens):
            return ReturnNode(tokens[1])

        @self.pg.production('return_command : RETURN')
        def p_mono_return_command(tokens):
            return ReturnNode(NoOp())

        @self.pg.production('assignment : IDENTIFIER EQUAL test')
        def p_assignment(tokens):
            left = tokens[0].getstr()
            right = tokens[2] 
            return Assign(left, right)

        @self.pg.production('print : PRINT LPAR test RPAR')
        def p_print(tokens):
            return Print(tokens[2])
        
        @self.pg.production('powexpression : NUMBER')
        @self.pg.production('powexpression : IDENTIFIER')
        def p_powexpression(tokens):
            token = tokens[0]
            if(token.gettokentype() == 'NUMBER'):
                return Number(int(token.getstr()))
            elif(token.gettokentype() == 'IDENTIFIER'):
                return Ident(token.getstr())
        
        @self.pg.production('powexpression : defcall')
        def p_func_powexpression(tokens):
            return tokens[0]
        

        @self.pg.production('power : powexpression')        
        def p_mono_power(tokens):
            return tokens[0]

        @self.pg.production('power : powexpression POW factor')
        def p_power(tokens):
            left = tokens[0]
            right = tokens[2]
            return PowNode(left, right)
        
        @self.pg.production('factor : PLUS factor')
        @self.pg.production('factor : MINUS factor')  
        def p_factor(tokens):
            sign = tokens[0].gettokentype()
            symb = tokens[1]
            if(sign == 'PLUS'):
                return Positive(symb)
            elif(sign == 'MINUS'):
                return Invert(symb)
            else:
                raise Exception(f"{tokens}")

        @self.pg.production('factor : power') 
        def p_mono_factor(tokens):
            return tokens[0]
        
        #NEW AF
        @self.pg.production('powexpression : LPAR test RPAR')
        def p_factor_par(tokens):
            return tokens[1]
        
        @self.pg.production('term : factor MULT factor')
        @self.pg.production('term : factor DIV factor')
        def p_term(tokens):
            op = tokens[1].gettokentype()
            left = tokens[0]
            right = tokens[2]
            if(op == 'MULT'):
                return Mult(left,right)
            if(op == 'DIV'):
                return Div(left,right)
            else:
                raise Exception(f"{tokens}")
        
        @self.pg.production('term : factor')
        def p_mono_term(tokens):
            return tokens[0]


        @self.pg.production('expression : term PLUS term')
        @self.pg.production('expression : term MINUS term')
        def p_expression(tokens):
            op = tokens[1].gettokentype()
            left = tokens[0]
            right = tokens[2]
            if(op == 'PLUS'):
                return Sum(left,right)
            if(op == 'MINUS'):
                return Sub(left,right)
            else:
                raise Exception(f"{tokens}")
        
        @self.pg.production('expression : term')
        def p_mono_expr(tokens):
            return tokens[0]
        
        @self.pg.production('realexpression : expression LESS expression')
        @self.pg.production('realexpression : expression GREATER expression')
        @self.pg.production('realexpression : expression EQEQUAL expression')
        def p_realexpression(tokens):
            op = tokens[1].gettokentype()
            left = tokens[0]
            right = tokens[2]
            if(op == 'LESS'):
                return Less(left, right)
            elif(op == 'GREATER'):
                return Greater(left,right)
            elif(op == 'EQEQUAL'):
                return Equal(left, right)

        @self.pg.production('realexpression : expression')
        def p_mono_realexpression(tokens):
            return tokens[0]

        @self.pg.production('notexpression : NOT notexpression')
        def p_notexpression(tokens):
            return Negate(tokens[1])

        @self.pg.production('notexpression : realexpression')
        def p_mono_notexpression(tokens):
            return tokens[0]

          
        @self.pg.production('andexpression : notexpression  AND  notexpression')
        @self.pg.production('andexpression : andexpression  AND  notexpression')
        def p_andexpression(tokens):
            return And(tokens[0], tokens[2])

        @self.pg.production('andexpression : notexpression')
        def p_mono_andexpression(tokens):
            return tokens[0]

        @self.pg.production('orexpression : andexpression  OR  andexpression')
        @self.pg.production('orexpression : orexpression  OR  andexpression')
        def p_orexpression(tokens):
            return Or(tokens[0], tokens[2])

        @self.pg.production('orexpression : andexpression')
        def p_mono_orexpression(tokens):
            return tokens[0]
        
        @self.pg.production('test : orexpression')
        def p_mono_test(tokens):
            return tokens[0]

        
        @self.pg.error
        def error_handle(token):
            raise ValueError("Ran into a %s in where it wasn't expected" % token.gettokentype())
    
    def getParser(self):
        return self.pg.build()           