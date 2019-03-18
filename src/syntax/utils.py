from .global_vars import *
from lexer.tokens import Token_type
import sys

error_msg = {
    INVALID_TOKEN: "Token inválido na linha {}::{}",
    UNEXPECTED_TOKEN: "Token({}) inesperado na linha {}! Esperado: {}",
    UNEXPECTED_TOKEN_TYPE: "Tipo({}) inesperado na linha {}! Esperado: {}"
}

def assert_token_eq(token, token_to_assert):
    if not token == token_to_assert:
        print_fail(error_msg[UNEXPECTED_TOKEN].format(token, token.line, token_to_assert))
        exit()

def assert_token_type_eq(token, token_type):
    if not token.token_type == token_type:
        print_fail(error_msg[UNEXPECTED_TOKEN_TYPE].format(token.token_type, token.line, token_type))
        exit()


def assert_token_in(token, *tokens):
    if not token in tokens:
        print_fail(error_msg[UNEXPECTED_TOKEN_TYPE].format(token, token.line, "{INTEGER} | {REAL}"))
        exit()

def assert_token_valid(token):
    if token.token_type is Token_type.INVALID:
        print_fail(error_msg[INVALID_TOKEN].format(token.line, token))
        exit()

def print_fail(message, end = '\n'):
    sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

def print_pass(message, end = '\n'):
    sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)