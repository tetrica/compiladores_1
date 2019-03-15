from copy import deepcopy as dp
from . import tokens

class Token_list:
    def __init__(self, content=[]):
        self.__content = content
    
    @property
    def head(self):
        if self.__content:
            return dp(self.__content[0])
        
        return None
    
    @property
    def tail(self):
        if len(self.__content) > 1:
            return Token_list(dp(self.__content[1:]))
        
        return None
    
    def add_new_token(self, content, line):
        new_token = tokens.new_token(content, line)
        self.__content.append(new_token)