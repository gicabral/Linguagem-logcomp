from rply import LexerGenerator
import re

tokens = {
    'PRINT': r'print',
    'WHILE': r'while',
    'DEF':r'def',
    'IF': r'if',
    'ENDWHILE':r'endwhile',
    'ENDIF': r'endif',
    'ELSE': r'else',
    'RETURN': r'return',
    'NUMBER': r'\d+',
    'LPAR': r'\(',
    'RPAR': r'\)',
    'IDENTIFIER': r'[a-z]\w*',
    'COMMA':r'\,',
    'DOISP':r'\:',
    'LCHAVES':r'\{',
    'RCHAVES':r'\}',
    'PLUS':r'\+',
    'MINUS':r'\-',
    'POW': r'\*\*',
    'MULT': r'\*',
    'DIV': r'\/',
    'LESS': r'\<',
    'GREATER': r'\>',
    'EQEQUAL': r'\=\=',
    'EQUAL': r'\=',
    'NOT': r'\!', 
    'AND': r'\&\&',
    'OR' : r'\|\|',
}

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        for name, reg in tokens.items():
            self.lexer.add(name, reg)
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'\n+')
        self.lexer.ignore(r'\t+')
    
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()