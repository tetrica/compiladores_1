from . import token_list as TL

def tokenize(path):
    token_list = TL.Token_list()

    with open(path) as file:
        for i, line in enumerate(file):
            for char in line:
                print("ate amanha")