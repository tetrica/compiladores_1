from collections import namedtuple
from enum import Enum, auto
from .global_vars import *

_token = namedtuple('Token', [
    'content',
    'token_type',
    'line'
])

def __token_to_string(obj):
    return f"T<'{obj.content}', {obj.token_type}>"

def __token_equals(token, toke_other):
    same_content = toke_other.content == token.content
    same_type = toke_other.token_type == token.token_type

    return same_content and same_type

_token.__str__ = __token_to_string
_token.__eq__ = __token_equals

class Token_type(Enum):
    ID = auto()
    INVALID = auto()
    KEYWORD = auto()
    OPERATOR = auto()
    SYMBOL = auto()

def new_token(content, line):
    return _token(
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