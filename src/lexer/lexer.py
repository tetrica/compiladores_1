from . import token_list as TL
import unicodedata as ud

NO_SEMANTICS = (' ', '\n', '\t')
SYMBOLS = (',', ';', ':', '+', ':=')
KEYWORDS = ('var', 'integer', 'real', 'if', 'then')

def tokenize(path):
    buff = ''
    possible_double_symbol = False
    token_list = TL.Token_list()

    with open(path) as file:
        for index, line in enumerate(file):
            for char in line:
                if possible_double_symbol:
                    possible_double_symbol = False

                    if char == '=':
                        token_list.add_new_token(':=', index)
                    else:
                        token_list.add_new_token(':', index)

                        if char not in NO_SEMANTICS:
                            buff += char
                    continue

                if not char.isalnum():
                    if buff:
                        token_list.add_new_token(buff, index)
                        buff = ''

                    if char == ':':
                        possible_double_symbol = True
                    elif char in SYMBOLS:
                        token_list.add_new_token(char, index)
                    elif char not in NO_SEMANTICS:
                        buff += char

                elif char not in NO_SEMANTICS:
                    buff += char
            else:
                buff = ""
    return token_list