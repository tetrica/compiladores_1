from collections import namedtuple
from enum import Enum, auto

SYMBOLS = (',', ';', ':', ':=')
OPERATOR = ('+')
KEYWORDS = ('var', 'integer', 'real', 'if', 'then')

__token = namedtuple('Token', [
    'content',
    'token_type',
    'line'
])

def to_string(obj):
    
    return f"T<'{obj.content}', {obj.token_type}>"


__token.__str__ = to_string

class Token_type(Enum):
    ID = auto()
    INVALID = auto()
    KEYWORD = auto()
    OPERATOR = auto()
    SYMBOL = auto()

def new_token(content, line):
    return __token(
        content=content,
        line=line,
        token_type=__match_type(content)
        )

def __match_type(lexema):
    if lexema in OPERATOR:
        return Token_type.OPERATOR
    elif lexema in KEYWORDS:
        return Token_type.KEYWORD
    elif lexema in SYMBOLS:
        return Token_type.SYMBOL
    elif lexema.isalnum():
        return Token_type.ID
    else:
        return Token_type.INVALID