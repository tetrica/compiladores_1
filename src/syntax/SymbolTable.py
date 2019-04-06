class SymbolTable:
    def __init__(self):
        self.__escope = {}
        self.__queue = []

    def insert(self, token, _type=None):
        self.__escope[token.content] = {
            "type": _type,
            "token_type": token.token_type,
        }

    def find(self, token_name):
        if not token_name in self.__escope:
            return None
        
        return self.__escope[token_name]
    
    def enqueue(self, content):
        self.__queue.append(content)

    def declare_all_in_queue(self, id_type):
        for token in self.__queue:
            if token.content in self.__escope:
                exit(f'\x1b[1;31m variável "{token.content}" já declarada!\x1b[0m')

            self.__escope[token.content] = {
                'type': id_type,
            }
        
        self.__queue.clear()

    def verify_types_in_queue(self):
        first_type = self.__queue.pop(0)
        
        return all(token_type == first_type for token_type in self.__queue)

