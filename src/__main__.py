from lexer.lexer import tokenize
import sys

if __name__ == '__main__':
    file_code_path = sys.argv[1]
    
    tokenize(file_code_path)