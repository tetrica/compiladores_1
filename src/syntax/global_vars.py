from enum import auto

from lexer.tokens import new_token

ASSIGNMENT = new_token(':=', -1)
COLON = new_token(':', -1)
COMMA = new_token(',', -1)
IF = new_token('if', -1)
INTEGER = new_token('integer', -1)
PLUS = new_token('+', -1)
REAL = new_token('real', -1)
SEMICOLON = new_token(';', -1)
THEN = new_token('then', -1)
VAR = new_token('var', -1)

INVALID_TOKEN = auto()
UNEXPECTED_TOKEN = auto()
UNEXPECTED_TOKEN_TYPE = auto()
