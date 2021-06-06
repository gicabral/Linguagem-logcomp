from lexer import Lexer
from parser1 import Parser
from symboltable import SymbolTable
import sys

if(len(sys.argv) < 2):
    raise Exception("Nenhum arquivo foi fornecido")

with open(sys.argv[1]) as f:
    file = f.read()    

lexer = Lexer().get_lexer()
tokens = lexer.lex(file)

pg = Parser()
pg.parse()
parser = pg.getParser()
st = SymbolTable(name='root')
parser.parse(tokens).eval(st)