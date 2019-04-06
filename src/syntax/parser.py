from lexer.tokens import Token_type
from .global_vars import *
from .utils import *
from .SymbolTable import SymbolTable

symbolTable = SymbolTable()

def parse(token_list):
    for token in token_list:
        assert_token_valid(token)    

    token_list_updated = Z(token_list)

    last_token = token_list_updated.head

    assert_token_type_eq(last_token, Token_type.EOF)

    print_pass("Okay!")

def D(token_list):
    token_list_updated = L(token_list)

    current_token = token_list_updated.head

    assert_token_eq(current_token, COLON)

    token_list_updated = K(token_list_updated.tail)
    token_list_updated = O(token_list_updated)

    return token_list_updated

def E(token_list):
    token_list_updated = T(token_list)
    token_list_updated = R(token_list_updated)

    if not symbolTable.verify_types_in_queue():
        exit(f'\x1b[1;31m variáveis devem conter o mesmo tipo em uma expressão\x1b[0m')

    return token_list_updated

def I(token_list):
    current_token = token_list.head

    assert_token_eq(current_token, VAR)
    token_list_updated = D(token_list.tail)

    return token_list_updated

def K(token_list):
    current_token = token_list.head

    assert_token_in(current_token, INTEGER, REAL)

    symbolTable.declare_all_in_queue(current_token.content)

    return token_list.tail

def L(token_list):
    current_token = token_list.head

    assert_token_type_eq(current_token, Token_type.ID)

    symbolTable.enqueue(current_token)

    return X(token_list.tail)

def O(token_list):
    current_token = token_list.head

    if not current_token == SEMICOLON:
        return token_list

    return D(token_list.tail)

def R(token_list):
    current_token = token_list.head

    if not current_token == PLUS:
        return token_list

    token_list_updated = T(token_list.tail)
    token_list_updated = R(token_list_updated)

    return token_list_updated

def S(token_list):
    current_token = token_list.head
    token_list_updated = None

    if current_token == IF:
        token_list_updated = E(token_list.tail)

        current_token = token_list_updated.head
        assert_token_eq(current_token, THEN)

        token_list_updated = S(token_list_updated.tail)

    elif current_token.token_type == Token_type.ID:
        token_list_updated = token_list.tail

        if not symbolTable.find(current_token.content):
            exit(f'\x1b[1;31m variável "{current_token.content}" não declarada!\x1b[0m')

        symbolTable.enqueue(symbolTable.find(current_token.content)['type'])

        current_token = token_list_updated.head

        assert_token_eq(current_token, ASSIGNMENT)

        token_list_updated = E(token_list_updated.tail)

    else:
        print_fail(f"Esperava-se o stmt {IF} ou o tipo {Token_type.ID}! Recebido: {current_token}")
        exit()

    return token_list_updated

def T(token_list):
    current_token = token_list.head

    assert_token_type_eq(current_token, Token_type.ID)

    if not symbolTable.find(current_token.content):
        exit(f'\x1b[1;31m variável "{current_token.content}" não declarada!\x1b[0m')

    symbolTable.enqueue(symbolTable.find(current_token.content)['type'])

    return token_list.tail

def X(token_list):
    current_token = token_list.head

    if not current_token == COMMA:
        return token_list

    return L(token_list.tail)    

def Z(token_list):
    token_list_updated = I(token_list)
    token_list_updated = S(token_list_updated)

    return token_list_updated
