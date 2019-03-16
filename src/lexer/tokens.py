from collections import namedtuple
from enum import Enum, auto

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
        token_type=None
        )

#FIXME(Fabio): precisamos implementar isso
def __match_type(string):
    return Token_type.ID