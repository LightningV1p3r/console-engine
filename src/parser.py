# Copyright (c) 2021 LightningV1p3r

####################
# Libs
####################

import viperlogger

####################
# Logger
####################

parser_logger = viperlogger.Logger("Parser")

####################
#Nodes
####################

class ExpressionNode:
    
    def __init__(self, node1) -> None:
        self.node1 = node1

    def as_string(self) -> str:
        res = f'({self.node1})'
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class TermNode:

    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2

    def as_string(self) -> str:
        res = f'({self.node1} + {self.node2})'
        return res 

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()

    
class FlagNode:

    def __init__(self, val) -> None:
        self.val = val

    def as_string(self) -> str:
        res = f"'FLAG: {self.val}'"
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()


class KeywordNode:

    def __init__(self, val) -> None:
        self.val = val

    def as_string(self) -> str:
        res = f"'KEYWORD: {self.val}'"
        return res
    
    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        return self.as_string()

class ArgNode:

    def __init__(self, type, val) -> None:
        self.type = type
        self.val = val

    def as_string(self) -> str:
        res = f"'{self.type}: {self.val}'"
        return res

    def __str__(self) -> str:
        return self.as_string()

    def __repr__(self) -> str:
        print(self.as_string())

####################
#Parser
####################

class Parser:

    def __init__(self, tokens, keywords) -> None:
        self.tokens = tokens
        self.keywords = keywords
        self.pos = -1
        self.current_token = None
        self.advance()

    def advance(self) -> None:
        
        self.pos += 1

        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            parser_logger.debug(f"Advanced to token '{self.current_token}' at pos {self.pos}")
        
        else:
            self.current_token = None

    def reverse(self, iterations=1):

        iter_count = 0

        while iter_count < iterations:

            self.pos -= 1

            if self.pos < 0:
                self.pos += 1
                parser_logger.error('Failed to reverse pos due to invalid index!')
            else:
                self.current_token = self.tokens[self.pos]
                parser_logger.debug(f"Reversed to pos {self.pos} with value: '{self.current_token}'")

            iter_count += 1

    ####################
    #Checker
    ####################

    def checkfor_arg(self):
        pass

    def checkfor_keyword(self):
        pass

    def checkfor_flag(self):
        pass

    ####################
    #parsing
    ####################

    def parse(self):

        res = self.parse_expression()

    def parse_expression(self):
        pass

    def parse_term(self):
        pass

    def parse_factor(self):
        pass