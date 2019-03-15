from collections import namedtuple
from enum import Enum, auto

__token = namedtuple('Token', [
    'content',
    'token_type',
    'line'
])

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

def __match_type(string):
    return Token_type.ID