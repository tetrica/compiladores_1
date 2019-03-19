from lexer.lexer import tokenize
from syntax.parser import parse

import sys

if __name__ == '__main__':
    # file_code_path = sys.argv[1]
    file_code_path = 'tests/test.txt'
    
    token_list = tokenize(file_code_path)

    parse(token_list)

    # for token in token_list:
    #     print(token)
