from copy import deepcopy as dp
from . import tokens

class Token_list:
    def __init__(self, content=[]):
        self.__content = content
        self.__index = 0
    
    @property
    def head(self):
        if self.__content:
            return dp(self.__content[0])
        
        return None
    
    @property
    def tail(self):
        if len(self.__content) > 1:
            return Token_list(dp(self.__content[1:]))
        
        return Token_list(dp(self.__content[0]))
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index < len(self.__content):
            result = self.__content[self.__index]
            self.__index += 1
            return result
        
        raise StopIteration
        

    def add_new_token(self, content, line):
        new_token = tokens.new_token(content, line)
        self.__content.append(new_token)